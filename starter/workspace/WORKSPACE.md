# Workspace map

This directory is a workspace containing independent repositories. After setup, it has no Git repository of its own.

| Directory | Responsibility | Entry |
| --- | --- | --- |
| `cos/` | Direction, hypotheses, priorities, queue, decisions, learning, daily coordination | [CoS instructions](cos/INSTRUCTIONS.md) |
| `product/` | Product spec, code, tests, operational truth, as-built, human acceptance | [Product instructions](product/INSTRUCTIONS.md) |

The shared contract lives at [cos/system/WORKING_AGREEMENT.md](cos/system/WORKING_AGREEMENT.md). Every repo reads it explicitly. Product sessions do not inherit it automatically from a sibling repo. Missing access is a visible bootstrap blocker.

Default sibling names are `cos` and `product`. For additional products, copy a fresh product starter, update this map and [PRODUCTS.md](cos/PRODUCTS.md), and set its coordination links relative to its location. Do not copy another product's records.

Keep task worktrees beside the main checkouts, for example `cos-task` and `product-task`, so `../cos` and `../product` still resolve to the canonical checkouts. A product worktree reads the canonical CoS contract; a CoS worktree edits its own version of policy and merges it normally. Register writes always use the canonical CoS checkout's helper.

No code, deploy, production credentials, scheduled job, or external connector is configured by this starter.
