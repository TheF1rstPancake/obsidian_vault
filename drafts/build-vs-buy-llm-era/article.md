---
title: "Build vs buy in the LLM era: which infra layer are you willing to outsource?"
slug: build-vs-buy-llm-era
status: raw
target: substack
created: 2026-05-08
updated: 2026-05-08
tags: [build-vs-buy, ai, strategy]
---

# Build vs buy in the LLM era: which infra layer are you willing to outsource?

> Stub. Seed thoughts captured 2026-05-08. Awaiting voice recordings to flesh out.

## The thesis

Build vs buy used to be a cost-and-time decision. Now it feels like a coin toss — the pro/con list looks balanced because LLMs collapse so much of the "build" effort. The reframe: **stop asking "build or buy?" and start asking "which infra layer am I willing to outsource so my team can move opinionated work on top?"**

That changes the analysis. Vendors stop being feature-bundles and start being infra primitives. Your differentiation moves to the layer you build *above* them.

## The Gong example (lead with this)

"Gong is just fancy speech-to-text — I could rebuild it." Sure. Now build:
- Calendar integration logic across every customer's stack
- Decision rules for which meetings to join
- Escape hatches for the exception cases (force-add, force-remove)
- The "don't show up to therapy" guardrails
- Pipeline integrations, coaching analytics, multi-rep visibility

You probably don't use most of Gong's advanced surface. But the *infra* you'd have to build to even start customizing on top is the part you don't want to own. Gong becomes an infra layer — and now the question is "which speech-to-text-plus-calendar infra do I pick?", not "build vs buy."

The same pattern applies to support tooling: world-class support means email infra, omnichannel routing, multiplayer shared-inbox UX, agent draft workflows your support team can edit *without filing a Jira ticket to engineering every time*.

## The decision matrix (the part you steal)

Don't ask "build or buy?" Ask each row below. If most answers point to **buy**, you're outsourcing infra. If most point to **build**, the work *is* your differentiation.

| Question                                                                                                      | Buy if...                                                  | Build if...                                                 |
| ------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ----------------------------------------------------------- |
| Is the boring part (escape hatches, exception cases, edge integrations) the actual work?                      | Yes — that's commodity infra someone has already solved    | No — the happy path *is* the work, and it's narrow          |
| Will non-engineers need to change behavior frequently (workflows, routing, prompts, rules)?                   | Yes — they need a UI to self-serve without filing tickets  | No — changes are rare and engineering-driven anyway         |
| Is the value in the integration surface (calendar, identity, payments, telephony) or the workflow above it?   | Integration surface is the value — buy the infra           | The workflow above is the value — build that, buy below     |
| Does the vendor expose clean APIs/webhooks I can compose on top of?                                           | Yes — they're an infra layer I can build above             | No — they're a walled garden; building beats lock-in        |
| What does this look like at 10x customers / 10x data?                                                         | Vendor scales with you and you don't pay 10x               | Vendor pricing or limits will choke us before we get there  |
| How replaceable is this layer in 18 months if a better option appears?                                        | Replaceable — thin contract surface, low switching cost    | Sticky — switching means rebuilding workflows on top        |
| Does my team have ongoing capacity to maintain this, or just to build v1?                                     | Just v1 — buy the thing with a roadmap and a support team  | Ongoing — maintenance is core competency                    |

**Tiebreaker:** if the matrix is genuinely split, default to **buy the infra layer, build the opinionated work on top.** The mistake people make is the inverse — building infra they'll resent maintaining, while buying the opinionated layer that should reflect *their* point of view.

## Questions to ask the vendor (steal these)

When you're leaning buy, these surface whether they're an infra primitive or a walled garden:

1. "Show me your API and webhook surface." (If they bury the docs, that's the answer.)
2. "Can a non-engineer change a workflow / routing rule / prompt without filing a support ticket?"
3. "What happens if I want to export everything and leave?"
4. "How often does pricing change with usage?"
5. "Who else is building above your platform?" (Strong ecosystem = strong infra.)

## What to flesh out in future recordings

- More examples beyond Gong + support tooling — CRM, billing, observability?
- The "escape-hatch logic" pattern — boring infra is mostly the exception cases, not the happy path
- A specific war story (good or bad) where this matrix would have changed the call
- Companion piece: see `llm-apps-personalize-saas` for the upstream argument
- Companion piece: see `breadth-of-features-is-a-liability` for the corollary on what wins now
