from src.report import generate_report
from src.deploy import deploy, get_current_version
from src.health_check import check_health
from src.rollback import rollback


def run_pipeline():

    print("\n===== CI/CD PIPELINE STARTED =====")

    # Step 1: Deploy stable version
    print("\nStep 1: Deploying stable version")

    deploy("v1", "healthy")

    previous_version = get_current_version()

    print(f"Stable version: {previous_version}")

    # Step 2: Deploy new version
    print("\nStep 2: Deploying new version")

    deploy("v2", "unhealthy")

    # Step 3: Health check
    print("\nStep 3: Checking application health")

    health = check_health()

    # Step 4: Rollback
    if not health:

        print("\nApplication failure detected!")

        rollback(previous_version)

    # Step 5: Final health check
    print("\nStep 4: Final health check")

    final_health = check_health()

    if final_health:

        print("\nPipeline Result: SUCCESS")

        print("Application recovered successfully.")

    else:

        print("\nPipeline Result: FAILURE")
    # Step 5: Final health check
    print("\nStep 4: Final health check")

    final_health = check_health()

    final_version = get_current_version()

    if final_health:

        print("\nPipeline Result: SUCCESS")

        print("Application recovered successfully.")

        generate_report(
            "SUCCESS",
            final_version
        )

    else:

        print("\nPipeline Result: FAILURE")

        generate_report(
            "FAILURE",
            final_version
        )

if __name__ == "__main__":
    run_pipeline()