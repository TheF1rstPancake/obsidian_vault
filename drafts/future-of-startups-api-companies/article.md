---
title: "The Future of Startups Is API Companies"
slug: future-of-startups-api-companies
status: raw
target: ghost
created: 2026-06-15
updated: 2026-07-07
tags: [ai, startups, apis, agents, saas]
point: >
  When agent harnesses become commoditized and anyone can one-shot the
  software they need, the question isn't "what software do you build?" but
  "what specialization do you sell?" The startups of the future look like
  API companies: public-facing API surfaces that abstract away hard,
  edge-case-laden problems, a chat window as the customer interface, and
  most of the UI turned inward to arm internal teams. We're paying for
  specialization — taking something from "works on my machine" to "works
  for my organization" — and we'll buy it the way we've always bought
  programmatic access: through APIs.
---

I was wandering around my apartment with this idea and realized I hadn't recorded any of it. So here's the attempt to get it down.

Ben Stensel wrote a piece on his Substack about what the future of startups looks like in an AI world, and it got me thinking. His thesis, roughly: every major jump in technology produces a few behemoths — the household names — and then a fleet of smaller-but-still-meaningfully-large organizations that live underneath them.

You've got your Google, Microsoft, Amazon. But then think of all the SaaS tools underneath: Stripe, Intercom, Airtable. Real businesses, large businesses, that never reached full behemoth scale. In the AI world, the behemoths are Anthropic and OpenAI — and there's a whole layer of smaller organizations doing meaningful work beneath them.

But here's the question that keeps nagging at me. In a world where agent harnesses become commoditized — where anyone and everyone has a harness that can manage problems and build software very specific to their needs with little effort — what is the role of a software company?

If everyone has the harness, and you can build the software you need in one shot, why would you pay for a service *other* than the harness itself? And in that world, what does it even mean to be a startup? What can you show up and offer — some net-new, boots-on-the-ground thing — that people want to invest in and get on board with?

Nobody seems to have a great answer. At a minimum, it means we'll change how we evaluate the value of companies: based on whether they can survive this shift, or whether they're built on top of it. But I think there are trends we can already see that point at what the future looks like.

## We're going back to APIs

Strip any piece of software down and you get the same layer cake: a database, an API layer on top of it, a presentation or interface layer on top of that, and infrastructure wrapping the whole thing (infrastructure is its own rabbit hole — a place a lot of people struggle — but that's an aside for another time). Historically, the interface layer has gotten most of the attention, because it's what people actually see. You could have the cleanest database schema and the most elegant API in the world, and nobody gives a shit, because both exist in service of whatever application someone's staring at. Even the companies that are genuinely API-first — Stripe is the classic example — still ship an admin dashboard and prebuilt UI you can embed, because most users still engage with *something* visual.

So an entire discipline formed around that interface layer: how do you make it intuitive, how do you anticipate what people need, how do you build the systems and guardrails that guide someone toward the outcome they came for. And mostly, it's worked. But there's always been a tax sitting on top of it: the user has to look at their problem, look at your software, and morph their mental model into your application's model to get anything done. That's an invisible translation layer between what someone wants and how your software makes them ask for it — and it's the entire reason solutions engineering teams and implementation teams exist. Some users push through that translation easily. Those are your champion users — the ones who self-serve, understood the product, got on board, and became the advocates you point new customers toward. Most people aren't that. At Airtable we used to say just because anyone *could* use the platform doesn't mean everyone *would*. Over time that turned into something more precise: just because everyone can doesn't mean they'll be motivated to, or have the capacity to, do that translation themselves. Some people just aren't going to build the framework for turning their goals into your software's shape. That's not a character flaw. It's a real cost, and a lot of people don't want to pay it.

This is exactly what LLMs change. Users can speak outcomes, and the LLM does the translation for them. The part people get wrong is *how* it should do that translation. The lazy answer is: give Claude access to a browser, let it log in and click around your UI like a person would. Maybe there's some value in that for edge cases. But your interface was always backed by an API — the buttons in your UI are calling endpoints that do the actual work underneath — so the more direct path for an agent is the same one that was always there. The right interface for an LLM is programmatic, not visual.

None of this is actually new, either. Most SaaS products, even heavily UI-constrained ones, have offered some form of API access for years, and historically that access existed for two reasons. The first is bulk action: if someone needs to import or manipulate a lot of data at once, clicking through a UI one record at a time is a nonstarter, so you build an API to let them do it programmatically. The second is a more generic escape hatch. A customer shows up with some weird requirement that kind of fits your product and kind of doesn't, and the API lets you say "well, you could build that yourself" — classic objection handling, made with the quiet confidence that they probably won't actually go do it.

For a while we were drifting away from that. Products got smarter and more complete, and the pitch became "you shouldn't need the API, we've built everything into the app." Then everyone's application grew its own chat window, and now people are talking to a dozen different in-app agents at once — each one still just calling that same product's API underneath. Headless is really that same pattern with the interface moved outside any single application: the orchestrator is your LLM of choice, sitting in a terminal or a chat window instead of inside any one product, acting through APIs because that's what was always sitting underneath the UI. If your product isn't exposing an API — or at minimum MCP — it's not long for this world, because the thing showing up at your product's door increasingly isn't a person clicking through your onboarding flow. It's their agent, showing up to get a job done.

So the way you take action changes. It's not "I go click around a web browser." I don't need to learn all the nuanced mechanics of some SaaS tool. I authenticate with my AI agent of choice and let it go take the action for me.

And in many ways, I no longer care about the things we used to obsess over. User experience. How many clicks it takes. How annoying a task is to accomplish — because I'm not the one doing it. I speak declaratively to my agent and it goes and does the thing. It deals with the nuance: "it would be nice if this were one API call, but I actually have to make three." Unless you're really watching the logs, that's invisible to you now. You don't have to care.

What we're really doing is going back to the primary way people will engage with technology companies: through APIs. We build abstraction layers on top of problems people care about solving but don't have the specialization to do well themselves — and *especially* not well for a broader team.

## Your primary user is now an AI

That has a real consequence for how you build the API itself: the primary user of your application is no longer a human. It's an AI, acting on a human's behalf. That changes the calculus of API design in a way that mirrors the old UI design tension — it just moved down a layer.

Make your input structure too complex — too much required metadata, too many fields just to give the API enough context to trigger successfully — and you've handed the AI more surface area to get something wrong. Every extra piece of metadata you ask it to provide is another place for it to lose its grip and make a mistake. But constrain it too tightly and you limit how many ways the AI can combine calls to actually reach the outcome someone asked for. That's the same tradeoff UI designers have always made about anticipating user needs and putting the right buttons in the right place. It just lives in your API and CLI design now, because that's where the actual user is operating.

Two things end up mattering more than anything else. The first is documentation, with examples that actually run. One thing that used to drive me crazy: half the example payloads in our docs didn't work if you actually dropped them into staging. I spent an entire summer building a system that scraped our own doc pages, loaded the example payloads, ran them against a mocked environment, and flagged whichever ones failed so I could go fix them — because there's nothing more frustrating than prepping an example and having it not work. Now imagine an AI hitting that same broken example. It doesn't have the patience or the instinct a person has to poke around and guess what you *meant*. It just hits a wall and gets stuck.

Which is the second thing: error codes. Your API's ergonomics really come down to two questions — how quickly can someone get to a first successful call (how hard is authentication and setup), and how quickly can they resolve an error once they hit one. If your agent gets stuck in a loop because your error message is unclear and the next step is unclear, it can't course-correct. And what it reports back to the user is "yeah, this doesn't work" — even when it probably does work, if the agent had been given enough context to fix its own mistake. That's the worst outcome available to you, and it's a direct result of building error handling for a human patient enough to dig through your docs — when the thing actually hitting your API was never going to read them in the first place.

> [!tip] What API ergonomics means now
> - Keep input schemas as lean as the logic allows — every required field is another chance for the AI to get it wrong, but don't strip away so much flexibility that it can't combine calls to reach an outcome.
> - Test your own documentation examples against a real or mocked environment. If a human copy-pasting your docs hits a dead end, an AI hits the same one with none of the patience to work around it.
> - Judge your API by two numbers: time to first successful call, and time to resolve an error. The second one matters more than people think — an agent that can't self-correct just reports "doesn't work" back to the user, which is the worst outcome you can produce.

None of this is really new — it's the same discipline good API teams have always had. What's changed is the stakes. APIs used to be a secondary layer, an escape hatch for the handful of people who'd bother to use it. Now they're becoming the primary surface, because the user base is changing: it's not people anymore, or not only people. It's their AI, doing things on their behalf, and it needs everything a good API was always supposed to give a developer — just at a scale and speed no human integration ever asked for.

## You're paying for the harness, not the model

This connects to something I keep circling back to: what are you actually paying for? You're paying for specialization. And there's a real distinction emerging right now between paying for a *model* and paying for the *harness* around it.

Go back to the beginning. Why were Claude Code, Codex, and the other frontier-lab harnesses so popular? They were the first to build them — and build them well — on top of their own proprietary models. The two were tightly coupled. Buying into Claude meant buying into their harness *and* their models. And there was a real argument that the model helped: smarter models do better on highly complex tasks, and harnesses are complex. So you were paying for two specializations at once — the model provider's, and someone's understanding of how to take advantage of it.

But the battle is moving. Tools like OpenClaw, Hermes, Gumloop — bring-your-own-model, bring-your-own-keys. You pick the model you think is best for the task. Salesforce didn't buy Fin because Intercom had trained some uniquely good support model; they bought a harness that lets any organization build a robust support engine on top of *whatever* models are available. And the telling thing about Intercom is that the model is totally opaque — you have no idea what they're running, and you have no choice. They pick and choose to drive their costs, and that's fine, as long as it delivers the outcome you need.

The admission buried in all of this: the models themselves are replaceable. With the right harness, the right prompts, the right context and tools, most frontier models get you to a similar outcome. The path each takes might differ — you might prefer one model's choices over another's, more often than not — but the harness is what you're really paying for.

So why haven't the *generalized* harnesses won? If Hermes is a general-purpose agent that can do everything, its revenue should be booming — amassing users and revenue as a result. Instead there are a dozen legal AI startups and a dozen AI support harnesses, because when you limit the scope of what a harness has to handle, it performs significantly better, the setup is much easier, and a user can drop in and solve the one job they came to do. General-purpose frameworks still require a *lot* of setup.

But does that mean a future of 17 harnesses — one drifting toward each team — where we've traded yesterday's SaaS sprawl for tomorrow's agent-harness sprawl? That doesn't sound like a great place to live either, and it feels like a repeat of the past. [?] Either way, specialization is the thing to look for right now: does this tool give me something I'm not able to build out of the box myself?

## The thing you can't one-shot is multiplayer

Building software for yourself — hacking something together on your laptop — is something people have always done. The hard part has never been that. The hard part has always been: how do I make this collaborative? How do I make it multiplayer-friendly?

Even if you bootstrap your org down to a handful of people, you still have to consider that two of them might try to take action at the same time, and you need to resolve that state, or keep track of it.

In software engineering, this is just Git. Everything is file-based, it goes into Git, there are entire processes for resolving conflicts — and we have entire software companies built around the specialization of managing that problem.

Could you rebuild Git? Probably. Could you rebuild an internal version of GitHub that's just what you need and none of the bells and whistles? Probably. *Why would you?* That's the open question. Maybe at some point people do, to an extent. But building — or paying for — that specialization still feels worth it.

So what are we actually paying for? We're paying for the abstraction of complicated problems we *could* solve ourselves if we were willing to devote the time — but we don't want to. It becomes mostly a *want* thing. If our agents are technically capable, and building something like GitHub is well understood, there's no reason your agent couldn't rebuild it for you. But do you want to take on that specialization know-how? Probably not.

Could you rebuild Stripe? Maybe a very basic version, in not that much time. But there's a ton of legal and compliance baggage that's hard to abstract away — and that *is* a lot of what Stripe gives you. They've built that specialization into the payment layer. That's what you're paying them for.

> [!note] The pattern
> In every one of these cases the software is rebuildable. What isn't easily rebuildable is the specialization baked into it — conflict resolution, compliance, the accumulated judgment about edge cases. That's the moat, and it survives commoditized harnesses.

## "Why can't I just rebuild your product myself?"

There's a new move in software evaluations right now — buyers getting cute. *What's to prevent me from rebuilding your product in Claude Code for nothing?*

The honest answer: if you could, you would have.

Technical skill was never the only barrier. Motivation and prioritization are still enormous ones. Your technical toolbox has genuinely expanded — you've got an LLM coding agent at your disposal now — but an expanded toolbox doesn't mean you'll actually deploy successfully.

And apps built for a single user, in a vacuum, *are* easy. They always were. Citizen developers and shadow IT have existed forever — people with the technical know-how building one-off applications for themselves, or a very small group. You don't want to stop them; the things they go and do often unlock a lot of productivity and value for the organization. So we gave them a name, put them in a permanent corner, and said they were special.

The number of people who can do that is expanding. But building a *multiplayer, collaborative* system is a different animal. It requires a certain set of skills — infrastructure, deployment, maintenance, monitoring. And it requires a kind of skill we've badly overlooked: knowing which questions to ask, and knowing when you don't know the answer.

That's the part the LLM doesn't hand you. It's gotten remarkably good at letting you speak things into existence — but it'll also build you something overkill, or push you confidently in a direction you weren't comfortable with and shouldn't have gone. You can burn a ton of time watching it try to solve a problem when the fundamental question you asked was the wrong one. Everything goes back to LLMs being a force multiplier: ask the right things, and you're substantially more effective; ask the wrong things, and you just waste more time than you otherwise would have.
