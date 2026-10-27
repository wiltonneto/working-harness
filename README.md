# Working harness

A work harness for a **solo founder running a digital company** with Claude Code or Codex. The founder owns direction and judgment. **The chief of staff coordinates; product repositories execute.**

CoS owns priorities, decisions, research, and the daily plan; products own specs, code, tests, and current truth. A written baton carries work into product, and evidence returns it to the queue. Files preserve context between sessions.

## Operating principles

These summarize practices evidenced in the source operating system, not a particular product's principles:

1. **Truth over comfort:** verify, challenge assumptions, and label uncertainty.
2. **Velocity with depth control:** move routine work quickly; name the questions that earn deeper work.
3. **The founder decides; the system does the work:** finish delegated work without turning the founder into an execution bottleneck.
4. **Measure what's working; kill what isn't:** recheck outcomes and stale premises.
5. **Magic before scale:** establish felt value before scaling distribution, hiring, or infrastructure.
6. **State-aware and self-revising:** change the process as risk changes, and turn reflection into a better mechanism.

The [shared working agreement](starter/workspace/cos/system/WORKING_AGREEMENT.md) is canonical for both tools. [The operating model](docs/operating-model.md) separates observed practices from proposed defaults such as disabled jobs and zero paid spend.

## Structure and quick start

```text
docs/                       Setup, file guide, operating model, example
tools/                      Validation and register behavior checks
starter/workspace/
  cos/                      Coordination repository starter
    system/WORKING_AGREEMENT.md   Shared canonical instructions
    system/learning-loop.md      Errors -> reviewed improvements
    system/jobs/                 External-job contracts; nothing scheduled
  product/                  Execution repository starter
```

Prerequisites: Git, Python 3.9+, and either Claude Code or Codex already installed and authenticated. This repository installs the harness files, not the CLI, a model, an application server, or scheduled jobs.

Run from a directory that should contain both new folders. Use unused destination names; the guarded block stops rather than copying over an existing workspace:

```sh
(
  set -eu
  git clone https://github.com/wiltonneto/working-harness.git
  cd working-harness
  python3 tools/validate.py
  python3 tools/check_register.py
  test ! -e ../my-workspace
  cp -R starter/workspace ../my-workspace
  git -C ../my-workspace/cos init -b main
  git -C ../my-workspace/product init -b main
  python3 tools/validate.py --workspace ../my-workspace
)
```

This leaves sibling `working-harness/` (clean reference) and `my-workspace/{cos,product}` (independent operating repos). Do not initialize the enclosing workspace as one repo. The starter copies preserve the harness's MIT notice; choose licensing for your own product separately.

Configure `cos/STATE.md` first, then `product/PROJECT.md`, product principles, and CoS priorities/hypotheses/registry. Review and commit each fresh repo's initial files before task worktrees. Keep spend and external/production authority disabled until explicitly extended. [Setup](docs/setup.md) covers worktrees, existing projects, and additional products.

## First use

From the same parent directory, choose one read-only bootstrap:

```sh
(cd my-workspace/cos && claude --permission-mode plan)
# or
codex -C my-workspace/cos --sandbox read-only --ask-for-approval on-request
```

For a separate execution session, replace `cos` with `product`. Both use thin `AGENTS.md`/`CLAUDE.md` entrypoints pointing to the shared contract. Start with:

> Read AGENTS.md, the linked shared agreement, and INSTRUCTIONS.md. Report the files read, your role, authority, and missing configuration. Do not modify anything.

Once bootstrap and configuration are reviewed, allow only the local edits needed for the assigned task. Use a fresh owned worktree per session and keep approval prompts enabled; no bypass/full-access mode is needed.

## Why the empty files exist

They are known homes for your company's state, without invented history or inherited permissions. Fill them when real events occur. The [file guide](docs/file-guide.md) gives every file's expected contents, owner, and update trigger.

| Files | Purpose / who updates them |
| --- | --- |
| CoS `STATE.md`; `priorities.md`, `BACKLOG.md`, `ROADMAP.md` | Authority/risk; now, ranked work, forward arc. Human ratifies authority; CoS updates when evidence/direction changes. |
| `HYPOTHESES.md`, `PRODUCTS.md`, `PARKING_LOT.md` | Beliefs/tests, repo map, deferred ideas/triggers. CoS maintains as these change. |
| Both repos' `MEMORY.md`, `session-log.md` | Scoped lesson pointers and dated outcomes/next actions. Each role writes after learning/at close. |
| CoS `logs/decisions.md`, **`error-log.md`**, `backlog-inbox.md` | Rulings, failures/lessons, and result/improvement facts. Authorized sessions append through the register door; CoS reviews and ranks. |
| `logs/job-runs.md` | Start/finish/state/usage, written by an external runner only if later configured. |
| Product `PROJECT.md`, `ARCHITECTURE.md`, `STATUS.md` | Commands/environment, code map, verified truth. Product updates at setup or relevant changes. |
| Product `strategy/`; content directories and templates | Product principles, human judgments; batons, research, daily outputs, specs and receipts. The owning role fills the appropriate shape per event. |

## Logging must improve the harness

The [error log](starter/workspace/cos/logs/error-log.md) is a working input, not an archive nobody reads:

**Event -> error entry -> recurring-class review -> owned backlog improvement -> enforcer and verification -> updated queue and memory pointers.**

Use the [error-entry template](starter/workspace/cos/templates/error-entry.md) and register door. Keep unknown causes unknown; link recurrences. CoS ranks improvements; product implements code-related batons. A failure class needs a verified guard or explicit owner/deferral. Writing a lesson is not fixing it. The [learning workflow](starter/workspace/cos/system/learning-loop.md) defines this once for sessions and jobs.

## Evening work and the morning digest

The [portable contracts](starter/workspace/cos/system/jobs/README.md) describe:

- **Evening review:** error classes -> improvements; evidence-based backlog triage; qualified low-risk CoS tasks.
- **Deep research:** requested or proactively justified studies that earn depth for a real decision.
- **Morning compile:** one digest of verified outcomes, research implications, and judgments still owed.

**No schedules or runners are installed.** The [config template](starter/workspace/cos/system/jobs/job-config.template.md) starts disabled. The external runner must enforce permissions, usage, serialization, liveness/recovery, and separately authorized delivery. Every task still needs authority; an absent human does not approve spend, deploys, access changes, messages, or publishing. Product stays read-only in these evening presets.

## First task

Start documentation-only: CoS writes a bounded baton for a five-step manual-verification checklist for the product idea in `PROJECT.md`. Product creates the checklist with expected outcomes, assumptions and limits, verifies its links, and returns a receipt; CoS updates the queue. No build, installation, deployment, paid call, or fabricated incident is needed. [Full work cycle](docs/work-cycle.md).

## Limits and checks

Keep this clean distribution separate from operational records. Instructions are not access controls; real commands, principles, permissions, release gates, and jobs require configuration. Both CLI read paths were tested on macOS; see [compatibility](docs/compatibility.md).

Licensed under the [MIT License](LICENSE). Preserve the copyright and permission notice when copying the harness.
