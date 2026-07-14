---
title: "The future of SE: from demo machine to GTM architect"
slug: se-as-gtm-architect
status: shaping
target: ghost
created: 2026-05-08
updated: 2026-07-14
tags: [sales-engineering, ai, gtm, careers]
---

# The future of SE: from demo machine to GTM architect

## The thesis

If "FDE" is just *help me implement*, it's replaceable with a custom agent that knows the customer's stack. If "SE" is just demos, AEs can spin up tailored demo environments themselves with the right tools. The part of SE that doesn't collapse is the part nobody talks about: **SEs are the only role that already speaks to every silo** — sales, CS, product, support, ops. AI doesn't kill SE. It promotes it.

The future SE org is smaller in body count but higher leverage: a tier of **SE/AI architects** who build the GTM tools that connect those silos, plus a small SWAT bench that drops in on genuinely novel use cases. The work shifts from "sit in demos" to "ship the demo infrastructure, the discovery agents, the proposal generators, the post-sale handoff workflows."

## Why that silo-spanning claim is actually true

Every fast-growing team runs into the same problem: there's more work in a day than there's time to do it, and the playbooks don't exist yet for half of what shows up. AI helps with some of that. It can gather signals and synthesize them into a well-packaged thought. What it can't do is the internalization: deciding what that thought means for your org, your team, your roles. That still takes conversation and judgment, and there's no shortcut for the time it takes.

As teams get overwhelmed, they tend to fall into one of two failure modes. First, a team stakes a claim to a bucket of work so it has something exclusive to point to as its value. Second, a team clamps down its own roles and responsibilities so it has a defensible reason to say no — support teams do this constantly, building ticket tiers and letting some tickets wait longer than others because there's no bandwidth to give everything equal treatment.

Both moves carve out clean boundaries, and the space between the boundaries is where problems go to die. The sum of the parts doesn't add up to an efficient whole: if every team optimizes for what it owns, the gaps between what they own is where customers get dropped. When a customer's problem doesn't fit any bucket, someone still has to do the work, because the business is going to make sure that customer gets helped regardless of whose job it technically is. What usually happens is a finger-pointing match, then a semi-random assignment, then frustration. Or, the people willing to absorb the work — usually your top performers, the ones who can do their regular job and still find bandwidth for more — do it over and over until they can't anymore.

There's a better move if you want to grow your team's scope, and your own: own the gray area on purpose. Say, as a team, "we're responsible for the in-between. We don't know what that work entails yet. We're going to document it, learn it, share it back out, and decide later whether it belongs somewhere else."

Solutions/SE teams are unusually well-suited to make that claim, for two reasons. It's a jack-of-all-trades skill set built to support sales and CS rather than own a P&L of its own, and it's the only team that actually sits at the intersection of product, engineering, and go-to-market. Product and engineering are too deep in the build to see day-to-day GTM friction. Support, sales, and CS are each specialized enough that none of them can see across the seams between the others. If AI is what turns SE from a team that sits in meetings into a team that ships tools, those tools are the thing that brings order to a part of the business no one else has the reach or the mandate to touch. A support org builds systems to manage its tickets. It isn't going to be the one figuring out how those tickets become structured product-roadmap feedback, because that question is inherently more cross-functional than support-to-engineering. Everyone needs to contribute to it, and solutions is the only team positioned to own it.

## The headcount math (the part execs care about)

Old model: SE headcount scales ~linearly with AE headcount. Roughly 1:3 or 1:4.

New model: a small architect tier (1–3 people for a mid-market org) plus a SWAT bench (2–4) replaces 10–15 traditional SEs. The architect tier ships *tools*, not meetings. AEs self-serve the 80% of cases the tools cover. The SWAT bench is reserved for genuinely novel deals.

That's the pitch to the CRO: same revenue coverage, ~⅓ the headcount, *and* faster cycle times because the tooling is shared.

## What the architect tier actually ships (steal this list)

The first 90-day output of an SE-architect role, in priority order:

1. **A discovery agent** that ingests an account's public footprint + CRM history and outputs a customized discovery deck the AE can run
2. **A demo-environment generator** the AE triggers themselves — tailored data, branding, customer-specific scenarios
3. **A proposal/SOW assembler** wired to product pricing, legal templates, and previous deal patterns
4. **A post-sale handoff bot** that hands a clean implementation packet to CS, including everything promised in the sales cycle (this is where most deals leak today)
5. **A product-feedback aggregator** — the SE's view of "what's blocking deals?" piped into product/eng with structured tags

> [!note] The maintenance objection, and why it's weaker now
> The standard pushback: if solutions owns all these tools, doesn't the team just become a bottleneck? One person understands how something works, everyone else depends on them, and a growing share of their time goes to upkeep instead of new work.
> That argument gets a lot weaker in the AI era. Writing the code, or asking an AI to explain how an existing system works, is close to trivial now. You don't need a heavyweight development lifecycle for the rest of the team to understand and contribute to these tools. What you do need is to settle a couple of guiding principles up front — where these tools live (a dedicated cloud environment vs. a hosted platform for small internal apps) and who can touch them. Decide that early and the bottleneck risk mostly goes away.

## Set the charter broad, on purpose

Two things make the gray-area ownership actually stick: an intentionally broad charter, and a self-image the team can rally around.

The charter statement I keep coming back to: *our primary objective is to help sales close more business and help customer success retain it.* Any customer-facing request can be traced back to that. Some leaders push back that it reads too broad. But narrowing it any other way commits the same mistake every other team makes: an "optimized," indefensible boundary. When a customer's problem lands right on the line, you'll cave every time, not "make an exception this once." A real exception looks like upgrading a fast-growing mid-market account into enterprise support because the signals justify it. A problem that isn't totally support, isn't totally a new sale, and is beyond what engineering has context to solve on its own isn't an exception. It's just what solutions gets tapped for.

Then ask the team what it wants to be known as. The answers converge fast: helpful, supportive, solution-oriented. One team I worked with put it as "we promise not to complain too often," which is really the same idea from a different angle — we know we're going to get handed things nobody else wants, and we're going to step up without making a production of it, because the mandate is to help close business and retain customers, and there's no shortage of ways to serve that mandate.

Worth contrasting this with GTM engineering, since it's the other team people expect to fill this role. GTM engineering is too far removed from the day-to-day of the business to make this claim. It's well-suited to own lead capture and routing, quota tracking, data automations between systems, tool purchasing, and vendor management. But ask GTM engineering to map the customer experience and you get a pile of Salesforce stages full of assumptions and gray area someone else still has to manage, because the team is operating one level removed from where the actual friction happens. Solutions teams build with an operational mindset — good enough, ship it, iterate — where GTM engineering tends to build with a production mindset. That difference is a feature here, not a shortcut.

> [!tip] Steal the charter, not the org chart
> Two sentences, said out loud to the team and to leadership:
> - **Mandate:** "Our primary objective is to help sales close more business and help customer success retain it. Any customer-facing request can be tied back to that."
> - **Identity:** ask the team what adjectives it wants to be known for. If the answer is some version of "helpful, solution-oriented, doesn't complain," you're aligned. The mandate gives the team scope; the identity gives it the posture to actually use that scope.

## Map the customer journey, then draw a box around solutions

A second tactical move worth doing early: map the customer journey in terms of capabilities customers expect from a human, not product features. Customers expect someone to talk to about the contract. Someone for growth and expansion conversations. Someone to reach out to with support issues. That's why those teams exist in the first place. Within each of those relationships there are patterns to the types of questions that come up, and patterns to where the meaningful handoffs actually happen.

The common objection here is "we don't know our journey well enough yet to map it." That doesn't hold up. You have a customer journey today, whether or not it's written down. The goal isn't exhaustive coverage — it's identifying what's true often enough to be useful. If a pattern holds for half your customers, that's enough to work from.

For each type of request, name a primary owner and a secondary backup. Support tickets: support primary, engineering backup for anything that's actually an incident or too technical for support to unblock on its own. Whether something is a new sale, a new use case, or an existing use case that needs more attention: sales or CS, depending. And underneath most of those primary owners, the backup is solutions — because solutions is the team with the technical range to actually judge whether a problem belongs to them or somewhere else. A support ticket about a complex migration is the clearest example: understanding the current state, the end state, what isn't working, and what the customer actually wants is more than the support charter was built to handle, and more than engineering has the context to take on cold.

Once that map exists, draw one more box over the whole thing: anything unclear goes to solutions. That doesn't mean solutions accumulates everything forever. If solutions looks at a request and says "this doesn't need my skills, it belongs with support" or "this is really a sales conversation," and hands it back, that's the system working, not a failure. No other team has the technical breadth to make that judgment call.

> [!tip] Map capabilities, not features
> Ask what customers expect to be able to do with a human, not with the product: talk about the contract, talk about growth, get support. For each capability, name a primary owner and a backup. You don't need every case mapped — patterns that hold half the time are enough to start from. Then draw one more box over the whole map: unclear → solutions.

## Don't run your team like an API

There's a popular framing worth pushing back on here: treat your team like an API. Requests come in with a defined shape, work happens, a response comes out. It's appealing because it looks clean. It also assumes every endpoint and every parameter is known up front, and that's not true, especially early on. The most-used endpoint ends up being the generic one — a block of unstructured text that says, in effect, "help, I'm stuck."

Every team that builds an intake form for this eventually finds the same thing: the biggest bucket on the form is "other." That's not a data quality problem. It's a signal that someone got handed a problem they don't know how to solve and want backup on it. That's fine. It's the job.

The real protection isn't a tighter task definition — you can't define your way out of the unknown, and trying just wastes time pigeonholing requests into categories they don't fit. The actual protection is setting the expectation that the team will push back on a request when it believes another team is genuinely equipped to own it instead. That's the muscle worth building, not a sharper API contract.

## Where this leaves SE

Put the pieces together. AI collapses the "SE as demo machine" job, because AEs and their own tools can do that without help. What's left is a smaller team with more leverage, and its real qualification isn't a fixed bucket of tasks — it's the willingness to own the parts of the business nobody else is positioned to own, plus the tools to make owning that gray area sustainable instead of exhausting. The org chart gets leaner. The mandate gets broader, on purpose. AI doesn't just promote SE into an architect role. It's what finally makes owning the gray area a career path instead of a fast track to burning out your best people.

## What to flesh out in future recordings

- A specific example of an SE-architect tool I'd ship first and why
- The career-path question: how does an IC SE become an architect? What skills are missing today?
- The SWAT bench framing — when does it actually get used? Who staffs it?
- The transition: how do existing SE orgs shrink without nuking morale? Re-skill or replace? [?]
- The guiding principles for where these internal tools should actually live — dedicated cloud environment vs. a hosted platform for small apps — and who decides
- How do you get leadership buy-in when the charter "feels too broad"? What's the actual conversation, beyond just asserting it?
- Counter-argument: is the "speaks to every silo" claim still true if Slack/Linear/HubSpot agents close those gaps directly? When does SE become redundant *for real*? [?]
- Companion piece: see `fde-is-consulting` for the adjacent role evolution
- Companion piece: see `ai-native-se-stack` — the stack is what these new SEs build
