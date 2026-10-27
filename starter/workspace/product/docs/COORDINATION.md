# Product -> CoS bridge

The baton flows in; evidence flows back. Product owns implementation. CoS owns rank and strategic rulings.

1. Save a stable, task-specific receipt under `receipts/`, including original baton, exact revision/environment, result, evidence links, limits, and open work. Use the [receipt template](../receipts/_TEMPLATE.md).
2. Check the canonical CoS checkout is available and the current task permits register writes. Body links must resolve from the destination `cos/logs/`, not from the product receipt. The helper appends bytes; it does not rewrite links.
3. From the product checkout or a sibling product worktree, invoke the reviewed helper:

```sh
python3 ../cos/system/register.py backlog \
  --id RECEIPT-ID --session SESSION-ID \
  --title 'Verified task outcome' --body receipts/task-result.md
```

`RECEIPT-ID`, `SESSION-ID`, and the body path are placeholders; fill them for the real task. The program locates CoS from its own path, refuses a linked Git worktree as the target, locks all three registers, and writes only the selected register. It does not commit, push, call a provider, or change rank. Read the script before using it in a new project.

Use `error` for a failure class with an enforcer or owner. Use `decision` only to record a ruling or delegated call whose authority already exists; the tool cannot grant it. CoS uses the same door and stages its own intended records under its normal Git flow.

4. Record successful delivery, returned ID, and time in the product session log only on confirmed success. Keep the registered body immutable. A lock conflict is a pending write: keep the receipt and report the holder. Never delete someone else's lock automatically. After a crash or uncertain outcome, inspect the register for the same ID before retrying. Duplicate IDs are refused, never silently appended twice.
5. CoS verifies incoming evidence, appends an acknowledgement referencing the receipt, then updates queue and priorities. Product cannot mark the entire company loop closed merely because a local suite passed.

If sibling access or write permission is unavailable, do not bypass it. Keep the product receipt PENDING and give the CoS session the relative artifact path and exact pending operation. Independent product work can continue within its authority.
