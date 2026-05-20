---
title: "The AI-native SE stack: scaling sub-linearly with headcount"
slug: ai-native-se-stack
status: shaping
target: substack
created: 2026-05-07
updated: 2026-05-20
tags: [sales-engineering, ai, ops]
---

# The AI-native SE stack: scaling sub-linearly with headcount

## The thesis

Sales engineering headcount traditionally scales linearly with the sales team. You hire more AEs, you hire a balancing number of SEs. Part of the reason is that it's just easier — easier to do the math, easier to justify, and it removes guesswork. For every X AEs, you need Y supporting resources.

The other reason is that SEs aren't quota-carrying in the same way AEs are. The SE quota is a balance of the AEs they support. When a deal is won or lost, the AE gets the credit. How do you know the SE actually contributed? You kind of assume it. There are qualitative markers — the AE gives them a pat on the back — but that's about it.

That linear scaling is the thing I'd break. If I were rebuilding an SE team today, or inheriting one, I think there's a simple framework that lets you scale account-owning resources — CSMs and AEs — without scaling the supporting resources behind them. The way you do it is: you capture the SE brain and use AI.

This is going to be counterintuitive to a lot of SE leaders. A lot of leaders take pride in the size of their team — it's a signal of importance. But importance is your output to the business. If I can make it so that every contract that closes returns more revenue to the business — instead of paying off the operational support that got it closed — that's a win across the board. It frees up budget to grow in other areas, it increases the value of the business, and it increases the equity I hold in it. Wanting a smaller, higher-leverage team isn't a downgrade; it's the point.

## Why SEs have always wanted to automate themselves out

In a lot of SE orgs there's this desire to automate ourselves out of the job. SEs tend to be systems thinkers. Even at a 2:1 ratio, there's enough work and enough bullshit that the SE wants to figure out — how do I save my energy for the places where I can actually be helpful? How do I enable my AEs to be self-sufficient?

Every SE loves an AE who's willing to take on more autonomy, learn the product, own parts of the technical conversation. The AEs who freeze and punt every time a product question comes up are the least fun people to work with. That's also, paradoxically, where the SE proves the most value — but it's not where you want to live.

The balance you're trying to strike: enough supporting resources behind your AEs that deals close, but as few as possible, so more of the closed revenue flows back to the business instead of paying off the supporting cast.

## Why the old automation attempts failed

Historically when teams try to automate the SE, you build a knowledge hub or an "intelligent" intake form that tells the AE what to do next. It goes stale almost immediately — especially if the product is evolving rapidly, your ICP is shifting, or you're moving up-market into a motion you haven't run before. Maintenance kills it.

The deeper problem is that the system needs to be **self-documenting** — not self-learning, those are different things — and historically the documentation depended on people. Not everyone contributes. Some people don't think it's important. Some can't recognize what's worth capturing. The result is wildly inconsistent person to person, and because most teams have plenty of SEs anyway, fully automating it never feels urgent. So SEs do it in pockets: they build shared assets and lingo with their pod of AEs, and it never scales further, because the level of effort to maintain and propagate it is just beyond what feels worth it.

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

### Organization matters less than you think

The historical instinct with traceability is to make it clean: every functional capability maps to exactly one solution-agnostic capability, every solution-agnostic capability maps to exactly one goal. Humans in the loop want there to be one right answer. They get over-specific.

LLMs invert this. **Documentation is becoming more important; the organization of it is becoming less.** Context windows are large enough, and grep-over-text is good enough — we've seen it with Claude Code — that you can let the relationships be messy. A functional capability can map to multiple solution-agnostic capabilities. Multiple solution-agnostic capabilities can mean roughly the same thing. That's fine.

Organize by what something *is* — goal, agnostic requirement, functional capability — and let the relationships between them stay imperfect. The interface to all of this is going to be an LLM, and the LLM will navigate the mess for you. Yes, LLMs have bad judgment about novel prioritization, but that's not what we're asking them to do here. We're asking them to summarize and evaluate existing text and stay in the general vicinity. That's something they're inherently good at — better than your team would be doing it by hand.

### How the data lands

The inputs:

- **Calls.** Gong, Granola, whatever your recorder of choice is — transcripts, speaker attribution, the works.
- **Emails.** This is the underinvested one. Most teams monitor calls and do call coaching, but a huge amount of communication happens between calls, and some of it represents the phases of your sales cycle far more cleanly than the calls themselves do. You have to be willing to monitor and manage email too.
- **Attachments.** Decks, PDFs, support docs, requirements lists — everything that comes alongside the calls and emails.
- **Product updates.** Every pull request should be analyzed for what it functionally changes about the product. With coding agents writing most PRs now, the raw material is there.
- **Roadmap.** The one input the system can't pull on its own. This is where human intervention is required, and where the initial SE team builds the process with product to feed forward-looking capabilities into the brain.

The agent scans these as events occur and extracts into the three buckets. Insertion policy: insert everything to start. If the extracted item is a close duplicate of something already in the library, don't reinsert — but *do* attach the new customer to the existing entry as metadata. Even when the framing isn't new, the fact that another customer used that framing is itself valuable signal. Wire in Salesforce/CRM for segment, price, ICP context so you can slice the library later.

You get a live-updating cascading tree of knowledge. Every conversation your team has gets summarized and landed somewhere — not just as a "oh shit, what happened on that call" transcript, but as a self-documenting record of *how your team is speaking about your product*.

### What the data unlocks once it's there

Because every entry is tied to customers and outcomes, you can ask which framings are winning and which aren't. If a phrase your team uses correlates with weaker outcomes, is the phrase ineffective — or is it a signal that the customers it's used on are outside your ICP? And if they're outside ICP, why? Most teams don't have any of this today.

The interface is a chat agent sitting on top of the three tables. You can walk from goals and outcomes to solution-agnostic requirements to a recommended solution. I'm being a little loose with "recommended solution" — in practice it's a list of requirements with green checkboxes, and in my experience it's hard to fully escape the requirements table at some point in a sales conversation. Teams like seeing that.

What I'm being vaguer about — and need to come back to — is how all of these core components get tied together into a single solution package or write-up that's actually customer-facing. [?] Drafting a summary email of the heard problem and the way the product solves it is one obvious output. A pattern-match query from an SE working a hard deal ("who else have we proposed solutions to that looks like this?") is another. The central audit trail and the central brain support both.

## What the SE actually becomes

The SE's job shifts to maintaining and shepherding the agents that run this system.

A lot of "go-to-market engineer" job postings out there are really just rebranded Salesforce operations. That's too narrow. Your SEs interface directly with customers, hear pain points from AEs, and hear directly from implementation when something has gone wrong. They have touched grass in a way your ops team never has. Their ability to build the agents that run this system is going to be far better than what any Salesforce operator can deliver.

As AEs run calls — even just live, from the transcript — you can process the conversation, match against the existing patterns, and feed back: here's what we heard, here's what we recommend. AEs are generally quite good at getting customers to talk about their problems; the part they struggle with is translating that into a solution conversation that isn't just product-speak. The brain does that translation for them. The AE doesn't have to come into the chat interface as a separate ritual — as soon as a call ends, the summary lands. Mid-call curveball? They can go ask the chat live.

What's left for the SE is to be a **SWAT team**. Three triggers for spending an SE:

1. **Greenfield problems** — a customer brings a problem where the mapping into the brain is unclear or unexplored.
2. **High-stakes opportunities** — the deal is big enough that you'll pay the cost of more bodies to de-risk it.
3. **Fire drills** — retention issues, escalations, success problems that the central brain can't unblock on its own.

### Cold-start problem

The brain itself isn't hard to build, but there's a real cold-start cost. You need a diligent, dedicated, high-output initial team to sit on calls, tune the agents' judgment about what's meaningful, and stand up the process with product for the roadmap input. The system isn't free; it's just dramatically cheaper to *run* than to *bootstrap*.

## Headcount planning under this model

This makes planning harder in one specific way: how do you know how many fire drills you'll have? But the framework is simpler than it sounds.

Most SE leaders default to an 80/20 split — 80% customer-facing, 20% operations. That ratio exists because the team is large enough that you have to justify their existence by putting them in front of customers constantly. In this model, flip it closer to **70/30**, because you want them to have the time to build, maintain, and grow the systems.

The shift in math is the bigger point: you move from a **ratio-based** model (X AEs → Y SEs) to a **deterministic** model based on the total number of accounts you expect to close.

The arithmetic:

- Scope to **enterprise contract accounts only**. Self-serve goes into a different support bucket and shouldn't be in this universe.
- Assume ~80% of those accounts follow the happy path through the brain — both land and renewal — without SE touch.
- The remaining ~20% are the ones an SE actually needs to engage on (greenfield, high-stakes, fire drills).
- Each SE can carry roughly **5–10 accounts** at a time depending on complexity. [?] (Want to sharpen this with real data.)
- Headcount = (20% of your enterprise account base for the year) ÷ ~5 accounts per SE.

For high-end strategic accounts, the long tail looks a little different — it's more about how many opportunities are in pipeline and how many an SE wants to juggle at once — but the 80/20 still holds.

One constant that hasn't changed with AI: for every hour you spend with a customer, there are roughly two hours of follow-up work, especially on complex deals. So 70% of a 40-hour week is ~30 hours customer-facing, which given the 1:2 ratio means roughly 8–10 hours of actual customer calls per week, and the rest follow-up.

## What to flesh out in future recordings

- The hiring implication: if AI absorbs the linear work, what's left for the humans who *aren't* the SWAT team? (Probably its own article.)
- A concrete before/after: a workflow I've personally moved from manual → AI-native, with metrics if I have them.
- The "presented incorrectly, it's more confusing for customers than helpful" point — what does *correct* presentation of the traceability tree look like to a customer? [?]
- How the three-table outputs get composed into a single customer-facing solution package. [?]
- Sharpening the 5–10 accounts/SE number with real data.
