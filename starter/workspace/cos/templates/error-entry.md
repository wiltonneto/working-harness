# Error entry body — fill for a real event

No incident is recorded by this template. Choose a stable receipt ID and title when invoking the register door; do not reuse an ID for a different event.

- **Surfaced:** date/time, session, role, and observed failure, surprise, or near-miss.
- **Evidence:** exact revision/environment and relevant artifact, log, test, or query links. Remove secrets and private payloads.
- **Root cause:** the established mechanism with evidence, or `unknown / under investigation`. Keep hypotheses separate.
- **Impact:** what was affected and what was checked to bound the effect.
- **Severity:** low / medium / high / critical, with a reason.
- **Status:** OPEN / MITIGATED / FIXED / MONITORING / WONTFIX (with reason).
- **Failure class:** the reusable root pattern, not just this symptom.
- **Related entries / recurrence:** prior receipt IDs and what is new; preserve their history.
- **Immediate fix or mitigation:** what changed, revision, and verification; or what remains owed.
- **Durable learning:** why this class can recur and how future work should differ.
- **Enforcement:** test, hook, shared function, preflight, or runtime guard; if absent, name its owner and next action. A prose instruction alone is not enforcement.
- **Improvement backlog item:** link/ID, or `pending CoS review` with owner; explain if no further action is justified.
- **Closure evidence:** show the guard detecting a bad case and permitting a good case where applicable, at the exact revision; otherwise leave OPEN or MONITORING.

Before registering, make body links resolve from `cos/logs/`, where the helper appends the body unchanged. Keep delivery status in the originating session log, outside this immutable body.
