#!/usr/bin/env python3
r"""
apply_corrections.py

Deterministically applies the reviewed corrections manifest to predicate
JSON files. No LLM involved - every action here was already decided during
manual review (review_worklist_progress_csv.xlsx); this script only
executes those decisions mechanically and logs exactly what it did.

Usage:
    python apply_corrections.py --base-dir data/ART --manifest corrections_manifest.csv --out-log corrections_log.md

File naming convention assumed (matches the example given):
    {base_dir}\{TECHNIQUE}\{TECHNIQUE}_test{N}_predicates.json
For techniques with a context split (currently only T1082: normal/elevated):
    {base_dir}\{TECHNIQUE}\{context}\{TECHNIQUE}_test{N}_predicates.json

If your actual folder layout differs, edit build_file_path() below - do not
guess blindly, since T1053.005 previously had an output-path bug from
exactly this kind of mismatch.
"""

import argparse
import csv
import json
import re
import sys
from pathlib import Path


def _normalize(s: str) -> str:
    """Strip dots/spaces/underscores and lowercase, so 'T1021.002',
    'T1021 002', and 'T1021_002' all compare equal."""
    return re.sub(r"[.\s_]", "", s).lower()


def find_technique_dirs(base_dir: Path, technique: str):
    """Technique folders are inconsistently named across the corpus - some
    use dots (T1082), some use spaces (T1021 002), and some are
    double-nested (T1112/T1112/, mirroring the ART/ART double-nesting seen
    at the archive root). Search by normalized name instead of assuming one
    exact string, and search two levels deep for the double-nesting case."""
    target = _normalize(technique)
    matches = []
    if not base_dir.exists():
        return matches
    for d in base_dir.rglob("*"):
        if d.is_dir() and _normalize(d.name) == target:
            matches.append(d)
    return matches


def find_predicate_file(base_dir: Path, technique: str, test: str, context: str):
    """Recursively search under every matching technique directory for a
    predicate JSON file for this test number. Filenames vary (dot vs
    underscore vs no separator), so match on 'test{N}_predicates.json' with
    a negative lookahead so test2 doesn't match test20."""
    tech_dirs = find_technique_dirs(base_dir, technique)
    if not tech_dirs:
        return None, []

    pattern = re.compile(rf"test{re.escape(test)}(?!\d)_predicates\.json$", re.IGNORECASE)
    candidates = []
    for tech_dir in tech_dirs:
        for f in tech_dir.rglob("*.json"):
            if pattern.search(f.name):
                candidates.append(f)

    if not candidates:
        return None, []

    if context:
        ctx_key = context.split("_")[-1] if "_" in context else context  # "t1082_elevated" -> "elevated"
        ctx_filtered = [f for f in candidates if ctx_key.lower() in str(f.parent).lower()]
        if ctx_filtered:
            candidates = ctx_filtered

    # de-duplicate (rglob can revisit the same real path via nested matches)
    seen = set()
    unique = []
    for f in candidates:
        rp = f.resolve()
        if rp not in seen:
            seen.add(rp)
            unique.append(f)

    return unique[0], unique


SECTIONS = ["preconditions", "effects", "unconsumed_or_uncertain"]


def find_predicate(entries, name):
    for i, e in enumerate(entries):
        if e.get("name") == name:
            return i
    return None


def find_predicate_anywhere(data: dict, name: str):
    """Predicates aren't always where the manifest assumes - notably many
    T1112 tests keep 'unconfirmed' effects (e.g. registry-key-modified) in
    unconsumed_or_uncertain rather than effects, and that array uses a
    different schema (name/note, no category/justification). Search every
    section so a predicate is found regardless of which one it actually
    lives in."""
    for sec in SECTIONS:
        entries = data.get(sec, [])
        idx = find_predicate(entries, name)
        if idx is not None:
            return sec, idx
    return None, None


def apply_action(data: dict, row: dict, log: list):
    target_section = row["section"]  # where a rename/add should end up
    action = row["action"]
    old_name = row["predicate_old"].strip()
    new_name = row["predicate_new"].strip()
    category = row["category_new"].strip()
    justification = row["justification"].strip()

    for sec in SECTIONS:
        if sec not in data:
            data[sec] = []

    if row["needs_manual_verification"].strip().upper() == "TRUE":
        log.append(
            f"  [NEEDS MANUAL CHECK] {row['technique']} #{row['test']} ({target_section}): "
            f"'{old_name or '(unspecified)'}' -> action='{action}', proposed new='{new_name or '(n/a)'}'. "
            f"Reason: {justification}"
        )
        return

    if action == "drop":
        found_sec, idx = find_predicate_anywhere(data, old_name)
        if found_sec is None:
            log.append(f"  [WARN] Could not find '{old_name}' anywhere to drop - skipped.")
            return
        data[found_sec].pop(idx)
        log.append(f"  [OK] Dropped '{old_name}' from {found_sec}.")

    elif action == "rename":
        found_sec, idx = find_predicate_anywhere(data, old_name)
        if found_sec is None:
            log.append(f"  [WARN] Could not find '{old_name}' anywhere to rename - skipped.")
            return

        new_entry = {
            "name": new_name,
            "category": category or data[found_sec][idx].get("category", ""),
            "justification": justification or data[found_sec][idx].get("note", ""),
        }

        if found_sec == target_section:
            data[found_sec][idx] = new_entry
            log.append(f"  [OK] Renamed '{old_name}' -> '{new_name}' in {found_sec}.")
        else:
            # e.g. sitting in unconsumed_or_uncertain but belongs in effects
            # once the evidence makes it a confirmed fact rather than uncertain
            data[found_sec].pop(idx)
            data[target_section].append(new_entry)
            log.append(
                f"  [OK] Moved '{old_name}' from {found_sec} -> {target_section} "
                f"as '{new_name}' (schema normalized: name/category/justification)."
            )

    elif action == "add":
        if find_predicate(data[target_section], new_name) is not None:
            log.append(f"  [WARN] '{new_name}' already present in {target_section} - skipped add.")
            return
        data[target_section].append({
            "name": new_name,
            "category": category,
            "justification": justification,
        })
        log.append(f"  [OK] Added '{new_name}' to {target_section}.")

    else:
        log.append(f"  [WARN] Unknown action '{action}' - skipped.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-dir", required=True, help="Root folder containing per-technique predicate JSON files")
    ap.add_argument("--manifest", required=True, help="corrections_manifest.csv")
    ap.add_argument("--out-log", default="corrections_log.md", help="Where to write the human-readable run log")
    ap.add_argument("--dry-run", action="store_true", help="Don't write files, just show what would happen")
    args = ap.parse_args()

    base_dir = Path(args.base_dir)
    manifest_rows = list(csv.DictReader(open(args.manifest, newline="", encoding="utf-8")))

    # group rows by (technique, test, context) so we open/save each file once
    grouped = {}
    for row in manifest_rows:
        key = (row["technique"], row["test"], row["context"])
        grouped.setdefault(key, []).append(row)

    full_log = ["# Corrections apply log\n"]
    files_touched = 0
    files_missing = 0

    for (technique, test, context), rows in grouped.items():
        full_log.append(f"\n## {technique} test #{test}" + (f" ({context})" if context else ""))

        path, all_matches = find_predicate_file(base_dir, technique, test, context)

        if path is None:
            tech_dirs = find_technique_dirs(base_dir, technique)
            if not tech_dirs:
                full_log.append(f"  [MISSING] No folder found matching technique '{technique}' anywhere under {base_dir}.")
            else:
                full_log.append(
                    f"  [MISSING] Found technique folder(s) {[str(d) for d in tech_dirs]} "
                    f"but no file matching 'test{test}_predicates.json' inside."
                )
            files_missing += 1
            continue

        full_log.append(f"File: `{path}`")
        if len(all_matches) > 1:
            full_log.append(
                f"  [WARN] {len(all_matches)} candidate files matched - using first: {path}. "
                f"Others: {[str(p) for p in all_matches[1:]]}"
            )

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        row_log = []
        for row in rows:
            apply_action(data, row, row_log)
        full_log.extend(row_log)

        if not args.dry_run:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
            full_log.append(f"  -> saved.")
        else:
            full_log.append(f"  -> dry run, not saved.")

        files_touched += 1

    full_log.append(f"\n---\nFiles touched: {files_touched}   Files missing: {files_missing}")

    with open(args.out_log, "w", encoding="utf-8") as f:
        f.write("\n".join(full_log))

    print("\n".join(full_log))
    print(f"\nLog written to {args.out_log}")

    if files_missing:
        print(f"\nWARNING: {files_missing} file(s) were not found. Nothing was guessed - fix paths and re-run for those.", file=sys.stderr)


if __name__ == "__main__":
    main()
