"""Reproduce every numerical test. No external dependencies or network access."""
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
MODULES = (
    "probe_checks.py", "physics_checks.py", "control_checks.py",
    "labor_checks.py", "dispatch_checks.py", "retained_checks.py",
)

def main():
    for name in MODULES:
        print(f"\n=== {name} ===", flush=True)
        subprocess.run([sys.executable, str(HERE / name)], cwd=HERE, check=True)
    print("\nAll six numerical modules completed successfully.")

if __name__ == "__main__":
    main()
