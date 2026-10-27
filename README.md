# Working harness

A work harness for a **solo founder running a digital company** with Claude Code or Codex. The founder owns direction and judgment. **The chief of staff coordinates; product repositories execute.**

CoS owns priorities, decisions, research, and the daily plan. Products own specs, code, tests, and current truth. A written baton carries work into product; evidence returns it to the coordination queue. Files carry context between sessions and tools.

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

Clone or use **Use this template**, and choose an unused workspace destination:

```sh
git clone https://github.com/wiltonneto/working-harness.git
cd working-harness
cp -R starter/workspace ../my-workspace
git -C ../my-workspace/cos init -b main
git -C ../my-workspace/product init -b main
```

Fill CoS `STATE.md` and product `PROJECT.md`, then review and commit each new repo's initial files. Run `claude` or `codex` inside `cos/` for coordination or `product/` for execution:

> Read AGENTS.md and the canonical instructions it links to. Report your role, authority, and missing configuration before changing anything.

Thin `AGENTS.md`/`CLAUDE.md` entrypoints share neutral instructions. Operational CoS and product have separate histories. [Setup](docs/setup.md) covers worktrees and additional products.

## Why the empty files exist

They provide homes for **your company's** state without invented history or inherited permissions. Fill them as work earns it. The [complete guide](docs/file-guide.md) covers every starter file, contents, owner, and update trigger.

| File(s) | What belongs there | Owner / when updated |
| --- | --- | --- |
| CoS `STATE.md` | Stage, risk, owner, time zone, delegation, ceilings | Human ratifies; CoS updates at setup or changed risk/authority |
| `priorities.md`, `BACKLOG.md`, `ROADMAP.md` | Now; ranked owned work; forward outcomes and gates | CoS when evidence or direction changes |
| `HYPOTHESES.md` | Beliefs, unknowns, contrary evidence, next tests | CoS after evidence; human rules strategic changes |
| `PRODUCTS.md`, `PARKING_LOT.md` | Repo map; deferred ideas with revival triggers | CoS when products or deferrals change |
| Both repos' `MEMORY.md`, `session-log.md` | Scoped durable pointers; dated outcomes, omissions, next actions | Respective role after a lesson / at session close |
| CoS `logs/decisions.md` | Why an actual ruling or delegated call was made | Authorized session through register door, per call |
| **CoS `logs/error-log.md`** | **Failures, surprises, near-misses, cause/unknown, class, lesson, guard/owner** | **Every role after an event; CoS reviews classes** |
| `logs/backlog-inbox.md` | Result facts, improvement proposals, acknowledgements | Authorized session through register door, per receipt |
| `logs/job-runs.md` | Start/end/state, output, usage, recovery owner | External runner if later configured; starts empty |
| Product `PROJECT.md`, `ARCHITECTURE.md` | Real commands/environments; map into actual code | Product at setup or tooling/code-structure changes |
| `STATUS.md` | Verified current build/environment/evidence/limits | Product when reality changes |
| `strategy/PRODUCT_PRINCIPLES.md` | This product's own rules and experience bar | Human/product when intent is established or revised |
| `strategy/HUMAN_TEST_QUEUE.md` | Agent-checked build, remaining human judgment, actual verdict | Product registers; human supplies verdict |
| Content directories and `templates/` | Dated batons, research, daily artifacts, specs, as-built and receipts | The owning role when the corresponding event happens |

## Logging must improve the harness

The [error log](starter/workspace/cos/logs/error-log.md) is a working input, not an archive nobody reads:

**Event -> error entry -> recurring-class review -> owned backlog improvement -> enforcer and verification -> updated queue and memory pointers.**

Use the [error-entry template](starter/workspace/cos/templates/error-entry.md) and register door. Keep unknown causes unknown; link recurrences. CoS ranks improvements; product implements code-related batons. A failure class needs a verified guard or explicit owner/deferral. Writing a lesson is not fixing it. The [learning workflow](starter/workspace/cos/system/learning-loop.md) defines this once for sessions and jobs.

## Evening work and the morning digest

These [portable contracts](starter/workspace/cos/system/jobs/README.md) extend work beyond the founder's working day:

| Job | Useful work | Morning input |
| --- | --- | --- |
| Evening review | Parse error classes into improvements; recheck/reprioritize backlog within delegation; finish clearly authorized, reversible, verifiable low-risk CoS tasks | Proposed versus verified fixes, queue changes, completed tasks, decisions/blocks |
| Deep research | A founder-requested question or proactively justified study tied to a real decision; CoS chooses depth, sources, limits, and stopping point | Evidence, contrary findings, synthesis, recommendation, uncertainty |
| Morning compile | Reconcile outputs with current truth and actual run states | One short digest and today's plan; detailed artifacts linked |

**Schedules and runners are not installed.** The [configuration template](starter/workspace/cos/system/jobs/job-config.template.md) starts disabled. An external runner must supply scheduling/time zone, permissions, usage limits, serialization, liveness/recovery, and separately authorized delivery. Those integrations are not included.

An absent human does not approve deployment, spend, access changes, messages, or publishing. Per-task authority still applies; missing authority or a required human ruling stops that lane. Product stays read-only in these evening presets. Cloning creates no jobs or credentials.

## One cycle

Fictional example: a reading-list app loses completion state. CoS scopes a baton; product fixes, verifies, and returns evidence, logging the missing check. Evening review turns the recurring class into an owned guard improvement; product work remains a baton. Justified research feeds morning judgment. The founder gets one digest of verified outcomes and decisions owed. [Full cycle](docs/work-cycle.md).

## Limits and checks

Keep this clean distribution separate from operational records. Instructions are not access controls; real commands, principles, permissions, release gates, and jobs require configuration. Both CLI read paths were tested on macOS; see [compatibility](docs/compatibility.md).

Python 3.9+ for the helpers:

```sh
python3 tools/validate.py
python3 tools/check_register.py
```

**License not yet selected.** Public availability does not grant an open-source license.
