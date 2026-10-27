# Return receipt — stable unique ID

This is a template, not an actual event. Track delivery status in the product session log; keep mutable registration status out of the body that will be appended to CoS.

- Task, original baton, and ruling:
- Product / session / owner:
- Current outcome and exact revision/environment:
- Evidence: as-built, checks, STATUS, human queue if applicable:
- Strategic premise confirmed, rejected, or still untested:
- Fact for the queue (completion, corrected scope, blocker, newly found work):
- Failure class / error receipt if relevant:
- What only the human can judge:
- Open work with owner and exact next action:

Use the same receipt ID when retrying. Before registering, make all evidence links valid from the CoS logs directory, because the body is appended there unchanged. Prefer workspace-relative Markdown links, for example `../../product/STATUS.md` from CoS logs. After success, record the returned ID and time in the product session log; preserve the registered receipt body. If the outcome is uncertain, inspect the target for the ID before retrying. “Duplicate ID” means inspect the existing record; it does not prove that its body matches.
