---
title: "Production Engineering vs. Operational Engineering"
slug: production-vs-operational-engineering
status: raw
target: substack
created: 2026-06-15
updated: 2026-06-23
tags: [engineering, forward-deployed, ai, team-design]
point: >
  There are two distinct engineering postures, and they evaluate
  trade-offs differently. Production engineering says "if you can't do
  it well, don't do it at all" — it standardizes and owns a problem
  100%, building the backbone everything else grows on. Operational
  engineering says "cover the 80%, ship it, and deal with the edges as
  they surface." In an AI world the old "citizen developer" category is
  collapsing and this distinction matters more, not less. You need both
  teams to balance each other: operations alone drowns in edge cases,
  production alone can't move fast enough.
---

# Production Engineering vs. Operational Engineering

There's a big difference between what I'd call *production engineering* and *operational engineering*. Historically we've drawn this line as "software engineers" versus "citizen developers" — but in an AI world the citizen developer idea is collapsing. Far more people now fit that description, and the tools have lowered the bar for who can build something that works. That's exactly why the distinction is worth revisiting.

This is related to the forward-deployed engineering conversations we've been having, but it's a slightly different lens — which is why it deserves its own treatment. The core of it is this: the two postures evaluate an *acceptable trade-off* completely differently.

## Where you're allowed to draw the cut line

The difference shows up in what's acceptable — where you're allowed to draw the cut line.

A production engineering team is trying to build a solution that meets a lot of people's needs. The standard is high. Operational engineering doesn't mean being sloppy, but it's much more comfortable cutting corners to get to an end state faster — knowing there's going to be some downstream pain you'll have to revisit.

> [!tip] Two ways to evaluate a trade-off
> - **Production:** "If you can't do it well, don't do it at all." Standardize it, own it 100%.
> - **Operational:** "I just want to cover the 80% — or even the 70%. That's still meaningful and beneficial. So ship it, and note there are going to be cases where we hit issues. We'll deal with those."

## The example that brought this on: duplicates

Right now in our software we're dealing with duplicates. What happens when we reach out to one org to establish a relationship, and then through our discovery process we *rediscover* that same org under a different name? How does the system resolve that?

This threw my production engineering team for a loop — because it's genuinely a hard problem. How do you know about subsidiaries? Do we need to buy a tool? Do we need to do all of these things to resolve identity properly?

My operational engineering lens is different: we'll know it's the same company if we attempt to reach out to the same person twice under different names. We reached out to Company A's generic support email, and Company B *also* routed us to that same generic support email. That's all we need. That should cover most of the cases — and specifically the cases we can reasonably feel comfortable we'll even be able to *detect*.

So don't worry about all the other edges and variations. We're not concerned with those right now, and we don't have to be. It's okay to just have the logic and process in place that we can expand on later — rather than sticking our head in the sand and ignoring the problem entirely.

## Why operational teams are comfortable with the 80%

A lot of this comes from the fact that operational teams are used to being more customer-facing. They understand that *shit happens* — and as long as they have the tools to go find the broken cases and resolve them, they can get it done.

A lot of engineers, on the other hand, don't want to retouch things they've already built. They don't want to take a manual action to resolve something after the fact. That's totally fair — and it's exactly the right place you *want* your production engineers thinking from. But it is a materially different way of looking at the work.

> [!note] Worth noting
> Neither posture is "right." The discomfort a production engineer feels about manual cleanup is the same instinct that produces a durable backbone. The operational engineer's comfort with mess is what lets the 80% ship today. The friction between them is the point.

## Why you need both teams

This is the real argument: you need both, and they balance each other out.

If you *only* ever had an operations team, you'd only ever cover the 80%. You'd always be bogged down by the 20% of errors and edge cases, and you'd probably end up with a hodgepodge system held together by hacks.

A production engineering team standardizes. It forces you to own something 100%. That owned thing becomes the backbone — the thing that lets you keep growing and expanding and taking on more, without burying yourself under the weight of your own shortcuts.

> [!warning]
> An operations-only org doesn't fail loudly — it accretes. Each 80% solution is individually reasonable, but the unowned 20% compounds into a system nobody can fully reason about. The backbone is what you sacrifice for speed, and you don't notice it's gone until you can't scale. [?] — worth a concrete example here from our own stack.

## Tension is the mechanism, not just the state

I said the friction between the two postures is the point. Here's the mechanism that makes that friction productive: you want the team that *should* own a job to feel the pain of doing it.

I get frustrated when engineering teams punt complexity to go-to-market — "oh, that's a go-to-market problem" — and quietly assume the GTM team will figure out how to absorb the workload without anyone getting buried. There's a responsible version of that delineation, and accountability matters. But there's real value in making whoever you want to be *primarily* responsible for a job feel the weight of doing it. Otherwise they'll never improve it.

The classic example is security reviews. Traditionally engineering says, "that's the go-to-market team's responsibility — they're the ones interfacing with customers." The reality is GTM doesn't have the information to fill out a security review. They need engineering to help. And when engineering is unwilling or unable to do that, it becomes very hard for the GTM team to build any system around it. So what do you do? You push it back: *no, you're filling these out.* And once engineering feels the pain of answering everything ad hoc — no standard repository of answers, every response from scratch, because they're the owners of the information — they get incentivized to build the system. To hand it back to go-to-market in a better place.

That's the whole game. Applying pressure in the right area forces your teams to build systems that allow for repeatability, scalability, and better business margins.

## The real question: humans or software?

Then someone pointed out to me — it shouldn't really be go-to-market versus engineering. That framing is a *proxy* for a sharper question: do you want this job done by humans you hire, or done in software? That delineation functionally tells you which team should own it.

> [!tip] The proxy that actually decides
> "Go-to-market vs. engineering" is just shorthand for **"hire bodies vs. build software."** Decide *that* first, and the team assignment falls out of it.

If you decide you need bodies to manage the experience — support, customer success, sales, BDRs — you've committed to it being a go-to-market problem. And you'll keep hiring. Not necessarily linearly, but as the business grows there are always new bodies you have to add, which means some share of your revenue gets eaten by the people you hire to support it.

The other option is software. Yes, software still requires people — but it doesn't scale linearly anymore. Once the system exists, it grows and grows and supports significantly more customers than any one person can. The economies of scale are just fundamentally different from choosing to hire people.

So why not make software do everything? That comes down to trade-offs and prioritization. Maybe it's people today, software later — that's a perfectly acceptable answer to a lot of this. And some problems genuinely aren't great solves for software.

Support is the example that's actively flipping. Traditionally it needed bodies — there were so many idiosyncrasies, and even in a world of chatbots and choose-your-own-adventure flowcharts ("select this option, get routed to the right place"), there was always a fleet of humans behind it catching what trickled through, at volumes that made the team keep growing. But more and more of that flowchart-driven process, even the dynamic parts, is something software can now solve.

In an AI world, how much your go-to-market team can technically arm themselves and build their own systems directly determines how many bodies you have to go hire.

## The takeaway

Production and operational engineering aren't a hierarchy, and they aren't the same job done at different quality levels. They're two different answers to the question *"what's an acceptable trade-off?"* — and a healthy org needs both answers in tension.

There are still problems where the answer is to hire: salespeople, support, forward-deployed engineers. There are real cases where you *want* humans. The question is just how many tools and systems you give them to decrease how many you need to hire. And there are problems where, if you counted the bodies you'd have to bring on, the overhead is simply more than you're willing to take on. Those have to go to software — and more and more problems are landing in that second bucket.

That's the part engineering teams need to get comfortable with: owning them. You can no longer just punt because something is complex. Complexity and cost used to be reason enough to say "we don't want software here" — that's traditionally where most teams drew the line. They aren't good enough reasons anymore.

[?] — possible follow-up thread: how does the collapsing "citizen developer" category change the *ratio* of these two teams you need? The "how much can GTM arm themselves" point starts to answer this — in an AI world, operational/GTM capacity may expand faster than production, shifting more problems across the "hire vs. build" line toward software.
