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
| Review becomes queue work, not another report | Evening review rechecks backlog premises, groups recurring error classes, ranks under existing priorities, and completes qualified reversible CoS tasks. Product code remains read-only for the CoS night preset. | CoS night-shift prompt, backlog and error/enforcement lanes |
| CoS chooses depth and research | Founder requests and work that earns uninterrupted study are prioritized for decision value, night suitability, freshness, and depth versus cost. Research and night outputs feed the morning brief rather than making the founder reconcile several reports. | CoS OS, depth/research governor and night-selection rubric; job output contract |

These are observations of checked-out instructions, not an audit of compliance or a claim about current production. Some historical helper text conflicts with newer repo rules; the extraction follows the explicit newer boundary and register rules. Domain-specific product principles are not generalized into universal business rules.

## What this template preserves

The shared [working agreement](../starter/workspace/cos/system/WORKING_AGREEMENT.md) is the invariant contract. Each repository has its own role and read order. The CoS owns the queue and rulings; product owns the spec, implementation, status, and evidence. Product may file coordination facts through one serialized register door, but it cannot use that door to rule on strategy or change priority.

The morning brief is a decision surface: what matters, what moved, what needs judgment, and what is already being done under delegation. End-of-day work re-verifies the queue against artifacts, addresses recurring failure classes, and selects research that earns depth. The source uses external jobs; this starter supplies [portable contracts](../starter/workspace/cos/system/jobs/README.md) that may first be run manually. No runner or schedule is installed.

## Operating principles evidenced in the source

The source CoS OS explicitly names six: truth over comfort; velocity with depth control; the founder decides and the system does the work; measure what's working and kill what isn't; magic before scale; and a state-aware, self-revising system. The canonical [working agreement](../starter/workspace/cos/system/WORKING_AGREEMENT.md) adapts those for reuse. These govern how the company works. A product's own principles are separate inputs and are left unset.

The source also requires evidence-weighted recommendations, reporting bad news and omitted checks, review of plans as well as changes, read-on-resume/write-on-close continuity, and filing reflection into the paths the next session reads. The [learning loop](../starter/workspace/cos/system/learning-loop.md) applies those practices without copying any private incident, historical measurement, or original product doctrine.

## Proposed adaptations, not observations

- Shared policy has one canonical Markdown home in CoS. Thin local `AGENTS.md` files route both tools to it; `CLAUDE.md` imports its local entrypoint. The source already advocates neutral scripts and docs; this package makes the routing uniform.
- The register helper writes only the three allowed coordination surfaces, uses one exclusive lock, refuses duplicate receipt IDs, and never commits or pushes. This is a new implementation of the observed register-door pattern, not a copy of the original tool.
- Product writes durable outbound receipts before registering them. If CoS is unavailable, the receipt stays pending; work is not silently declared closed.
- Permissions begin with local reversible work only. Merges, paid calls, external communication, production access, and deployment need project-specific authority; the source's standing production privileges do not transfer.
- Scheduling is deliberately uninstalled. The clock has reusable prompts and explicit owners; adding unattended execution needs its own runtime controls and first-cycle verification.
- The job contracts separate evening review, deep research, and morning compilation for portability. They consolidate shared boundaries in one contract and leave the runner, schedule, usage enforcement, and notification integration outside the repository. This is a template design, not a claim that the source used these exact files or job split.
- The preset holds unattended edits to its own shared instruction text for interactive review, in addition to the observed restriction on changing its own job prompts. Explicitly authorized CoS implementation tasks may still improve mechanisms; this guardrail does not turn every reversible internal task into a founder decision.
- Error entry/review shapes and an explicit review-to-backlog-to-enforcer loop make the existing learning practice discoverable. This small starter uses one error register; it does not reproduce the source's severity-based digest routing. Its job-run ledger is an empty contract for a future serialized external writer, not an implemented logger.
- Product principles, risk stage, commands, time zone, ceilings, and release process are setup inputs. No private product doctrine or obsolete operational claim is carried into a new company.

Use [setup](setup.md) to instantiate this structure and [the cycle](work-cycle.md) to see the seams.
