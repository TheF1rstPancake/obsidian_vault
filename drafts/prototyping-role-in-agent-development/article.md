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

That's the part that's easy to skip. If you jump straight to "build a dashboard," you can build a really shitty one that gives you really shitty signals downstream, and it'll still look like progress because there are numbers on a page. Most people, if you ask them cold, can't articulate what data they need to make a decision. They can't word-vomit the full list of signals and thresholds on the spot. That's what the prototype is actually for: it's the thing that forces that articulation out of you.

So the first step isn't the dashboard. It's figuring out what you're trying to decide, and only then figuring out what would need to be on a page to let you decide it.

## What "done" looks like for a prototype
