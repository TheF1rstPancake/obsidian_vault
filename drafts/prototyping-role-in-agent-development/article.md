---
title: "The Dashboard Isn't the Point. The Decision Is."
slug: prototyping-role-in-agent-development
status: raw
target: ghost
created: 2026-07-14
updated: 2026-07-14
tags: [agent-development, prototyping, ai-agents]
visibility: public
point: >
  Sastra's advice to build a dashboard before you build an agent is a good
  instinct pointed at the wrong artifact. The dashboard isn't the goal, it's
  a byproduct of figuring out what signals actually drive a decision. This
  piece breaks down what a prototype is really for in agent development:
  clarifying the job to be done, turning your if-this-then-that thinking
  into a skill file an agent can follow, and then bringing that same
  prototype back as a control pane, not for doing the work, but for
  watching whether the agent is doing it right.
---

Sastra recently published a blog post arguing that the best way to build agents isn't to build the agent first. It's to build the dashboard, then build the agent on top of it. It's an interesting framing, and I think it's mostly right, but I think it's aimed at the wrong artifact.

Their version of "dashboard" is very BI-flavored: metrics, tables, a control plane someone reviews to decide what action an agent should take. And building that kind of dashboard genuinely isn't hard. You can vibe-code one in an afternoon. But if you start from "build a dashboard," you skip the actual first-principles question, which is: what signals do I even need to make this decision?

## The problem with starting at the dashboard

I built a lot of dashboards for the sales team at Airtable. The recurring question was some version of "how do you prioritize your book of business?" There was never one right answer to that. The job was always to find data that was meaningful and accessible to the decisions people actually needed to make.

That's part of why prototyping matters more now than it used to. Everyone can write code well enough to put something together on their own laptop, no production system required, so a prototype isn't a luxury reserved for engineers anymore. You can write the best PRD in the world and you're still relying on someone's reading comprehension to get the idea right from the page. Give people something alive to react to instead, and you skip that dependency. It's one of the more reliable ways I've found to get a team on the same page.

That's the part that's easy to skip. If you jump straight to "build a dashboard," you can build a really shitty one that gives you really shitty signals downstream, and it'll still look like progress because there are numbers on a page. Most people, if you ask them cold, can't articulate what data they need to make a decision. They can't word-vomit the full list of signals and thresholds on the spot. That's what the prototype is actually for: it's the thing that forces that articulation out of you.

So the first step isn't the dashboard. It's figuring out what you're trying to decide, and only then figuring out what would need to be on a page to let you decide it. The problem then becomes fidelity: how far do you let that prototype run before it stops clarifying the decision and starts becoming the decision.

## What "done" looks like for a prototype

A prototype is done when it's answered the question you built it to answer, not when it looks shippable. That line is easy to blow past. I catch myself doing it constantly: tweak one more thing, then one more thing after that, and the prototype quietly turns into a V1. The APIs work. The core components are all there. What's left is UI polish. At that point it doesn't feel like a prototype anymore, it feels like something you should just ship.

That's exactly when the conversation goes sideways. Once something looks close to finished, people stop debating the problem and start debating the implementation. Is that the right button? Is that the right label? Those are fine questions, but they're not the first ones. Until everyone agrees on the problem and on which data or actions actually matter to solving it, there's no basis for making those calls. Button placement is arbitrary until the problem is settled.

There's a second cost that matters more for agents than it ever did for dashboards. If two or three people each build a full prototype for the same problem, independently, you don't just get duplicated effort. You get a Frankenstein product: multiple plausible paths to the same goal, each built on slightly different assumptions about what the goal even was. A person can navigate that ambiguity. An agent mostly can't. Even with a large context window, contradictory paths to the same objective invite hallucination and missteps, because the agent has no way to know which one is "right." Now you're litigating which version was correct instead of getting the work done.

None of this requires the prototype to be complete or the interactions to be polished. It requires one path forward. That's the actual definition of "done" here: agreement on the problem, on the handful of data points and actions that matter, and on a single sequence for how they fit together, before anyone starts arguing about pixels.
