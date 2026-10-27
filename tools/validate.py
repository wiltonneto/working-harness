#!/usr/bin/env python3
"""Validate this clean distribution or an untouched assembled workspace. No writes."""

import argparse
import ast
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"\[[^\]\n]+\]\(([^)\s]+)\)")
MACHINE_PATH = re.compile(r"/(?:Users|home|Volumes)/[A-Za-z0-9_.-]+|[A-Za-z]:\\Users\\")
SECRET = re.compile(
    r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"
    r"|\b(?:AKIA|ASIA)[A-Z0-9]{16}\b"
    r"|\bgh[pousr]_[A-Za-z0-9]{30,}\b"
    r"|\bsk-[A-Za-z0-9_-]{24,}\b"
)


def check_tree(root):
    errors = []
    count = links = imports = 0
    for path in sorted(root.rglob("*")):
        if ".git" in path.relative_to(root).parts:
            continue
        if path.is_symlink():
            errors.append("symlink: " + str(path.relative_to(root)))
            continue
        if not path.is_file():
            continue
        count += 1
        if path.suffix not in (".md", ".py") and path.name not in (".gitignore", "LICENSE", "HARNESS_LICENSE"):
            errors.append("unexpected file type: " + str(path.relative_to(root)))
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeError:
            errors.append("non-text file: " + str(path.relative_to(root)))
            continue
        if MACHINE_PATH.search(text) or SECRET.search(text):
            errors.append("possible machine path or credential: " + str(path.relative_to(root)))
        if path.suffix == ".py":
            try:
                ast.parse(text, filename=str(path))
            except SyntaxError as exc:
                errors.append(str(exc))
        if path.suffix != ".md":
            continue
        for match in LINK.finditer(text):
            href = match.group(1)
            parsed = urlsplit(href)
            if parsed.scheme:
                if parsed.scheme != "https":
                    errors.append("unexpected link scheme in " + str(path.relative_to(root)))
                continue
            if href.startswith("/"):
                errors.append("absolute file link in " + str(path.relative_to(root)))
                continue
            target = (path.parent / unquote(parsed.path)).resolve()
            links += 1
            if not target.is_relative_to(root.resolve()) or not target.exists():
                errors.append("broken/outside link: " + str(path.relative_to(root)) + " -> " + href)
            if parsed.fragment:
                errors.append("anchor needs explicit validator support: " + href)
        if path.name == "CLAUDE.md":
            if text != "@AGENTS.md\n":
                errors.append("Claude entrypoint must be the thin local import: " + str(path.relative_to(root)))
            if not (path.parent / "AGENTS.md").is_file():
                errors.append("missing local AGENTS.md: " + str(path.relative_to(root)))
            imports += 1
    return errors, {"files": count, "local_links": links, "claude_imports": imports}


def check_workspace(workspace):
    errors = []
    contract = workspace / "cos/system/WORKING_AGREEMENT.md"
    if not contract.is_file():
        errors.append("missing canonical shared agreement")
    for role, route in [("cos", "system/WORKING_AGREEMENT.md"),
                        ("product", "../cos/system/WORKING_AGREEMENT.md")]:
        entry = workspace / role / "AGENTS.md"
        if not entry.is_file():
            errors.append("missing entrypoint for " + role)
            continue
        contents = entry.read_text()
        if route not in contents or "INSTRUCTIONS.md" not in contents:
            errors.append("canonical route missing for " + role)
        if (entry.parent / route).resolve() != contract.resolve():
            errors.append("shared canonical route diverges for " + role)
        if entry.stat().st_size > 1000:
            errors.append("entrypoint is no longer thin for " + role)
        for required in ["INSTRUCTIONS.md", "CLAUDE.md", "MEMORY.md", "session-log.md", ".gitignore", "HARNESS_LICENSE"]:
            if not (workspace / role / required).is_file():
                errors.append("missing " + role + "/" + required)
    notices = [workspace / role / "HARNESS_LICENSE" for role in ("cos", "product")]
    if all(path.is_file() for path in notices) and notices[0].read_bytes() != notices[1].read_bytes():
        errors.append("starter harness license notices differ")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", type=Path, help="validate a pristine assembled copy instead")
    args = parser.parse_args()
    root = args.workspace.resolve() if args.workspace else ROOT
    workspace = root if args.workspace else root / "starter/workspace"
    errors, counts = check_tree(root)
    errors.extend(check_workspace(workspace))
    if not args.workspace:
        license_path = root / "LICENSE"
        if not license_path.is_file():
            errors.append("missing distribution LICENSE")
        else:
            for role in ("cos", "product"):
                notice = workspace / role / "HARNESS_LICENSE"
                if notice.is_file() and notice.read_bytes() != license_path.read_bytes():
                    errors.append(role + " harness notice differs from distribution LICENSE")
    if errors:
        print("FAIL\n" + "\n".join(errors), file=sys.stderr)
        return 1
    print("PASS: " + ", ".join(str(value) + " " + key for key, value in counts.items())
          + "; canonical routes, thin entrypoints, Python syntax, text/path/credential checks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
