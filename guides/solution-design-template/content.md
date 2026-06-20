---
title: "The solution design template"
slug: guide-solution-design-template-content
status: ready
target: ghost-page
visibility: paid
created: 2026-06-19
updated: 2026-06-20
tags: [sales-engineering, customer-success, renewals, implementation, template]
point: >
  A fill-in-the-blank solution design document built in three parts: problem
  definition (solution-agnostic), a requirements table written without any
  product language, and only then the mechanics of your specific recommendation.
  That sequence is the whole point — the agnostic requirements are the shared
  agreement a customer could take to any vendor, which is exactly why they hold
  up at implementation, expansion, and renewal long after the deal is signed.
---

# The solution design template

This is the companion artifact to *Are you trying to be right, or help the customer?* — the framework there, made fillable. The structure is deliberate and the order is the point:

1. **Problem definition** — the customer's world, with no mention of your product.
2. **Solution-agnostic requirements** — a table any vendor could be scored against.
3. **Solution recommendation** — your specific bridge, mapped to those requirements.

If you skip to Part 3, you've written a brochure. The value lives in Parts 1 and 2 being honest *before* your solution shows up.

Copy everything below into your own doc and replace the bracketed prompts.

---

## Part 1 — Problem definition (solution-agnostic)

*Fill this in during pre-sale discovery, not after. The four boxes are the anchor for every conversation downstream — AEs, CSMs, and QBRs all reference them. None of this should mention your product. If a box reads like a feature pitch, you've written it wrong.*

- **Current state:** [What is the customer doing today? The actual workflow, tools, and people involved — described as they'd describe it.]
- **Problems / pain:** [What's not working? Why are they taking this call? Cost, risk, friction, time — in their words, not yours.]
- **Goals and objectives:** [What does success look like? The measurable or observable end state — "reduce X from N to M by Q3," not "improve efficiency."]
- **Ideal solution:** [If they had a magic wand, what would the solution look like? The customer's own vision — even if it doesn't match what you sell. Especially if it doesn't.]

## Part 2 — Solution-agnostic requirements

*This is the section that does the work. Write every row as if you're describing what **any** good solution must do — no product names, no feature names. If the customer took this table to three of your competitors, they should be able to score each vendor against it line by line. That's the test for whether a requirement is truly solution-agnostic.*

Each requirement traces back to a box in Part 1. Priority is the customer's call to make — but it's your job to shape the conversation about what's a need versus a nice-to-have.

| Requirement | Priority | Rationale (traces to) |
|---|---|---|
| [System must support X] | Need | [Objective: reduce manual handoffs (Box 3 — Goals)] |
| [Must integrate with the system of record without manual export] | Need | [Problem: data re-keyed by hand today (Box 2 — Problems)] |
| [Should surface workload across the team in one view] | Nice | [Ideal solution: "see who's overloaded at a glance" (Box 4)] |
| [Must meet [compliance/residency/latency] constraint] | Need | [Current state: regulated environment (Box 1)] |

> [!tip] The requirements you seed here are your differentiator
> If you understand the customer's problem better than they do, you can shape this list so your strengths show up as table-stakes requirements. Be honest about what you can't do — steer those toward "nice-to-have" — and add the needs most buyers don't think to ask for. When they go evaluate other vendors against this table, the list now quietly favors you.

## Part 3 — Solution recommendation

*Only now do you talk about your product. Everything above stands on its own; this part is the bridge from the agnostic requirements to your specific offering.*

### Your bridge

[One paragraph, high level: how your solution addresses the requirements in Part 2. This is the fifth box — the reframe of the customer's ideal solution in your terms. Not a feature list; the shape of the answer.]

### Requirements-to-solution mapping

| Requirement (from Part 2) | How we address it | In / out of scope |
|---|---|---|
| [Requirement] | [The specific capability, workflow, or config that meets it] | In |
| [Requirement] | [Partial — meets it via X, with caveat Y] | In |
| [Requirement they might assume] | [Not something we do] | Explicitly out |

State the explicitly-out items plainly. A capability the customer might reasonably assume comes with the solution either gets claimed here or disclaimed here — silence is the failure mode.

### Implementation

| Commitment | Owner | Target date | Depends on |
|---|---|---|---|
| [Deliverable] | [Us / Customer] | [Date] | [Blocking dependency] |

- **Customer responsibilities:** [Access, environments, SME time, data — what you need from them and by when.]
- **Our responsibilities:** [What you deliver and the form it takes — config, code, docs, training.]

### Acceptance criteria

- **Acceptance test:** [The concrete, testable check — "X happens when Y, verified in a 15-minute screen-share."]
- **Who signs off:** [The customer-side person who confirms acceptance.]
- **Definition of done:** [The bar that ends implementation and starts steady-state.]

> [!tip] Steal this rule
> If a criterion can't be demonstrated in a 15-minute screen-share, it's not an acceptance criterion — it's an aspiration. Rewrite it until it's testable.

## Open items

*The honest list of what isn't resolved yet. Keep it out of the frozen sections above.*

| Open item | Who decides | Deadline | Blocking? |
|---|---|---|---|
| [Decision or unknown] | [Owner] | [Date] | [Yes / No] |

---

That's the template. The discipline isn't filling it out once — it's resisting the urge to lead with Part 3. Get Parts 1 and 2 right and the recommendation writes itself; skip them and you're back to reading the spec sheet at the customer.
