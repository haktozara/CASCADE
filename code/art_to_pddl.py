"""
art_to_pddl.py

Translates an Atomic Red Team (ART) test — YAML definition + execution
evidence from the VM — into candidate PDDL predicates, using the
five-category scheme (Executor, Process, Privilege/User, Information,
Environment).

IMPORTANT: This script performs TRANSLATION ONLY. The LLM never plans,
sequences, or reasons about attack chains — it proposes candidate
predicates for a single ART test's action, which you then validate by
hand before adding to domain.pddl. Fast Downward handles all planning.

Usage:
    python art_to_pddl.py --yaml path/to/T1547.001.yaml --test-number 1 \
        --evidence path/to/execution_output.txt \
        --technique T1547.001 \
        --out t1547_001_test1_predicates.json
"""

import argparse
import json
import re
import sys
from pathlib import Path

from openai import OpenAI

# ---------------------------------------------------------------------------
# Five-category predicate scheme (fixed across all ART test translations)
# ---------------------------------------------------------------------------
CATEGORY_SCHEME = """
Five-category predicate scheme:

1. Executor — the mechanism/interpreter/binary that runs the attacker's
   command (e.g. powershell-invokable, cmd-invokable, interpreter-invokable).
2. Process — runtime process state created or required by the technique
   (e.g. process-running, process-spawned).
3. Privilege/User — the privilege level or user context required or
   obtained (e.g. user-is-admin, elevated-privilege, access-denied related
   states).
4. Information — data/artifacts read, written, or exfiltrated as part of
   the technique (e.g. credentials-dumped, registry-key-written,
   file-created).
5. Environment — persistent system/OS-level state changes that outlast the
   single execution and represent durable footholds (e.g.
   registry-run-key-set, startup-folder-entry-created, scheduled-task-created).

Notes from prior translations (for consistency, not as rules to force):
- T1059.001 (obfuscated PowerShell) required introducing Privilege/User
  predicates because of observed "Access is denied" failures during
  execution.
- T1547.001 (Registry Run Keys / Startup Folder) techniques have so far
  been almost entirely Environment-category, since their defining effect
  is a persistent registry/filesystem change rather than a transient
  process or privilege effect.
"""

SYSTEM_PROMPT = f"""You are a translation component in a symbolic AI planning
pipeline for cyberattack chain generation (replicating and extending the
Aurora system, Wang et al. 2024). Your ONLY job is to translate a single
Atomic Red Team (ART) test — its YAML definition plus real execution
evidence from a VM run — into candidate PDDL predicates.

You do NOT plan, sequence, or reason about how this technique combines
with others. A separate classical planner (Fast Downward) does all
planning deterministically. You only propose predicates for THIS action.

{CATEGORY_SCHEME}

For the given ART test, propose:
- "preconditions": predicates that must hold TRUE before this technique
  can execute (grounded in what the YAML's prerequisites/dependencies say,
  and what the evidence implies was already true).
- "effects": predicates that become true (or false, prefix with "not-")
  AFTER this technique executes successfully, grounded in the actual
  evidence, not just what the YAML claims should happen.

For each predicate, include:
- "name": short lisp-case PDDL predicate name
- "category": one of Executor, Process, Privilege/User, Information, Environment
- "justification": one sentence citing what in the YAML or evidence supports it

Respond ONLY with valid JSON, no markdown fences, no preamble, in this
exact shape:

{{
  "technique": "<technique id>",
  "test_number": <int>,
  "preconditions": [
    {{"name": "...", "category": "...", "justification": "..."}}
  ],
  "effects": [
    {{"name": "...", "category": "...", "justification": "..."}}
  ],
  "unconsumed_or_uncertain": [
    {{"name": "...", "note": "why this one is flagged for human review"}}
  ]
}}
"""


def split_evidence_by_test(evidence_text: str, technique: str) -> dict:
    """
    Split a combined VM evidence transcript (multiple ART sub-tests run in one
    Invoke-AtomicTest session) into per-test-number blocks, using the
    "Executing test: <TECH>-<N> ..." / "Done executing test: <TECH>-<N> ..."
    markers that Invoke-AtomicTest prints around each sub-test.

    Returns a dict mapping test_number (int) -> evidence block (str), covering
    only the sub-tests that have BOTH a start and matching end marker for the
    given technique. Sub-tests without a clean "Done executing test" marker
    (e.g. a crashed/hung run) are skipped and reported to the caller.
    """
    # NOTE: the trailing part deliberately stops right at "Done executing test:
    # TECH-N" and does NOT try to also consume the rest of that line (e.g. via
    # [^\n]*). Pasted terminal transcripts sometimes lose real newline
    # characters across long wrapped/error-heavy stretches of output (multiple
    # sub-tests end up on one giant "line" of text). Relying on \n to end a
    # block caused it to swallow one or more subsequent sub-tests whole
    # whenever that happened, silently dropping them from the split.
    pattern = re.compile(
        rf"(Executing test:?\s*{re.escape(technique)}-(\d+).*?"
        rf"Done executing test:?\s*{re.escape(technique)}-\2)",
        re.DOTALL,
    )
    blocks = {}
    for match in pattern.finditer(evidence_text):
        block_text, test_num_str = match.group(1), match.group(2)
        blocks[int(test_num_str)] = block_text.strip()
    return blocks


def build_user_prompt(technique: str, test_number: int, yaml_text: str, evidence_text: str) -> str:
    return f"""Technique: {technique}
ART Test Number: {test_number}

--- ART YAML DEFINITION ---
{yaml_text}

--- VM EXECUTION EVIDENCE ---
{evidence_text}

Translate this into candidate PDDL predicates per your instructions.
"""


def call_openai(system_prompt: str, user_prompt: str, model: str = "gpt-4o") -> str:
    client = OpenAI()  # reads OPENAI_API_KEY from environment
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0,
    )
    return response.choices[0].message.content


def strip_code_fences(text: str) -> str:
    """Defensive cleanup in case the model wraps JSON in ```json fences anyway."""
    text = text.strip()
    text = re.sub(r"^```(?:json)?\s*", "", text)
    text = re.sub(r"\s*```$", "", text)
    return text.strip()


def main():
    parser = argparse.ArgumentParser(description="Translate an ART test into candidate PDDL predicates.")
    parser.add_argument("--yaml", required=True, help="Path to the ART test YAML file")
    parser.add_argument("--evidence", required=True, help="Path to a text file with VM execution output/evidence")
    parser.add_argument("--technique", required=True, help="MITRE technique ID, e.g. T1547.001")

    test_group = parser.add_mutually_exclusive_group(required=True)
    test_group.add_argument("--test-number", type=int, help="A single ART test number within the technique")
    test_group.add_argument("--test-numbers", help="Comma-separated ART test numbers, e.g. 1,7,9,29")
    test_group.add_argument("--all", action="store_true",
                             help="Process every test number found in --evidence via "
                                  "'Executing test: <TECH>-N' / 'Done executing test: <TECH>-N' markers")

    parser.add_argument("--out", default=None,
                         help="Output JSON path. Only valid with a single --test-number. "
                              "For --test-numbers/--all, use --out-dir instead.")
    parser.add_argument("--out-dir", default=".",
                         help="Directory to write one JSON file per test number when using "
                              "--test-numbers or --all (default: current directory)")
    parser.add_argument("--model", default="gpt-4o", help="OpenAI model to use (default: gpt-4o)")
    parser.add_argument("--max-evidence-chars", type=int, default=20000,
                         help="Truncate any single test's evidence block to this many characters "
                              "before sending it to the model (default: 20000). Prevents huge dumps "
                              "(e.g. Get-WmiObject output listing every process's full property set) "
                              "from blowing past token-per-minute rate limits.")
    args = parser.parse_args()

    if args.out and (args.test_numbers or args.all):
        sys.exit("ERROR: --out is only valid with a single --test-number. Use --out-dir for batch runs.")

    yaml_path = Path(args.yaml)
    evidence_path = Path(args.evidence)

    if not yaml_path.exists():
        sys.exit(f"ERROR: YAML file not found: {yaml_path}")
    if not evidence_path.exists():
        sys.exit(f"ERROR: Evidence file not found: {evidence_path}")

    yaml_text = yaml_path.read_text(encoding="utf-8", errors="replace")
    evidence_text = evidence_path.read_text(encoding="utf-8", errors="replace")

    # ---- Work out which test numbers to process, and the evidence slice for each ----
    if args.test_number is not None:
        requested = [args.test_number]
    elif args.test_numbers:
        requested = [int(n.strip()) for n in args.test_numbers.split(",") if n.strip()]
    else:  # --all
        requested = None  # filled in after splitting evidence

    evidence_blocks = split_evidence_by_test(evidence_text, args.technique)

    if requested is None:
        if not evidence_blocks:
            sys.exit(f"ERROR: --all was given but no 'Executing test: {args.technique}-N' / "
                      f"'Done executing test: {args.technique}-N' markers were found in the evidence file.")
        requested = sorted(evidence_blocks.keys())
    elif not evidence_blocks:
        # Single combined-evidence-per-test-number workflow (original behaviour):
        # no split markers found at all, so treat the whole file as evidence for
        # every requested test number (matches the pre-existing single-test usage).
        evidence_blocks = {n: evidence_text for n in requested}

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    succeeded, skipped, failed = [], [], []

    for test_number in requested:
        block = evidence_blocks.get(test_number)
        if block is None:
            print(f"SKIPPING Test #{test_number}: no matching 'Executing test: "
                  f"{args.technique}-{test_number}' ... 'Done executing test' block found in evidence.")
            skipped.append(test_number)
            continue

        if len(block) > args.max_evidence_chars:
            omitted = len(block) - args.max_evidence_chars
            block = (block[:args.max_evidence_chars] +
                     f"\n\n[... TRUNCATED: {omitted} additional characters of evidence omitted "
                     f"to stay under the API's token-per-minute limit. This is usually a long "
                     f"structured dump (e.g. Get-WmiObject output listing many processes' full "
                     f"property sets) where the exit code and the first N processes already show "
                     f"the technique's behavior. Increase --max-evidence-chars if you need more, "
                     f"or note in the write-up that this test's evidence was truncated for "
                     f"translation purposes. ...]")
            print(f"NOTE: Test #{test_number}'s evidence was truncated from "
                  f"{omitted + args.max_evidence_chars} to {args.max_evidence_chars} characters "
                  f"before sending to the model.")

        user_prompt = build_user_prompt(args.technique, test_number, yaml_text, block)

        print(f"\nCalling {args.model} to translate {args.technique} Test #{test_number}...")
        try:
            raw_output = call_openai(SYSTEM_PROMPT, user_prompt, model=args.model)
        except Exception as e:
            print(f"WARNING: Test #{test_number} — API call failed ({type(e).__name__}: {e}). "
                  f"Skipping this test and continuing with the rest of the batch.")
            failed.append(test_number)
            continue
        cleaned = strip_code_fences(raw_output)

        try:
            parsed = json.loads(cleaned)
        except json.JSONDecodeError:
            print(f"WARNING: Test #{test_number} — model output was not valid JSON. Raw output below:\n")
            print(raw_output)
            failed.append(test_number)
            continue

        if args.out and len(requested) == 1:
            out_path = Path(args.out)
        else:
            out_path = out_dir / f"{args.technique.replace('.', '_')}_test{test_number}_predicates.json"
        out_path.write_text(json.dumps(parsed, indent=2), encoding="utf-8")

        print(f"Saved candidate predicates to: {out_path}")
        print("  === PRECONDITIONS ===")
        for p in parsed.get("preconditions", []):
            print(f"    [{p['category']}] {p['name']} — {p['justification']}")
        print("  === EFFECTS ===")
        for e in parsed.get("effects", []):
            print(f"    [{e['category']}] {e['name']} — {e['justification']}")
        if parsed.get("unconsumed_or_uncertain"):
            print("  === FLAGGED FOR HUMAN REVIEW ===")
            for u in parsed["unconsumed_or_uncertain"]:
                print(f"    {u['name']} — {u['note']}")

        succeeded.append(test_number)

    print(f"\n{'=' * 60}")
    print(f"BATCH SUMMARY for {args.technique}")
    print(f"  Succeeded: {succeeded if succeeded else 'none'}")
    if skipped:
        print(f"  Skipped (no evidence block found): {skipped}")
    if failed:
        print(f"  Failed (invalid JSON from model): {failed}")
    print("\nNext step: review each predicate above against the YAML and your own")
    print("judgement, then hand-write the validated action(s) into domain.pddl.")


if __name__ == "__main__":
    main()
