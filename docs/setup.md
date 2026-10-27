# Set up a new workspace

Keep this clean distribution separate from operational company records. Read the files before using them. The only helper included uses Python's standard library; nothing downloads or installs anything.

## 1. Assemble two sibling repositories

From the distribution root, choose a new, unused destination outside this clone. The following is an example for a POSIX shell; edit the destination first:

```sh
harness_workspace="../my-workspace"
if test -e "$harness_workspace"; then
  echo "Choose an unused destination; nothing was copied."
else
  cp -R starter/workspace "$harness_workspace"
fi
```

Continue only after confirming the copy succeeded and both starter directories are present. Initialize separate local Git histories in the assembled workspace if needed:

```sh
git -C "$harness_workspace/cos" init -b main
git -C "$harness_workspace/product" init -b main
```

Do not initialize the enclosing workspace as a repository. The template distribution has one history for convenient reuse; operational CoS and product have independent histories. Nothing here creates a remote, chooses a license, pushes, installs hooks, or publishes.

Review and commit the initial files in each new repo using your own local Git identity when ready. The worktree workflow requires an initial commit. Existing projects should receive only the reviewed instruction/workflow files they need; reconcile their existing law instead of overwriting it with this starter.

## 2. Configure the operating contract

- Fill CoS STATE: purpose, human owner, risk stage, time zone, boundaries, authority, and ceilings.
- Fill CoS PRODUCTS, priorities, hypotheses, and the product's principles. Start from the new project's facts.
- Fill product PROJECT: source map, actual commands, allowed environments, checks, review process, and any later release gates.
- Keep zero spend and no external/production authority until explicitly extended. This starter does not inherit privileges from the system it was extracted from.
- For a second product, copy another clean starter from the distribution, register it in PRODUCTS and WORKSPACE, and adjust product-specific references. The sibling `../cos` contract stays shared; do not clone its policy into each product.

## 3. Check both tools' bootstrap

Start an interactive Claude Code or Codex session **inside `cos` or `product`**, never only at the enclosing workspace root for product work. Give it:

> Read this repo's AGENTS.md, the linked shared agreement, and its INSTRUCTIONS.md. Report the files read, role, decision rights, writable surfaces, current configured state, and any missing access. Do not modify anything.

Repeat in the other repository and in a task worktree before relying on the setup. In Claude Code, `CLAUDE.md` imports only the local `AGENTS.md`. Both tools must explicitly open the linked canonical Markdown. Do not assume a sibling repo or a parent router is automatically in context. If sandbox/trust settings prevent the read, resolve that access explicitly or hand over the bounded task as an artifact; do not silently skip the agreement. See [compatibility](compatibility.md).

## 4. Start the first cycle

Use the [fictional work cycle](work-cycle.md) as a structural example. CoS records authority, ranks a task, and writes a baton. The product session verifies, specs, implements, and returns a receipt. CoS verifies the receipt and updates the queue.

After initial commits, task worktrees can remain siblings to keep links stable. For example, from the enclosing assembled workspace:

```sh
git -C cos worktree add ../cos-task -b task/coordination
git -C product worktree add ../product-task -b task/implementation
```

These commands create local branches and worktrees; run them only for an assigned task. Use distinct names for simultaneous tasks. Never reuse another session's worktree. Do not use a repository's global stash to isolate sessions.

Task product worktrees call `../cos/system/register.py` in the canonical CoS checkout. Its lock protects register appends only. Coordinate Git operations and writes to other shared files separately. CoS worktrees must also use the canonical door, rather than appending records on branches to merge later.

At close, preserve changes and review ignored state before any cleanup. No automatic worktree deletion, main merge, deploy, or scheduled job is configured.

## 5. Keep reuse clean

Operational records may be private even when they contain no credentials. Reuse the clean distribution, not a copy of your company's filled workspace. Inspect Git history as well as current files before any later publication. License selection is still the owner's decision.
