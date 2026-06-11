---
title: "Internally, documentation is going the other way"
slug: internal-docs-as-context
status: raw
target: substack
created: 2026-06-11
updated: 2026-06-11
tags: [sales-engineering, ai, documentation]
---

# Internally, documentation is going the other way

Working with coding agents has trained all of us on the same habit: plan first, then execute. Why? Context drift. The back-and-forth of *building* a plan is useful while you're building it; once the plan is set, that conversation history is no longer meaningful, and you're better off collapsing it down into "this is the plan, execute." Build the SE brain right and it does the same thing: it generates the plans that your AEs and CSMs hand to *their* own agent — the one customized to their accounts, their knowledge, all their bells and whistles — and the documentation is just how you shuffle that context from the central brain into their execution layer. "Why not make an API call?" Sure — and what do you package *into* the call? Probably a fucking lot of text. Long-form text is how you communicate decisions, next steps, goals, and objectives, between humans and agents alike. It's not disappearing. You just want to spin it up quickly, clearly, and make it actionable.

That last point is where a lot of SE leaders are the bottleneck today and don't realize it. You hold a pile of context in your head; you have an hour-long 1:1 with an AE and talk through a ton of stuff — but the fact that you *said* it doesn't mean it was absorbed, and because it lives in your head there's no clean way to hand it off. Run an AI summary over the transcript of that 1:1 and you still need somewhere for it to *land*: this is the plan, this is what we discussed, these are the requirements as we understood them. That somewhere is the brain.

So the framing isn't "documentation goes away." It's that the corpus of documentation is the substrate, and the cost of standing it up keeps dropping. The current conventional wisdom for getting good output from Claude Code or any coding agent is exactly the plan-first pattern above. Companies like Glean and the entire retrieval-augmented-generation category assume the same thing — that there is an underlying corpus of documentation, and you build the application on top of it. What *has* changed in the last six months, and seems to keep getting better, is **the number of separate systems you need to amass that documentation is collapsing.** You don't need a bespoke RAG system. You don't necessarily need engineering tooling or eng involvement to build the retrieval interface. There may still be benefits to those, but the floor for getting a useful LLM-driven brain off the ground keeps dropping.
