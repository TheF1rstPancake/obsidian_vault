---
title: "Removing yourself as the control plane"
slug: removing-yourself-as-control-plane
status: raw
target: ghost
created: 2026-07-30
updated: 2026-07-30
tags: [ai-agents, agent-architecture, workflow]
visibility: public
point: >
  Most people running AI agents are still the control tower: deciding what happens next, tracking whose turn it is, nudging every step forward. That's not a personality trait, it's how Claude Code, Cursor, and Codex are built, around a conversation thread that never leaves your hands. Moving to a model where you initiate work, define what should get done, and only show up for escalations is a bigger architectural jump than smarter one-shotting models suggest, because not everything is one-shotable and the clients themselves assume the work runs on your device.
---

Most people running AI agents today are the control tower. They decide what work happens, they track whose turn it is to act, and they nudge things forward turn by turn. That's not a personality quirk. It's how the tools are built.

Claude Code, Cursor, and Codex are all architected around a conversation thread. You open a thread, send a prompt, the agent responds, you read the response and reprompt to get closer to what you actually wanted. Skills and shared markdown files get pulled into that thread at various points, but the loop itself never leaves your hands. No work happens without your direction. You are, functionally, the control plane.

That's a fine model for a lot of work. But it makes the next step feel like a much bigger jump than it should: moving from being the control plane to letting agents manage other agents, while you become the person who starts the work, defines what should get done, and shows up when something needs escalating. Everything in between, the system handles itself.

## One-shotting isn't the same as removing yourself

As models get smarter, it's tempting to think this problem solves itself. Fable can one-shot a lot of requests now. You can be less precise in how you phrase something and the model will fill in the gaps and get to a reasonable conclusion. That's real progress, but it's still a control-plane pattern: you initiated the work, and it got done in one exchange.

Not everything is one-shotable. And you don't always want it to be. Some work needs a writer, a reviewer, and a revision pass, a structure no single prompt and no single agent is going to close out on its own. That's where most people get stuck: they know they don't want to keep managing turn-by-turn chat forever, but they don't have a model for what replaces it.

> [!tip] The intern vs. the manager
> The way most people use an AI client today is like using an intern. You point it at a problem, say "go," and it comes back with a lot of questions, because it genuinely doesn't know what it's doing yet.
> The alternative is acting like a manager with a team of five to ten people. Each person needs different instructions to do a different job. There's a shared baseline of understanding across the team, but it's a completely different architecture than briefing one intern at a time. You don't get there by writing a better prompt. You get there by rethinking who's actually driving.

## What an agent actually is

Strip it down and most agents are just prompts: a collection of markdown files that make up the instructions for what should run and when. Agents also carry a set of tools, MCP servers or other APIs, and how the agent knows to use those tools is dictated by the same prompts that define it. [?] One framework lays this out bluntly: an agent can be represented entirely as files and configuration on a file system. I couldn't cleanly make out the name of it on the recording, worth tracking down for the next pass.

Then there's the harness: the system that actually executes the agent. It takes the instructions, turns them into action, talks to one or more LLM providers, manages tool calls and reads the responses, and handles infrastructure like letting the agent write and run its own code.

Finally there's the client: your interface into the harness. It's where you configure things and where you have the conversation that triggers work in the first place.

Claude Code, Cursor, and Codex are all clients built explicitly on top of that stack, and every one of them treats a "deployed agent" as a conversation thread. That's the design choice that keeps you as the control plane.

## Not all harnesses give you the same room

Some clients are more flexible about letting you step out of that loop than others. Cursor tends to be more permissive. Claude Code is stricter, and you can see it in how Anthropic has handled programmatic access. The `claude -p` flag, the mechanism for calling Claude Code on demand to do one thing and return a result, has been through pricing changes that got walked back, and the general direction has been to push programmatic use through the API rather than letting people script the client directly.

If you want to remove yourself from the control flow, writing code that triggers agent actions on events is the actual mechanism. But once you step outside the clients that give you that for free, you're building it yourself, and that's not trivial. Where does the chat interface live? How do you get notified when something needs your attention? How do you track what's in flight? Do you care which LLM provider is underneath, and how locked in are you willing to be? None of these questions exist when you're doing turn-by-turn chat in a client. They all show up the moment you stop.

## The other constraint: your laptop is the runtime

There's a second thing holding this model in place that's easy to miss: most of these clients assume the work happens on your device. Conversation history might live on a server and sync across machines, but the actual computation, the place where the work is being done, is mostly local. Close the laptop or let it sleep, and whatever was running halts with it.

That's why everyone is walking around with their laptop open. They're babysitting long-running jobs so they can redirect them the moment something's needed. It's a symptom of the same underlying architecture: you're not just the control plane for decision-making, you're also the runtime.

Getting past that means the execution needs to live somewhere you don't have to be physically present for, a system you're an observer of rather than the primary actor in. Which is a strange kind of trade: you're decentralizing yourself out of the loop, but the actual execution ends up more centralized, living in one durable system instead of scattered across whatever device happens to be open. That tension, between wanting to step back and needing somewhere durable to step back to, is probably the real design problem here.

More on this soon.
