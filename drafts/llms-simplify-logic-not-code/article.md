---
title: "The Point of LLMs Isn't Less Code. It's Less Logic."
slug: llms-simplify-logic-not-code
status: raw
target: ghost
created: 2026-07-15
updated: 2026-07-15
tags: [ai, engineering, llms, product]
visibility: public
point: >
  Teams keep framing LLM adoption as deterministic versus non-deterministic, but that's the
  wrong axis. The real question is how many if-this-then-that branches it takes to capture a
  workflow's nuance. When that number gets large, the fix is to hand the judgment call to an
  LLM instead of coding it. Ironically, coding agents are bad at doing this to their own output:
  trained on decades of verbose, deterministic code, they'll happily build you a 2,000-line
  state machine when a few sentences of natural language would do. The actual shift LLMs demand
  isn't less code up front. It's less logic, and a lot more observability once the thing is live.
ghost_url:
---

Every engineering team I talk to that's adopting LLMs ends up having some version of the same conversation: is this process deterministic, or is it non-deterministic? It's the wrong question. LLMs are non-deterministic in the sense that you can feed the same model the same prompt twice and get two different answers. But most business workflows aren't actually asking for that kind of determinism. There's a flowchart. There's a specific outcome you want, and you want to hit it consistently. The steps to get there are generally known. You could write those steps as a pile of if-this-then-that statements and it would work, deterministically, maybe 60% of the time, with the other 40% kicked out as errors for a human to handle.

So the real axis isn't determinism versus non-determinism. It's the volume of if-this-then-that statements it takes to capture all the nuance in a workflow.

## Where the if-then tree breaks

Some problems have known inputs but messy thresholds. Signal A has to be greater than X but less than Y, and signal B has to be less than Z, and the combination of those conditions is genuinely hard to model. You end up setting arbitrary cutoffs, the branches multiply, and the whole thing becomes a web that's hard to reason about and harder to maintain. What you actually want isn't a bigger tree. You want something that looks at the signals, applies a set of guiding principles, and makes a judgment call.

That's where an LLM earns its place: not as a code generator, but as a replacement for the decision tree itself. Instead of building the tree, you make an API call. Here are the signals, here's the outcome I want, go figure it out.

## LLMs are bad at using LLMs
