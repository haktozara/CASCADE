"""
predicate_table.py — deterministic, rule-based validator for LLM-proposed
PDDL predicates, cross-checked against an ART test's YAML definition.

No LLM call is made here on purpose: this is meant to be an independent
check on the translation step (art_to_pddl.py), not a second opinion from
the same kind of model that could share the same blind spots.

Usage:
    python predicate_table.py --json output/T1053.005/test_11.json \
                               --yaml atomics/T1053.005/T1053.005.yaml \
                               --test-number 11 \
                               --out output/T1053.005/test_11_crosscheck.md

    # JSON-only mode (no YAML available yet) — still produces the table,
    # but every rule falls back to "NO YAML — cannot verify":
    python predicate_table.py --json output/T1053.005/test_11.json

Rules checked (mirrors the eight fields from the project's methodology
notes): elevation_required, executor, dependencies, registry hive,
interactive session, process-spawned, output-written, obfuscation.
Each candidate predicate is checked against whichever rules are relevant
to it; predicates that don't match any rule are marked MANUAL REVIEW
rather than silently passed.
"""
import argparse
import json
import re
import sys

try:
    import yaml as pyyaml
except ImportError:
    pyyaml = None


# ---------------------------------------------------------------------
# YAML loading
# ---------------------------------------------------------------------
def load_yaml_test(yaml_path, test_number):
    """Load a specific atomic_tests entry from an ART technique YAML file."""
    if yaml_path is None:
        return None
    if pyyaml is None:
        print("WARNING: pyyaml not installed — run `pip install pyyaml --break-system-packages`. "
              "Falling back to JSON-only mode.", file=sys.stderr)
        return None
    with open(yaml_path) as f:
        data = pyyaml.safe_load(f)
    tests = data.get("atomic_tests", [])
    if test_number is not None and 1 <= test_number <= len(tests):
        return tests[test_number - 1]
    # Fall back: return the whole file if we can't isolate one test
    return {"_all_tests": tests}


def load_predicate_json(json_path):
    with open(json_path) as f:
        return json.load(f)


# ---------------------------------------------------------------------
# Rule functions
# Each returns (evidence_str, decision) where decision in
# {"PASS", "FLAG", "REVIEW", "NO YAML"}
# ---------------------------------------------------------------------
def rule_elevation(name, justification, yaml_test):
    if yaml_test is None:
        return "no YAML loaded", "NO YAML"
    elevation = yaml_test.get("executor", {}).get("elevation_required")
    mentions_admin = any(k in name.lower() for k in ["admin", "elevat", "privileg"])
    if not mentions_admin:
        return "not privilege-related", "PASS"
    if elevation is True:
        return "YAML elevation_required: true — confirms privilege precondition", "PASS"
    if elevation is False:
        return ("YAML elevation_required: false — contradicts predicate. "
                "Known-unreliable field (see T1046, T1053.005 #4/#9); "
                "do not auto-reject, flag for manual privilege-context check."), "FLAG"
    return "elevation_required not set in YAML", "REVIEW"


def rule_executor(name, justification, yaml_test):
    if yaml_test is None:
        return "no YAML loaded", "NO YAML"
    executor_name = yaml_test.get("executor", {}).get("name", "")
    if "executor" not in name.lower() and not any(
        e in name.lower() for e in ["powershell", "cmd", "command", "interpreter"]
    ):
        return "not executor-related", "PASS"
    if executor_name and executor_name.lower() in name.lower():
        return f"YAML executor '{executor_name}' matches predicate", "PASS"
    if executor_name:
        return f"YAML executor is '{executor_name}', predicate does not reference it", "REVIEW"
    return "no executor field in YAML", "REVIEW"


def rule_dependencies(name, justification, yaml_test):
    if yaml_test is None:
        return "no YAML loaded", "NO YAML"
    has_deps = bool(yaml_test.get("dependencies"))
    mentions_payload = any(k in name.lower() for k in ["payload", "tool-present", "file-present", "dependency"])
    if not mentions_payload:
        return "not dependency-related", "PASS"
    if has_deps:
        return "YAML has a dependencies block — supports an Environment/tooling precondition", "PASS"
    return "YAML has no dependencies block — predicate may be unsupported", "REVIEW"


def rule_registry(name, justification, yaml_test):
    if yaml_test is None:
        return "no YAML loaded", "NO YAML"
    if "registry" not in name.lower():
        return "not registry-related", "PASS"
    cmd_blob = json.dumps(yaml_test.get("executor", {})).lower()
    hive_match = re.search(r"hk(lm|cu|cr|u)\\", cmd_blob)
    if hive_match:
        return f"registry hive reference found in command ({hive_match.group(0)})", "PASS"
    if "reg " in cmd_blob or "registry" in cmd_blob:
        return "command references registry but no explicit hive path matched", "REVIEW"
    return "no registry reference found in YAML command text", "FLAG"


def rule_interactive_session(name, justification, yaml_test):
    if yaml_test is None:
        return "no YAML loaded", "NO YAML"
    if "interactive" not in name.lower() and "session" not in name.lower():
        return "not session-related", "PASS"
    desc = (yaml_test.get("description") or "").lower()
    if "interactive" in desc or "logon" in desc or "session" in desc:
        return "YAML description references an interactive/logon session", "PASS"
    return ("no explicit interactive-session evidence in YAML — flagged in methodology notes "
            "as typically inferred from execution artifacts rather than YAML structure"), "REVIEW"


def rule_process_spawned(name, justification, yaml_test):
    if yaml_test is None:
        return "no YAML loaded", "NO YAML"
    if "process" not in name.lower():
        return "not process-related", "PASS"
    cmd_blob = json.dumps(yaml_test.get("executor", {})).lower()
    if any(k in cmd_blob for k in ["start-process", "cmd /c", "invoke-", "new-object"]):
        return "command text shows a process-spawning pattern", "PASS"
    return "no clear process-spawning pattern in command text", "REVIEW"


def rule_output_written(name, justification, yaml_test):
    if yaml_test is None:
        return "no YAML loaded", "NO YAML"
    if not any(k in name.lower() for k in ["output", "file-written", "written"]):
        return "not output/file-related", "PASS"
    cmd_blob = json.dumps(yaml_test.get("executor", {})).lower()
    if any(k in cmd_blob for k in ["out-file", ">", "set-content", "add-content"]):
        return "command text shows an output/write pattern", "PASS"
    return "no clear output-write pattern in command text", "REVIEW"


def rule_obfuscation(name, justification, yaml_test):
    if yaml_test is None:
        return "no YAML loaded", "NO YAML"
    if "obfuscat" not in name.lower():
        return "not obfuscation-related", "PASS"
    cmd_blob = json.dumps(yaml_test.get("executor", {})).lower()
    if re.search(r"-e(nc)?\b|frombase64string|-w hidden|-windowstyle hidden", cmd_blob):
        return "command text shows an obfuscation/encoding flag", "PASS"
    return "no obfuscation flag found in command text", "REVIEW"


RULES = [
    rule_elevation,
    rule_executor,
    rule_dependencies,
    rule_registry,
    rule_interactive_session,
    rule_process_spawned,
    rule_output_written,
    rule_obfuscation,
]


# ---------------------------------------------------------------------
# Cross-check driver
# ---------------------------------------------------------------------
def crosscheck_candidate(name, category, justification, yaml_test):
    results = [rule(name, justification, yaml_test) for rule in RULES]
    # Keep only rules that actually judged this candidate (i.e. not the
    # generic "not X-related" pass-through)
    relevant = [(ev, dec) for ev, dec in results if not ev.startswith("not ")]

    if not relevant:
        return "No matching rule for this predicate", "MANUAL REVIEW"

    if any(dec == "FLAG" for _, dec in relevant):
        ev = "; ".join(e for e, d in relevant if d == "FLAG")
        return ev, "FLAG"
    if any(dec == "NO YAML" for _, dec in relevant):
        return "No YAML loaded — cannot verify", "MANUAL REVIEW"
    if any(dec == "REVIEW" for _, dec in relevant):
        ev = "; ".join(e for e, d in relevant if d == "REVIEW")
        return ev, "MANUAL REVIEW"

    ev = "; ".join(e for e, d in relevant if d == "PASS")
    return ev, "PASS"


def build_table(predicate_data, yaml_test):
    rows = []
    for section in ("preconditions", "effects"):
        for cand in predicate_data.get(section, []):
            evidence, decision = crosscheck_candidate(
                cand["name"], cand.get("category", ""), cand.get("justification", ""), yaml_test
            )
            rows.append({
                "candidate": cand["name"],
                "category": cand.get("category", ""),
                "source_justification": cand.get("justification", ""),
                "crosscheck_evidence": evidence,
                "decision": decision,
                "section": section,
            })
    for cand in predicate_data.get("unconsumed_or_uncertain", []):
        rows.append({
            "candidate": cand["name"],
            "category": "(unclassified)",
            "source_justification": cand.get("note", ""),
            "crosscheck_evidence": "Flagged by translator as uncertain — always MANUAL REVIEW regardless of YAML",
            "decision": "MANUAL REVIEW",
            "section": "unconsumed_or_uncertain",
        })
    return rows


def render_markdown(rows, technique, test_number, privilege_context=None):
    context_suffix = f" ({privilege_context})" if privilege_context else ""
    lines = [
        f"# Predicate cross-check — {technique} Test #{test_number}{context_suffix}",
        "",
        "| Candidate | Category | Evidence | Cross-check | Decision |",
        "|---|---|---|---|---|",
    ]
    for r in rows:
        lines.append(
            f"| `{r['candidate']}` | {r['category']} | {r['source_justification']} | "
            f"{r['crosscheck_evidence']} | **{r['decision']}** |"
        )
    return "\n".join(lines)


def find_technique_yaml(yaml_root, technique):
    """Best-effort: atomics/<technique>/<technique>.yaml is ART's standard layout."""
    if yaml_root is None:
        return None
    import os
    candidate = os.path.join(yaml_root, technique, f"{technique}.yaml")
    return candidate if os.path.exists(candidate) else None


def run_batch(json_dir, yaml_root, out_path):
    import os
    import glob

    json_files = sorted(glob.glob(os.path.join(json_dir, "**", "*.json"), recursive=True))
    if not json_files:
        print(f"No JSON files found under {json_dir}", file=sys.stderr)
        return

    all_sections = []
    summary = {}  # technique -> {"PASS": n, "FLAG": n, "MANUAL REVIEW": n}

    for jf in json_files:
        if "/sample_data/" in jf.replace("\\", "/"):
            continue  # Colab's own default demo files, not ours

        try:
            predicate_data = load_predicate_json(jf)
            if not isinstance(predicate_data, dict):
                print(f"SKIPPED {jf}: not a predicate JSON (top-level is {type(predicate_data).__name__}, expected dict)",
                      file=sys.stderr)
                continue

            technique = predicate_data.get("technique", "?")
            test_number = predicate_data.get("test_number")

            # Privilege context (normal vs elevated) isn't stored inside the
            # JSON -- it only exists as the folder the file sits in
            # (e.g. output/T1082/normal/, output/T1082/elevated/). Without
            # reading it here, two files with the same technique + test
            # number but different privilege context produce identical
            # report headers and get silently conflated downstream.
            # Fall back to no label if the immediate parent folder is just
            # the technique's own output folder (no privilege-context split
            # for that technique).
            parent_dir_name = os.path.basename(os.path.dirname(jf))
            privilege_context = (
                parent_dir_name
                if parent_dir_name not in (technique, ".", "")
                else None
            )

            yaml_path = find_technique_yaml(yaml_root, technique)
            yaml_test = load_yaml_test(yaml_path, test_number)

            rows = build_table(predicate_data, yaml_test)
            md = render_markdown(rows, technique, test_number, privilege_context)
            all_sections.append(md)

            summary_key = (technique, privilege_context)
            summary.setdefault(summary_key, {"PASS": 0, "FLAG": 0, "MANUAL REVIEW": 0})
            for r in rows:
                summary[summary_key][r["decision"]] = summary[summary_key].get(r["decision"], 0) + 1

            yaml_note = "" if yaml_path else "  [NO YAML FOUND — all rows fell back to MANUAL REVIEW]"
            context_note = f" [{privilege_context}]" if privilege_context else ""
            print(f"Checked {jf} ({technique} #{test_number}){context_note}{yaml_note}")
        except Exception as e:
            print(f"SKIPPED {jf}: {type(e).__name__}: {e}", file=sys.stderr)
            continue

    summary_lines = [
        "# Corpus-wide predicate cross-check summary",
        "",
        "| Technique | Context | PASS | FLAG | MANUAL REVIEW |",
        "|---|---|---|---|---|",
    ]
    for (tech, context), counts in sorted(summary.items(), key=lambda kv: (kv[0][0], kv[0][1] or "")):
        summary_lines.append(
            f"| {tech} | {context or '—'} | {counts.get('PASS', 0)} | "
            f"{counts.get('FLAG', 0)} | {counts.get('MANUAL REVIEW', 0)} |"
        )
    summary_md = "\n".join(summary_lines)

    full_report = summary_md + "\n\n---\n\n" + "\n\n---\n\n".join(all_sections)

    if out_path:
        with open(out_path, "w") as f:
            f.write(full_report)
        print(f"\nWrote consolidated report to {out_path}")
    else:
        print("\n" + full_report)

    print("\n--- Summary ---")
    for (tech, context), counts in sorted(summary.items(), key=lambda kv: (kv[0][0], kv[0][1] or "")):
        flagged = counts.get("FLAG", 0) + counts.get("MANUAL REVIEW", 0)
        total = sum(counts.values())
        label = f"{tech} [{context}]" if context else tech
        print(f"  {label}: {total - flagged}/{total} clean PASS, {flagged} need attention")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", default=None, help="Path to a single predicate JSON from art_to_pddl.py")
    parser.add_argument("--json-dir", default=None,
                         help="Batch mode: recursively cross-check every JSON under this directory "
                              "(e.g. output/) instead of a single file")
    parser.add_argument("--yaml", default=None, help="Path to the ART technique YAML file (single-file mode)")
    parser.add_argument("--yaml-root", default=None,
                         help="Batch mode: root of the atomics/ folder — looks up "
                              "<yaml-root>/<technique>/<technique>.yaml automatically per file")
    parser.add_argument("--test-number", type=int, default=None,
                         help="Which atomic_tests[] entry to check against (1-indexed, single-file mode)")
    parser.add_argument("--out", default=None,
                         help="Write markdown to this path (default: stdout). In batch mode this is the "
                              "consolidated report path.")
    args = parser.parse_args()

    if args.json_dir:
        run_batch(args.json_dir, args.yaml_root, args.out)
    elif args.json:
        predicate_data = load_predicate_json(args.json)
        test_number = args.test_number or predicate_data.get("test_number")
        yaml_test = load_yaml_test(args.yaml, test_number)
        rows = build_table(predicate_data, yaml_test)
        md = render_markdown(rows, predicate_data.get("technique", "?"), test_number)
        if args.out:
            with open(args.out, "w") as f:
                f.write(md)
            print(f"Wrote {args.out}")
        else:
            print(md)
    else:
        parser.error("Provide either --json (single file) or --json-dir (batch mode)")
