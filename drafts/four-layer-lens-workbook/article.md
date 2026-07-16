---
title: "Using the four-layer lens: scorecard, Replit, and Airtable"
slug: four-layer-lens-workbook
status: raw
target: ghost
created: 2026-07-16
updated: 2026-07-16
tags: [software, frameworks, build-vs-buy, how-to]
related: ["decomposing-software-apps"]
point: >
  Once you have Data / Logic / Interface / Infrastructure as a shared map,
  evaluate any tool with a per-layer scorecard, then watch products move across
  layers over time. Replit is deliberately empty at logic; Airtable grew by
  absorbing hosted logic — and that trajectory is usually where build-vs-buy
  actually flips.
---

# Using the four-layer lens: scorecard, Replit, and Airtable

*Companion to the four-layer lens essay. That piece argues why arguments about software go wrong when people compare apps at different layers. This one is the how-to: a scorecard you can run, a Replit worked example, and an Airtable trajectory counter-example.*

## How to actually use the lens

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

The API was technically a logic surface — you could build any workflow you wanted on top — but you had to host it. That meant every meaningful Airtable extension required an engineer with a server. This is the exact single-player-vs-multiplayer trap from the lens essay, in vendor form: the API gave you somewhere to put logic, but the *infrastructure* burden of running it landed back on you, so most non-engineering teams couldn't use it in any sustainable way.

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

## When the caller is an agent

The lens essay stops at a short bridge: AI lives in the logic layer, and APIs become the front door once agents call you. The practical follow-through is worth spelling out here.

**You don't control the interface anymore.** Historically, for most users, the chain read *web interface → APIs → database*. For a growing share of users it now reads *LLM chat → APIs → database*. Same three layers, different middle experience for you as the builder — because the thing at the top of that chain used to be yours and now isn't.

A web interface is deterministic in the sense that matters here: you built it. You decide what renders, what the user can click, what path they're funneled down. Swap that page for an LLM chat and you control none of it. The user isn't choosing from buttons you laid out. They're talking to a system that decides, on its own, whether to call you at all, and if so, how.

That reframes the competitive question. It stops being just "is my API well-designed for an LLM caller" and becomes "does the LLM choose me over the alternative, and does the user even notice." Three things change once you take that seriously: how you build and surface the APIs you expose, how users actually engage with your product day to day, and how users come to understand the value they're getting from you at all. That third one is easy to underestimate. If a chatbot is quietly the thing fetching your data and running your logic on someone's behalf, the user may never see your brand, your UI, or your onboarding flow again. Being good is necessary but no longer sufficient — you also have to be legible enough, as an API, for an agent to pick you over a competitor, and the user has to be able to tell that the pick was the right one.

> [!note] So what happens to the UI?
> It doesn't disappear, but its job changes. If agents are the ones executing actions inside your product, someone still needs to see what happened — what the agent did, whether it was right, where to intervene if something's wrong. The UI's new job looks less like "the surface humans use to get work done" and more like a control plane for supervising what your AI is doing on your behalf. That's a genuinely open interface-design problem, not a solved one.

**What's the actual best interface for an AI to call?** REST has been the dominant API shape for a long time. That's a historical fact, not evidence that REST is what an LLM wants. MCP is one candidate. Command-line interfaces are having a real moment too — the old Unix philosophy of small, chainable, self-documenting tools might have had it right all along, and an LLM never has to leave that environment to figure out what to do next. I don't think we know the answer yet. My honest guess is that MCP is an interesting start, not the final form.

**REST's core assumption doesn't hold for LLMs.** REST wants everything modular: give the developer the building blocks (resources, verbs) and trust them to combine those blocks into whatever they need. That's a reasonable bet on a human developer who can read docs, reason through edge cases, and course-correct. It's a worse bet on an LLM. Every decision point you hand an LLM — every place it has to choose which combination of calls to make — is a place it can get it wrong. CRUD is still the floor. But CRUD alone leaves too much interpretation to the model. The more useful move, and the one MCP already nudges toward, is dedicated, action-oriented endpoints that collapse a multi-step sequence into one call an LLM can make with a much smaller chance of getting it wrong — the same instinct as building a page to guide a human toward the right sequence of clicks, just aimed at a model instead of a person.

None of this means throwing out what we know. We've been building APIs for SaaS products for decades, and most of those lessons still apply. The primary interface for a growing share of your users is going to be an LLM talking to your APIs on their behalf. Design for that caller specifically.

## Steal this

Run the scorecard on the next vendor or internal rebuild debate you walk into. If the argument collapses three layers into one ("it's just speech-to-text"), name the missing layers out loud. If someone is reaching for a 3-of-4 empty-logic platform to recreate commodity SaaS logic, ask the give-away question before the prototype starts. And if a vendor just shipped hosted scripting, automations, or agents-with-execution, treat that as a layer move — not a feature announcement.
