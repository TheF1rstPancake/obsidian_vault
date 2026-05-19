---
title: "The AI-native SE stack: scaling sub-linearly with headcount"
slug: ai-native-se-stack
status: shaping
target: substack
created: 2026-05-07
updated: 2026-05-19
tags: [sales-engineering, ai, ops]
---

# The AI-native SE stack: scaling sub-linearly with headcount

## The thesis

Sales engineering headcount traditionally scales linearly with the sales team. You hire more AEs, you hire a balancing number of SEs. Part of the reason is that it's just easier — easier to do the math, easier to justify, and it removes guesswork. For every X AEs, you need Y supporting resources.

The other reason is that SEs aren't quota-carrying in the same way AEs are. The SE quota is a balance of the AEs they support. When a deal is won or lost, the AE gets the credit. How do you know the SE actually contributed? You kind of assume it. There are qualitative markers — the AE gives them a pat on the back — but that's about it.

That linear scaling is the thing I'd break. If I were rebuilding an SE team today, or inheriting one, I think there's a simple framework that lets you scale account-owning resources — CSMs and AEs — without scaling the supporting resources behind them. The way you do it is: you capture the SE brain and use AI.

## Why SEs have always wanted to automate themselves out

In a lot of SE orgs there's this desire to automate ourselves out of the job. SEs tend to be systems thinkers. Even at a 2:1 ratio, there's enough work and enough bullshit that the SE wants to figure out — how do I save my energy for the places where I can actually be helpful? How do I enable my AEs to be self-sufficient?

Every SE loves an AE who's willing to take on more autonomy, learn the product, own parts of the technical conversation. The AEs who freeze and punt every time a product question comes up are the least fun people to work with. That's also, paradoxically, where the SE proves the most value — but it's not where you want to live.

The balance you're trying to strike: enough supporting resources behind your AEs that deals close, but as few as possible, so more of the closed revenue flows back to the business instead of paying off the supporting cast.

## Why the old automation attempts failed

Historically when teams try to automate the SE, you build a knowledge hub or an "intelligent" intake form that tells the AE what to do next. It goes stale almost immediately — especially if the product is evolving rapidly, your ICP is shifting, or you're moving up-market into a motion you haven't run before. Maintenance kills it.

What hasn't changed, even with AI, is the *volume* of written artifacts around any opportunity. Contracts, solution write-ups, requirements docs, decks — all written. Call transcripts are now ubiquitous because LLMs are good at parsing those walls of text and extracting the key beats by audience.

The maintenance problem is what flips with LLMs in the loop. It's no longer a never-ending slog of manual updates. It becomes trivial.

## The frame to lead with

Don't lead with the tool list. Lead with **which workflows break first as the company grows, and in what order to AI-enable them.** The tools are supporting cast.

The first workflow to AI-enable is the handoff from sales to implementation. The output of the SE *is* the input into the implementation or onboarding team — whether it's a new land or a growth motion. The reason you do solution validation at all is twofold: get the customer to realize the solution is possible, and set implementation up for success. If you didn't care about implementation succeeding, you'd just lie and say yes to everything.

Implementation teams love consistency. They love structure and patterns. Every customer is unique, and you want to lean into that uniqueness in the discovery conversation — but the package you hand off should be consistent, and ideally draw parallels to other customers.

## The three-table system

Pick your organizational tool of choice. Google Sheets technically works; it's a bad call. Airtable is what I'd use.

There are a few repeatable data points that come up on every opportunity. No matter what sales framework you run — MEDDIC or otherwise — you will always have:

1. **Customer goals and outcomes**, and the *solution-agnostic* requirements the customer (and you) think are needed to hit them.
2. **How the market frames these problems** — how customers think about them, what other tools they're evaluating, the vocabulary in play.
3. **Your product's functional capabilities** — what it actually does, and how each capability ladders up to the goals and outcomes.

That's it. Three layers, with traceability between them. This isn't new — it's requirements gathering and traceability 101. Most SaaS orgs don't do it because it's a lot of paperwork, and if you present it back to customers incorrectly it's more confusing than helpful. Those are solvable problems.

The historical blocker was maintenance. Somebody had to sit there and manually collate. Someone does something cool this week and you want to codify it — good luck keeping the doc fresh.

With LLMs, this is trivial. As your team sends emails, decks, and PDFs — almost all of which already use the framing of "here's our understanding of your problem, here's what you said you need, here's what we can deliver" — the model parses and categorizes. With larger context windows, it can pull the existing data and decide: is this a duplicate, a reframe, or genuinely additive? You get a live-updating cascading tree of knowledge, as long as you can hook into the source systems.

## What the SE actually becomes

The SE's job shifts to maintaining and shepherding the agents that run this system.

A lot of "go-to-market engineer" job postings out there are really just rebranded Salesforce operations. That's too narrow. Your SEs interface directly with customers, hear pain points from AEs, and hear directly from implementation when something has gone wrong. They have touched grass in a way your ops team never has. Their ability to build the agents that run this system is going to be far better than what any Salesforce operator can deliver.

Sitting on top of the three tables, you have a chat interface and an agent. As AEs run calls — even just live, from the transcript — you can process the conversation, match against the existing patterns, and feed back: here's what we heard, here's what we recommend. You don't need to trust the AE to pull out the right signals; the system does it.

What's left for the SE is to be a **SWAT team**. A high-value opportunity comes in where you don't want to risk the AE running solo. Or a mid-market deal lands that looks like a potential new frontier — low revenue risk if it goes wrong, but if it goes right it represents an entire new customer segment. Those are the moments you spend an SE on.

## Headcount planning under this model

This makes planning harder in one specific way: how do you know how many fire drills you'll have? But the framework is simpler than it sounds.

Most SE leaders default to an 80/20 split — 80% customer-facing, 20% operations. That ratio exists because the team is large enough that you have to justify their existence by putting them in front of customers constantly. In this model, flip it closer to **70/30**, because you want them to have the time to build, maintain, and grow the systems.

One constant that hasn't changed with AI: for every hour you spend with a customer, there are roughly two hours of follow-up work, especially on complex deals. So 70% of a 40-hour week is ~30 hours customer-facing, which given the 1:2 ratio means roughly 8–10 hours of actual customer calls per week, and the rest follow-up. [?] (The arithmetic gets fuzzy here — needs a cleaner pass.)

Call it 8–10 active customers per SE at any given time. Then apply 80/20 to your customer base: of the customers you plan to have, the top 20% are the ones an SE actually needs to touch. Divide that 20% by ~10 accounts per SE, and that's your headcount. The rest of the base is served by the system.

## What to flesh out in future recordings

- The hiring implication: if AI absorbs the linear work, what's left for the humans who *aren't* the SWAT team? (Probably its own article.)
- A concrete before/after: a workflow I've personally moved from manual → AI-native, with metrics if I have them.
- The "presented incorrectly, it's more confusing for customers than helpful" point — what does *correct* presentation of the traceability tree look like to a customer? [?]
- Cleaner version of the headcount math.
