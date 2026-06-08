---
title: "Forward deployed engineering and the Lego kit"
slug: fde-is-consulting
status: shaping
target: substack
created: 2026-05-07
updated: 2026-06-08
tags: [careers, fde, consulting, implementation]
---

# Forward deployed engineering and the Lego kit

Every software company eventually runs into the same question. When the platform doesn't quite fit what a customer is trying to do, who is responsible for closing the gap? Engineering, by extending the platform? Implementation, by working around what the platform doesn't yet do? Some third team, writing customer-specific code that lives somewhere in between?

Forward Deployed Engineering is, [increasingly](https://jobsbyculture.com/blog/forward-deployed-engineer-boom-2026), the answer companies are reaching for. The pitch is structural, not cosmetic. The promise: instead of letting implementation teams accumulate workarounds in customer codebases — six bespoke versions of the same patch scattered across customer instances, nobody sure which one is canonical, the eventual maintenance nightmare — embed engineers *with* customers, have them write code that flows back into the core product, and use that loop to keep the platform on pace with what customers actually need.

That's a real promise — but it doesn't dissolve the implementation problem, it just renames it. Research, prioritization, the discipline to ship fast without making a mess: those are still real skills with real overhead, and they still need real scaffolding around the role to function. The pitch that you can hand an engineer with people skills to a customer and the feedback loop will close itself is just [if](https://www.itamarnovick.com/startup-anti-pattern-4-if-you-build-it-they-will-come/) [you](https://www.entrepreneur.com/leadership/why-the-motto-if-you-build-it-they-will-come-is-bs/227850) [build](https://samuelmullen.com/articles/startup-fallacies-if-you-build-it-they-will-come) [it](https://www.forentrepreneurs.com/why-startups-fail/), [they](https://www.productgrowth.blog/p/the-field-of-dreams-fallacy-why-building-a-great-product-isnt-enough) [will](https://mgvcapital.substack.com/p/distribution-the-real-reason-startups) [come](https://news.quantosei.com/2026/02/23/the-saas-fallacy/) in a new wrapper. That isn't how SaaS has ever worked.

The bet is interesting. The execution is where I keep getting stuck.

## Three questions FDE has to answer

People cite Palantir as the model constantly. But [what Palantir actually built](https://blog.palantir.com/a-day-in-the-life-of-a-palantir-forward-deployed-software-engineer-45ef2de257b1) wasn't "send an engineer to the customer and have them ship production code." It was a structure where three specific questions had clear answers. For the FDE bet to produce a coherent product instead of a Frankensteined one, those three things have to be true:

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

The [Palantir example](https://medium.com/activated-thinker/a-comprehensive-analysis-of-palantirs-forward-deployed-engineering-model-4502a036b5e4) is the one people point to, and it actually does work — but [most companies citing it are reading it wrong](https://review.firstround.com/so-you-want-to-hire-a-forward-deployed-engineer/).

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

### The same pattern at Recurrency

At Recurrency we had a feature called "rules" — an engine for injecting custom SQL queries into the product that changed its behavior customer by customer. Same structural shape as Airtable scripting: core engineering built the primitive, and the implementation team composed it into customer-specific solutions that lived on top of it.

In both cases, core engineering was bad at one specific thing — knowing what customers actually wanted to use the primitive for, and building templates for it. They struggled because they thought in terms of highly generalized solutions: one template that handles every case. The implementation team looked at the same problem and thought differently: *this version covers 60% of my customers, and that's fine; here's a variant for the next 20%, and another for the last 20%.*

Engineering looks at three variants of the same script and asks why there are three versions of one thing. Implementation looks at three variants and sees three playbooks that, together, cover the whole problem space. Both are right from where they sit. The difference is depth. The bar implementation has to clear is *deployable for this cluster of customers.* The bar engineering has to clear is *configurable by any user, globally, forever* — and designed so the customization is done by the user, not by your implementation team standing over their shoulder. Those are different jobs, and the second one is much more expensive.

That's the whole reason the division of labor works — and the whole reason "just have the FDE write the production version" undercounts the cost. The scrappy version encodes assumptions specific to one customer: their data shape, the urgency of the moment, the parts you didn't bother to generalize because you didn't have to. Promoting it to a first-party feature means redoing it for a much wider set of users. You can object that LLMs are collapsing the distance between "scrappy thing" and "generalizable solution," and there's something to that — they do give implementation more room to contribute real code. But code review still takes time, and the design work of globalizing a customer-shaped solution doesn't disappear because the first draft was faster to write.

But there's a deeper problem that good structure alone doesn't fix.

## The duct tape isn't the product

There's a version of the FDE pitch I haven't engaged with yet, and it's the strongest one. It goes: implementation teams already write workarounds for every customer. The workarounds get reused, they accumulate in customer codebases, they're maintained inconsistently. FDE fixes that. The same person doing the workaround can write it in production-quality code, contribute it back to the platform, and now you have one canonical version maintained by the team that built the rest of the platform. Faster, cleaner, more sustainable.

That argument concedes too much by accepting its own framing. Implementation's job *is* to build fast — to unblock customers, to keep revenue from stalling when the platform doesn't quite fit. Nobody apologizes for that. The reason implementation has to exist at all is that product and engineering missed something during the original build, or the market shifted and customers are solving problems nobody anticipated yet. Both are normal. Both are fine.

The question is what happens *after* the fast build. The implementation team duct-tapes seven pieces together, the customer is unblocked, revenue is preserved. Now what?

In the model that works, the duct tape is *evidence*. It proves there's a real customer need the platform doesn't address. The duct-taped solution gets reused for the next two or three customers who hit the same gap — because rebuilding from scratch every time would burn the team for no reason — but the expectation, always, is that a fully engineered version is coming from product and engineering, informed by what the duct tape revealed about what customers actually need.

The FDE pitch quietly proposes a different model: if the duct tape is written by an engineer in production-quality code, it can *become* the engineered version directly. Skip the rebuild. Ship the duct tape.

That's where the model breaks. The duct tape was shaped by the engagement that produced it — the urgency of unblocking, the specific shape that fit that customer's data, the assumptions baked into the workaround. Promoting it into the platform skips the design work that product owes the rest of the customer base (*is this the right shape for everyone?*) and the work that engineering owes the platform (*is this the right shape long-term?*). The duct tape is evidence of a real need. It is not, by virtue of being written in production-grade code, the right answer for the platform.

FDEs are skunk works. They're a SWAT team — fast, scrappy, dispatched to solve problems the platform can't yet, equipped with whatever tools the engineering team has given them to work with. That role is real and worth hiring for. What it isn't is a substitute for the design discipline that product and engineering owe the platform when deciding what to absorb.

And — back to the structural point — workarounds are pressure relief. They route around the missing feature instead of forcing the org to confront it. The better the workaround, the less pressure on the platform to absorb the underlying need.

The Airtable scripting team is, in retrospect, a case study in this. The ~70% of script requests that clustered around project-and-task management — the many-to-one relationship gap — never became a first-class platform feature in the time I was there. The reason isn't that engineering didn't notice. The reason is that the workaround was good enough, deployed widely enough, customizable enough, that the urgency dispersed. CS knew how to deploy it. Implementation knew how to customize it. Customers were satisfied enough. The pain was absorbed, smoothed over, made manageable.

And to be clear — to a real degree, this was success. The scripting team kept customers happy. Engineering got to work on greenfield features instead of going back to patch a relational-model gap they'd shipped years earlier. Looking at it as a resource allocation problem, the calculus made sense. It used to really piss me off that they wouldn't prioritize the underlying fix. Looking back, I understand why they didn't.

What I couldn't see — what nobody could see — is the other side of the ledger. How many deals didn't close because a prospect evaluated Airtable, saw the relational limitations, and went with a competitor? How many customers didn't expand because the workaround was workable but not delightful? How many quietly churned and the cause was never attributed to this specific gap? Unknown. Unmeasured. Probably unmeasurable.

That's the actual problem. Not that engineering made the wrong call — they made the rational call given the information they had. The feedback loop captured what was visible: support tickets, customer complaints, the volume of script requests our team handled. It missed the invisible side: prospects who walked, expansions that never happened, the slow accumulation of being known as "the spreadsheet that doesn't quite do projects."

If our team had been bad at the workaround, the pain would have stayed sharp and the platform would have had to move. If our team had been adequate but slow, the volume would have built up the case for first-classing it. We were good and fast, and the pressure dispersed. Our competence is, structurally, what kept the platform from evolving in that specific way.

Renaming our team FDE wouldn't have changed that. The pitch is that FDEs would be more motivated to push the first-party solution back into the platform. Maybe. But the structural pressure relief — the fact that we had a workable, deployable, customizable solution that absorbed the pain — would still have been there, working against the platform fix every time. The team writing the workarounds is not the team that needs the pain to be sharp. The team that needs the pain to be sharp is whoever owns the product roadmap.

The root cause of what an org needs to build internally is its product feedback loop — what reaches the people making roadmap decisions, in what form, with what evidence behind it. Renaming the implementation team doesn't fix the feedback loop. Hiring FDEs into engineering doesn't fix it. "Just contribute the code back to the platform" is the symptom you want, not a solution to what's causing the symptom to be missing.

What actually fixes a broken product feedback loop is an explicit accounting of what workarounds are absorbing — pattern by pattern, with customer volume and long-term cost attached — and a discipline of deciding whether the platform should take each one on or stay out of it deliberately. That's product work. It can't be delegated to the team that's elbow-deep in the workaround, because the team writing the workaround has no incentive to advocate for their own work being replaced.

## What problem are you actually solving?

Behind everything above is a question most companies don't answer before they post their first FDE role: *what core problem are you actually trying to solve?*

If you're early and the honest answer is *"I'm willing to make one-offs to get customers in the door and figure out scale later,"* the right shape is straightforward. A slice of the engineering team reserves bandwidth for urgent customer requests and writes whatever code is required to get the deal across the line. They sometimes talk to customers. They sometimes ship production code that addresses a single customer's situation. The feedback loop is approximately zero — the people writing the platform are the people on the customer call. Greenfield slows under the weight of fire drills, and that's a fine tradeoff at this stage. Greenfield isn't the bottleneck yet. Saying yes is.

That model has a known breaking point. If you're successful, you'll have too many customers, too many one-offs in the codebase, too many features to build — and the engineering team can't keep up with all of it while also owning the core product, deciding what to absorb, and maintaining what they've already absorbed. Something has to step in and prioritize.

If you're going to hit that breaking point anyway — and the pitch implicit in raising any kind of round is that you will — you're better off doing the real Palantir model from the start, not a collapsed version of it.

The real Palantir model isn't *"embed engineers inside customer environments and have them contribute production code back."* It's a customer-facing implementation team (call them FDEs; the title is fine) that uses toolkits engineering provides to unblock customers, working closely with core engineering to absorb the worth-absorbing patterns into the product over time. Different team. Different mandate. Different bar to clear.

That setup takes more bodies and more discipline. It covers a wider array of use cases than the engineering-with-customer-time model can cover at scale, because the implementation team takes the brunt of hacky one-offs the engineering team can't or won't, and engineering builds the long-lasting first-party features that the scrappy "just get it done" implementation team won't.

Between them sits an architect tier. Not necessarily a job title — a function. Someone who sees the volume of one-offs the implementation team is absorbing, the patterns underneath, and the cost of *not* first-classing each one. Someone with enough technical depth to argue with engineering and enough customer exposure to know what's actually being asked for. They're the someone the three structural questions earlier in this article kept gesturing at. Their job is prioritization: which patterns get absorbed, in what order, with what scope. They pseudo-product-manage the implementation team, and they're the bridge into engineering's roadmap.

This is what we eventually built at Recurrency. The implementation team got better with AI tools — writing PRDs, building mockups, sketching the diagrams engineering needs to estimate the work. Engineering and customer-facing teams met in the middle through a smaller architect tier that owned the prioritization calls. There was real tension in it: customer-facing was accountable to retention and revenue and pushed hard; engineering was accountable to costs and timelines and pushed back. That tension is a *feature*. It forced go-to-market to think hard about what was actually critical, and it forced engineering to engage explicitly with what they were declining. Engineering retained veto — *that's not a core part of our business model* is a real thing they could say. But veto is different from absence.

What goes wrong is when a company is past the engineering-team-with-customer-time stage but still operating like they're inside it. The customer volume has outpaced what one team can absorb. The answer the org reaches for is *we'll hire FDEs into engineering and have them build the one-offs.* That collapses the two teams into one, removes the architect, and lands the result back in the muddle the rest of this article is about.

A sharper version of the surface warning is already in the literature. Both [First Round Review](https://review.firstround.com/so-you-want-to-hire-a-forward-deployed-engineer/) and [Barry's piece on FDE culture](https://www.barry.ooo/posts/fde-culture) arrive at variations of *"FDE-as-renamed-SE produces a consulting shop, not a product company."* That's right on the symptom. The structural cause is that you tried to skip the architect.

The engineering team needs to own the Lego kit. The implementation team is there to combine the blocks. The architect tier between them owns the prioritization of what the platform should learn next, and answers to both sides for the choice. None of those is the same job, and the muddle most current FDE roles produce is what happens when you pretend they are.
