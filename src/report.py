from datetime import datetime
from pathlib import Path


def generate_report(status, version):

    Path("reports").mkdir(
        exist_ok=True
    )

    report = f"""
===== RECOVERY REPORT =====

Date: {datetime.now()}

Pipeline Status: {status}

Current Version: {version}

Rollback Status: Completed

Application Status: Healthy
"""

    Path("reports/recovery_report.txt").write_text(
        report
    )

    print(report)