# Working harness

A file-based operating system for working with Claude Code or Codex: **the chief of staff coordinates; product repositories execute.** The human owns direction and judgment. Agents carry authorized work through implementation, verification, and closeout.

CoS owns priorities, hypotheses, decisions, and the daily plan. Each product owns its specs, code, tests, and current status. A written baton carries work into product; evidence and a return receipt bring the result back to the coordination queue.

## Structure

```text
docs/                       Setup, operating model, and a full example
tools/                      Link/instruction checks and register tests
starter/workspace/
  cos/                      Coordination repo starter
    system/WORKING_AGREEMENT.md   Shared canonical instructions
  product/                  Execution repo starter
```

Each repo has thin `AGENTS.md` and `CLAUDE.md` entrypoints pointing to the same neutral instructions. The distribution is one Git repository; your operational workspace uses separate CoS and product histories.

## Quick start

Clone this repository or use GitHub's **Use this template** button. Choose an unused workspace destination:

```sh
git clone https://github.com/wiltonneto/working-harness.git
cd working-harness
cp -R starter/workspace ../my-workspace
git -C ../my-workspace/cos init -b main
git -C ../my-workspace/product init -b main
```

Review and commit the initial files in each new repo. Start `claude` or `codex` inside `cos/` for coordination, or inside `product/` for execution. Begin with:

> Read AGENTS.md and the canonical instructions it links to. Report your role, authority, and missing configuration before changing anything.

See [setup](docs/setup.md) for worktrees, multiple products, and existing repositories. Keep this clean distribution separate from filled company records.

## One workflow

Fictional example: a reading-list app loses completion state after restart.

1. CoS records the authorized scope, ranks the task, and writes a baton with acceptance criteria.
2. Product verifies the symptom, updates the behavior spec, implements the fix, and runs checks.
3. Product records the exact revision and evidence, then files a return receipt through the serialized register helper.
4. CoS verifies the result and updates the queue. Human judgment is requested only where still needed.

The [full cycle](docs/work-cycle.md) shows the artifacts and failure paths. [The operating model](docs/operating-model.md) distinguishes observed practices from template adaptations.

## Customize

- CoS `STATE.md`: owner, risk stage, time zone, boundaries, authority, and ceilings.
- CoS priorities, hypotheses, and product registry: your actual direction and work.
- Product `PROJECT.md` and `strategy/PRODUCT_PRINCIPLES.md`: commands, environments, acceptance bar, and review/release process.

## Limits and checks

This is a working convention, not an application or permission system. It installs no scheduler, deployment integration, credentials, or services. Commands and operational authority begin unconfigured. Operational copies can contain private information; reuse the clean starter, not a company's filled workspace.

Python 3.9+ is needed for the helpers. From this repository:

```sh
python3 tools/validate.py
python3 tools/check_register.py
```

The shared-instruction read path was tested with both CLIs on macOS. [Compatibility notes](docs/compatibility.md) cover the tested scope, sibling-directory assumptions, and runtime permissions.

**License not yet selected.** Public availability does not grant an open-source license.
