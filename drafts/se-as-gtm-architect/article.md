---
title: "Own the gray area: the SE claim AI doesn't kill"
slug: se-as-gtm-architect
status: raw
target: ghost
created: 2026-05-08
updated: 2026-07-21
tags: [sales-engineering, ai, gtm, careers]
related: ["ai-native-se-stack", "fde-is-consulting"]
point: >
  SE survives AI by owning the gray area between GTM silos: a broad charter
  plus the willingness to absorb work nobody else is positioned to own.
  Solutions is unusually well-placed to make that claim because it already
  sits at the intersection of product, engineering, and go-to-market, where
  product and support teams don't.
---

# Own the gray area: the SE claim AI doesn't kill

*This piece is adjacent to [The AI-native SE stack](/ai-native-se-stack/), which lays out the org design: the SE brain, the SWAT bench, and the headcount math. This one is narrower: why solutions is the team built to own the gray area between GTM silos in the first place.*

## The claim

If "FDE" is just *help me implement*, a custom agent that knows the customer's stack can replace a lot of it. If "SE" is just demos, AEs can spin up tailored demo environments themselves with the right tools. The part of SE that doesn't collapse is the part nobody talks about: **SEs are the only role that already speaks to every silo** — sales, CS, product, support, ops. AI doesn't kill SE. It raises the value of the team that can own what falls between those buckets. SE, solutions engineering, solutions team: same role, different name tag depending on the org chart, and this piece uses them interchangeably.

## Why the silo-spanning claim is actually true

Most fast-growing teams run into the same problem: there's more work in a day than there's time to do it, and the playbooks don't exist yet for half of what shows up. AI helps with some of that. It can gather signals and synthesize them into a well-packaged thought. What it can't do is the internalization: deciding what that thought means for your org, your team, your roles. That still takes conversation and judgment, and there's no shortcut for the time it takes.

As teams get overwhelmed, they tend to fall into one of two failure modes. First, a team stakes a claim to a bucket of work so it has something exclusive to point to as its value. Second, a team clamps down its own roles and responsibilities so it has a defensible reason to say no — support teams do this often, building ticket tiers and letting some tickets wait longer than others because there's no bandwidth to give everything equal treatment.

Both moves carve out clean boundaries. If every team optimizes for what it owns, the gaps between what they own are where customers get dropped. When a customer's problem doesn't fit any bucket, someone still has to do the work, because the business is going to make sure that customer gets helped regardless of whose job it technically is. What usually happens is a finger-pointing match, then a semi-random assignment, then frustration. Or, the people willing to absorb the work — usually your top performers — do it over and over until they can't anymore.

Own the gray area on purpose instead, if you want to grow your team's scope, and your own. Say, as a team, "we're responsible for the in-between. We don't know what that work entails yet. We're going to document it, learn it, share it back out, and decide later whether it belongs somewhere else."

Solutions teams are unusually well-suited to make that claim. They bring a jack-of-all-trades skill set built to support sales and CS rather than own a P&L of their own, and they're the only team that actually sits at the intersection of product, engineering, and go-to-market. Product and engineering are too deep in the build to see day-to-day GTM friction. Support, sales, and CS are each specialized enough that none of them can see across the seams between the others.

## Set the charter broad, on purpose

The charter statement I keep coming back to: *our primary objective is to help sales close more business and help customer success retain it.* Any customer-facing request can be traced back to that. Some leaders push back that it reads too broad. But narrowing it any other way commits the same mistake every other team makes: an "optimized," indefensible boundary. When a customer's problem lands right on the line, you'll cave every time.

Then ask the team what it wants to be known as. The answers converge fast: helpful, supportive, solution-oriented. One team I worked with put it as "we promise not to complain too often," which is really the same idea from a different angle — we know we're going to get handed things nobody else wants, and we're going to step up without making a production of it.

GTM engineering is well-suited to own lead capture and routing, quota tracking, data automations between systems, tool purchasing, and vendor management. Ask it to map the customer experience and you get a pile of Salesforce stages full of assumptions and gray area someone else still has to manage, because the team is operating one level removed from where the actual friction happens. Solutions teams build with an operational mindset (good enough, ship it, iterate) where GTM engineering tends to build with a production mindset, and it's the operational mindset that can actually sit with a messy, half-defined problem long enough to own it.

> [!tip] Steal the charter, not the org chart
> Two sentences, said out loud to the team and to leadership:
> - **Mandate:** "Our primary objective is to help sales close more business and help customer success retain it. Any customer-facing request can be tied back to that."
> - **Identity:** ask the team what adjectives it wants to be known for. If the answer is some version of "helpful, solution-oriented, doesn't complain," you're aligned. The mandate gives the team scope; the identity gives it the posture to actually use that scope.

## Map capabilities, then draw a box around solutions

A second early move: map the customer journey in terms of capabilities customers expect from a human, not product features. Customers expect someone to talk to about the contract. Someone for growth and expansion. Someone for support issues. Within each of those relationships there are patterns to the types of questions that come up, and patterns to where the meaningful handoffs actually happen.

You have a customer journey today, whether or not it's written down. The goal isn't exhaustive coverage — it's identifying what's true often enough to be useful. If a pattern holds for half your customers, that's enough to work from.

For each type of request, name a primary owner and a secondary backup. Underneath most of those primary owners, the backup is solutions — because solutions is the team with the technical range to actually judge whether a problem belongs to them or somewhere else. Once that map exists, draw one more box over the whole thing: anything unclear goes to solutions. That doesn't mean solutions accumulates everything forever. If solutions looks at a request and says "this belongs with support" or "this is really a sales conversation," and hands it back, that's the system working.

> [!tip] Fill in your own version
> | Capability (what the customer expects to do with a human) | Primary owner | Backup |
> |---|---|---|
> | Talk about the contract | Sales/CS | Solutions |
> | Growth and expansion | CS/Sales | Solutions |
> | Support issues | Support | Solutions |
> | Anything unclear | — | Solutions |
>
> A pattern that holds half the time is enough to start the row.

## Don't run your team like an API

There's a popular framing worth pushing back on: treat your team like an API. Requests come in with a defined shape, work happens, a response comes out. It's appealing because it looks clean. It also assumes every endpoint and every parameter is known up front, and that's not true, especially early on. The most-used endpoint ends up being the generic one — a block of unstructured text that says, in effect, "help, I'm stuck."

In my experience, teams that build an intake form for this eventually find the same thing: the biggest bucket on the form is "other." That's a signal that someone got handed a problem they don't know how to solve and want backup on it. That's fine. It's the job.

You can't define your way out of the unknown, so the real protection is setting the expectation that the team will push back on a request when it believes another team is genuinely equipped to own it instead. That's the muscle worth building.

## Where this leaves SE

AI collapses a lot of the "SE as demo machine" work. What's left is the willingness to own the parts of the business nobody else is positioned to own. The org chart gets leaner either way. The difference is whether solutions claims that gray area on purpose or has it assigned by default, one dropped ticket at a time.
