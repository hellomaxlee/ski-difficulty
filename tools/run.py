"""
Start the Sugarbush Trail Analyzer web server.
Usage: uv run python tools/run.py
"""

import subprocess
import sys


def main():
    subprocess.run(
        [
            sys.executable, "-m", "uvicorn",
            "tools.app:app",
            "--reload",
            "--host", "0.0.0.0",
            "--port", "8000",
        ],
        check=True
    )


if __name__ == "__main__":
    main()
