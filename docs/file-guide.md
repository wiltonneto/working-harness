# What each starter file is for

The empty files are deliberate homes for the **new company's** state, not unfinished examples. They give the next session a known read path without importing someone else's decisions, incidents, research, or permissions. Fill STATE and PROJECT first; add other records when real work earns them. Do not invent history to make a table look active.

Paths below are relative to `starter/workspace/`. CoS owns coordination; product owns code-dependent truth. Dated records preserve the trail, while durable state is kept current. A role listed as owner still needs task authority and actual runtime permissions to write.

Both [cos/HARNESS_LICENSE](../starter/workspace/cos/HARNESS_LICENSE) and [product/HARNESS_LICENSE](../starter/workspace/product/HARNESS_LICENSE) preserve the distribution's [MIT license](../LICENSE) when the repos are copied separately. These notices cover inherited harness files, not a new company's independently authored content. Keep them; the template maintainer updates all notice copies together if licensing is deliberately revised.

## CoS current state and continuity

| File | Purpose / expected contents | Owner | Update trigger |
| --- | --- | --- | --- |
| [cos/STATE.md](../starter/workspace/cos/STATE.md) | Stage, risk surfaces, human owner, time zone, boundaries, delegation, ceilings, disabled/enabled job authority | Human ratifies; CoS maintains | Setup; new risk surface or explicit authority change |
| [cos/priorities.md](../starter/workspace/cos/priorities.md) | Workstream outcomes, verified current state, owner, next action, blockers | CoS | What matters now changes |
| [cos/BACKLOG.md](../starter/workspace/cos/BACKLOG.md) | Ranked owned work, evidence/error IDs, authority, acceptance/enforcer, next action | CoS | Receipt/review/ruling changes an item's premise or priority |
| [cos/ROADMAP.md](../starter/workspace/cos/ROADMAP.md) | Forward outcomes, prerequisites, evidence gates, review triggers | CoS within ruled direction | The forward arc changes; not every daily update |
| [cos/HYPOTHESES.md](../starter/workspace/cos/HYPOTHESES.md) | Convictions, testable beliefs, unknowns, supporting/contrary evidence, next test | CoS; human rules strategic adoption/killing | Research or product evidence changes belief |
| [cos/PRODUCTS.md](../starter/workspace/cos/PRODUCTS.md) | Product checkout map, instruction and status links | CoS | Add, rename, move, or retire a product |
| [cos/PARKING_LOT.md](../starter/workspace/cos/PARKING_LOT.md) | Deferred ideas with reason, owner, and a concrete revival trigger | CoS | Defer an idea or its trigger becomes true |
| [cos/MEMORY.md](../starter/workspace/cos/MEMORY.md) | Durable lesson/fact pointers, why useful, recheck trigger; no duplicate product facts | CoS | A lesson would change a future session's approach |
| [cos/session-log.md](../starter/workspace/cos/session-log.md) | Dated result/evidence/omissions, receipts, pending owners and exact next actions | Closing CoS session | End of substantive work; append corrections |
| [cos/thesis/README.md](../starter/workspace/cos/thesis/README.md) | Home for earned durable direction and its ruling/hypothesis links | CoS; human owns direction | A thesis is adopted or revised |
| [cos/ops/README.md](../starter/workspace/cos/ops/README.md) | Home for dated bounded batons, approval state, ruling and queue links | CoS | A coordination conclusion requires product execution |
| [cos/research/README.md](../starter/workspace/cos/research/README.md) | Home for dated studies: selection rationale, provenance, contrary evidence, synthesis and limits | Research session; CoS selects depth | A requested or justified proactive study is authorized |
| [cos/daily/README.md](../starter/workspace/cos/daily/README.md) | Home for real dated briefs/spines and distinct evening/research outputs with run IDs | Designated CoS writer / bounded job | Day opens, receipt arrives, or a configured run produces output |

## Logs and the learning loop

| File | Purpose / expected contents | Owner / writer | Update trigger |
| --- | --- | --- | --- |
| [cos/logs/decisions.md](../starter/workspace/cos/logs/decisions.md) | Why a ruling/delegated call was made, authority, evidence, trade-offs, affected task | CoS owns; all authorized roles use register `decision` | An actual call, explicitly labeled proposal, or correction |
| [cos/logs/error-log.md](../starter/workspace/cos/logs/error-log.md) | Failure/near-miss, evidence, cause or unknown, impact, class, lesson, enforcer/owner, status | CoS owns; every role uses register `error` | Failure, surprise, diagnosis, recurrence, or verified follow-up |
| [cos/logs/backlog-inbox.md](../starter/workspace/cos/logs/backlog-inbox.md) | Evidence-backed proposals, completion/blocker facts, CoS acknowledgements; no ranking | CoS owns; authorized roles use register `backlog` | A product result or learning review should change queue truth |
| [cos/logs/job-runs.md](../starter/workspace/cos/logs/job-runs.md) | Start/finish/state, attempt IDs, contract revision, outputs, total usage and recovery owner | Separately configured external runner, serialized | Before/after an external invocation; incomplete starts stay visible |

The error log starts empty, **not unused**. The standing [learning loop](../starter/workspace/cos/system/learning-loop.md) turns entries into reviewed classes, owned backlog improvements, verified guards, and updated read paths. The register helper handles the first three logs only. A job-run ledger writer and scheduler are not implemented by this template.

## Product current truth

| File | Purpose / expected contents | Owner | Update trigger |
| --- | --- | --- | --- |
| [product/PROJECT.md](../starter/workspace/product/PROJECT.md) | Purpose, real commands, source/test map, environments, review/release process, authority | Product owner; human approves extensions | Setup or project tooling/operating scope changes |
| [product/STATUS.md](../starter/workspace/product/STATUS.md) | What's actually built/verified/landed/live/accepted, with revision/environment/evidence/limits | Product | A current claim becomes true, false, or stale |
| [product/ARCHITECTURE.md](../starter/workspace/product/ARCHITECTURE.md) | Router from concern to code, spec and verification; no invented modules | Product | Code structure changes; use configured generation/check method |
| [product/strategy/PRODUCT_PRINCIPLES.md](../starter/workspace/product/strategy/PRODUCT_PRINCIPLES.md) | This product's durable decision rules and experience bar, distinct from operating principles | Human rules; product maintains | Product intent is established or deliberately revised |
| [product/strategy/HUMAN_TEST_QUEUE.md](../starter/workspace/product/strategy/HUMAN_TEST_QUEUE.md) | Exact build/environment, agent checks, 1–3 human steps, expected experience/cost, actual verdict | Product registers; human supplies verdict | Human judgment remains after agent checks; revision/verdict changes |
| [product/MEMORY.md](../starter/workspace/product/MEMORY.md) | Product-scoped pointers to reusable implementation lessons, with recheck trigger | Product | A durable code-related lesson is learned |
| [product/session-log.md](../starter/workspace/product/session-log.md) | Dated results, omissions, receipts/delivery state, blockers, next action | Closing product session | End of substantive work or delivery outcome update |
| [product/spec/README.md](../starter/workspace/product/spec/README.md) | Home/index for behavior law, linked ruling and acceptance; spec changes before code | Product | Authorized behavior changes |

## Fillable shapes, not live records

Copy a template to a real task/date/run path and fill it; keep the reusable shape clean. A template or example is never a ruling, incident, run, or test verdict.

| Template | What to fill | Owner / trigger |
| --- | --- | --- |
| [cos/templates/baton.md](../starter/workspace/cos/templates/baton.md) | Authority, scope/exclusions, verified premise, acceptance, budget/rollback, return contract | CoS when handing work to product |
| [cos/templates/error-entry.md](../starter/workspace/cos/templates/error-entry.md) | Evidence, cause/unknown, class, recurrence, lesson, fix/guard/owner and closure proof | Any role after a failure, surprise, or near-miss |
| [cos/templates/session-close.md](../starter/workspace/cos/templates/session-close.md) | Outcomes, decisions, omitted checks, learning-loop IDs, pending work and next action | Each substantive session at close |
| [cos/templates/daily.md](../starter/workspace/cos/templates/daily.md) | Brief, overnight consequences, research, human rulings, today's owned task spine | Designated CoS writer at daily compile/update |
| [product/spec/prompts/_TEMPLATE.md](../starter/workspace/product/spec/prompts/_TEMPLATE.md) | Baton/ruling, source verification, scope, spec, checks, authority, acceptance and closeout | Product at task open |
| [product/docs/AS_BUILT_TEMPLATE.md](../starter/workspace/product/docs/AS_BUILT_TEMPLATE.md) | Actual behavior, revision/environment, checks, limits, human residue and return receipt | Product when delivery is ready to report |
| [product/receipts/_TEMPLATE.md](../starter/workspace/product/receipts/_TEMPLATE.md) | Stable ID, factual outcome, original authority and evidence links valid from CoS logs | Product when returning facts; preserve body after registration |
| [cos/system/jobs/job-config.template.md](../starter/workspace/cos/system/jobs/job-config.template.md) | Disabled job config: owner, time zone, runner, allowlists, tasks/authority, limits, outputs and recovery | Human/CoS before proposing an external job integration |

## Durable instructions and mechanisms

These files are already populated because they explain the operating system. Edit their canonical home deliberately; do not fill them with session history.

| Files | Purpose and owner / update trigger |
| --- | --- |
| [WORKSPACE.md](../starter/workspace/WORKSPACE.md), workspace [AGENTS.md](../starter/workspace/AGENTS.md), [CLAUDE.md](../starter/workspace/CLAUDE.md) | Human/CoS-maintained workspace map and optional thin router; change when layout changes |
| CoS [AGENTS.md](../starter/workspace/cos/AGENTS.md)/[CLAUDE.md](../starter/workspace/cos/CLAUDE.md), product [AGENTS.md](../starter/workspace/product/AGENTS.md)/[CLAUDE.md](../starter/workspace/product/CLAUDE.md) | Thin local tool entrypoints; maintainer changes only when routing changes |
| [cos/system/WORKING_AGREEMENT.md](../starter/workspace/cos/system/WORKING_AGREEMENT.md) | Shared operating principles, delegation, evidence and coordination rules; human ratifies changes |
| CoS [INSTRUCTIONS.md](../starter/workspace/cos/INSTRUCTIONS.md), product [INSTRUCTIONS.md](../starter/workspace/product/INSTRUCTIONS.md) | Role responsibilities and read/close paths; role owner changes when workflow changes |
| [cos/OPERATING_SYSTEM.md](../starter/workspace/cos/OPERATING_SYSTEM.md) | CoS cadence, depth control, learning and reflection; change when the operating rhythm changes |
| [cos/system/learning-loop.md](../starter/workspace/cos/system/learning-loop.md) | Shared log/review/backlog/enforcement/verification workflow; change when the learning mechanism changes |
| [cos/system/register.py](../starter/workspace/cos/system/register.py) | Reviewed serialized append mechanism for error/decision/inbox records; maintainer changes with meaningful behavior tests |
| [cos/system/maintenance.md](../starter/workspace/cos/system/maintenance.md) | Thin manual pointer to the canonical review contract, avoiding a second rule copy |
| [cos/system/jobs/README.md](../starter/workspace/cos/system/jobs/README.md) | External-runner configuration and stop boundaries; human/CoS change only under approved scope |
| [evening-review.md](../starter/workspace/cos/system/jobs/evening-review.md), [deep-research.md](../starter/workspace/cos/system/jobs/deep-research.md), [morning-compile.md](../starter/workspace/cos/system/jobs/morning-compile.md) | Portable job-specific prompts; job maintainer reviews changes interactively, never an unattended job rewriting itself |
| [product/docs/COORDINATION.md](../starter/workspace/product/docs/COORDINATION.md) | Product-to-CoS receipt transport, link origin, duplicate/uncertain outcomes; change when bridge behavior changes |
| CoS [.gitignore](../starter/workspace/cos/.gitignore), product [.gitignore](../starter/workspace/product/.gitignore) | Exclude local/private generated state; repo owner reviews when storage changes. Ignore rules do not sanitize committed history. |

The distribution's [setup](setup.md), [model](operating-model.md), [cycle](work-cycle.md), and [compatibility](compatibility.md) docs explain reuse. `tools/validate.py` checks the clean distribution or pristine assembled copy; `tools/check_register.py` exercises the append mechanism in disposable copies. Neither installs jobs or operates a company.
