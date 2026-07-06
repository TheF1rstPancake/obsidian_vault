---
title: "FDE is what happens when implementation engineering gets a better title."
slug: fde-is-consulting
status: published
target: ghost
created: 2026-05-07
updated: 2026-07-06
tags: [careers, fde, consulting, implementation]
point: >
  FDE only works if three jobs (customer-facing implementation, platform
  stewardship, and an architect tier between them) have clear owners; most
  current FDE roles collapse all three onto one team without giving them
  authority over any of them. In the AI-agent era the split doesn't disappear,
  it moves up a layer: core engineering owns the harness (runtime, permissions,
  tools, evals, deployment surface) and the FDE owns deploying it into specific
  customer and task contexts. Which layer you actually own tells you which
  flavor of FDE you are, and which failure mode you're exposed to.
ghost_url: https://thefirstpancake.ghost.io/fde-is-consulting/
---

# FDE is what happens when implementation engineering gets a better title.

Every software company eventually runs into the same question. When the platform doesn't quite fit what a customer is trying to do, who is responsible for closing the gap? Engineering, by extending the platform? Implementation, by working around what the platform doesn't yet do? Some third team, writing customer-specific code that lives somewhere in between?

Let's get one thing straight before we continue. The reason you have to answer these questions is that your customers are not always rational nor capable of implementing your solution. In a perfect world, you'd build something rich, feature-complete, and intuitive enough that your customers could pick it up and deploy it without ever having to talk to a person. You build, money comes in. That is not how any of this works in practice. Customers are messy, products get shipped incomplete, markets evolve faster than you can keep up. So you need *something* to bridge the gap.

Forward Deployed Engineering is, increasingly, the answer companies are reaching for. The promise: instead of letting implementation teams accumulate workarounds in customer codebases (six bespoke versions of the same patch scattered across customer instances, nobody sure which one is canonical, the eventual maintenance nightmare), embed engineers *with* customers, have them write code that flows back into the core product, and use that loop to keep the platform on pace with what customers actually need.

That's a real promise. But the pitch that you can hand an engineer with people skills to a customer and the feedback loop will close itself is just "if you build it, they will come" in a new wrapper. That isn't how SaaS has typically worked.

## Three questions FDE has to answer

People cite [Palantir](https://a16z.com/the-palantirization-of-everything/) as the model constantly. As I understand it, what made their version work was structural rather than the embedding itself: three specific questions had clear answers. The engineer on-site shipping code was the visible part, not the load-bearing one. For the FDE bet to produce a coherent product instead of a Frankensteined one, those three things have to be true:

1. **Someone decides what gets generalized.** When the FDE team sees the same workaround across three customers, who decides whether that workaround becomes a first-class platform feature? Is it FDE? Product? Engineering? A standing review?
2. **Someone owns maintaining the generalized version.** Once a pattern is absorbed into the platform, who is responsible for keeping it working (performance, backward compatibility, deprecation paths)? Is it the FDE who wrote the original version? Core engineering? Whoever's on call this week?
3. **Someone prevents the platform from accumulating customer-shaped weirdness.** When a customer-specific feature gets absorbed into the core, how do you stop the platform from collecting options that exist because one important customer needed them, edge cases that only make sense if you know the original engagement, settings that contradict other settings?

These aren't gotcha questions. The promise of "patterns flow back to the platform" doesn't survive contact with reality if nobody owns the decisions about what flows, who maintains the result, and what gets refused.

Every FDE job posting I've read in the last year is silent on at least one of these. Most are silent on all three, ultimately because these organizations are not sure what problem they are trying to solve. So they've created an FDE and given them none of the scaffolding or systems to be successful. "But Gio, we're a small company and we just need all hands to pitch in!" Fine. But we have to separate the idea that implementation teams are *capable* of productively contributing code from the idea that doing so is their *primary responsibility*.

## The roles and responsibilities problem

There's a traditional division of labor that's worked for a long time. Engineering owns the platform: what it does, how it scales, what shape it takes. Product owns the strategy: what the platform is supposed to do next, for whom, in what order. Implementation supplements both: it helps customers get to value inside what the platform already does, and it tells engineering and product where the platform needs to go next.

In that division, the three questions above have answers built into the org chart. Generalization decisions go to product, sometimes with engineering input. Maintenance goes to engineering. Frankenstein-prevention is the job of whoever owns the platform's long-term shape, which is both product (what do we want to build) and engineering (how do we build reusable components).

FDE as currently packaged folds all three onto one team. The FDE writes the workaround. The FDE notices the pattern. The FDE writes the production code that absorbs it. The FDE (or someone, it's never clear who) has to maintain it later. And the FDE is the one supposed to push back when a customer asks for the seventh thing that doesn't fit the platform's shape, except they're embedded in the customer and their job is to make the customer succeed. The pushback rarely happens.

This is implementation plus product plus platform stewardship, on one team. The other product and engineering teams still exist, and each pulls in a different direction. The customer-facing org wants the deal unstuck. Product wants the pattern to generalize. Engineering wants the platform clean. The customer wants their specific thing, today. The FDE is the only person in the room accountable for all four landing, and owns none of the systems that would let them negotiate any of the four down. The only lever they actually control is the workaround. So when the pulls conflict (and they usually conflict), the only move available is to write another one.

And then another. They write the workaround for customer one. They write it again for customer two, slightly differently. They notice the pattern by customer three. They surface it to engineering. Engineering says *interesting, we'll consider it for next quarter*. The FDE writes it again for customer four. Eventually one of two things happens. Either some version of the workaround gets absorbed into the platform, possibly the wrong version, possibly with no consistent ownership for maintenance. Or it doesn't get absorbed at all, and the FDE quietly maintains six variations of it across customer codebases until they burn out or quit. That outcome is exactly what the FDE model was supposed to prevent.[^title]

## What good FDE looks like, structurally

Think of the platform as a Lego kit. The core engineering team designs and produces the bricks. The forward deployed engineers combine those bricks into solutions shaped to each customer's situation. The custom code composes on top of the platform rather than living inside it. When the FDE team sees the same pattern across customers, that pattern becomes a candidate for first-class inclusion in the platform, and the decision about whether to absorb it belongs to core engineering, not the FDE. This is, as I read it, more or less the Palantir model, and I think most companies citing it are reading it wrong.

In that model, the answers are clear. Generalization decisions belong to core engineering. Maintenance belongs to core engineering. Frankenstein-prevention belongs to core engineering, which can say no to absorbing a pattern that would muddy the platform without paying for the FDE's customer relationship.

That model only works if core engineering takes its job seriously. If the kit doesn't have bricks, the FDE has nothing to combine. If core engineering won't make absorption decisions, patterns pile up in customer code forever. If nobody owns Frankenstein-prevention, every customer slowly ends up with a slightly different version of the product.

### The Airtable scripting example

A version of this played out at Airtable when scripting shipped. The platform had APIs, but APIs required customers to host code somewhere, and most of our customers couldn't or wouldn't. Scripting changed that: code that lived inside the Airtable base, triggered by a button or an automation. The customer didn't have to host anything.

A team of about three of us became the script-writing arm. Every week, customers came in with use cases the standard product couldn't quite cover. We'd write the script, deploy it for that customer, move on. Everyone (leadership, engineering, sometimes us) worried that we were building unsustainable custom solutions at customer-by-customer scale. That we'd be crushed under maintenance.

We weren't. Because there were patterns.

Roughly 70% of script requests turned out to be project-and-task management, because Airtable handled many-to-one relationships in ways that surprised customers. Delete a project and the tasks didn't cascade-delete. Change a parent field and the children didn't propagate. Every customer was reinventing the same handful of scripts to paper over this.

So we did three things:

1. **Wrote a small set of canonical scripts** for the patterns we saw repeatedly.
2. **Published them** in the help center and the script library so customers and CS could grab them directly.
3. **Trained CS and implementation** on how to deploy and modify them, so the work didn't have to route through our team.

What we didn't do: write custom code in the production codebase. We didn't ship Airtable features ourselves. What we did do was *expand the set of customer use cases the company could say yes to*, using building blocks the engineering team had given us. When we noticed patterns, we surfaced them to engineering and product as candidates for first-class platform features. Some got absorbed. Some stayed as scripts. That decision belonged to engineering and product, not to us.

Maintenance of an absorbed pattern fell to engineering. And because engineering could always decline to absorb something, leaving it as a script, the platform never had to take on customer-shaped weirdness just to keep us unblocked.

### The same pattern at Recurrency

At Recurrency we had a feature called "rules": an engine for injecting custom SQL queries into the product that changed its behavior customer by customer. Same structural shape as Airtable scripting: core engineering built the primitive, and the implementation team composed it into customer-specific solutions that lived on top of it.

In both cases, core engineering was bad at one specific thing: knowing what customers actually wanted to use the primitive for, and building templates for it. They struggled because they thought in terms of highly generalized solutions: one template that handles every case. The implementation team looked at the same problem and thought differently: *this version covers 60% of my customers, and that's fine; here's a variant for the next 20%, and another for the last 20%.*

Engineering looks at three variants of the same script and asks why there are three versions of one thing. Implementation looks at three variants and sees three playbooks that, together, cover the whole problem space. Both are right from where they sit. The difference is depth. The bar implementation has to clear is *deployable for this cluster of customers.* The bar engineering has to clear is *configurable by any user, globally, forever*, and designed so the customization is done by the user, not by your implementation team standing over their shoulder. Those are different jobs, and the second one is much more expensive.

That's the whole reason the division of labor works, and the whole reason "just have the FDE write the production version" undercounts the cost. The scrappy version encodes assumptions specific to one customer: their data shape, the urgency of the moment, the parts you didn't bother to generalize because you didn't have to. Promoting it to a first-party feature means redoing it for a much wider set of users. You can object that LLMs are collapsing the distance between "scrappy thing" and "generalizable solution," and there's something to that. They do give implementation more room to contribute real code. But code review still takes time, and the design work of globalizing a customer-shaped solution doesn't disappear because the first draft was faster to write.

## What the split looks like once you're deploying agents

Everything above holds no matter what an FDE is shipping. But more and more, the thing an FDE is handed to deploy is an AI agent, and that sharpens where the line between the two teams falls. It doesn't erase that line so much as move it up a layer.

Start with the assumption underneath. When you deploy an ordinary SaaS feature, "the platform" is one thing: what core engineering ships and what the FDE configures on top. When you deploy an agent, that one thing splits in two. There's the harness: the runtime the agent executes in, the permissions it holds, the tools it's allowed to call, the evals that tell you whether it's working, the observability that tells you why it broke, the deployment surface, the security boundary around all of it. And there's the deployment: which task this agent does for this customer, what context and data it's wired into, which tools it needs that don't ship in the box, why it fails in this particular field.

Core engineering owns the harness. That's the Lego kit restated for agents: the runtime, the permission model, the reusable tool framework, the eval and observability layer, the deployment surface, the reliability and security boundaries. Those are the bricks. They're expensive, they're global, and the bar they clear is *configurable by anyone, forever*, not *deployable for this cluster of customers this quarter*.

The FDE owns deploying that harness into a specific customer or task context. Mapping the workflow the agent is supposed to live inside. Choosing which task is worth automating first. Wiring in the customer's context and data. Adding the narrow, customer-specific tools the harness doesn't ship. Debugging the failure modes that only surface in the field. Translating the customer's mess back into pressure on the product. Same job it always was, combine the bricks into something one customer can use, with a sharper line around what counts as a brick.

Draw that line in the wrong place and you can watch it do damage. Airtable scripting started in the browser. Because the code ran in the customer's own browser, it inherited the browser's reach: it could make web requests, reach a service on the customer's VPN, talk to something running on their laptop. People built real workflows on that. When scripting moved to automations so it could run on a schedule instead of a button click, it moved onto our AWS infrastructure, and that runtime change quietly deleted every use case that depended on reaching the customer's own network. The people most excited to automate those jobs got the least. That was a harness decision, runtime and security boundary, and it belonged to core engineering. No amount of FDE scrappiness at the deployment layer could route around it, because the FDE doesn't own the runtime. An FDE can add a tool. An FDE cannot change what the agent is fundamentally allowed to touch.

The three questions from the top of this piece don't change when the platform becomes a harness. They move up with it. Someone still decides what gets generalized, which now means which field-built tool or eval gets promoted into the core harness. Someone still owns maintaining the generalized version, which is now harness code every deployment leans on. And someone still has to keep the platform from collecting customer-shaped weirdness, which is now a harness quietly accumulating one customer's tool, another's permission exception, a third's eval that only makes sense if you were on the original call. Same failure modes, one layer up.

Drawing the line here is useful mostly because it tells you which job you actually have. Look at where your week goes, not at what your badge says.

> [!tip] What flavor of FDE are you?
> Sort yourself by where your time actually goes, not by your title.
>
> | Where your week actually goes | What that makes you | The risk to watch |
> |---|---|---|
> | Building and maintaining reusable harness pieces: runtime, tool framework, evals, observability | Product or core engineering wearing a field-facing hat | Field work turns into shadow roadmap engineering that never gets the review real platform code gets |
> | Mapping customer workflows and deploying or configuring primitives that already exist | Implementation or solutions architecture | You become the deployment bottleneck if nothing routes what you learn back into the product |
> | Adding narrow tools, connectors, and evals for patterns you see repeat across customers | The real FDE middle: field-specific productization | It only holds up if there's a real promotion path from your field tools into the core harness |
> | Writing bespoke code for every customer with no reusable harness or tooling story underneath | A consulting shop with an engineering title | Margin and support burden compound, and no customer ends up owning anything durable |
> | Deploying a harness core owns, but with no way to add tools or influence the primitives | A demo-and-deploy bottleneck | You ship a generic product that works in the pitch and breaks in the real workflow |
>
> None of these is a wrong thing to be. The failure is not knowing which one you are, or hiring for the field-productization middle and building the org for the consulting shop.

But there's a deeper problem that good structure alone doesn't fix.

## The duct tape isn't the product

There's a stronger version of the FDE pitch worth taking head-on. It goes: implementation teams already write workarounds for every customer. The workarounds get reused, they accumulate in customer codebases, they're maintained inconsistently. FDE fixes that. The same person doing the workaround can write it in production-quality code, contribute it back to the platform, and now you have one canonical version maintained by the team that built the rest of the platform. Faster, cleaner, more sustainable.

That argument concedes too much by accepting its own framing. Implementation's job *is* to build fast: to unblock customers, to keep revenue from stalling when the platform doesn't quite fit. Nobody apologizes for that. The reason implementation has to exist at all is that product and engineering missed something during the original build, or the market shifted and customers are solving problems nobody anticipated yet. Both are normal. Both are fine. That gap is not a failure. It's the distance between what got built and what the market does with it once it's in customers' hands.

The question is what happens *after* the fast build. The implementation team duct-tapes seven pieces together, the customer is unblocked, revenue is preserved. Now what?

In the model that works, the duct tape is *evidence*. It proves there's a real customer need the platform doesn't address. The duct-taped solution gets reused for the next two or three customers who hit the same gap (rebuilding from scratch every time would burn the team for no reason), but the expectation, always, is that a fully engineered version is coming from product and engineering, informed by what the duct tape revealed about what customers actually need.

The FDE pitch quietly proposes a different model: if the duct tape is written by an engineer in production-quality code, it can *become* the engineered version directly. Skip the rebuild. Ship the duct tape.

That's where the model breaks. The duct tape was shaped by the engagement that produced it: the urgency of unblocking, the specific shape that fit that customer's data, the assumptions baked into the workaround. Promoting it into the platform skips the design work that product owes the rest of the customer base (*is this the right shape for everyone?*) and the work that engineering owes the platform (*is this the right shape long-term?*). The duct tape is evidence of a real need. It is not, by virtue of being written in production-grade code, the right answer for the platform.

FDEs are the fast, scrappy team dispatched to solve problems the platform can't yet, equipped with whatever tools the engineering team has given them to work with. That role is real and worth hiring for. What that role can't do is substitute for the design discipline that product and engineering owe the platform when deciding what to absorb.

Workarounds are pressure relief. They route around the missing feature instead of forcing the org to confront it. The better the workaround, the less pressure on the platform to absorb the underlying need.

The Airtable scripting team is, in retrospect, a case study in this. The ~70% of script requests that clustered around project-and-task management (the many-to-one relationship gap) never became a first-class platform feature in the time I was there. The reason isn't that engineering didn't notice. The reason is that the workaround was good enough, deployed widely enough, customizable enough, that the urgency dispersed. CS knew how to deploy it. Implementation knew how to customize it. Customers were satisfied enough. The pain was absorbed, smoothed over, made manageable.

And to be clear, to a real degree this was success. The scripting team kept customers happy. Engineering got to work on greenfield features instead of going back to patch a relational-model gap they'd shipped years earlier. Looking at it as a resource allocation problem, the calculus made sense. The underlying fix kept losing to greenfield work, and from engineering's seat that was a defensible call.

What's harder to see is who never got the workaround at all. Our team wrote the scripts. CS deployed them once a customer surfaced the problem. But the workaround only helped customers we (or CS) identified and reached. The prospect who evaluated Airtable on their own, hit the relational gap, and went somewhere it was easier never showed up in the script-request volume. The customer who would have expanded if the capability were a discoverable first-party feature, rather than a thing you got handed if you complained loudly enough, never registered either. The ubiquity of the workaround across the customers we *did* reach is itself the signal: the use case is real, and common. The unknown is how many people never got to it because the path through Airtable was only clear in our heads, not in theirs.

That's the actual problem. Not that engineering made the wrong call. They made the rational call given the information they had. The feedback loop captured what was visible: support tickets, customer complaints, the volume of script requests our team handled. It missed the invisible side: prospects who walked because the workaround wasn't a feature they could find on their own, expansions that never happened, the slow accumulation of being known as "the spreadsheet that doesn't quite do projects."

If our team had been bad at the workaround, the pain would have stayed sharp and the platform would have had to move. If our team had been adequate but slow, the volume would have built up the case for first-classing it. We were good and fast, and the pressure dispersed. My read is that our competence was, in a real way, part of what kept the platform from evolving here. Calling us FDEs instead of a scripting team wouldn't have touched that. The team writing the workarounds is not the team that needs the pain to be sharp. The team that needs the pain to be sharp is whoever owns the product roadmap.

The root cause is your product feedback loop: what reaches the people making roadmap decisions, in what form, with what evidence behind it. "Just contribute the code back to the platform" treats the symptom and leaves that loop untouched.

What actually fixes the loop is an explicit accounting of what workarounds are absorbing, pattern by pattern, with customer volume and long-term cost attached, and a discipline of deciding whether the platform should take each one on. That's product work. It can't be delegated to the team writing the workarounds; they have no incentive to advocate for their own work being replaced.

The pushing function comes from the implementation team. They're the ones absorbing the customer cost every week, and they're the ones who can see when a workaround is propping up volume that ought to be a real feature. Engineering's natural posture, given the workaround exists, is to deprioritize: there's always something else to build, and the escape hatch is right there. That asymmetry is exactly what makes a functioning workaround dangerous to leave un-evaluated. *Implementation has it covered* is a sentence that stays true forever, and the gap never gets re-examined unless someone whose job it is to re-examine it forces the question.

## What problem are you actually solving?

Underneath all of this is a question most companies don't answer before they post their first FDE role: *what core problem are you actually trying to solve?*

If you're early and the honest answer is *"I'm willing to make one-offs to get customers in the door and figure out scale later,"* the right shape is straightforward. A slice of the engineering team reserves bandwidth for urgent customer requests and writes whatever code is required to get the deal across the line. They sometimes talk to customers. They sometimes ship production code that addresses a single customer's situation. The feedback loop is approximately zero: the people writing the platform are the people on the customer call. Greenfield slows under the weight of fire drills, and that's a fine tradeoff at this stage.

That model has a known breaking point. If you're successful, you'll have too many customers, too many one-offs in the codebase, too many features to build, and the engineering team can't keep up with all of it while also owning the core product, deciding what to absorb, and maintaining what they've already absorbed. Something has to step in and prioritize.

The mistake isn't running the early model. The mistake is staying in it past the breaking point and pretending you haven't crossed.

What comes next is not a renamed version of the early model. As I understand the [Palantir setup](https://blog.palantir.com/dev-versus-delta-demystifying-engineering-roles-at-palantir-ad44c2a6e87), it's a customer-facing implementation team (call them FDEs; the title is fine) that uses toolkits engineering provides to unblock customers, working closely with core engineering to absorb the worth-absorbing patterns into the product over time. The embedding and the production code are downstream of that, not the substance of it. Different team. Different mandate. Different bar to clear.

That setup takes more bodies and more discipline. The implementation team takes the brunt of hacky one-offs the engineering team has no bandwidth for. Engineering builds the long-lasting first-party features the implementation team isn't equipped to ship. Each team is doing what the other won't, and the platform covers a wider array of use cases than either one could alone. Stripe's [Forward Deployed Engineering team](https://stripe.com/jobs/listing/backend-engineer-forward-deployed-engineering/7249744) describes the role in similar terms: taking hard customer problems and turning them into platform capabilities that scale beyond the original engagement.

Between them sits an architect tier. Not necessarily a job title, more of a function. Someone who sees the volume of one-offs the implementation team is absorbing, the patterns underneath, and the cost of *not* first-classing each one. Someone with enough technical depth to argue with engineering and enough customer exposure to know what's actually being asked for. They're the missing owner the three questions kept pointing to: who decides what gets generalized, who maintains it, who keeps the platform from collecting customer-shaped weirdness. Their job is prioritization: which patterns get absorbed, in what order, with what scope. They pseudo-product-manage the implementation team, and they're the bridge into engineering's roadmap.

This is what we eventually built at Recurrency. The implementation team got better with AI tools: writing PRDs, building mockups, sketching the diagrams engineering needs to estimate the work. Engineering and customer-facing teams met in the middle through a smaller architect tier that owned the prioritization calls. There was real tension in it: customer-facing was accountable to retention and revenue and pushed hard; engineering was accountable to costs and timelines and pushed back. That tension is a *feature*. It forced go-to-market to think hard about what was actually critical, and it forced engineering to engage explicitly with what they were declining. Engineering retained veto: *that's not a core part of our business model* is a real thing they could say. But veto is different from absence.

What goes wrong is when a company is past the engineering-team-with-customer-time stage but still operating like they're inside it. The customer volume has outpaced what one team can absorb. The answer the org reaches for is *we'll hire FDEs into engineering and have them build the one-offs.* That collapses the two teams into one, removes the architect, and lands the result back in the muddle these roles keep producing.

There's a sharper way to put the surface-level warning: an FDE org that's really just a renamed SE team produces a consulting shop, not a product company. That's right on the symptom. The structural cause is that you tried to skip the architect.

The engineering team needs to own the Lego kit. The implementation team is there to combine the blocks. The architect tier between them owns the prioritization of what the platform should learn next, and answers to both sides for the choice. None of those is the same job, and the muddle most current FDE roles produce is what happens when you pretend they are.

[^title]: "Forward Deployed Engineer" as a title is doing three different jobs at once. It's a recruiting brand: the cohort of people who are technically savvy *and* customer-facing is small, and "FDE" reads sexier on LinkedIn than "Implementation Engineer." It's a customer credibility signal: engineers carry more weight in the room than CSMs. And it's claiming to point at structurally new work that's different from how most organizations have approached customers in the past. The first two are honest. The third is what this article is about.

    A related point: the people who take these jobs aren't aspiring full-time back-end engineers. They want the puzzle of combining what exists into something a specific customer can use. That craft is real and worth hiring for explicitly. *"Be scrappy and write production code in our main repo"* isn't a description of it.
