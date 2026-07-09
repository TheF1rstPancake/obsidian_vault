---
title: "Data, Logic, Interface, Infrastructure: a four-layer lens for any software app"
slug: decomposing-software-apps
status: shaping
target: ghost
created: 2026-05-09
updated: 2026-07-09
tags: [software, frameworks, mental-models]
---

# Data, Logic, Interface, Infrastructure: a four-layer lens for any software app

## The thesis

Most arguments about software — "should we build it?", "is this product good?", "what does this tool actually do?", "why can't I just rebuild that in Claude?" — get muddier than they need to be because people compare apps at the wrong level. One person is talking about the UI, another about the data model, a third about the deployment story. They're all right, and they're all talking past each other.

A simple lens that cuts through this: **every software app is some combination of three layers — Data, Logic, Interface — wrapped in a fourth, Infrastructure.** Once you can articulate where a tool sits across those four, evaluation gets a lot less hand-wavy — and so does the question of how much of it an LLM can actually rebuild for you, and increasingly, where AI itself sits inside the stack of the products you already run.

## The four layers

**Data layer** — what the system stores and how it's structured. Schemas, entities, relationships, persistence. The "nouns" of the app.

**Logic layer** (a.k.a. the application layer) — what the system does with the data. Business rules, workflows, computations, decisions. This is where APIs sit. The "verbs."

**Interface layer** — how humans (or other systems) interact with the logic and data. UI, APIs, CLIs, webhooks, agents. The surface area.

**Infrastructure** — the fourth layer nobody puts on the brochure. Where each of the other three actually *runs*, how it's accessed, what it costs in compute. Hosting, identity, networking, observability, deploys, security boundaries. The plumbing that lets the other three run reliably — and the layer where most of the hard, invisible decisions live.

### A concrete spine: rebuilding ChatGPT

Take a tool everyone knows and run it down the layers.

**Data.** What do you actually need to store to make the universe of the app exist? For a ChatGPT (or Claude) clone it's almost embarrassingly small at the core: *users*, and *users' conversations* — the messages and text within them. Layer on preferences and memories and you've got the rest, but the spine is users → conversations. (Plus a password, which probably isn't even its own table — implementation detail.)

**Logic.** How you interface with that data. The floor is CRUD — create, read, update, delete — for every data element you store. Create a user, update their password or name, read their details on login, delete on request; the same four verbs for conversations as the user chats. Here's the part worth knowing: **we've known how to automate CRUD forever.** Express, the Python backends — you define your data models (the tables, their objects, the relationships between them) and the framework *procedurally* generates the CRUD endpoints. No LLM required; this has been a boring, solved problem for years. The logic layer only gets interesting when you start *chaining* those operations into something opinionated — e.g. a new conversation is created with an empty title, then the system reads your first message, summarizes it, and writes that summary back as the title. That block — read, interpret, store — is your *actual* logic. It's the part that makes the app *this* app.

**Interface.** How people actually engage. For most tools today that's a web page firing calls at the logic layer, which acts on the data layer and renders results back. (Where the logic *lives* — in the browser or on a server — is its own holy war in modern web programming, and not the point here; the layer cake holds either way. Code that runs and data that's stored are separate concerns.)

**Infrastructure.** Where each of those layers runs, how it's accessed, and what compute you're willing to pay for. Contrast a single-page web app — data lives in the browser's local session, logic is JavaScript functions calling each other (maybe one outbound request), the browser renders everything itself — against ChatGPT, where most data sits in a database, endpoints pull it, and a web UI (or a desktop app) presents it. Same three layers on paper; completely different infrastructure underneath. There are a ton of ways to build the infrastructure that supports the same three layers, and the right one depends on requirements most people never write down.

## Why can't I just rebuild it in Claude?

This is the question the whole lens is built to answer, and it shows up in two flavors:

- **Externally** — customers debating whether your tool is worth paying for: "why would I subscribe when I could just rebuild this myself with Claude?" (I'll reference Claude throughout because it's my tool of choice, but read it as *any* agentic coding setup.)
- **Internally** — the same impatience pointed at your own people. Why does this take engineering so long? And, increasingly, why is the solutions-engineering or forward-deployed team *filing tickets* instead of fixing things themselves — "you've got Claude, make Claude do it."

Both betray the same gap: a fundamental misread of what it takes to build a *production* system, as opposed to something that merely runs.

**The one-shot mirage.** You've seen the posts — "I told Fable to build it and it one-shotted the whole thing." What those posts leave out is the *full prompt*: all the context and constraints the author front-loaded because they understood the technical tree well enough to know what to inject. "Build me a Minecraft clone" is not the whole prompt. The more you understand the terrain, the more context you can insert, and the higher your odds of a one-shot success climb. Leave it to chance and the LLM does what it's optimized to do — take the **shortest path to resolution**. The shortest path is almost never a full-grade production application.

So where, layer by layer, does Claude actually help — and where does it quietly hand you something that only *looks* finished?

> [!tip] Where Claude helps, layer by layer
> - **Data** — strong. Modeling tables and relationships is well-trodden ground.
> - **Logic (CRUD)** — strong, and arguably trivial; this was procedurally generated long before LLMs existed.
> - **Logic (opinionated)** — good, *if* you can specify the behavior precisely enough.
> - **Interface** — strong. Scaffolding a UI is the showcase demo.
> - **Infrastructure** — weakest by far. The choices depend on requirements most people never articulate, so they never make it into the prompt.

**Infrastructure is where it falls apart — because of requirements you didn't say out loud.** Take real-time collaboration, table-stakes since Google Docs. You cannot get it from a single-page app that runs entirely in your browser. Two browsers don't talk to each other without some middleman to relay state between them. (Yes, there are peer-to-peer frameworks — before anyone comes for me in the comments — but that's a *complicated* setup, and the odds that Claude one-shots it *and* you understand the result well enough to extend it without breaking everything on your next prompt are not realistic.) One small requirement — "make it collaborative" — reorders every infrastructure decision beneath it, which in turn colors the code at every other layer.

**The real divide: single-player vs. multiplayer.** Building something on your laptop is trivial, and getting more trivial by the month. Building something that works for *one person* has always been trivial — it's why every big enterprise has the legendary spreadsheet that Sally has run for twenty years as her entire job. What *hasn't* gotten any easier is the **multiplayer application**: one where multiple people engage with the same system at once. That comes with a host of complexities most people never think through — and because they don't think it through, they don't inject it into their Claude prompts, so Claude doesn't account for it, so what it produces works for them and only for them. Even if you tunnel your laptop out with ngrok or Tailscale so others can hit it, it'll *run* — it just won't meet the objective you actually need it to. That gap, **"it works on my machine" → "it works for my entire team,"** is exactly why engineering still can't just move infinitely fast even with Claude, and why your fairly-technical-but-not-principal-engineer folks can't simply go fix things in the production app themselves. Infrastructure and environment choices color a huge share of the code you write, and they're among the least understood parts of writing code.

> [!warning] "It runs" is not "it works"
> ngrok-ing your laptop to the world clears the lowest possible bar — the thing responds. Production means it works for *everyone at once*, under requirements (collaboration, concurrency, persistence, auth) you have to know to ask for in the first place. Claude can't infer the requirements you never stated.

## Where AI actually sits: the logic layer, and what that does to interface design

Everything above is about how good Claude is at *building* each layer. There's a second, separate claim worth pulling apart: where does the AI itself — the model you're calling, not the coding agent that built your app — actually *live* inside the four-layer stack of any application that uses it?

The answer is unambiguous: the logic layer. Every interaction with an LLM, even a self-hosted one, is an API call out to some service that packages up a request, sends it, and hands back a response. That's the definition of the logic layer: a collection of APIs, calling other APIs. What you expose to your interface is a series of APIs, which in turn call another set of APIs — one of which might be a model. AI didn't add a new layer to the stack. It became a very active resident of the one that was already there.

That matters because of who's making the calls. For most of software history, the entity hitting your logic layer was a human, via a browser, via your interface layer. That's changing. Increasingly, the thing calling your logic isn't a person clicking through your UI — it's a chatbot or agent acting on a person's behalf. The user's interface is their chatbot. The chatbot's interface into *your* product is your APIs. Machines don't want to drive a web browser. They're much better at, and much better served by, code and code-shaped interfaces.

**That flips a long-standing assumption about APIs.** For years, an API was the escape hatch: "you're a technical user with requirements we don't build UI for, here's the API, knock yourself out." That framing assumed the API was a secondary surface for a minority of users. If the primary user of your product is increasingly a person directing an LLM, the API stops being the escape hatch. It becomes the front door. API development is becoming a first-party experience again, not an afterthought bolted onto the "real" (UI) product.

**The deeper shift: you don't control the interface anymore.** Put the same three layers in a chain and the change gets sharper. Historically, for most users, that chain read *web interface → APIs → database*. What's changing for a growing share of users is that it now reads *LLM chat → APIs → database*. Same three layers, completely different middle experience for you as the builder — because the thing at the top of that chain used to be yours and now isn't.

A web interface is deterministic in the sense that matters here: you built it. You decide what renders, what the user can click, what path they're funneled down. The user's actions on that page aren't fully deterministic, but they're constrained by what you designed. You control the page. Swap that page for an LLM chat and you control none of it. The user isn't choosing from buttons you laid out. They're talking to a system that decides, on its own, whether to call you at all, and if so, how. That's not "constrained but non-deterministic" anymore. That's open-ended, and it's a system you don't own or steer in any sense.

That reframes the competitive question. It stops being just "is my API well-designed for an LLM caller" and becomes "does the LLM choose me over the alternative, and does the user even notice." Three things change once you take that seriously: how you build and surface the APIs you expose, how users actually engage with your product day to day, and how users come to understand the value they're getting from you at all. That third one is the easy one to underestimate. If a chatbot is quietly the thing fetching your data and running your logic on someone's behalf, the user may never see your brand, your UI, or your onboarding flow again. Being good is necessary but no longer sufficient — you also have to be legible enough, as an API, for an agent to pick you over a competitor, and the user has to be able to tell that the pick was the right one.

> [!note] So what happens to the UI?
> It doesn't disappear, but its job changes. If agents are the ones executing actions inside your product, someone still needs to see what happened — what the agent did, whether it was right, where to intervene if something's wrong. The UI's new job looks less like "the surface humans use to get work done" and more like a control plane for supervising what your AI is doing on your behalf. That's a genuinely open interface-design problem, not a solved one. Nobody has a clean answer yet for where errors get surfaced when the action was taken programmatically instead of by a human clicking through a form.

**What's the actual best interface for an AI to call?** REST has been the dominant API shape for a long time. That's a historical fact, not evidence that REST is what an LLM wants. MCP is one candidate. Command-line interfaces are having a real moment too — the old Unix philosophy of small, chainable, self-documenting tools might have had it right all along [?] — and an LLM never has to leave that environment to figure out what to do next, which suits how these models actually work. I don't think we know the answer yet. My honest guess is that MCP is an interesting start, not the final form.

**REST's core assumption doesn't hold for LLMs.** REST wants everything modular: give the developer the building blocks (resources, verbs) and trust them to combine those blocks into whatever they need. That's a reasonable bet on a human developer who can read docs, reason through edge cases, and course-correct. It's a worse bet on an LLM. Every decision point you hand an LLM — every place it has to choose which combination of calls to make — is a place it can get it wrong. CRUD is still the floor: create, read, update, delete for every resource you store, otherwise nothing works programmatically at all. But CRUD alone leaves too much interpretation to the model. The more useful move, and the one MCP already nudges toward, is dedicated, action-oriented endpoints that collapse a multi-step sequence into one call an LLM can make with a much smaller chance of getting it wrong — the same instinct as building a page to guide a human toward the right sequence of clicks, just aimed at a model instead of a person.

None of this means throwing out what we know. We've been building APIs for SaaS products for decades, and most of those lessons still apply. The primary interface for a growing share of your users is going to be an LLM talking to your APIs on their behalf. Design for that caller specifically. Don't just assume the old defaults still fit.

## How to actually use the lens (the part you steal)

When evaluating *any* software — a vendor, an internal tool, a new product, your own architecture — ask these questions per layer:

| Layer          | The question                                                              | What "good" looks like                                                  |
| -------------- | ------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Data           | Whose data model is this? Mine, theirs, or shared? Can I export it cleanly? | Clear schema, easy export, I own my records                             |
| Logic          | Where does the business logic live? Vendor's code, my config, or my code?  | Logic I customize lives in *my* layer; vendor's logic stays vendor's     |
| Interface      | What surfaces does it expose? UI only, or also APIs/webhooks/MCP/agents?   | Multiple surfaces — UI for humans, APIs for composition, events for reactivity |
| Infrastructure | What am I outsourcing — and what am I locked into?                         | Standard primitives (auth, storage, compute) that I could swap if needed |

A few patterns this lens makes obvious:

- **"It's just X"** complaints (e.g. "Gong is just speech-to-text") are usually collapsing 3 layers into 1. The product is the *combination*, not any single layer.
- **Vendor lock-in** is almost always at the data layer. If you can't get your data out, the other layers don't matter.
- **The layer where you put your own logic** is where your competitive advantage lives. Outsource the others.
- **LLMs make the interface layer cheap** — and the data and CRUD layers nearly free. That's why so many apps suddenly feel "rebuildable." But the *opinionated* logic and (especially) the *infrastructure* layers haven't gotten cheaper at the same rate, which is why the rebuilt version so often works for one person and falls over for a team.
- **The interface layer is quietly splitting in two** — a human-facing UI and a machine-facing API/tool surface — and for a growing share of products the second one is becoming primary, not secondary.
- **When the caller becomes an agent instead of a human, "being chosen" becomes part of interface design.** A human stuck with a bad UI still has to use your product if it's the one their company bought. An agent doesn't have that loyalty — it can route around you. Legibility to the caller is now a competitive feature, not a technical nicety.

## Worked example: where does Replit actually fit?

Replit is a great test case because on the surface it touches *all four layers* — and that's exactly why people get confused about whether it's the right tool. Run it through the lens:

| Layer          | Replit's offer                                                                       | Strength    |
| -------------- | ------------------------------------------------------------------------------------ | ----------- |
| Data           | Replit DB, Postgres integrations (Neon, Replit Postgres), object storage             | **Strong** — standard, portable primitives |
| Logic          | Whatever code you (or Replit Agent) write. *No pre-built business logic.*           | **Weak** — you're responsible for every line of it |
| Interface      | Web hosting, custom domains, scaffolded Next.js/Express/Flask UIs, auth UI templates | **Strong** — the part Agent really shines on |
| Infrastructure | Hosting, deploys, env vars, secrets, scheduled jobs, reserved VMs                    | **Strong** — opinionated but solid |

**The pattern this reveals:** Replit is a *3-of-4* product. It's powerful at data primitives, interface scaffolding, and infrastructure — and it's *deliberately empty* at the logic layer. You bring the logic. That's not a flaw, it's the product.

### When Replit is the right tool

Reach for it when **the logic is small, bespoke, or you genuinely don't want any vendor's opinion baked in.** Internal tools, prototypes, single-purpose dashboards, side projects, anything where "I just want to wire some APIs together with a UI" is the actual job. The logic layer being empty is a feature here — you're not fighting anyone else's idea of how the workflow should go.

### When Replit is the wrong tool

Reach for something else when **someone else has already solved your logic layer and you'd be rebuilding it badly.** Examples:

- Building "internal Linear" instead of using Linear → you're rebuilding their logic layer (issue states, sprint mechanics, search ranking) for no reason
- Building "internal CRM" instead of using HubSpot → same problem; pipeline logic is genuinely complex and someone else has years of edge cases solved
- Building "our own Gong" → speech-to-text is the easy part; the calendar logic, escape hatches, and multiplayer workflows are the *actual* product

The give-away question: **"Is the logic I need to build the differentiating part of my work, or is it commodity logic that already exists somewhere?"** If the latter, Replit is a trap. You'll spend months recreating someone else's product and end up with a worse version that nobody else maintains.

## Counter-example: Airtable growing into the logic layer

The lens isn't static — products *move* across it over time. Airtable is the cleanest example.

**Airtable circa 2018** was a 3-of-4 product:

| Layer          | Airtable's offer                          |
| -------------- | ------------------------------------------ |
| Data           | Strong — flexible schema, easy to model   |
| Logic          | **Weak** — you got an API, but the logic ran on *your* servers |
| Interface      | Strong — grid/kanban/gallery/form views   |
| Infrastructure | Strong — hosted, no ops needed            |

The API was technically a logic surface — you could build any workflow you wanted on top — but you had to host it. That meant every meaningful Airtable extension required an engineer with a server. This is the exact single-player-vs-multiplayer trap from earlier, in vendor form: the API gave you somewhere to put logic, but the *infrastructure* burden of running it landed back on you, so most non-engineering teams couldn't use it in any sustainable way.

**Then Scripting Block, Automations, and Extensions launched.** Airtable absorbed the logic layer. Suddenly you could write JavaScript that ran *inside* Airtable, triggered by record changes or button clicks, with no hosting on your side. Custom logic became composable by anyone who could write a few lines of code — no DevOps, no auth glue, no uptime to manage.

That single change moved Airtable from 3-of-4 to 4-of-4 and unlocked a vastly larger user population. The data was already there. The interface was already there. What was missing was a place to put the *opinionated workflow logic* without hiring an engineer to host it.

There are still limits — execution time caps, no long-running jobs, no real persistent state outside Airtable itself — but those are constraints inside a coherent layer, not a missing layer.

### The pattern

Watch for this move whenever a vendor adds **hosted logic** (scripting, automations, agents-with-execution, "actions"). It almost always corresponds to:
- A jump in adoption, especially with non-engineering teams
- A new wave of templates and ecosystem activity
- A re-framing of the build-vs-buy question for users *currently* using the tool
- An expansion of who counts as a "builder" in that ecosystem

LLM agents inside SaaS tools are the current version of this. Same pattern, new substrate — and note *which* layer they're absorbing: the hosted-logic layer, the one that's hardest to stand up yourself.

## The deeper takeaway

The four-layer lens is most powerful as a *dynamic* tool, not a static one:

1. **For evaluation** — where does this tool sit across the four layers *today*?
2. **For trajectory** — which layers are they trying to absorb next, and what unlocks if they succeed?
3. **For your own architecture** — which layers do you own, which do you outsource, and is that mix still right as the tools beneath you absorb new layers?
4. **For "can I just rebuild it?"** — which layers would you actually have to recreate, and is the hard one (opinionated logic, multiplayer infrastructure) the one Claude is *weakest* at? Usually, yes.
5. **For "who's actually calling this?"** — is your primary caller still a human on a browser, or is it increasingly an agent hitting your APIs? If it's shifting toward the latter, your interface investment needs to shift with it, and so does your answer to a harder question: does that agent choose you, and does anyone notice if it didn't?

The "vibe-code your own tool" platforms (Replit, Bolt, v0, Lovable, etc) are 3-of-4 with empty logic — they hand you the other three and let you write whatever logic you want. That fits when your logic is small and bespoke. It traps you when commodity logic already exists elsewhere, deeper.

Mature SaaS tools are usually 4-of-4 — but the logic layer's *flexibility* varies enormously. A good logic layer (Airtable's scripting, Notion's databases-as-code, Linear's API+webhooks combo) lets users compose. A weak one (rigid no-code workflows, "configure this dropdown" logic) ships fast but limits where the tool can go.

Pick the right shape for the job, and watch how the tools you depend on are reshaping themselves underneath you — including, now, which layer they expect a machine rather than a human to be calling, and whether that machine has any reason to keep calling you.

## What to flesh out in future recordings

- A second worked example using a more traditional SaaS (Gong or Salesforce) so the lens isn't only demonstrated against build-it-yourself platforms
- Counter-cases: apps where the layers are deliberately fused (e.g. notebooks, IDEs) and the lens needs adjusting
- A specific Replit-was-wrong story (the writing-pipeline thread is one — log how that conclusion was reached, ideally as a concrete single-player-that-needed-to-be-multiplayer failure)
- Tighten the "where AI fits per layer" breakdown into a standalone graphic/table — the rant version is in, but it could be its own steal-this artifact
- The open question flagged in "Where AI actually sits" — REST vs. MCP vs. CLI as the right interface for an AI caller — deserves its own full treatment rather than a paragraph here; revisit once there's a clearer point of view
- What the UI-as-control-plane actually looks like in practice — a concrete example of an app that's already built this well (or badly) would sharpen that section a lot
- The "tool of choice" idea (how you get an agent to pick you over a competitor, and how a user even notices) is currently one paragraph — it deserves its own worked example, maybe a concrete before/after of an API that's legible to an agent vs. one that isn't
- Companion piece: `build-vs-buy-llm-era` — this lens is the prerequisite for that decision
- Companion piece: `llm-apps-personalize-saas` — LLMs as a new interface layer over existing data + logic
- Companion piece: `breadth-of-features-is-a-liability` — feature breadth usually means a wider interface layer, not a deeper logic layer
- Companion piece: `apis-as-the-new-frontend` — the shift from API-as-escape-hatch to API-as-first-party-surface, and what "designed for an LLM caller" actually means in practice
