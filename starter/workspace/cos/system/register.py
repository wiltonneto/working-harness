#!/usr/bin/env python3
"""Append one receipt to the canonical CoS registers. Python 3.9+, stdlib only.

No Git commands, shell commands, network, commits, pushes, or priority changes.
One lock serializes writers using this door; it cannot constrain raw file edits.
After a crash, inspect receipt IDs and lock ownership before recovery or retry.
"""

import argparse
import datetime
import json
import os
from pathlib import Path
import re
import sys


TARGETS = {
    "decision": "decisions.md",
    "error": "error-log.md",
    "backlog": "backlog-inbox.md",
}
TOKEN = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,79}\Z")
MAX_BODY = 128 * 1024


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=TARGETS)
    parser.add_argument("--id", required=True, dest="receipt_id")
    parser.add_argument("--session", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--body", required=True, type=Path)
    args = parser.parse_args()
    if not TOKEN.fullmatch(args.receipt_id) or not TOKEN.fullmatch(args.session):
        parser.error("ID and session must be 1-80 letters, digits, dots, underscores, or hyphens")
    if not args.title.strip() or len(args.title) > 180 or any(ord(c) < 32 for c in args.title):
        parser.error("title must be one nonempty line of at most 180 characters")

    cos = Path(__file__).resolve().parent.parent
    if (cos / ".git").is_file():
        parser.error("target is a linked worktree; use the canonical CoS checkout's helper")
    logs = cos / "logs"
    local = cos / ".local"
    if logs.is_symlink() or local.is_symlink():
        parser.error("register directories must not be symlinks")
    paths = [logs / name for name in TARGETS.values()]
    if any(p.is_symlink() or not p.is_file() for p in paths):
        parser.error("all canonical register files must exist as regular files")
    try:
        with args.body.open("rb") as source:
            raw = source.read(MAX_BODY + 1)
        if len(raw) > MAX_BODY:
            parser.error("body exceeds 128 KiB")
        body = raw.decode("utf-8").strip()
        if not body or "<!-- receipt-id:" in body:
            parser.error("body must be nonempty and cannot contain a register receipt marker")
        local.mkdir(exist_ok=True)
    except (OSError, UnicodeError) as exc:
        parser.error(str(exc))

    stamp = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    lock = local / "register.lock"
    lock_flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0)
    try:
        lock_fd = os.open(str(lock), lock_flags, 0o600)
    except FileExistsError:
        print("PENDING: register lock exists; inspect ownership, do not auto-break: " + str(lock), file=sys.stderr)
        return 3
    except OSError as exc:
        print("PENDING: cannot acquire register lock: " + str(exc), file=sys.stderr)
        return 3

    try:
        with os.fdopen(lock_fd, "w", encoding="utf-8") as held:
            json.dump({"pid": os.getpid(), "session": args.session, "time": stamp}, held)
            held.flush()
            os.fsync(held.fileno())
        marker = "<!-- receipt-id: " + args.receipt_id + " -->"
        if any(marker in path.read_text(encoding="utf-8") for path in paths):
            print("DUPLICATE: inspect existing receipt " + args.receipt_id + " before retrying", file=sys.stderr)
            return 4
        target = logs / TARGETS[args.mode]
        entry = (
            "\n\n" + marker + "\n## " + args.receipt_id + " — " + args.title.strip()
            + "\n\n- Recorded (UTC): " + stamp + "\n- Session: " + args.session
            + "\n- Mode: " + args.mode + "\n\n" + body + "\n"
        ).encode("utf-8")
        flags = os.O_WRONLY | os.O_APPEND | getattr(os, "O_NOFOLLOW", 0)
        fd = os.open(str(target), flags)
        with os.fdopen(fd, "ab") as destination:
            destination.write(entry)
            destination.flush()
            os.fsync(destination.fileno())
        print(json.dumps({"status": "recorded", "id": args.receipt_id,
                          "target": "logs/" + target.name, "time": stamp}))
        return 0
    except (OSError, UnicodeError) as exc:
        print("UNCERTAIN: inspect receipt ID before retrying: " + str(exc), file=sys.stderr)
        return 5
    finally:
        lock.unlink()


if __name__ == "__main__":
    sys.exit(main())
