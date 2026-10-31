from src.deploy import deploy


def rollback(previous_version):

    print("\n===== AUTOMATED ROLLBACK =====")

    if previous_version is None:

        print("No previous version available.")
        return False

    deploy(previous_version, "healthy")

    print(f"Rollback completed: {previous_version}")

    return True