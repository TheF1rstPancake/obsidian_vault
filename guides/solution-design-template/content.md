---
title: "The solution design template"
slug: guide-solution-design-template-content
status: ready
target: ghost-page
visibility: paid
created: 2026-06-19
updated: 2026-06-19
tags: [sales-engineering, customer-success, renewals, implementation, template]
point: >
  A fill-in-the-blank solution design document built to outlive the sale. The
  same artifact that closes the deal becomes the post-sale team's defense of
  scope at implementation, expansion, and renewal. Seven sections plus a renewal
  protection log so that 12 months later — after the AE has rotated and the
  implementation team has handed off — someone can still answer "what did we
  actually promise this customer?"
---

# The solution design template

This is the companion artifact to *The solution design document protects the renewal, not the sale*. The argument there: the document's biggest payoff isn't at signature — it's 9–18 months later, when the people who made the promises are gone and someone has to reconstruct what the customer was told. This template is built for that second life.

## How to use it

Fill it in *during* the pre-sale technical discovery, not after. The act of writing forces the questions that surface scope gaps while you can still negotiate them. Two rules:

1. **Freeze what's frozen.** Once a section is agreed with the customer, changes go in the revision history — never silently overwrite. The diff *is* the value at renewal time.
2. **Write the "explicitly out" column like you'll be quoted on it.** You will be. Vague scope is the single most common reason a post-sale team can't defend itself a year later.

The section most teams skip is Section 6 (Renewal protection). It's the one that turns a closing artifact into an operating one. Don't skip it.

Copy everything below into your own doc and replace the bracketed prompts.

---

## Header

| Field | Value |
|---|---|
| **Customer** | [Account name] |
| **AE** | [Account executive] |
| **SE** | [Solutions engineer / author] |
| **CS Owner** | [CSM who will inherit this account] |
| **Date** | [Initial draft date] |
| **Revision history** | [v1 — date — what changed — who] |

> [!warning] Revision history is not optional
> Every change after the first customer sign-off goes here as a new row. If you can't see *what changed and when*, you can't defend scope at renewal. The revision history is the spine of this whole document.

## Section 1 — Business context

*What problem are we actually solving, what does success look like, and who owns that outcome on the customer side?*

- **The problem:** [What is broken / costly / risky today, in the customer's words. Avoid product language.]
- **What success looks like:** [The measurable or observable end state. "Reduce X from N to M by Q3," not "improve efficiency."]
- **Business owner:** [Who on the customer side is accountable for this outcome — not the technical buyer, the person whose number moves.]
- **Why now:** [The trigger / deadline / mandate driving the timing.]

## Section 2 — Technical environment

*The current state we're integrating into. Capture it precisely; this is what implementation will check against reality.*

- **Current stack:** [Systems, versions, hosting model relevant to the solution.]
- **Integrations required:** [Each system we touch, the direction of data, and the method — API, webhook, file drop, etc.]
- **Data flows:** [Where the data originates, how it moves, where it lands. Note volumes and frequency if they affect design.]
- **Constraints:** [Security, compliance, network, latency, residency — anything that bounds the solution.]

## Section 3 — Solution scope

*The hardest-working section. Three columns, and the middle one matters most.*

- **In scope:** [What we are committing to deliver. Be specific enough to test against.]
- **Explicitly out of scope:** [What we are *not* doing, stated plainly so no one assumes it later. This is the column that protects the renewal.]
- **Deferred / phase 2:** [Things acknowledged but parked, with the condition under which they'd come back.]

> [!tip] The "explicitly out" test
> For every capability the customer might reasonably *assume* comes with the solution, write one line either claiming it (in scope) or disclaiming it (out of scope). Silence is the failure mode — an unstated assumption becomes a support ticket and then a renewal risk.

## Section 4 — Implementation commitments

*Who does what, by when, and what each side depends on from the other.*

| Commitment | Owner | Target date | Depends on |
|---|---|---|---|
| [Deliverable] | [Us / Customer] | [Date] | [Blocking dependency] |

- **Customer responsibilities:** [Access, environments, SME time, data — what we need *from them* and by when.]
- **Our responsibilities:** [What we deliver, and the form it takes — config, code, docs, training.]
- **Critical path:** [The dependencies that, if late, slip everything.]

## Section 5 — Acceptance criteria

*How do we know it worked? Written before build, agreed with the customer.*

- **Acceptance test:** [The concrete check — "X happens when Y, verified by Z."]
- **Who signs off:** [The customer-side person who confirms acceptance.]
- **Definition of done:** [The bar that ends implementation and starts steady-state.]

> [!tip] Steal this rule
> If a criterion can't be demonstrated in a 15-minute screen-share, it's not an acceptance criterion — it's an aspiration. Rewrite it until it's testable.

## Section 6 — Renewal protection

*The section that makes this document an operating artifact instead of a closing one. Schedule these reviews now.*

- **90-day review:** [Is the solution doing what Section 1 said success looks like? Gaps logged below.]
- **6-month review:** [Has the environment (Section 2) or scope (Section 3) drifted? Note new integrations, new use cases, new owners.]
- **Renewal QBR:** [Walk the original Section 1 success criteria against reality. This is the evidence that the solution delivered — or the early warning that it didn't.]

**Scope drift log:**

| Date | What changed | In/out of original scope? | Action |
|---|---|---|---|
| [Date] | [New ask / assumed capability / changed integration] | [Was this ever committed?] | [Absorbed / new SOW / declined] |

> [!warning] Drift is normal — undocumented drift is fatal
> Customers will ask for more; that's healthy. The danger is when a year of small "can you also…" asks gets silently absorbed, and at renewal the customer measures you against a scope no one ever agreed to. Every drift gets a row. The log is how you separate "expansion opportunity" from "scope creep we never priced."

## Section 7 — Open items / decisions needed

*The honest list of what isn't resolved yet. Don't let it leak into the frozen sections.*

| Open item | Owner | Needed by | Blocking? |
|---|---|---|---|
| [Decision or unknown] | [Who decides] | [Date] | [Yes/No] |

---

That's the template. The discipline isn't in filling it out once — it's in keeping Sections 3 and 6 honest after the deal closes, when no one's watching and everyone's busy. That's exactly when the document earns its keep.
