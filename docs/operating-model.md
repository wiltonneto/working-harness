# How the system works

The chief of staff holds the whole picture. Product sessions hold the implementation. The seam between them is a document, and the return path is evidence.

## Practices observed in the source system

| Practice | How it works | Source home inspected |
| --- | --- | --- |
| Two independent repositories | CoS holds strategy, priorities, decisions, and the daily clock. Product holds code, specs, tests, deployment records, and as-built truth. CoS never deploys. | Both repository `AGENTS.md` files, “Workspace & boundary” |
| Real delegated responsibility | Decide reversible implementation details within authority; bring directional, costly, irreversible, or externally consequential choices to the human. Finish already authorized work instead of recommending it back. | Both `AGENTS.md` files, “Operating as an officer”; product “The finishing rule” |
| State before process | The operating posture changes with the people, money, data, and reputation at risk. The CoS controls depth, research priorities, and deferrals with triggers. | CoS `OPERATING_SYSTEM.md`, STATE and SYSTEM |
| A written decision loop | Problem -> hypothesis -> principles -> spec -> acceptance, established before implementation. Product verifies a baton's factual premise rather than treating prose as live truth. | Workspace preamble; CoS handoff workflow; product prompt template |
| One fact, one home | Strategy belongs with coordination; code-dependent documentation belongs with product. Current state is updated; dated decisions and session records preserve the trail. | Both `AGENTS.md` files, “Documentation governance” |
| Written handoff and return | CoS records a ruling or labels a proposal, ranks an owned task, and writes a bounded baton. Product writes an as-built that links back, then files facts into coordination registers. Ranking stays with CoS. | CoS handoff workflow; product “Workspace & boundary” |
| Continuity off disk | Priorities, recent session records, scoped durable memory, and today's coordination spine rebuild context. Each session closes the loop in files. Memory is an index and aid, never a rival source of truth. | CoS `AGENTS.md`, `CLAUDE.md`, and OS coordination spine |
| Isolation and serialized shared writes | Each session has its own worktree. Cross-repo execution can use a fresh worktree per repo after reading each repo's law. Registers and shared runtime resources need separate coordination. | Both `AGENTS.md`; worktree workflows |
| Evidence before confidence | Review findings are inputs to verify, including rejected findings. Readiness binds checks to the actual revision and environment. Human judgment is reserved for felt quality. | Product “Officer honesty duties”, “Session bar”, and human test queue; review workflow |
| Learning changes the system | Capture failures by class and supply an enforcer, or name its owner. A daily compile and bounded night work keep the queue true. | CoS OS, error workflow, and night-shift prompt |

These are observations of checked-out instructions, not an audit of compliance or a claim about current production. Some historical helper text conflicts with newer repo rules; the extraction follows the explicit newer boundary and register rules. Domain-specific product principles are not generalized into universal business rules.

## What this template preserves

The shared [working agreement](../starter/workspace/cos/system/WORKING_AGREEMENT.md) is the invariant contract. Each repository has its own role and read order. The CoS owns the queue and rulings; product owns the spec, implementation, status, and evidence. Product may file coordination facts through one serialized register door, but it cannot use that door to rule on strategy or change priority.

The morning brief is a decision surface: what matters, what moved, what needs judgment, and what is already being done under delegation. End-of-day work re-verifies the queue against artifacts and addresses recurring failure classes. Both are manual workflows in this starter.

## Proposed adaptations, not observations

- Shared policy has one canonical Markdown home in CoS. Thin local `AGENTS.md` files route both tools to it; `CLAUDE.md` imports its local entrypoint. The source already advocates neutral scripts and docs; this package makes the routing uniform.
- The register helper writes only the three allowed coordination surfaces, uses one exclusive lock, refuses duplicate receipt IDs, and never commits or pushes. This is a new implementation of the observed register-door pattern, not a copy of the original tool.
- Product writes durable outbound receipts before registering them. If CoS is unavailable, the receipt stays pending; work is not silently declared closed.
- Permissions begin with local reversible work only. Merges, paid calls, external communication, production access, and deployment need project-specific authority; the source's standing production privileges do not transfer.
- Scheduling is deliberately uninstalled. The clock has reusable prompts and explicit owners; adding unattended execution needs its own runtime controls and first-cycle verification.
- Product principles, risk stage, commands, time zone, ceilings, and release process are setup inputs. No private product doctrine or obsolete operational claim is carried into a new company.

Use [setup](setup.md) to instantiate this structure and [the cycle](work-cycle.md) to see the seams.
