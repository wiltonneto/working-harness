# External jobs: evening work -> morning decisions

These are portable contracts for a scheduler outside this repository. **Nothing is scheduled, installed, enabled, or authorized by these files.** You may run a configured contract manually first; wiring launchd, cron, a service, or an agent scheduler is a separate action requiring the owner's approval.

The source operating model uses the hours without the founder for evidence review, bounded internal work, and research that earns its depth. The reusable parts are the prompts and artifact flow. Machine-specific schedules, launchers, credentials, production permissions, and notification channels are not included.

## Jobs and their seams

| Contract | Inputs | Output | Authority |
| --- | --- | --- | --- |
| [Evening review](evening-review.md) | Current queue and priorities; receipts; recent errors/open classes; current artifacts | Dated review, improvement proposals, re-derived rankings, and any completed authorized CoS task evidence | Reads by default. CoS queue edits and each execution task require recorded scope. Product stays read-only in this preset. |
| [Deep research](deep-research.md) | Founder requests, active hypotheses, blocked decisions, approved source/tool and usage limits | Dated sourced research, contrary findings, implications, and morning summary | A request or a justified proactive topic inside delegated research scope; no new spend/provider/access. |
| [Morning compile](morning-compile.md) | Latest completed/partial outputs, job run states, current queue/status, human rulings | A short brief and today's coordination spine | One designated CoS writer; artifact creation only. Sending a digest needs separate authorization. |

Run evening review and research serially in one orchestration, or give separate jobs disjoint outputs and a real shared-writer protocol. Both feed morning compile; morning compile does not wait forever or invent missing results. Do not fork the shared operating rules into three scheduler prompts: each contract reads the canonical [agreement](../WORKING_AGREEMENT.md), [STATE](../../STATE.md), and its linked workflows.

## Configure a runner later

1. Copy and fill the [job configuration template](job-config.template.md) in your operational workspace. Keep `enabled: false` until the human approves the integration. Resolve every unset field. Pick local evening/morning times and an IANA time zone; no example time is a schedule.
2. Point the external runner at the approved repo/worktree and contract file. Pass only the config path, run ID, date/time zone, and approved task IDs. Use existing permitted authentication; no API fallback, credential export, or silent provider change.
3. Enforce the read/write allowlist, invocation/time/usage ceilings, and denial policy in the runner's actual permissions. Prompts do not enforce them. With missing authority, an unavailable source/tool, or a new ruling, stop the dependent lane and write the exact blocker.
4. Serialize canonical writes. Reserve the job's CoS workspace and output paths; check live ownership and dirty files. A clean tree alone is not proof of no other writer. Shared error/decision/inbox appends still use [register.py](../register.py). The external runner owns and serializes [job-runs.md](../../logs/job-runs.md); the model does not raw-edit that ledger. No run-ledger writer is implemented here.
5. Record STARTED before invoking the model. Record terminal status and the full attempt's usage on every exit the runner can observe: COMPLETED / PARTIAL / FAILED / SKIPPED / BLOCKED. Preserve every attempt, not only the final retry. A stale STARTED is INCOMPLETE/UNKNOWN; a missing record is UNKNOWN, not proof that a job never ran. After an uncertain outcome, inspect existing outputs and receipt IDs before retrying.
6. Manually drive and inspect one complete cycle, including a refusal/failure path and the next morning's consumption, before scheduling it. Confirm paths, time zone, restart behavior, conflict handling, permissions, and budget observation. The creator must supply the runner/locking implementation and its tests; these Markdown contracts do not claim it exists.
7. Only then enable the external schedule under explicit authority. Keep the runner able to disable a job without deleting its artifacts. Do not enable sends/notifications as a side effect of enabling artifact generation.

## Shared stop boundaries

Read the per-task authority afresh. **An absent human is not approval.** Do not deploy, merge or push, spend paid-provider funds, change access/credentials, contact people, or make public changes unless that exact action is authorized by a separate applicable contract. These presets authorize none of those actions. Subscription runs also need an agreed invocation/time allowance; a zero paid-API budget does not mean unlimited usage.

Do not change your own contract, permissions, ceilings, or schedule. Do not break locks, take over another session's files/processes, or hunt for equivalent commands after a denial. If scope, evidence, resource ownership, or remaining budget is uncertain, stop that lane, name the gap, and continue only independent work already permitted. Proposals about the harness's own instructions remain proposals for an interactive review.

No result may imply HUMAN_ACCEPTED, LIVE, or even VERIFIED unless its evidence supports that state. Leave detailed evidence on disk and bring a concise consequence-first digest to the morning decision surface.
