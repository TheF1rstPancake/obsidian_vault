---
title: "Data, Logic, Interface, Infrastructure: a four-layer lens for any software app"
slug: decomposing-software-apps
status: raw
target: substack
created: 2026-05-09
updated: 2026-05-09
tags: [software, frameworks, mental-models]
---

# Data, Logic, Interface, Infrastructure: a four-layer lens for any software app

> Stub. Seed thoughts captured 2026-05-09. Awaiting voice recordings to flesh out.

## The thesis

Most arguments about software — "should we build it?", "is this product good?", "what does this tool actually do?" — get muddier than they need to be because people compare apps at the wrong level. One person is talking about the UI, another about the data model, a third about the deployment story. They're all right, and they're all talking past each other.

A simple lens that cuts through this: **every software app is some combination of four layers — Data, Logic, Interface — wrapped in Infrastructure.** Once you can articulate where a tool sits across those four, evaluation gets a lot less hand-wavy.

## The four layers

**Data layer** — what the system stores and how it's structured. Schemas, entities, relationships, persistence. The "nouns" of the app.

**Logic layer** — what the system does with the data. Business rules, workflows, computations, decisions. The "verbs."

**Interface layer** — how humans (or other systems) interact with the logic and data. UI, APIs, CLIs, webhooks, agents. The surface area.

**Infrastructure** — wraps all three. Hosting, identity, networking, observability, deploys, security boundaries. The plumbing that lets the other three run reliably.

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
- **LLMs make the interface layer cheap.** That's why so many apps suddenly feel "rebuildable" — but the data and logic layers haven't gotten cheaper at the same rate.

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
| -------------- | ----------------------------------------- |
| Data           | Strong — flexible schema, easy to model   |
| Logic          | **Weak** — you got an API, but the logic ran on *your* servers |
| Interface      | Strong — grid/kanban/gallery/form views   |
| Infrastructure | Strong — hosted, no ops needed            |

The API was technically a logic surface — you could build any workflow you wanted on top — but you had to host it. That meant every meaningful Airtable extension required an engineer with a server. Most non-engineering teams couldn't actually use the API in any sustainable way.

**Then Scripting Block, Automations, and Extensions launched.** Airtable absorbed the logic layer. Suddenly you could write JavaScript that ran *inside* Airtable, triggered by record changes or button clicks, with no hosting on your side. Custom logic became composable by anyone who could write a few lines of code — no DevOps, no auth glue, no uptime to manage.

That single change moved Airtable from 3-of-4 to 4-of-4 and unlocked a vastly larger user population. The data was already there. The interface was already there. What was missing was a place to put the *opinionated workflow logic* without hiring an engineer to host it.

There are still limits — execution time caps, no long-running jobs, no real persistent state outside Airtable itself — but those are constraints inside a coherent layer, not a missing layer.

### The pattern

Watch for this move whenever a vendor adds **hosted logic** (scripting, automations, agents-with-execution, "actions"). It almost always corresponds to:
- A jump in adoption, especially with non-engineering teams
- A new wave of templates and ecosystem activity
- A re-framing of the build-vs-buy question for users *currently* using the tool
- An expansion of who counts as a "builder" in that ecosystem

LLM agents inside SaaS tools are the current version of this. Same pattern, new substrate.

## The deeper takeaway

The four-layer lens is most powerful as a *dynamic* tool, not a static one:

1. **For evaluation** — where does this tool sit across the four layers *today*?
2. **For trajectory** — which layers are they trying to absorb next, and what unlocks if they succeed?
3. **For your own architecture** — which layers do you own, which do you outsource, and is that mix still right as the tools beneath you absorb new layers?

The "vibe-code your own tool" platforms (Replit, Bolt, v0, Lovable, etc) are 3-of-4 with empty logic — they hand you the other three and let you write whatever logic you want. That fits when your logic is small and bespoke. It traps you when commodity logic already exists elsewhere, deeper.

Mature SaaS tools are usually 4-of-4 — but the logic layer's *flexibility* varies enormously. A good logic layer (Airtable's scripting, Notion's databases-as-code, Linear's API+webhooks combo) lets users compose. A weak one (rigid no-code workflows, "configure this dropdown" logic) ships fast but limits where the tool can go.

Pick the right shape for the job, and watch how the tools you depend on are reshaping themselves underneath you.

## What to flesh out in future recordings

- A second worked example using a more traditional SaaS (Gong or Salesforce) so the lens isn't only demonstrated against build-it-yourself platforms
- The "where does AI fit?" angle — LLMs touch each layer differently (interface biggest, logic medium, data smallest)
- Counter-cases: apps where the layers are deliberately fused (e.g. notebooks, IDEs) and the lens needs adjusting
- A specific Replit-was-wrong story (the writing-pipeline thread is one — log how that conclusion was reached)
- Companion piece: `build-vs-buy-llm-era` — this lens is the prerequisite for that decision
- Companion piece: `llm-apps-personalize-saas` — LLMs as a new interface layer over existing data + logic
- Companion piece: `breadth-of-features-is-a-liability` — feature breadth usually means a wider interface layer, not a deeper logic layer
