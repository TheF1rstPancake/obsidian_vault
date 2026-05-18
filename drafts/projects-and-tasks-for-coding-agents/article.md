---
title: "Building Is Cheap. Roadmapping Is the Hard Problem."
slug: projects-and-tasks-for-coding-agents
status: raw
target: substack
created: 2026-05-18
updated: 2026-05-18
tags: [ai-agents, coding-agents, project-management, workflows]
---

I saw a post recently that stuck with me: *building is cheap, roadmapping is not the hard problem.* [?] That framing is a little more solution-oriented than I'd put it, but the root cause it's pointing at is very real — and it's something I keep running into with coding agents.

## The multitasking trap

It is absurdly easy to multitask with agents now. At any given moment, I can have ten different tabs open, ten different agents writing ten different pieces of code against the same system. They operate independently. I know how to slice up work so each one is on a unique part of the problem, and I can shuttle shared learnings between them so they grow together.

The mechanics are solved. The cognitive overload isn't.

I'll kick off something because I know it's important, and then it gets deprioritized because I have to go troubleshoot one of the other nine things. As those resolve, I come back up for air and realize I don't actually know where I am. Have I solved the core problem? Have I just created new problems? Is half of this work disjointed and floating around with no home?

## Why plans don't save you

The obvious answer is "write a plan." But plans break in both directions:

- **Go macro, and the plan lacks specificity.** Individual agents drop into the work, hit problems the global plan never anticipated, and disappear down rabbit holes the plan can't account for.
- **Go micro, and you lose the relationships.** You can write a tight plan per agent, per project — but how all those plans relate to each other becomes really hard to track.

There's no good middle. The thing connecting the micro to the macro — the structure that says *these five threads ladder up to this one goal* — doesn't exist in any of the tools.

## Projects and tasks, again

This is the same problem I watched organizations struggle with when I was at Airtable. Most of the workflows we supported were, at their core, project and task management. You could decompose maybe 80% of what people were doing into: *projects spawn tasks.*

What the projects were, what the tasks were, what spawned what, what metadata mattered — all of that was unique per workflow. But the underlying shape was inescapable. Projects and tasks.

The LLM world has the same shape, and it has it more urgently. Things jump around fast. Spawning is cheap. You can hold a vague sense of "these agents are working toward this goal" in your head — until you can't.

## What's missing in the tools

Claude Code, Codex, Cursor, [?] pick your coding agent of choice — none of them natively support the idea that *I have a goal, I am spawning many agents at it, and I need to evaluate whether I am marching toward that goal.* That evaluation is still entirely on the human. The tools don't give you a framework for it.

So you go looking for it elsewhere. Stitching together a Linear board, a Notion doc, a spreadsheet, a scratch markdown file. None of which know anything about the agents themselves, which is the whole point.

I have some ideas on how to solve this, and how you'd actually build it. That's probably another article.
