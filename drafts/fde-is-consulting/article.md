---
title: "Forward deployed engineering and the Lego kit"
slug: fde-is-consulting
status: shaping
target: substack
created: 2026-05-07
updated: 2026-06-07
tags: [careers, fde, consulting, implementation]
---

# Forward deployed engineering and the Lego kit

Every software company eventually runs into the same question. When the platform doesn't quite fit what a customer is trying to do, who is responsible for closing the gap? Engineering, by extending the platform? Implementation, by working around what the platform doesn't yet do? Some third team, writing customer-specific code that lives somewhere in between?

Forward Deployed Engineering is, increasingly, the answer companies are reaching for. The pitch is structural, not cosmetic. The promise: instead of letting implementation teams accumulate workarounds in customer codebases — six bespoke versions of the same patch scattered across customer instances, nobody sure which one is canonical, the eventual maintenance nightmare — embed engineers *with* customers, have them write code that flows back into the core product, and use that loop to keep the platform on pace with what customers actually need.

That's a real promise. It's not branding. It's not a re-titled implementation team. The bet is that the people doing the customizing should also be the people shipping the platform, because the loop between "what customers need" and "what the platform does" is too important to mediate through a separate team's ticket queue.

The bet is interesting. The execution is where I keep getting stuck.

## Three questions FDE has to answer

For "embed engineers with customers and let patterns flow back to the platform" to actually produce a coherent product instead of a Frankensteined one, three things have to be true:

1. **Someone decides what gets generalized.** When the FDE team sees the same workaround across three customers, who decides whether that workaround becomes a first-class platform feature? Is it FDE? Product? Engineering? A standing review?
2. **Someone owns maintaining the generalized version.** Once a pattern is absorbed into the platform, who is responsible for keeping it working — performance, backward compatibility, deprecation paths? Is it the FDE who wrote the original version? Core engineering? Whoever's on call this week?
3. **Someone prevents the platform from accumulating customer-shaped weirdness.** When a customer-specific feature gets absorbed into the core, how do you stop the platform from collecting options that exist because one important customer needed them, edge cases that only make sense if you know the original engagement, settings that contradict other settings?

These aren't gotcha questions. They're the questions that have to have answers for the FDE bet to pay off. The promise of "patterns flow back to the platform" doesn't survive contact with reality if nobody owns the decisions about what flows, who maintains the result, and what gets refused.

Every FDE job posting I've read in the last year is silent on at least one of these. Most are silent on all three. The silence isn't an editorial choice — it's a real gap. The companies hiring these roles haven't decided yet, and the FDE who takes the job inherits the absence of those decisions.

## The roles and responsibilities problem

There's a traditional division of labor that's worked for a long time. Engineering owns the platform — what it does, how it scales, what shape it takes. Product owns the strategy — what the platform is supposed to do next, for whom, in what order. Implementation supplements both — it helps customers get to value inside what the platform already does, and it tells engineering and product where the platform needs to go next.

In that division, the three questions above have answers built into the org chart. Generalization decisions go to product, sometimes with engineering input. Maintenance goes to engineering. Frankenstein-prevention is the job of whoever owns the platform's long-term shape, which is also engineering, because they're the ones who have to live with the code.

FDE as currently packaged folds all three onto one team. The FDE writes the workaround. The FDE notices the pattern. The FDE writes the production code that absorbs it. The FDE — or someone, it's never clear — has to maintain it later. And the FDE is the one supposed to push back when a customer asks for the seventh thing that doesn't fit the platform's shape, except they're embedded in the customer and their job is to make the customer succeed. The pushback rarely happens.

That's not implementation work. It's not product work either. It's implementation plus product plus platform stewardship, on one team, with no clear authority over any of them.

(Worth noting: "Forward Deployed Engineer" as a title is doing three different jobs at once. It's a recruiting brand — the cohort of people who are technically savvy *and* customer-facing is small, and "FDE" reads sexier on LinkedIn than "Implementation Engineer." It's a customer credibility signal — engineers carry more weight in the room than CSMs. And it's claiming to point at structurally new work. The first two are honest. The third is what this article is about.)

## Who pays the bill

Two specific costs land on the FDE.

**Nobody describes the Lego kit.** The job descriptions say *be scrappy, write code, work with customers, contribute back to the platform.* They don't say what platform primitives the FDE is supposed to be composing. What's stable. What's evolving. Where the documented escape hatches are. The implicit ask is: *figure out what the platform should have done, write it, then maintain it, then somehow also ship a customer integration on top of it.* The FDE is being asked to do platform work without the authority that comes with owning the platform.

**The FDE isn't a full-time platform engineer.** The FDEs I've worked with weren't aspiring to be full-time back-end systems engineers. If that's what they wanted, that's what they'd be. They're in the role because they like interfacing with customers and they like the puzzle of combining what exists into something a specific customer can use. That's a legitimate craft — and it's the craft the role *should* be hiring for. "Be scrappy and write production code in our main repo" isn't that craft.

So the FDE absorbs the gap. They write the workaround for customer one. They write it again for customer two, slightly differently. They notice the pattern by customer three. They surface it to engineering. Engineering says *interesting, we'll consider it for next quarter*. The FDE writes it again for customer four.

Eventually one of two things happens. Either some version of the workaround gets absorbed into the platform — possibly the wrong version, possibly with no consistent ownership for maintenance. Or it doesn't get absorbed at all, and the FDE quietly maintains six variations of it across customer codebases until they burn out or quit.

That outcome is exactly what the FDE model was supposed to prevent. It's what the model produces instead when the three structural questions don't have answers.

## What good FDE looks like, structurally

The Palantir example is the one people point to, and it actually does work — but most companies citing it are reading it wrong.

Palantir's core engineering team builds the platform. The forward deployed engineers go into the customer environment and combine Palantir's building blocks into a working solution for that customer. The custom code lives *on top of* the platform, not *inside* it. When the FDE team sees the same pattern across customers, that pattern becomes a candidate for first-class inclusion in the platform — and the decision about whether to absorb it is made by core engineering, not by the FDE.

The three structural questions have answers in that model. Generalization decisions belong to core engineering. Maintenance belongs to core engineering. Frankenstein-prevention belongs to core engineering, who can say no to absorbing a pattern that would muddy the platform without paying for the FDE's customer relationship.

That model only works if core engineering takes its job seriously. If the platform doesn't have building blocks, the FDE has nothing to combine. If core engineering won't make absorption decisions, patterns pile up in customer code forever. If nobody owns Frankenstein-prevention, every customer slowly ends up with a slightly different version of the product.

### The Airtable scripting example

A version of this played out at Airtable when scripting shipped. The platform had APIs, but APIs required customers to host code somewhere — and most of our customers couldn't or wouldn't. Scripting changed that: code that lived inside the Airtable base, triggered by a button or an automation. The customer didn't have to host anything.

A team of about three of us became the script-writing arm. Every week, customers came in with use cases the standard product couldn't quite cover. We'd write the script, deploy it for that customer, move on. Everyone — leadership, engineering, sometimes us — worried that we were building unsustainable custom solutions at customer-by-customer scale. That we'd be crushed under maintenance.

We weren't. Because there were patterns.

Roughly 70% of script requests turned out to be project-and-task management — because Airtable handled many-to-one relationships in ways that surprised customers. Delete a project and the tasks didn't cascade-delete. Change a parent field and the children didn't propagate. Every customer was reinventing the same handful of scripts to paper over this.

So we did three things:

1. **Wrote a small set of canonical scripts** for the patterns we saw repeatedly.
2. **Published them** in the help center and the script library so customers and CS could grab them directly.
3. **Trained CS and implementation** on how to deploy and modify them, so the work didn't have to route through our team.

What we didn't do: write custom code in the production codebase. We didn't ship Airtable features ourselves. What we did do was *expand the set of customer use cases the company could say yes to*, using building blocks the engineering team had given us. When we noticed patterns, we surfaced them to engineering and product as candidates for first-class platform features. Some got absorbed. Some stayed as scripts. That decision belonged to engineering and product, not to us.

The three structural questions had answers. Who decides what gets generalized: engineering and product, with our input. Who maintains it: engineering, once absorbed. Frankenstein-prevention: built into the absorption decision — engineering could decline to absorb a pattern, and we'd keep it as a script.

That's what good implementation engineering looks like, structurally. The questions have answers. The system functions.

But there's a deeper problem that good structure alone doesn't fix.

## Workarounds are pressure relief

There's a version of the FDE pitch I haven't engaged with yet, and it's the strongest one. It goes: why make core engineering rebuild what the FDE team already shipped at the customer site? The people closest to the problem are empowered to solve it directly. The platform evolves faster because the loop between "a customer needs X" and "X exists" is shorter.

That argument is intuitive, and on its own terms it isn't wrong. What it misses is that "building any given feature once, as fast as possible" isn't actually the long-term goal. The long-term goal is for the platform to evolve toward what customers actually need. And platforms evolve by feeling the pain of a gap until somebody owns closing it.

Workarounds — including high-quality FDE workarounds — are pressure relief. They route around the missing feature instead of forcing the org to confront it. The better the workaround, the less pressure on the platform to absorb the underlying need.

That cuts in the opposite direction from what the FDE pitch claims. The pitch is "FDE makes the platform faster." The structural reality is closer to "FDE makes the platform slower over time, because platforms only move when they're forced to, and a competent FDE team is exceptionally good at preventing the forcing."

The Airtable scripting team is, in retrospect, a case study in this. The ~70% of script requests that clustered around project-and-task management — the many-to-one relationship gap — never became a first-class platform feature in the time I was there. The reason isn't that engineering didn't notice. The reason is that the workaround was good enough, deployed widely enough, customizable enough, that the urgency dispersed. CS knew how to deploy it. Implementation knew how to customize it. Customers were satisfied enough. The pain was absorbed, smoothed over, made manageable.

If our team had been bad at the workaround, the pain would have stayed sharp and the platform would have had to move. If our team had been adequate but slow, the volume would have built up the case for first-classing it. We were good and fast, and the pressure dispersed. Our competence is, structurally, what kept the platform from evolving in that specific way.

Renaming our team FDE wouldn't have changed that. The pitch is that FDEs would be more motivated to push the first-party solution back into the platform. Maybe. But the structural pressure relief — the fact that we had a workable, deployable, customizable solution that absorbed the pain — would still have been there, working against the platform fix every time. The team writing the workarounds is not the team that needs the pain to be sharp. The team that needs the pain to be sharp is whoever owns the product roadmap.

The root cause of what an org needs to build internally is its product feedback loop — what reaches the people making roadmap decisions, in what form, with what evidence behind it. Renaming the implementation team doesn't fix the feedback loop. Hiring FDEs into engineering doesn't fix it. "Just contribute the code back to the platform" is the symptom you want, not a solution to what's causing the symptom to be missing.

What actually fixes a broken product feedback loop is an explicit accounting of what workarounds are absorbing — pattern by pattern, with customer volume and long-term cost attached — and a discipline of deciding whether the platform should take each one on or stay out of it deliberately. That's product work. It can't be delegated to the team that's elbow-deep in the workaround, because the team writing the workaround has no incentive to advocate for their own work being replaced.

## The closing

The promise of FDE relies on a structure the FDE can't build for themselves. Generalization decisions need a clear owner. Maintenance needs a clear owner. Frankenstein-prevention needs a clear owner. And — the one most companies forget — someone has to be watching the workarounds for what the platform should be learning, because the FDE team is too close to the customer to see that picture and the platform team is too far from the customer to notice on their own.

If those owners exist and the FDE's job is to combine platform primitives at the customer site and surface patterns upward, the model works. The work is real, the role is honest, the customer wins, the platform evolves.

If they don't, two things happen at once. The FDE becomes the bag everyone holds — making generalization decisions because nobody else will, maintaining the absorbed code because nobody else will, watching the platform turn Frankenstein with no authority to stop it. And the platform itself stops evolving in proportion to how good the FDE team gets at preventing the evolution from being necessary.

Engineering owns the Lego kit. Implementation supplements. Product watches the workarounds for what the platform should learn next, and is willing to act on what it sees. That triangle is what an FDE function quietly relies on, and what gets quietly broken when "FDE" becomes the answer to "why isn't our platform keeping up?"

The engineering team needs to own the Lego kit. The FDE team is there to combine the blocks. Someone has to be paying attention to which combinations are doing work the platform should be doing instead. Everything else follows from that.
