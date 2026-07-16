---
title: "Data, Logic, Interface, Infrastructure: a four-layer lens for any software app"
slug: decomposing-software-apps
status: shaping
target: ghost
created: 2026-05-09
updated: 2026-07-16
tags: [software, frameworks, mental-models]
related: ["four-layer-lens-workbook"]
point: >
  Arguments about software go wrong when people compare apps at different
  layers. Name Data, Logic, Interface, and Infrastructure, and the rebuild /
  buy / agent-caller questions stop talking past each other, especially once
  you see that running software is not the same as multiplayer production.
---

# Data, Logic, Interface, Infrastructure: a four-layer lens for any software app

## The thesis

Most arguments about software ("should we build it?", "is this product good?", "what does this tool actually do?", "why can't I just rebuild that in Claude?") get muddier than they need to be because people compare apps at the wrong level. One person is talking about the UI, another about the data model, a third about the deployment story. They're all right, and they're all talking past each other.

A simple lens that cuts through this: **every software app is some combination of three layers (Data, Logic, Interface) wrapped in a fourth, Infrastructure.** Once you can articulate where a tool sits across those four, evaluation gets a lot less hand-wavy, and so does the question of how much of it an LLM can actually rebuild for you.

## The four layers

**Data layer.** What the system stores and how it's structured. Schemas, entities, relationships, persistence. The "nouns" of the app.

**Logic layer** (a.k.a. the application layer). What the system does with the data. Business rules, workflows, computations, decisions. This is where APIs sit, and the interface layer below is how that logic gets exposed. The "verbs."

**Interface layer.** How humans (or other systems) interact with the logic and data. UI, CLIs, webhooks, agents. The surface area.

**Infrastructure.** The fourth layer nobody puts on the brochure. Where each of the other three actually *runs*, how it's accessed, what it costs in compute. Hosting, identity, networking, observability, deploys, security boundaries. The plumbing that lets the other three run reliably, and the layer where most of the hard, invisible decisions live.

### A concrete spine: rebuilding ChatGPT

Take a tool everyone knows and run it down the layers.

**Data.** What do you actually need to store to make the universe of the app exist? For a ChatGPT (or Claude) clone it's almost embarrassingly small at the core: *users*, and *users' conversations* (the messages and text within them). Layer on preferences and memories and you've got the rest, but the spine is users → conversations. (Plus a password, which probably isn't even its own table. Implementation detail.)

**Logic.** How you interface with that data. The floor is CRUD (create, read, update, delete) for every data element you store. Create a user, update their password or name, read their details on login, delete on request; the same four verbs for conversations as the user chats. Here's the part worth knowing: **we've known how to automate CRUD forever.** Express, the Python backends — you define your data models (the tables, their objects, the relationships between them) and the framework *procedurally* generates the CRUD endpoints. No LLM required; this has been a boring, solved problem for years. The logic layer only gets interesting when you start *chaining* those operations into something opinionated. Example: a new conversation is created with an empty title, then the system reads your first message, summarizes it, and writes that summary back as the title. That block (read, interpret, store) is your *actual* logic. It's the part that makes the app *this* app.

**Interface.** How people actually engage. For most tools today that's a web page firing calls at the logic layer, which acts on the data layer and renders results back. (Where the logic *lives*, in the browser or on a server, is its own holy war in modern web programming, and not the point here; the layer cake holds either way. Code that runs and data that's stored are separate concerns.)

**Infrastructure.** Where each of those layers runs, how it's accessed, and what compute you're willing to pay for. Contrast a single-page web app (data lives in the browser's local session, logic is JavaScript functions calling each other, maybe one outbound request, the browser renders everything itself) against ChatGPT, where most data sits in a database, endpoints pull it, and a web UI (or a desktop app) presents it. Same three layers on paper; completely different infrastructure underneath. There are a ton of ways to build the infrastructure that supports the same three layers, and the right one depends on requirements most people never write down.

## Why can't I just rebuild it in Claude?

This is the question the whole lens is built to answer, and it shows up in two flavors:

- **Externally:** customers debating whether your tool is worth paying for. "Why would I subscribe when I could just rebuild this myself with Claude?" (I'll reference Claude throughout because it's my tool of choice, but read it as *any* agentic coding setup.)
- **Internally:** the same impatience pointed at your own people. Why does this take engineering so long? And, increasingly, why is the solutions-engineering or forward-deployed team *filing tickets* instead of fixing things themselves — "you've got Claude, make Claude do it."

Both betray the same gap: a fundamental misread of what it takes to build a *production* system, as opposed to something that merely runs.

**The one-shot mirage.** You've seen the posts: "I told Fable to build it and it one-shotted the whole thing." What those posts leave out is the *full prompt*: all the context and constraints the author front-loaded because they understood the technical tree well enough to know what to inject. "Build me a Minecraft clone" is not the whole prompt. The more you understand the terrain, the more context you can insert, and the higher your odds of a one-shot success climb. Leave it to chance and the LLM does what it's optimized to do: take the **shortest path to resolution**. The shortest path is almost never a full-grade production application.

> [!tip] Where Claude helps, layer by layer
> Claude quietly looks finished when it is only solving the easiest layers.
> - **Data:** strong. Modeling tables and relationships is well-trodden ground.
> - **Logic (CRUD):** strong, and arguably trivial; this was procedurally generated long before LLMs existed.
> - **Logic (opinionated):** good, *if* you can specify the behavior precisely enough.
> - **Interface:** strong. Scaffolding a UI is the showcase demo.
> - **Infrastructure:** weakest by far. The choices depend on requirements most people never articulate, so they never make it into the prompt.

**Infrastructure** is where the hidden requirements show up fastest. Take real-time collaboration, table-stakes since Google Docs. You cannot get it from a single-page app that runs entirely in your browser. Two browsers don't talk to each other without some middleman to relay state between them. (Yes, there are peer-to-peer frameworks, before anyone comes for me in the comments, but that's a *complicated* setup. The odds that Claude one-shots it *and* you understand the result well enough to extend it without breaking everything on your next prompt are not realistic.) One small requirement ("make it collaborative") reorders every infrastructure decision beneath it, which in turn colors the code at every other layer.

**The real divide: single-player vs. multiplayer.** Building something on your laptop is trivial, and getting more trivial by the month. Building something that works for *one person* has always been trivial. It's why every big enterprise has the legendary spreadsheet that Sally has run for twenty years as her entire job. What *hasn't* gotten any easier is the **multiplayer application**: one where multiple people engage with the same system at once. That comes with a host of complexities most people never think through. Because they don't think it through, they don't inject it into their Claude prompts, so Claude doesn't account for it, so what it produces works for them and only for them. Tunnel your laptop out with ngrok or Tailscale so others can hit it and it'll *run*. It just won't meet the objective you actually need it to.

> [!warning] Production means it works for everyone at once
> Production means it works for everyone at once under requirements like collaboration, concurrency, persistence, and auth. Claude can't infer the requirements you never stated.

That gap, from "it works on my machine" to "it works for my entire team," is exactly why engineering still can't just move infinitely fast even with Claude, and why your fairly-technical-but-not-principal-engineer folks can't simply go fix things in the production app themselves. Infrastructure and environment choices color a huge share of the code you write, and they're among the least understood parts of writing code.

## Where AI sits in the stack

Everything above is about how good Claude is at *building* each layer. There's a second, shorter claim: where does the AI itself (the model you're calling, not the coding agent that built your app) actually *live* inside the four-layer stack?

In the logic layer. Every interaction with an LLM is an API call — even in a self-hosted setup, you're still making that request internally — out to a service that packages a request, sends it, and hands back a response. AI became a very active resident of the logic layer that was already there.

That matters because of who's making the calls. For most of software history, the entity hitting your logic layer was a human, via a browser, via your interface layer. Increasingly, the thing calling your logic is a chatbot or agent acting on a person's behalf. The user's interface is their chatbot. The chatbot's interface into *your* product is your APIs.

> [!tip] APIs stop being the escape hatch
> For years, an API was secondary: "you're a technical user with requirements we don't build UI for — here's the API." If the primary user of your product is increasingly a person directing an LLM, the API becomes the front door. Design for that caller. Don't assume the old defaults still fit.

## The check that earns the lens

Before you argue rebuild, buy, or "Claude can just do it," name the layer you're actually talking about and who's actually calling it. If you can't say which of the four is load-bearing for the decision, or whether the caller is a person or an agent acting for one, you're probably comparing a UI demo to a multiplayer production system. Those aren't the same argument.
