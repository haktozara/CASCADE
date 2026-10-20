# Symbolic Attack Chain Generation from Atomic Red Team Techniques

**An empirical study of predicate representation granularity** — MSc Cyber Security dissertation (CSC8209), Newcastle University, by Ramya Varunsegar.

📄 Paper: [`paper/preprint.pdf`](paper/preprint.pdf)

## The question

Does a reduced **five-category** predicate scheme (Executor, Process, Privilege/User, Information, Environment) give equivalent planning outcomes to AURORA's **nine-category** Attack Action Linking Model (AALM) when generating symbolic attack chains?

## How it works

```
Atomic Red Team test  ──►  GPT-4.1 (temp 0)  ──►  manual review  ──►  PDDL domain  ──►  Fast Downward  ──►  attack chain
   (YAML + real run)       translator only      89 corrections       actions            A* planner          or "no plan"
```

**The LLM proposes. Fast Downward decides.** GPT-4.1 only translates evidence into candidate predicates. It never reasons about the plan. Corrections are applied by a deterministic script, not by an LLM.

## Try the demo (5 minutes, no API key)

1. Install [Fast Downward](https://www.fast-downward.org/) (see [`demo/README.md`](demo/README.md)).
2. Run:
   ```bash
   FD=/path/to/fast-downward.py ./demo/run_demo.sh --failure
   ```
3. Compare with [`demo/expected_output.txt`](demo/expected_output.txt).

It walks through technique **T1547.001** (registry Run keys): the ART evidence → the predicates → the PDDL action → the planner resolving a four-step chain at cost 4, then the **T1055** failure case, where the planner correctly reports no plan exists.

## Headline numbers

| | |
|---|---|
| Corpus | 16 ATT&CK techniques from Atomic Red Team |
| Predicates cross-checked | 808 |
| Corrections applied | 89 (11.0%) |
| Techniques solved | 13 / 16 (81.3%) |
| Mean ΔPi | 0.125 |
| Genuine resolution gain | 1 technique (T1560.001) |

## What this does and does not show

Please read this before citing any number above.

- **The nine-category domain is a byte-identical relabelling** of the five-category domain, so identical plan validity and cost hold **by construction**. They are not an independent empirical finding.
- The **81.3%** figure is a correctness check on the pipeline. It is not the granularity result.
- **ΔPi** is the only metric that can show a granularity effect. The one genuine finding is T1560.001 (1 of 16). T1003.001's ΔPi = 1 is an artefact of placeholder-only representation.
- The Jaccard = 1.0 / edit distance = 0 fidelity check is a pipeline-correctness check, not independent ground-truth validation. The circularity is disclosed in the paper.
- T1055 fails 0/13 largely because Defender (AV/EDR) was active on the test VM. That is a property of this environment, not necessarily of the technique.
- The starter-chain problem sets `lsass-memory-accessible` as a **placeholder**: all T1003.001 sub-tests failed on the real VM.
- Technique labels use pre-v19 MITRE ATT&CK.

## Repository map

| Folder | Contents |
|---|---|
| `paper/` | Preprint |
| `pddl/` | Five- and nine-category domains, 12 per-technique problem files, and the starter-chain domain/problem used in the demo |
| `data/ART.zip` | Evidence (ART YAML + execution logs) and reviewed predicate JSON for all 16 techniques |
| `code/` | Translation (`art_to_pddl.py`), deterministic corrections (`apply_corrections.py`), cross-check table (`predicate_table.py`), review helper |
| `results/` | Corrections manifest (89 rows) and log, cross-check report, category-resolution and fidelity CSVs, review worklist, figures |
| `demo/` | `run_demo.sh`, expected output, T1547.001 evidence |

To re-run translation you need an OpenAI API key in the `OPENAI_API_KEY` environment variable (`pip install -r requirements.txt`).

## Credits

- [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) (Red Canary) — evidence source; YAML definitions retain their original licence.
- [Fast Downward](https://www.fast-downward.org/) — planner.
- AURORA / AALM — the nine-category model compared against.

## Licence

Code: MIT (see `LICENSE`).
