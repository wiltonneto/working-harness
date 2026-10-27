#!/usr/bin/env python3
"""Exercise the authored register door in disposable copies only; no network."""

import concurrent.futures
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parent.parent


def main():
    with tempfile.TemporaryDirectory(prefix="harness-register-") as temp:
        cos = Path(temp) / "cos"
        shutil.copytree(ROOT / "starter/workspace/cos", cos)
        body = Path(temp) / "body.md"
        body.write_text("Fictional verification receipt. No operational event.\n", encoding="utf-8")
        script = cos / "system/register.py"

        def run(receipt_id, mode="backlog"):
            return subprocess.run(
                [sys.executable, str(script), mode, "--id", receipt_id,
                 "--session", "test", "--title", "Fictional outcome", "--body", str(body)],
                capture_output=True, text=True,
            )

        originals = {p.name: p.read_bytes() for p in (cos / "logs").iterdir()}
        assert run("R-one").returncode == 0
        inbox = cos / "logs/backlog-inbox.md"
        first = inbox.read_bytes()
        assert first.startswith(originals[inbox.name])
        assert run("R-one").returncode == 4
        assert inbox.read_bytes() == first
        # One ID cannot silently be reused on another surface either.
        assert run("R-one", "error").returncode == 4
        for mode, filename in [("decision", "decisions.md"), ("error", "error-log.md")]:
            assert run("R-" + mode, mode).returncode == 0
            assert (cos / "logs" / filename).read_bytes().startswith(originals[filename])
        assert run("../invalid").returncode != 0
        lock = cos / ".local/register.lock"
        lock.write_text("owned by test\n", encoding="utf-8")
        assert run("R-locked").returncode == 3
        assert lock.read_text() == "owned by test\n"
        lock.unlink()
        # Race the same ID: exactly one append succeeds; others are locked or duplicates.
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
            results = list(pool.map(lambda _: run("R-race").returncode, range(6)))
        assert results.count(0) == 1, results
        assert all(code in (0, 3, 4) for code in results), results
        assert inbox.read_text().count("<!-- receipt-id: R-race -->") == 1
        # Cross-file redirects must be refused without changing the redirect target.
        error_file = cos / "logs/error-log.md"
        error_file.unlink()
        outside = Path(temp) / "outside.md"
        outside.write_text("untouched", encoding="utf-8")
        error_file.symlink_to(outside)
        assert run("R-symlink").returncode != 0
        assert outside.read_text() == "untouched"
        error_file.unlink()
        error_file.write_bytes(originals[error_file.name])
        # A linked worktree must use the primary checkout's door.
        (cos / ".git").write_text("gitdir: fictional-worktree\n", encoding="utf-8")
        assert run("R-worktree").returncode != 0
        assert not lock.exists()
    print("PASS: append preservation, all modes, duplicate IDs, lock contention, concurrent ID race, symlink refusal, worktree refusal")


if __name__ == "__main__":
    main()
