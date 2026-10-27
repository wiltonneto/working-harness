# Error -> review -> backlog -> better harness

This is the shared learning workflow. Every role uses it; CoS owns the cross-company review and ranked queue. Follow the [working agreement](WORKING_AGREEMENT.md) and current [STATE](../STATE.md) for authority.

## Log when the failure is still observable

Log a failed run, crash, unexpected behavior, false claim, missed handoff, research failure, or near-miss. Record the diagnosis even if the fix is deferred. Do not fabricate an incident because a review ran quietly.

Use the [error-entry body](../templates/error-entry.md) and append through the canonical [register door](register.py) in `error` mode. A product session keeps deep forensics beside its code and links them from the shared entry. A CoS/research session keeps the supporting artifact in its own repository. Root cause is `unknown` until evidence establishes it.

Read related entries first. A recurrence is a new dated note referencing the existing class/receipt IDs, not a rewrite of someone else's record or a second competing diagnosis. An immediate fix can close an incident while the underlying class remains open.

## Review classes, not a recital of incidents

At session close for a material failure, and during an explicitly authorized evening review, CoS:

1. Reads the recent error entries and still-open classes. Rechecks linked evidence; a prior entry is an input, not proof of present state.
2. Groups recurring root patterns. Separates symptoms from causes and confirmed findings from rejected or unverified claims.
3. Checks whether an enforcer already exists and actually fires. An old proposed fix that never landed is unfinished work, not a fresh idea.
4. Proposes the smallest improvement that prevents the class or makes recurrence observable. Prefer a portable script, test, shared function, or runtime guard over another instruction copy.

Use this output shape in a dated review artifact:

| Class / related receipt IDs | Evidence and recurrence | Existing guard / gap | Proposed enforcer and falsifiable acceptance | Owner / authority needed | Queue item or reason to defer |
| --- | --- | --- | --- | --- | --- |

Do not turn frequency alone into priority. Consider impact, current goals, the decision or work it unlocks, confidence in the cause, and the cost of the fix. Record why an apparent finding was rejected too.

## Put a real improvement on the queue

File the evidence-backed proposal through `backlog` mode, referencing the error IDs and review artifact. CoS reuses an existing item when the class is already queued; otherwise it adds an owned [BACKLOG](../BACKLOG.md) item with acceptance, next action, expected enforcer, and required authority. CoS ranks it within already ruled priorities. A direction, budget, or taste decision remains the founder's.

If the change belongs in product, CoS writes a [baton](../templates/baton.md) and product executes under its own law. An evening CoS review does not grant product-write authority. If an internal CoS fix is already authorized, bounded, reversible, and verifiable, complete it rather than merely recommending it again.

## Verify the improvement and close the read paths

Run the relevant checks and, where applicable, demonstrate that the new guard catches the bad case and allows the good case. Bind results to a revision and environment. Do not weaken a gate simply to make a failing run green.

Return a completion receipt to the inbox. Append a follow-up `error` entry with a distinct ID, linked to the original class and queue item; preserve the original account. State whether the incident is fixed, the class is enforced, or observation is still owed. CoS updates the queue, current docs invalidated by the change, and any durable memory pointer. Check sibling implementations when a rule has multiple copies.

The next morning's brief carries the consequence: class addressed, verified result, what is still open, and any human ruling needed. The detailed trail stays linked. A memo, an error entry, a backlog proposal, and a verified enforcer are different stages; do not report the last one merely because the first three exist.

The [job contracts](jobs/README.md) can reuse this workflow from an external scheduler later. No review schedule or job is installed here.
