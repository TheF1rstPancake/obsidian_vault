---
title: "The 0→1 fight: self-serve or headcount?"
slug: zero-to-one-self-serve-or-headcount
status: raw
target: substack
created: 2026-05-14
updated: 2026-05-14
tags: [strategy, ops, ai, build-vs-buy, gtm]
---

# The 0→1 fight: self-serve or headcount?

> Stub. Seed thesis from the LinkedIn post on AI-built meal planning tools (linked below). Awaiting voice recordings to develop the broader organizational angle.

## The seed thesis (from a LinkedIn post)

> "Any tool is judged by how quickly users go from 'I have an idea' to 'here's a working version.' Feature checklists only get you from 0→0.3. How a tool handles errors determines if you make it the rest of the way."

That observation is about AI tools, but it generalizes. **Every team eventually faces the same question for every workflow they own: do we hand users a self-serve tool that will get them to 0.3, or do we put a human body in the path?**

The 0→1 fight is where most products and most internal workflows quietly stall — not at launch, not at scale, but in the middle stretch where users have to figure out what to do when the happy path breaks. That stretch is where teams decide, sometimes deliberately and sometimes by accident, whether the workflow gets a person assigned to it or a tool.

## Why this matters now

This decision used to be easy. Self-serve tools were limited; humans handled anything ambiguous. Self-serve was for the obvious cases; everything else got an SE, an FDE, a CSM, a deal desk, a solutions architect.

AI tools just moved the line. They can now plausibly handle 70% of "ambiguous" 0→1 work that used to require a human — *until* they fail, at which point they fail without explanation and the user has nowhere to go. The line between "self-serve handles this" and "you need a body" is now genuinely fuzzy, and the failure mode of getting it wrong has changed shape too.

## The tradeoff (the part you steal)

When you're deciding whether a given workflow should be self-serve or staffed, ask these questions. They generalize across product surfaces, internal ops, customer onboarding, and AI tooling specifically.

| Question | Lean self-serve if... | Lean human body if... |
| --- | --- | --- |
| How frequent is this workflow? | High volume, repeated by many users | Rare, high-stakes, low-volume |
| How costly is being stuck mid-way? | Low — user can give up and try later without consequence | High — being stuck blocks revenue, churns the user, or causes downstream damage |
| How well does the tool surface and explain errors? | Errors are legible, actionable, debuggable by the user | Errors are opaque ("Unexpected error" with no context), and the user has no way in |
| Can the user reason about *why* the tool did what it did? | Yes — the tool is transparent about its decisions | No — outputs feel magical until they're broken |
| What's the cost of the user just giving up? | Low — they'll come back, or it's not your most valuable user | High — this is a deal, a power user, a strategic account |
| What's the long-tail variance of inputs? | Narrow — most users are doing roughly the same thing | Wide — every user's situation is different in ways that matter |

**Tiebreaker:** when you genuinely can't tell, default to **human body for the first 90 days, self-serve afterward**. Use the human to learn what the workflow actually looks like in the wild, *then* automate. The opposite order — automate first, hire a human when it breaks — tends to leave six months of stranded users behind.

## The vaporware trap

The LinkedIn post identified a specific failure mode: tools that look great on first pass and collapse the moment a user tries to actually finish the job. Beautiful vaporware. Feature checklists that get you to 0.3.

The organizational version of this is when leadership decides "we don't need an SE/CSM/solutions team — the product is good enough to self-serve." The product *is* good enough... for the demo. The 0→1 fight happens after the demo, and it's the part that doesn't show up on the product roadmap because nobody on the team has watched a real user get stuck and rage-quit in silence.

The headcount math is the same trap inverted: "we'll just hire more humans" works until those humans become the bottleneck and you discover you never invested in the parts of the workflow that *could* have been self-served. Then you're paying linearly forever for a problem you could have automated halfway through.

## What to flesh out in future recordings

- A specific story of a team that got this wrong in *one* direction — over-indexed on self-serve and ate the churn, or over-indexed on humans and capped their own growth
- The AI-specific version: when does an AI agent count as "self-serve" vs "a body"? It's not really either. Maybe there's a third category — "supervised self-serve" — where AI handles the happy path and a human handles the escalations, and the *handoff* is the actual workflow
- A 90-day self-staffed → automated playbook: what specifically does the human do, what do they document, what gets handed off to the tool?
- Counter-position: when *should* you ship vaporware on purpose to validate demand before building the durable version? The 0→1 fight isn't always the right fight.
- Connection to LinkedIn post 02 (the meal-planner narrative) as the opening hook — possibly excerpt 2-3 lines verbatim, then pivot to the organizational scale
- Companion piece: `build-vs-buy-llm-era` — same decision frame applied to vendor selection
- Companion piece: `breadth-of-features-is-a-liability` — "feature checklists only get you to 0.3" is the same thesis
- Companion piece: `decomposing-software-apps` — the four-layer lens helps explain why error handling failures sit in the interface/logic seam
- Companion piece: `ai-native-se-stack` — the SE org of the future is essentially the human-body half of this exact question
- Companion piece: `fde-is-consulting` — FDEs are the canonical "body assigned to 0→1" role

## Source: the LinkedIn post that seeded this

Saved at `vault-meta/voice-samples/02-linkedin-meal-planner-zero-to-one.md`. The post is the user's own prior thinking; this article extends it from a tool-evaluation observation into an organizational design decision.
