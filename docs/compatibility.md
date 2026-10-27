# Claude Code and Codex compatibility

Checked against official documentation and tested on macOS on 2026-10-27 with Claude Code 2.1.311 (`claude-opus-5-5`) and Codex CLI 0.162.1 (`gpt-6.1-sol`). In one synthetic, read-only product-entrypoint probe per tool, each model read the sibling shared agreement and local role instructions, returned unpredictable markers correctly, and respected CoS ranking ownership and the absence of deployment authority. Other entrypoints, host configurations, and application behavior were not exercised by those model probes.

Each repo's `AGENTS.md` is a thin router to the same shared working agreement and local role instructions. `CLAUDE.md` contains `@AGENTS.md`. Policy and workflows live in neutral Markdown and the reviewed Python helper. No personal global config, skill installation, model profile, permission allowlist, symlink, MCP server, or paid API is required by the package.

Codex discovers project instructions from its project root to the current working directory. A sibling CoS repo is outside that discovery chain; the product entrypoint explicitly tells the agent to open the canonical file. Global overrides and instruction-size limits can affect loading. Start in the repo or its worktree and check what was actually read. [Official Codex instruction discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md).

Claude Code supports a local `CLAUDE.md` import of `AGENTS.md`. Relative imports resolve from the importing file. The local import avoids automatic cross-repo import dependencies; the shared contract is an explicit file read. Host trust and sandbox settings still apply, so the bootstrap check must confirm that read. [Official Claude Code memory documentation](https://code.claude.com/docs/en/memory).

## Supported layout and limits

| Assumption | How to verify / recover |
| --- | --- |
| Main checkouts and task worktrees share one parent directory | Move only copies during setup; update links deliberately if using a different layout. Worktree sibling links resolve to canonical CoS/product checkouts. |
| The coordination repo is named `cos` | Product entrypoint and workflow links target `../cos`. Change all these references and validate if renaming it. |
| The product is initially named `product` | Additional products need registry/map entries and adjusted references. No automatic arbitrary-layout resolver is included. |
| A session can read CoS policy | Confirm with the read-only bootstrap prompt. If inaccessible, report the exact file and dependent work; do not rely on remembered policy. |
| Python 3.9+ for register and validators | Uses the standard library. Core Markdown remains readable without Python, but register writes must wait for the approved door. |
| Local filesystem with exclusive file creation, append, and fsync | The register uses an exclusive lock file. Network shares and distributed synchronization are untested and require a different coordinator. |
| POSIX setup examples and local Git | Prepared and tested on macOS. Linux-compatible primitives are used; Linux and Windows runtime behavior were not exercised. Windows needs an equivalent copy flow or a POSIX environment. |
| Small neutral instruction files | Static validation checks routes and import targets. Actual model instruction following and local/global overrides still need the two-tool bootstrap check. |

The register refuses known linked Git worktree targets (`.git` file), duplicate IDs, and symlink register targets. Its lock has no automatic expiry: after a crash, inspect the holder and receipt outcome before recovery. It does not enforce human authority, validate factual claims, rewrite body links, commit records, or make arbitrary filesystem writes safe. Do not use raw edits as a concurrent fallback.

The source system had more mature leases, CI/release provenance, production read tools, and scheduler enforcement. Those integrations are project-specific and intentionally left as explicit configuration work here.
