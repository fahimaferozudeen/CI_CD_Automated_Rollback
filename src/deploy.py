import json
from pathlib import Path

STATE_FILE = Path("deployment_state.json")


def deploy(version, status="healthy"):

    state = {
        "version": version,
        "status": status
    }

    STATE_FILE.write_text(
        json.dumps(state, indent=4)
    )

    print(f"Deploying {version}...")
    print(f"Deployment status: {status}")


def get_current_version():

    if not STATE_FILE.exists():
        return None

    state = json.loads(
        STATE_FILE.read_text()
    )

    return state["version"]