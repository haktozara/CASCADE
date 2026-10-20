# Demo setup

You only need Fast Downward. No API key and no internet are needed to run the demo.

## Install Fast Downward (Linux / macOS / WSL)

```bash
sudo apt install cmake g++ make python3     # on Debian/Ubuntu/Kali/WSL
git clone https://github.com/aibasel/downward.git ~/downward
cd ~/downward && python3 build.py
```

## Run

From the repository root:

```bash
./demo/run_demo.sh              # main walkthrough
./demo/run_demo.sh --failure    # plus the T1055 failure case
FD=/other/path/fast-downward.py ./demo/run_demo.sh   # if installed elsewhere
```

Compare against `expected_output.txt`. The plan and its cost (4) should match exactly. The failure-case message depends on the Fast Downward version: recent versions print "Task is provably unsolvable.", older ones print "Search stopped without finding a solution."
