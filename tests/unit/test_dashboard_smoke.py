import subprocess
import sys


def test_dashboard_smoke_is_read_only() -> None:
    result = subprocess.run(
        [sys.executable, "scripts/check_dashboard_smoke.py"],
        check=True,
        capture_output=True,
        text=True,
    )

    assert "dashboard-smoke ok:" in result.stdout
