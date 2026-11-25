"""Run the two papers' numerical replications from any working directory."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
PROGRAMS = (
    'run_all.py',
    'figures.py',
    'deployment/first_site.py',
    'deployment/learning_state.py',
    'deployment/check_stationary_policy.py',
    'deployment/allocation_and_bids.py',
    'deployment/competition.py',
)

if __name__ == '__main__':
    for name in PROGRAMS:
        path = ROOT / name
        print(f'\nRunning {name}', flush=True)
        subprocess.run([sys.executable, str(path)], cwd=path.parent, check=True)
