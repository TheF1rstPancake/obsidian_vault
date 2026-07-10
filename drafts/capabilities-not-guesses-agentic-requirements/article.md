---
title: "Capabilities, Not Guesses: Requirements in the Agentic Era"
slug: capabilities-not-guesses-agentic-requirements
status: raw
target: ghost
created: 2026-07-10
updated: 2026-07-10
tags: [product-management, ai-agents, requirements]
visibility: public
point: >
  Founding product teams without users often freeze on what to make agentic, fearing wasted work on the wrong requirements. But the tools users need rarely change between current and future state — only where those tools live does. If you understand the current state, the objective, and the resulting gap, you know the capabilities required even without knowing every combination users will invoke them in. That's exactly the gap an LLM agent is built to fill: hand it the capabilities, let user intent surface the ordering at runtime, and use failure signals to decide what to build next.
---

There's a tension I keep running into with my product engineering team right now. We're building a product from the ground up with no users yet, and there's a constant pull between building now, knowing some of it won't work, versus waiting for an initial set of users to learn from before we build anything.

That tension is most acute around one question: what do we make agentic in the product?

The engineering fear is straightforward. I don't fully know my requirements. If I build against the wrong ones, I've spent real time on something I'll have to tear out and rebuild. Worse, I end up with a feature that's just a failure.

But here's where it gets interesting. On the go-to-market side, we agree we don't know everything. We don't know every edge case, every exception a user will throw at us. There are almost certainly load-bearing assumptions sitting in our unknown unknowns that will change our approach once they surface. All of that is true.

What we do feel confident about is the set of capabilities people are looking for. What questions will they ask? What actions will they want an agent to take on their behalf? That part is clear. What's not clear is how people will mix and match those capabilities to get to their outcome.

That gap, known tools, unknown combinations, is exactly what an agentic LLM is designed for. It takes user intent, which you usually can't fully specify upfront, looks at the available suite of tools, and works toward an outcome. If it can't get there, that's not a dead end, it's a signal. Good observability tells you a user tried to do something and the system couldn't help. That becomes a review process: did this actually need to work, or is it a fringe case we don't need to touch?

## Why this feels new

If you've worked at a Series B company or later, you're used to making product bets off real signal. You have users to talk to, users to demo in front of. When you're on a founding team, you usually don't have that. You're making educated guesses about what's required, and it's fully on you, as the PM or the engineer, to say "this is what I think is right." There's no backstop. That's where the fear of wasted work comes from: you build something you're proud of, it hits real users, and it gets shredded.

I think agentic capability changes that calculus, not by removing the guesswork, but by changing what part of the guesswork actually matters.

## The problem you're solving is already known

Every product exists to solve a problem. If that problem isn't known, that's worth pausing on entirely, maybe the business itself isn't sustainable yet. But assuming it is: you should understand what the world looks like today, what users do in the absence of your product, and the negative consequences that come from that absence.

If that's sounding familiar, it's because this is just solution-agnostic design. Current state, negative consequences, and the future state that closes the gap. Most founders don't frame it as "I'm solving a negative problem," though. They frame it as moving toward an objective. Either way, the gap between current state and that objective is the surface area your product needs to cover.

> [!note] The diagram trick
> I've done this myself, on internal PRDs and customer-facing decks alike: draw the current state busier than it really is, more boxes, more mess, more manual steps, so the future state reads as clean and inevitable by comparison. It works because people pick up on that visual intuition without examining it. But it's a hack, not a finding. The real current state is usually calmer and more methodical than the version you'd sketch to make your product look good.

## What actually changes, and what doesn't
