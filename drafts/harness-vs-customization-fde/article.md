---
title: "Are You an FDE or Just a Production Engineer With People Skills?"
slug: harness-vs-customization-fde
status: raw
target: ghost
created: 2026-07-06
updated: 2026-07-06
tags: [forward-deployed-engineering, engineering-org, ai-agents]
visibility: public
point: >
  Forward deployed engineering is implementation engineering under a new name, and the
  cleanest way to tell which one you're actually doing is to ask who builds the harness
  (the core agent infrastructure) versus who builds customization on top of it. If you're
  building the harness, you're a production engineer, whatever your title says. The second
  test is who owns hard problems that are core to the business: if the answer isn't "we hire
  enough people to do it," the problem has to be solved in software, not handed to your
  existing team because AI made them faster.
---

One of the more clarifying questions in forward deployed engineering is also the simplest: who is building the harness, and who is building the customizations and deployments on top of that harness?

If you strip away the AI jargon, this isn't a new framework. Every product has a core and a last mile: the core infrastructure, and the delivery and customization layer that makes that infrastructure usable for a specific customer. Forward deployed engineering is just implementation engineering wearing a new name, and the harness question is the fastest way to find out which side of that line you're actually standing on.

If you, as the FDE, are being asked to build the harness itself, the agent infrastructure your customers interact with, you are being asked to be a production engineer. You are building the core product. You are not doing last-mile customization. That's not a bad thing to be asked to do, but it's a different job, and the technical bar is much higher than most people expect walking into an FDE role.

In theory, with Claude or any capable coding agent, I could contribute to that production-level infrastructure. The real question is whether I should. Am I the best person to be doing that, or am I better used building increasingly sophisticated last-mile features that make the product richer for the customers in front of me? For me, it's the latter. So the first axis is: am I building the harness, or am I building on top of it?

## Where the line actually shows up

I don't have a fully settled framework for this yet, it's evolving fast, but three areas keep showing up as reliable signal.

**Prompt engineering.** A lot of the "harness vs. customization" question shows up as: how do you encode instructions in a way your company's agents will actually understand? There's real corporate and industry jargon baked into these systems that a new user won't have. Take Airtable Omni. Put me next to someone who's never used Airtable, and I'll get better results in fewer prompts, not because I'm smarter, but because I understand the underlying system and the context it was probably trained on. That gap is exactly where FDE work lives: encoding institutional knowledge into prompts so customers don't have to already know it.

**Experimentation, the art of the possible.** This might be the single biggest differentiator. When I talk to peers, I'm consistently surprised by how little people realize is already possible with the tools they have. Take PR review. If your process has automated tests, branch rules, rebase requirements, all reasonable guardrails, it also creates a lot of start-stop friction. You submit a PR, wait for tests, get flagged as behind, don't notice, and the thing sits in limbo. A test that passed locally fails in CI, and nobody looks at the PR until everything's green.

None of that has to be manual. You can build something that watches GitHub status and takes the next action when an event fires: tags the right reviewer, reruns the check, nudges the branch. I automated a lot of my own PR workflow this way, entirely locally, on skills in my own environment, and it meaningfully cut the time between submitting a PR and getting it approved. It also let me hold more PRs in flight at once, because I was doing less context-juggling myself.

That's a small example, but it's the pattern: prototyping and pushing the bounds of what your agents can do out of the box is squarely FDE work. Your core engineering team, focused on shipping the roadmap, mostly won't have the slack to do this kind of exploration. If nobody on your team is doing it, that's worth noticing.

**Skills and MCP tools.** There's still a lot of real custom code to write here, but it's worth being precise about what kind. Skills are mostly prompt engineering plus lightweight scripting, encoding specific customer context, and then testing to make sure the skill delivers consistent results. Same logic applies to MCP tools: if you're being asked to stand up the MCP server itself, you're doing production engineering. If you're adding tools into an existing MCP server that standardize how certain actions get taken, that's forward deployed work.

There's a nuance inside that one too. You don't want to build a bespoke tool per customer forever. Deciding when a one-off tool graduates into the standard tool repository, available to everyone, is itself a production engineering call.

> [!tip] Three questions to find out what you actually are
> If you're trying to figure out whether your role (or your team) is really forward deployed engineering or production engineering with a customer-facing coat of paint, ask:
> - Where does prompt engineering fit into my day-to-day work?
> - Where does experimentation, art-of-the-possible work, fit in?
> - Where does skill development or MCP tool deployment fit in?
>
> If the honest answer is "unclear," or keeps gravitating toward building sustainable core infrastructure, that's a signal you've been pulled into a traditional engineering role with customer-facing responsibilities layered on top. That's not automatically a problem, but it's a much higher technical bar, and not everyone signed up for that job.

## The second axis: software or people

There's a fuzzier question underneath all of this: for a given hard problem, do you want software to manage it, or do you want people to manage it?

It's tempting for organizations to default to "forward deployed engineering should just go handle it." This is an old story: implementation teams get told to just build it for the customer, because it doesn't hit the roadmap and doesn't require an expensive planning cycle. It's assumed the scrappy implementation team will figure it out.

The question you actually need to answer is how core the problem is to your value proposition. If it's genuinely core, then the follow-up is: are you willing to hire a small army of people to manage it? If not, it has to be solved in software, or it doesn't get solved. If you decide it's core and you are willing to hire that army, fine, accept the cost and move on.

Where this goes wrong is when a team decides a problem is core, recognizes that building software for it is still hard even with faster tools, and then quietly assumes that since everyone's individual technical skills have gone up, they can just hand the problem to existing employees and tell them to figure it out. That produces fragile, hard-to-manage systems, because the amount of infrastructure required to actually own a core problem is usually far more than a repurposed team without dedicated infrastructure ownership can build.

Support is a good example of a problem that's changed shape recently. Every company has some version of "we have to do support," but very different views on whether top-tier support is a market differentiator. Historically the answer was: hire a small army, get them increasingly efficient at ticket volume, and accept that as a fixed cost. Now it's technically possible to build automated systems that handle a meaningful share of that volume, but that's a decision to invest in core infrastructure, not a reason to tell your existing support team "you have Claude now, go automate yourselves."

Airtable is a good parallel here too. For a long time, the answer to "how do people learn to build applications on our platform" was bodies on the ground, walking customers through it. The shift happening now, and probably true across a lot of tooling right now, is that the entry point itself should mostly be solved by the product: better UX, or a headless interface where a user states the outcome they want and the system delivers it. That's a different model than adding more implementation headcount, and it's the model worth pressure-testing against any problem you've decided is critical.

The mistake is thinking you can shrink a team and ask the remainder to build and maintain that infrastructure on the side, because they're personally more efficient now. The infrastructure required to do this well is usually much bigger than people expect, and building it is a full commitment, not a side project for a smaller team.

Which is really the same conclusion as the first axis, just from a different direction: if your core engineering team is incapable of building the infrastructure a problem actually requires, you have the wrong core engineering team. Not the wrong FDE team.
