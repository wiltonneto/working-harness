# Job configuration — non-executable template

This file installs no scheduler and grants no authority. Fill a private operational copy; link canonical instructions instead of pasting them into a tool-specific job definition. Unset required fields mean BLOCKED, not a default permission.

| Field | Initial value / required contents |
| --- | --- |
| enabled | `false` |
| job_id / owner / recovery owner | UNSET; who runs it and who handles failures |
| contract | One of the linked contracts in [README](README.md) |
| canonical agreement / STATE | [WORKING_AGREEMENT](../WORKING_AGREEMENT.md) and [STATE](../../STATE.md), read fresh each run |
| scheduler / launcher | UNSET; external service or local runner, not implemented here |
| cadence / local time / IANA time zone | UNSET; owner chooses and authorizes later |
| auth / model | Existing approved subscription or other explicitly approved runtime; no new credentials or API fallback |
| workspace / baseline / ownership | UNSET; approved relative checkout/worktree, revision, single writer, and conflict/lock protocol |
| read allowlist | UNSET; only relevant repo instructions, state, queue, errors, receipts, and approved research sources |
| write allowlist | Distinct dated output paths only until explicitly extended; no product writes in these presets |
| output paths / run ID | Unique run ID; dated `daily/` output; research artifacts under `research/`; body links resolvable from their destination |
| runner ledger | [logs/job-runs.md](../../logs/job-runs.md); runner must implement serialized STARTED/terminal writes and incomplete-run handling |
| allowed tasks | Empty. Use the per-task table below; no task qualifies merely by appearing in BACKLOG |
| queue-edit delegation | None until recorded; otherwise report proposed ranking with evidence |
| paid API / provider ceiling | Zero; no calls unless explicitly authorized in STATE and task scope |
| subscription invocation/token/time allowance | UNSET; enforce and report a bounded allowance before running |
| tools / web / external sources | UNSET; allowlist and access boundaries; no sign-ins or grant changes |
| retries / uncertain outcome policy | No blind retries; inspect run/output/receipt IDs, then use only the configured retry allowance |
| permissions / denial handling | Actual runner controls; stop the affected operation on denial, no bypass |
| approval / expiry / revocation | UNSET; source of authority, expiry/review trigger, and how the human disables it |
| notification destination | None; separate authorization needed to send anything |

## Per-task authority

| Task ID / queue link | Existing ruling or delegated authority | Allowed repo/files/actions | Acceptance / verification | Rollback | Ceiling / deadline | Human decisions still open |
| --- | --- | --- | --- | --- | --- | --- |

An execution task must be within existing authority, bounded, reversible, independently verifiable, free of unresolved required human decisions, and safe for the currently owned resources. Mark unqualified tasks BLOCKED or PROPOSED and say why. For this evening preset, code/ops changes in a product become batons, not overnight CoS edits.

## Per-run record

- Job/run/attempt ID, contract revision, local date/time zone, baseline and actor.
- Start time recorded by runner before model invocation; finish/status or unresolved STARTED.
- Config/task-authority references; inputs actually read and their freshness.
- Output/evidence/receipt links; changed files and verification at revision.
- Usage for all attempts; limits hit; skips, permission denials, and uncertain operations.
- Recovery owner and exact next permitted action.

Use the same shape for a manual dry run and a later external schedule. A filled config is still only a proposal until the applicable owner has authorized and the actual runner enforces it.
