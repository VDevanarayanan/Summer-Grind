import subprocess
import json
import sys
result = subprocess.run(
    [sys.executable, "trail.py"],
    context_output=True,
    text=True
)
log = {
    "returncode": result.returncode,
    "stdout": result.stdout,
    "stderr": result.stderr
}
with open("log.json", "w")as f:
    json.dump(log, f, indent=4)
