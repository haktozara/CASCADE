#!/usr/bin/env bash
# Demo: T1547.001 (registry Run key) -> plan the starter attack chain with Fast Downward.
# Needs only Fast Downward. No API key, no internet, no LLM calls.
#
# Usage:  FD=/path/to/fast-downward.py ./demo/run_demo.sh      (default: ~/downward/fast-downward.py)
#         ./demo/run_demo.sh --failure                         (also run the T1055 failure case)
set -e
cd "$(dirname "$0")/.."
FD="${FD:-$HOME/downward/fast-downward.py}"
[ -f "$FD" ] || { echo "Fast Downward not found at $FD - see demo/README.md"; exit 1; }
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT

echo "=== 1. Evidence: Atomic Red Team test definition (T1547.001, test 1) ==="
grep -n -m1 -A 12 "name: Reg Key Run" demo/T1547.001/T1547.001.yaml || true
echo
echo "=== 2. LLM-translated predicates (GPT-4.1, temp 0, after manual review) ==="
cat demo/T1547.001/T1547_001_test1_predicates.json
echo
echo "=== 3. The PDDL action built from that evidence ==="
grep -A 15 "set-registry-run-key" pddl/starter/domain.pddl | sed -n '/:action/,$p' | head -12
echo
echo "=== 4. Fast Downward plans the starter chain (T1059.001 -> T1547.001 -> T1003.001 -> T1021.002) ==="
ROOT="$PWD"
( cd "$TMP" && python3 "$FD" "$ROOT/pddl/starter/domain.pddl" "$ROOT/pddl/starter/problem.pddl" \
    --search "astar(blind())" 2>&1 | grep -E "Plan length|Plan cost|Solution found!" ; cat sas_plan )
if [ "$1" = "--failure" ]; then
  echo
  echo "=== 5. Failure case: T1055 (process injection) - no action exists, so no plan ==="
  ( cd "$TMP" && rm -f sas_plan && python3 "$FD" "$ROOT/pddl/domain.pddl" "$ROOT/pddl/problems/problem_t1055_FAILUREMODE.pddl" \
      --search "astar(blind())" 2>&1 | grep -E "Search stopped|Solution found|Completely explored|provably unsolvable" )
fi
