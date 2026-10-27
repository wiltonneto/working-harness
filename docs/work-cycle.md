# One end-to-end work cycle

Everything in this example is fictional. No task, ruling, test result, or user verdict below is an actual event. The clean starter begins empty.

Suppose a local reading-list app lets people mark an item finished, but that state disappears after a restart. Its project already has code and an authorized local test command. CoS does not guess the cause or implement a fix from the strategy session.

| Step | Owner and action | Durable result |
| --- | --- | --- |
| 1. Rebuild context | CoS reads STATE, priorities, recent session records, memory pointers, and today's spine. The reported symptom is labeled unverified until product inspects it. | Priority premise and uncertainty recorded. |
| 2. Rule and rank | The human authorizes a local persistence fix, zero paid calls, no release. CoS records the ruling through `decision` mode, ranks TASK-EXAMPLE, and assigns the product owner. | One ruling in the decision register; linked BACKLOG item. |
| 3. Write the baton | CoS writes `ops/TASK-EXAMPLE.md` using the baton shape: preserve completion across restart, preserve unread items, no UI redesign or sync feature. Acceptance: complete an item, restart, observe completion; unread entries remain unchanged. | APPROVED baton with authority, acceptance, exclusions, and return contract. |
| 4. Enter execution | A separate product session opens an owned sibling worktree, reads both agreements and PROJECT, then verifies the symptom at source and in a local repro. It rejects a review claim that all item edits are lost because the repro disproves it. | Session prompt records confirmed/rejected claims and links the original baton. |
| 5. Spec and build | Product updates its persistence spec before code, implements the smallest adequate change, and runs the configured focused and broader gates. | Code, spec, and meaningful regression evidence in one change. |
| 6. Verify the experience | Product drives the actual local mark/restart/read flow. Evidence identifies the exact revision, local environment, interaction, result, and remaining human judgment. No release occurred. | STATUS says VERIFIED_LOCAL; as-built links to the original baton/ruling. Human queue asks only whether the resulting behavior feels understandable. |
| 7. Return facts | Product saves `receipts/TASK-EXAMPLE-result.md` with a stable receipt ID, evidence links resolvable from CoS logs, and limitations; it calls the canonical register door in `backlog` mode. | Append-only fact in `cos/logs/backlog-inbox.md`; product session log records delivery only after success. |
| 8. Learn by class | If the bug exposed a missing persistence boundary check, product records the failure class and actual regression test as enforcer using a separate error receipt ID. Unknown causal details stay unknown. | Shared learning links to product's deeper analysis/test. A log alone is not called a fix. |
| 9. Reconcile and decide | CoS reads the as-built/checks, acknowledges the incoming receipt, updates rank and priorities, and records any human verdict after it actually happens. If acceptance passed, the local task can close; release remains outside scope. | Queue reflects verified reality; no obsolete blocker is re-escalated. |
| 10. Close and resume | Each session records its outcome, omissions, better approach, open work, and exact next action. CoS folds receipts into today's spine. A later session reads these files. | The next session resumes without reconstructing chat or relying on tool-specific memory. |

The handoff is complete when implementation evidence has reached the queue and CoS has reconciled it. A local code change, a successful helper call, or a polished memo alone does not complete the whole cycle.

If the CoS write is blocked, product leaves its receipt PENDING and names the exact operation, target, reason, and next action. If a check fails, it reports the measured result. If product evidence refutes the strategic premise, CoS changes the plan instead of reissuing the old baton.

Use [setup](setup.md) for the actual directory and worktree commands. Use the [bridge](../starter/workspace/product/docs/COORDINATION.md) for register invocation and uncertain-outcome recovery.
