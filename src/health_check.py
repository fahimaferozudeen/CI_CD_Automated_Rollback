import json
from pathlib import Path

STATE_FILE = Path("deployment_state.json")


def check_health():

    if not STATE_FILE.exists():
        print("Health Check: FAILED")
        return False

    state = json.loads(
        STATE_FILE.read_text()
    )

    if state["status"] == "healthy":

        print("Health Check: SUCCESS")
        return True

    print("Health Check: FAILED")
    return False