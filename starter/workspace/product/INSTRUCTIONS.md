# Product execution

Own the implementation and its evidence. Start from a ruled baton or another explicit user task. Do not adopt a proposal as a ruling, infer live state from CoS prose, or re-rank the company queue.

## On resume

Read [PROJECT.md](PROJECT.md), [STATUS.md](STATUS.md), [ARCHITECTURE.md](ARCHITECTURE.md), [product principles](strategy/PRODUCT_PRINCIPLES.md), and the active baton/session prompt. Read the latest [session log](session-log.md) and [MEMORY.md](MEMORY.md). Inspect affected code, specs, and any narrower directory instructions before writing. Read the CoS priorities and today's coordination file if accessible; report stale or missing cross-repo context.

## Execution loop

1. Verify the premise at source. Record confirmed and rejected claims. If a required ruling is absent, return a precise blocker; continue independent authorized discovery.
2. Establish falsifiable acceptance and scope using the [session prompt](spec/prompts/_TEMPLATE.md). Update the [behavior spec](spec/README.md) before implementation. Link the original baton and ruling.
3. Implement in your owned worktree. Use only configured project commands and authorized resources in PROJECT. Diagnose failures; never classify a failing test as stale without evidence.
4. Run focused checks, the configured broader gate, and real-surface verification where relevant. Record revision and environment. Mark unavailable or omitted checks explicitly.
5. Write the [as-built](docs/AS_BUILT_TEMPLATE.md), update STATUS in the same change when possible, and create a [human test entry](strategy/HUMAN_TEST_QUEUE.md) for judgment only a human can provide. A LANDED change is not automatically LIVE or human accepted.
6. Save a [return receipt](receipts/_TEMPLATE.md), then file facts using the canonical CoS register door described in the [coordination bridge](docs/COORDINATION.md). Log failures, surprises, and near-misses using the shared [error-entry body](../cos/templates/error-entry.md) and [learning loop](../cos/system/learning-loop.md), even when the fix must wait. CoS owns rank, rulings, and shared-register commits.
7. Update the session log and durable context pointers. Complete authorized next steps; leave a precise blocker and next invocation for anything you cannot finish.

## Canonical homes

Code-dependent truth lives here: spec, tests, current status, architecture, as-built, runbooks, and release evidence. Strategic direction and ranking live in CoS. Deep incident analysis stays with product and links to the shared error class.

No build, release, production access, paid call, merge, or external communication is configured by this starter. Configure the real commands and authority in PROJECT and CoS STATE before using them. Local instructions are guidance; permissions and gates provide actual enforcement.
