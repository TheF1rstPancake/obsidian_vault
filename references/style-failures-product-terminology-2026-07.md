# Style failure modes — dual-product terminology & conditionals (2026-07)

Source: pancake-review annotations on `ai-native-se-stack` (2026-07). Canonical rules now live in [STYLE.md](../STYLE.md) §3 and the Argument integrity checklist; the editor prompt in `scripts/article_pipeline.py` mirrors them. This note is the regression list.

| Failure | Annotation signal | Fix |
|---|---|---|
| Bare "the product" with two systems on stage | "we are confusing which _product_ here… core, paid for product vs internal SE owner product" | Define short phrases up front (**core product** vs **SE brain**) and use them; never leave "the product" ambiguous. |
| Dangling / mushy system referent | "Dangling modifier here. The _core_ user facing product." | Name which system cannot handle the edge case; if the SWAT flywheel matters, say SEs synthesize edges back into the internal system. |
| Dropped load-bearing conditional | "If youve built a well defined, useful product…. This If is important." | Keep the *if*; do not promote "majority should flow through X" into a universal without the precondition. |

**Terminology convention for this article class** (internal GTM/ops tooling pieces that also discuss what customers buy):

- **Core product** — company's customer-facing, paid offering.
- **SE brain** (or equivalent internal name) — SE-owned internal product/framework AEs and CSMs operate.

Editor pass: treat each row as a **blocking** Argument integrity issue when the draft exhibits it.
