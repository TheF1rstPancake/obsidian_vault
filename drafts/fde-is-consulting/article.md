---
title: "Forward deployed engineering and the Lego kit"
slug: fde-is-consulting
status: shaping
target: substack
created: 2026-05-07
updated: 2026-06-05
tags: [careers, fde, consulting, implementation]
---

# Forward deployed engineering and the Lego kit

"Forward Deployed Engineer" is doing three different jobs as a title, and most companies posting for the role are conflating them.

1. *Recruiting brand.* "FDE" reads sexier on LinkedIn than "Implementation Engineer" or "Solutions Consultant," so it's the title companies use to attract a specific kind of person — technically savvy, customer-facing, real engineering chops or wants them. That cohort is genuinely rare.
2. *Customer credibility signal.* "Engineer" in the title shifts how the customer treats the person. Math and science backgrounds carry weight that other titles don't, and a Forward Deployed Engineer walks into the room with more authority than a Customer Success Manager would. SE for the sales conversation, FDE for the implementation conversation. Same counterbalancing move.
3. *Something structurally new.* The work is materially different from what implementation, professional services, and onboarding teams have done for decades.

The first two are honest. They're the same moves any SaaS company has used to title customer-facing technical roles, applied to a slightly different stage of the customer lifecycle. Nothing to argue with.

The third claim is where it gets messy — because if FDE really is structurally new, the way it's being packaged in 2026 job postings is going to bite both the companies hiring for it and the people taking the role.

## What's actually new about FDE

Two things are different about how FDE is being packaged today vs how implementation engineering was packaged ten years ago.

**FDE reports into Engineering, not Sales.** Implementation engineers, solutions consultants, and professional services teams have historically rolled up through the CRO or a customer-success leader. Most FDE postings I've read in the last year report into the CTO or VP of Engineering. The reporting line moved.

**FDE is expected to contribute production code.** Not just custom integration code that lives in the customer's environment — actual changes pushed back into the company's main codebase. Often paired with the expectation that FDEs will build customer-specific customizations *inside* the platform itself, not on top of it.

The first change is mostly cosmetic on its own. The second is the one I want to look at, because paired with the first, it stops being a small re-org choice and turns into a roles-and-responsibilities problem.

## The roles and responsibilities problem

Implementation has always been a *supplement* to product. Engineering ships the platform. Product decides what the platform is supposed to do. Implementation helps customers get to value inside what the platform already does — and tells engineering and product where the platform needs to go next.

The current FDE packaging inverts that. When FDE is responsible for production code and per-customer customization, FDE isn't supplementing product — it's absorbing work that product is supposed to be doing. The product team can ship a feature that's 60% complete and the FDE team will figure out the remaining 40% on a customer-by-customer basis. The implicit message: *engineering's job is to ship, making it usable is somebody else's problem*.

That's a comfortable arrangement for engineering and product. It's a brutal arrangement for FDE. And it's the wrong arrangement for the company, because the bar for "did we build this right" quietly drops to "the FDE team can compensate for it on the customer call."

## Who pays the bill

Two specific costs land on the FDE.

**Nobody describes the Lego kit.** When the job description says "be scrappy, write code, work with customers, contribute back to the platform," nobody is saying what platform primitives the FDE is supposed to be composing. What's stable. What's evolving. Where the documented escape hatches are. The implicit ask is: *figure out what the platform should have done, write it, then maintain it, then somehow also ship a customer integration on top of it.* That's not implementation work. That's implementation work plus product work plus platform work, and the FDE is being asked to do all three with no clear authority over any of them.

**The FDE isn't a full-time platform engineer.** The FDEs I've worked with weren't aspiring to be full-time back-end systems engineers. If that's what they wanted, that's what they'd be. They're in the role because they like interfacing with customers and they like the puzzle of combining what exists into something a specific customer can use. That's a legitimate craft — and it's the craft the role should actually be hiring for. "Be scrappy and write production code in our main repo" isn't that craft. It's a different job entirely, dressed in implementation clothes.

The pattern compounds. The FDE works around platform gaps for one customer. The next customer hits the same gap. The FDE works around it again because there's no canonical solution yet. The company doesn't notice the gap because the FDE has been smoothing it over for a year. By the time it surfaces, there are six bespoke versions of the workaround scattered across customer codebases and nobody knows which one is canonical.

## What good FDE looks like

The Palantir model is the one people point to, and it actually does work — but most companies citing it are reading it wrong.

Palantir's core engineering team builds the platform. The forward deployed engineers go into the customer environment and combine Palantir's building blocks into a working solution for that customer. The custom code lives *on top of* the platform, not *inside* it. When the FDE team starts seeing the same pattern across customers, that pattern becomes a candidate for first-class inclusion in the platform — and the decision about whether to absorb it is made by core engineering, not by the FDE.

That model only works if core engineering takes seriously its job of providing the Lego kit. If the platform doesn't have building blocks, the FDE has nothing to combine. Every engagement becomes a one-off. The implementation team can't pattern-match because there's no shared vocabulary to pattern-match in. And the FDE function reinvents professional services with extra steps.

### The Airtable scripting example

A version of this played out at Airtable when scripting shipped. The platform had APIs, but APIs required customers to host code somewhere — and most of our customers couldn't or wouldn't. Scripting changed that: code that lived inside the Airtable base, triggered by a button or an automation. The customer didn't have to host anything.

A team of about three of us became the script-writing arm. Every week, customers came in with use cases the standard product couldn't quite cover. We'd write the script, deploy it for that customer, move on. Everyone — leadership, engineering, sometimes us — worried that we were building unsustainable custom solutions at customer-by-customer scale. That we'd be crushed under maintenance.

We weren't. Because there were patterns.

Roughly 70% of script requests turned out to be project-and-task management — because Airtable handles many-to-one relationships in ways that surprise customers. Delete a project and the tasks don't cascade-delete. Change a parent field and the children don't propagate. Every customer was reinventing the same handful of scripts to paper over this.

So we did three things:

1. **Wrote a small set of canonical scripts** for the patterns we saw repeatedly.
2. **Published them** in the help center and the script library so customers and CS could grab them directly.
3. **Trained CS and implementation** on how to deploy and modify them, so the work didn't have to route through our team.

What we didn't do: go write custom code in the production codebase. We didn't ship Airtable features ourselves. What we did do was *expand the set of customer use cases the company could say yes to*, using building blocks the engineering team had given us. When we noticed patterns, we surfaced them to engineering and product as candidates for first-class platform features. Some got absorbed. Some stayed as scripts. That decision belonged to engineering and product, not to us.

That's what good implementation engineering looks like, and it's what good FDE should look like. Engineering owns the platform. Implementation owns combining the platform into customer outcomes. Patterns travel upward when they emerge. Custom code lives outside the platform until the platform decides to absorb it.

## What an honest FDE job description would look like

If you're hiring for an FDE role, three questions decide whether the role you're describing is real implementation engineering or implementation engineering plus an unspecified amount of platform work the rest of the company didn't want to do.

1. **What's the Lego kit?** What platform primitives can the FDE actually compose? What's stable? What's evolving? Where are the documented escape hatches, and where is the FDE expected to invent them?
2. **Where does the FDE's code live?** In the customer's environment? In a sandbox or extension layer? In the production codebase? The answer changes the role's whole shape — and the amount of platform-engineering judgment the FDE has to bring.
3. **Who decides what gets absorbed into the platform?** When the FDE team sees a pattern across customers, who decides whether it becomes a first-class feature? FDE alone? Product? Engineering? A standing review? The answer determines whether FDE is a supplement to product or a quiet replacement for it.

If the job description can answer those three questions clearly, the role is probably real implementation engineering wearing a "forward deployed" hat. If it can't — if it just says *be scrappy, work with customers, contribute code, figure it out* — what's being advertised is the *appearance* of an engineering role on top of an implementation role with no platform support behind either.

Engineering and product teams should be relentlessly focused on making it easier for customers to onboard themselves. Implementation engineering supplements that focus. It handles the customers and edges the platform doesn't reach yet, and it tells engineering where the platform needs to go next. Forward deployed engineering, packaged with that division of labor intact, is the same job under a sexier title. Packaged without it, it's a way for engineering to outsource the problem of making the product usable.

The engineering team needs to own the Lego kit. The FDE team is there to combine the blocks.
