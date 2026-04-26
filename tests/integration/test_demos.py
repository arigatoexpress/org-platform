import os
import subprocess
import sys
from pathlib import Path


def test_offline_demos_write_outputs(tmp_path: Path) -> None:
    env = os.environ.copy()
    env["ORG_PLATFORM_OFFLINE"] = "true"
    env["ORG_PLATFORM_OUTPUT_DIR"] = str(tmp_path)
    subprocess.run([sys.executable, "scripts/run_intel_demo.py"], check=True, env=env)
    subprocess.run([sys.executable, "scripts/run_crypto_demo.py"], check=True, env=env)

    assert (tmp_path / "data" / "intel" / "events.json").exists()
    assert (tmp_path / "data" / "crypto" / "watchlist.json").exists()
    assert list((tmp_path / "Intelligence").glob("iran-shipping-*.md"))
