---
title: "The AI-native SE stack: scaling sub-linearly with headcount"
slug: ai-native-se-stack
status: published
target: ghost
created: 2026-05-07
updated: 2026-07-08
tags: [sales-engineering, ai, ops]
point: >
  Sales engineering headcount doesn't have to scale linearly with the
  sales team. Treat the SE org as a product team building an internal
  "SE brain" (an LLM operating over a three-table documentation corpus
  of goals/outcomes, solution-agnostic requirements, and product
  capabilities), and AEs and CSMs become self-sufficient on most deals.
  SEs shift from per-deal support to building that brain and acting as
  a SWAT team for greenfield, high-stakes, and fire-drill cases, letting
  account-owning headcount grow while supporting headcount scales
  sub-linearly.
ghost_url: https://thefirstpancake.ghost.io/ai-native-se-stack/
---

# The AI-native SE stack: scaling sub-linearly with headcount

## The thesis

Sales engineering headcount traditionally scales linearly with the sales team. You hire more AEs, you hire a balancing number of SEs. Part of the reason is that it's just easier. Easier to do the math, easier to justify, and it removes guesswork. For every X AEs, you need Y supporting resources.

The other reason is that SEs aren't quota-carrying in the same way AEs are. The SE quota is a balance of the AEs they support. When a deal is won or lost, the AE gets the credit. How do you know the SE actually contributed? You kind of assume it. There are qualitative markers. The AE gives them a pat on the back. But that's about it.

That linear scaling is the thing I'd break. If I were rebuilding an SE team today, or inheriting one, I think there's a simple framework that lets you scale account-owning resources, CSMs and AEs, without scaling the supporting resources behind them. The way you do it: capture the SE brain and use AI.

This is going to be counterintuitive to a lot of SE leaders. A lot of leaders take pride in the size of their team. It's a signal of importance. But importance is your output to the business. If I can make it so that every contract that closes returns more revenue to the business, instead of paying off the operational support that got it closed, that's a win across the board. It frees up budget to grow in other areas, it increases the value of the business, and it increases the equity I hold in it. A smaller, higher-leverage team is the actual goal.

## The reframe: SEs build an internal product

The cleanest way to think about an AI-native SE org is as a **product team building an internal product**. The product is a requirements / capability mapping / solution-defining application. The audience is your AEs and CSMs. The product managers and engineers of that product are your SEs.

This is the reframe. Once you accept it, the mental model for what's important, how many people you need to hire, and what "good" looks like for an SE all shift.

This isn't a production-scale product. You're not building for tens or hundreds of thousands of concurrent users. You're building for **20, 30, 50, 100 people** at a typical small-scale startup, maybe 300 or 400 if you balloon. That has real implications. There are personas to design for and capability differences to handle, but the engineering surface area is small. A few motivated and competent SEs can handle this.

Under this frame, SEs split their time between two modes:

- **Internal product team** for the brain itself: the PMs and engineers of the AE/CSM-facing system.
- **External SWAT team**: when AEs and CSMs hit a customer scenario the product can't cleanly handle, you send an SE in for that specific case.

The majority of customer interactions should flow through the well-defined product. SEs only touch deals where the product's mapping breaks down.

That is the first cut between singleplayer and multiplayer. A setup one person can run for themselves is useful, but it is not the same thing as infrastructure another SE can inherit, extend, and trust. If the system breaks as soon as a second person touches it, it was never built for the team. The setup here is heavier than the singleplayer posts make it look, and it is worth the weight because the payoff is team-scale rather than personal-scale.

## Why SEs have always wanted to automate themselves out

In a lot of SE orgs there's this desire to automate ourselves out of the job. SEs tend to be systems thinkers. Even at a 2:1 ratio, there's enough work and enough bullshit that the SE wants to figure out: how do I save my energy for the places where I can actually be helpful? How do I enable my AEs to be self-sufficient?

Every SE loves an AE who's willing to take on more autonomy, learn the product, own parts of the technical conversation. The AEs who freeze and punt every time a product question comes up are the least fun people to work with. That's also, paradoxically, where the SE proves the most value. But it's not where you want to live.

The balance you're trying to strike: enough supporting resources behind your AEs that deals close, but as few as possible, so more of the closed revenue flows back to the business instead of paying off the supporting cast.

The tooling market has noticed this tension. Its answer is aimed at the wrong unit.

## The market is optimizing the wrong unit

Right now the tooling market is geared toward making a *singular SE* more efficient: something always listening, able to pivot live on a call, built to reduce the back-and-forth it takes to get to a technical win.[^ownership] Strip away the pitch and most of these tools are **automating the demo.** It used to be "you need a demo, let's schedule it for next week." Now it's "you want a demo? Here, knock yourself out."

That's a real improvement, but it's the wrong altitude. If demoing is the only job you think your SEs do, then yes, AI replaces them outright. "Make our SEs better at demos" quietly concedes that the SE is a demo machine.

And the back-and-forth never fully collapses, nor should you try to make it. The person who owns collapsing it is the **AE**; they drive the momentum and the beat of an engagement, and good SE orgs are already very responsive to that beat. When a problem lands way out of field, you *want* an SE to take a beat and think. So the question that matters is how long the delay is.

Traditionally that delay is about a week. Customers book a week out; you meet, make progress, schedule next week; meet, make progress, schedule next week. A big chunk of that cadence is pure SE bandwidth: how long it takes to think through a solution and document it. AI out of the box already compresses that. You should be able to come back confidently in **24–48 hours instead of seven days.** That compression does something a better demo can't. It removes one more player the AE has to wait on, so they can drive the conversation at a pace that's comfortable for them and the customer.

So reframe what the tool is *for*: it makes your **AEs less reliant on others.** Fewer bottlenecks, more self-sufficiency, one fewer player who has to weigh in before a deal can move.

## Why the old automation attempts failed

Historically when teams try to automate the SE, you build a knowledge hub or an "intelligent" intake form that tells the AE what to do next. It goes stale almost immediately, especially if the product is evolving rapidly, your ICP is shifting, or you're moving up-market into a motion you haven't run before. Maintenance kills it.

The deeper problem is that the system needs to be **self-documenting** (not self-learning, those are different things), and historically the documentation depended on people. Not everyone contributes. Some people don't think it's important. Some can't recognize what's worth capturing. The result is wildly inconsistent person to person, and because most teams have plenty of SEs anyway, fully automating it never feels urgent. So SEs do it in pockets: they build shared assets and lingo with their pod of AEs, and it never scales further, because the level of effort to maintain and propagate it is just beyond what feels worth it.

What hasn't changed, even with AI, is the *volume* of written artifacts around any opportunity. Contracts, solution write-ups, requirements docs, decks. All written. Call transcripts are now ubiquitous because LLMs are good at parsing those walls of text and extracting the key beats by audience.

The maintenance problem is what flips with LLMs in the loop. It's no longer a never-ending slog of manual updates. Running the system is dramatically cheaper than bootstrapping it.

## The documentation isn't going anywhere

**Three reasons it persists.**

**1. Customers want the paper trail.** If you're selling to enterprise (and, depending on the vertical, well into mid-market), customers want documentation. Sometimes it's purely for show. More often it's the need for something tangible to reference, something that makes the solution feel concrete. Until you actually implement, the solution isn't finalized; even after the deal closes there's unease and open questions. The job of the write-up is to state plainly what's going to happen and give the customer the comfort that there's a plan. If even one customer requires documentation, the documentation keeps getting produced, which means someone keeps producing it, and you want to produce it *fast*, because every cycle of back-and-forth is delay between you and a closed deal.

**2. Documentation is a receipt. Protection for you and the customer.** That paper trail is leverage during renewals and during the tense moments in implementation. When a customer pushes a requirement that was never agreed to, you can point at the document: "this is new, it wasn't something we scoped." Usually it reads as a change to scope, and scope changes have tradeoffs, usually on timeline, so let's make sure no one's surprised. That puts the onus back on the customer to acknowledge they changed the deal, which in my experience defuses the situation rather than escalating it. Without the receipt it degrades into conflicting accounts, and your implementation and support teams have nothing to stand on. Even with near-perfect transcript recall, you're now combing through call logs and reinterpreting phrases that were taken out of context. With a document that states the requirements and the plan, the room for interpretation is simply smaller.

This is also where requirements *quality* shows up. Lossy requirements, ones written as goals rather than functional needs, reopen exactly the ambiguity you were trying to close. Take "decrease time spent writing documents." That's a goal. There are a hundred ways to satisfy it, which is exactly the ambiguity a real requirement is supposed to remove. AI is genuinely good at producing decent, comprehensive-looking documentation quickly, *if* it has the right framework and guidance for how to document within the context of your business. That guidance is the piece most teams are missing, and it's the piece the solutions team usually fills in by hand, which is exactly how they become the bottleneck. Removing that bottleneck means handing the guardrails and frameworks to the customer-facing teams so they can produce the documentation themselves, with the SWAT escape hatch still bolted on for the genuinely novel case.

**3. Internally, documentation isn't shrinking either.** The same plan-first habit AI coding agents are teaching engineering teams is reshaping how context moves internally, from a central brain into each rep's own execution layer. The internal trend points the same direction as the customer-facing one.

So the three-table system below is nothing exotic. It's the documentation corpus the LLM operates over. Everything else (chat interface, summarizers, extractors) is increasingly off-the-shelf.

## The handoff that breaks first

The first place this shows up is the handoff from sales to implementation. It is the most documentation-heavy part of the motion, and usually the first one to feel growth pressure.

The output of the SE *is* the input into the implementation or onboarding team, whether it's a new land or a growth motion. The reason you do solution validation at all is twofold: get the customer to realize the solution is possible, and set implementation up for success. If you didn't care about implementation succeeding, you'd just lie and say yes to everything.

Implementation teams love consistency. They love structure and patterns. Every customer is unique, and you want to lean into that uniqueness in the discovery conversation. But the package you hand off should be consistent, and ideally draw parallels to other customers.

## The three-table system

Pick your organizational tool of choice. Google Sheets technically works; it's a bad call. Airtable is what I'd use.

There are a few repeatable data points that come up on every opportunity. No matter what sales framework you run (MEDDIC or otherwise), you will always have:

1. **Customer goals and outcomes**.
2. **Solution-agnostic requirements**: what the customer needs to hit those goals, in the language the market already uses to describe the problem.
3. **Your product's functional capabilities**: what it actually does, and how each capability ladders up to the goals and outcomes.

That's it. Three layers, with traceability between them. None of this is new. It's requirements gathering and traceability 101. Most SaaS orgs don't do it because it's a lot of paperwork, and if you present it back to customers incorrectly it's more confusing than helpful. Good documentation clears that up fast: state (1) the customer's specific problem, (2) the requirements needed to solve it, and (3) how the product meets those requirements, naming which pieces of the product do what. A table or flowchart works depending on the audience. The goal is to get past generic pattern-matching ("we've solved this before") and into specificity: exactly how each of this customer's requirements maps to your product.

### Organization matters less than you think

The historical instinct with traceability is to make it clean: every functional capability maps to exactly one solution-agnostic capability, every solution-agnostic capability maps to exactly one goal. SE teams writing this by hand want there to be one right answer. They get over-specific.

LLMs invert this. **Documentation is becoming more important; the organization of it is becoming less.** Context windows are large enough, and grep-over-text is good enough (we've seen it with Claude Code) that you can let the relationships be messy. A functional capability can map to multiple solution-agnostic capabilities. Multiple solution-agnostic capabilities can mean roughly the same thing. That's fine.

Organize by what something *is* (goal, agnostic requirement, functional capability) and let the relationships between them stay imperfect. The interface to all of this is going to be an LLM, and the LLM will navigate the mess for you. Yes, LLMs have bad judgment about novel prioritization, but that's not what we're asking them to do here. We're asking them to summarize and evaluate existing text and stay in the general vicinity. That's work no individual rep should be doing from memory: scanning the full solution space, matching requirements, surfacing the right framing. The system does it for them.

### How the data lands

The inputs:

- **Calls.** Gong, Granola, whatever your recorder of choice is: transcripts, speaker attribution, the works.
- **Emails.** This is the underinvested one. Most teams monitor calls and do call coaching, but a huge amount of communication happens between calls, and some of it represents the phases of your sales cycle far more cleanly than the calls themselves do. You have to be willing to monitor and manage email too.
- **Attachments.** Decks, PDFs, support docs, requirements lists, everything that comes alongside the calls and emails.
- **Product updates.** Every pull request should be analyzed for what it functionally changes about the product. With coding agents writing most PRs now, the raw material is there.
- **Roadmap.** The one input the system can't pull on its own. This is where human intervention is required, and where the initial SE team builds the process with product to feed forward-looking capabilities into the brain.

The agent scans these as events occur and extracts into the three buckets. Insertion policy: insert everything to start. If the extracted item is a close duplicate of something already in the library, don't reinsert, but *do* attach the new customer to the existing entry as metadata. Even when the framing isn't new, the fact that another customer used that framing is itself valuable signal. Wire in Salesforce/CRM for segment, price, ICP context so you can slice the library later.

You get a live-updating cascading tree of knowledge. Every conversation your team has gets summarized and landed somewhere. The transcript answers what happened on that call. The library answers how your team is speaking about your product.

### What the data unlocks once it's there

Because every entry is tied to customers and outcomes, you can ask which framings are winning and which aren't. If a phrase your team uses correlates with weaker outcomes, is the phrase ineffective, or is it a signal that the customers it's used on are outside your ICP? And if they're outside ICP, why? Without a system like this, those questions are just guesses.

The interface is a chat agent sitting on top of the three tables. It can be as simple as a skill inside Claude that every AE has access to: they ask "I've got this customer problem, what do I do?" and it walks them through the research with them. You can walk from goals and outcomes to solution-agnostic requirements to a recommended solution. I'm being a little loose with "recommended solution": in practice it's a list of requirements with green checkboxes, and in my experience it's hard to fully escape the requirements table at some point in a sales conversation. Teams like seeing that.

You can layer triggers on top: fire a summary on call completion, or push every rep a weekly digest of their deals with recommended next steps. But the right default is **ad-hoc, on-demand access.** Any time you build around a fixed trigger, you'll have people who don't want to wait for it, or who have an exception case the trigger doesn't cover. So at a minimum you need a way for someone to reach into the brain on their own terms and get back in the loop. There are plenty of agent harnesses out there you could use to build exactly this: a solution-engineering brain that gives the sales team on-demand access to what they need to push a deal forward without over-relying on the supporting resource.

The output is always a document plus an email asking for feedback. Format is org/audience-dependent (Excel, Word doc, slides) and it doesn't matter. The real problem is AEs who don't want to write it (or don't know how), combined with SEs being asked to provide extraordinary detail to protect post-sales and implementation teams, so these documents take too long to produce. AI reduces that to minutes *if* it has the right framework and plan, which is exactly what the brain creates. That's the payoff of the whole system.

## What the SE actually becomes

If the brain is an internal product, the SE's job description rewrites itself. They are the **product managers and engineers** of an application whose users are AEs and CSMs. AEs and CSMs, in turn, are the **forward-deployed engineers** of that product into customer accounts. When the product doesn't cleanly cover a customer's scenario, the SE goes out as the SWAT response.

A lot of "go-to-market engineer" job postings out there are really just rebranded Salesforce operations. That's too narrow. Your SEs interface directly with customers, hear pain points from AEs, and hear directly from implementation when something has gone wrong. They have touched grass in a way your ops team never has. Their ability to build the agents that run this system is going to be far better than what any Salesforce operator can deliver.

As AEs run calls (even just live, from the transcript), you can process the conversation, match against the existing patterns, and feed back: here's what we heard, here's what we recommend. AEs are generally quite good at getting customers to talk about their problems; the part they struggle with is translating that into a solution conversation that isn't just product-speak. The brain does that translation for them. The AE doesn't have to come into the chat interface as a separate ritual. As soon as a call ends, the summary lands. Mid-call curveball? They can go ask the chat live.

What's left for the SE on the customer-facing side is to be a **SWAT team**. Three triggers for spending an SE:

1. **Greenfield problems.** A customer brings a problem where the mapping into the brain is unclear or unexplored.
2. **High-stakes opportunities.** The deal is big enough that you'll pay the cost of more bodies to de-risk it.
3. **Fire drills.** Retention issues, escalations, success problems that the central brain can't unblock on its own.

That escape hatch matters as much as the automation. The whole system hands control back to the AEs and CSMs with guardrails, but a rep can always raise a hand and say "this is a genuinely custom case; even with the AI support I'm not sure I can carry it alone, I need a partner." That's when you pull an SE in.

### Cold-start problem

The brain itself isn't hard to build, but there's a real cold-start cost. You need a diligent, dedicated, high-output initial team to sit on calls, tune the agents' judgment about what's meaningful, and stand up the process with product for the roadmap input. Running it is dramatically cheaper than bootstrapping it.

The cold-start does more than bootstrap the brain. It is where you find out whether the system is actually multiplayer. If a second person can't contribute without breaking it, or without first absorbing every internal convention you built for yourself, then what you stood up is still singleplayer, and the bootstrap phase is where that surfaces. A system the team can extend has to let a new contributor add to it without needing to understand all of it first.

## Headcount planning under this model

This makes planning harder in one specific way: how do you know how many fire drills you'll have? But the framework is simpler than it sounds.

Most SE leaders default to an 80/20 split: 80% customer-facing, 20% operations. That ratio exists because the team is large enough that you have to justify their existence by putting them in front of customers constantly. In this model, flip it closer to **70/30**, because you want them to have the time to build, maintain, and grow the systems. They are, after all, the product team for the internal brain.

The shift in math is the bigger point: you move from a **ratio-based** model (X AEs → Y SEs) to a **deterministic** model based on the total number of accounts you expect to close.

The arithmetic:

- Scope to **enterprise contract accounts only**. Self-serve goes into a different support bucket and shouldn't be in this universe.
- Assume ~80% of those accounts follow the happy path through the brain (both land and renewal) without SE touch.
- The remaining ~20% are the ones an SE actually needs to engage on (greenfield, high-stakes, fire drills).
- Each SE can carry roughly **5–10 accounts** at a time depending on complexity. The math is 1 hour with a customer and about 2 hours of follow-up for every hour spent live. That adds up fast, which is why the calendar fills up before the week does.
- Headcount = (20% of your enterprise account base for the year) ÷ the number of accounts one SE can realistically carry.

For high-end strategic accounts, the long tail looks a little different. It's more about how many opportunities are in pipeline and how many an SE wants to juggle at once. But the 80/20 still holds.

One constant that hasn't changed with AI: for every hour you spend with a customer, there are roughly two hours of follow-up work, especially on complex deals. So 70% of a 40-hour week still leaves room for a handful of customer calls, and the rest is follow-up. What *has* changed is the calendar cost of that follow-up: the slowest part used to be the SE thinking through and documenting a solution, which is exactly the work AI compresses from a week down to 24–48 hours.

The reason this matters: businesses do not want headcount to grow one-for-one with revenue. They want a limiting factor, or more accurately a magnifying factor, on headcount as revenue grows. The internal product the SE team builds and maintains *is* that limiting factor. It also happens to be the environment highly motivated SEs want to work in anyway. The incentives align.

[^ownership]: The SE team owns the system. Sales does not. Hand demo automation to the sales team and they'll talk it into saying yes to everything the customer asks for and deal with the consequences at implementation. You want the system grounded in truth and experience: it should absorb context from deals, calls, conversations, and emails, package it up, and track what's actually working and what isn't. That grounding is the whole point, and it's why the brain belongs to the people who get held accountable for whether implementation succeeds.
