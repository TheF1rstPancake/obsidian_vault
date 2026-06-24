---
title: "The Future of Startups Is API Companies"
slug: future-of-startups-api-companies
status: raw
target: substack
created: 2026-06-15
updated: 2026-06-24
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

The biggest piece of this is the move toward what people are calling the *headless* experience. Every action you could take in a — and it's wild that we're already saying this — *legacy* web app, you can now take through an AI agent.

So the way you take action changes. It's not "I go click around a web browser." I don't need to learn all the nuanced mechanics of some SaaS tool. I authenticate with my AI agent of choice and let it go take the action for me.

And in many ways, I no longer care about the things we used to obsess over. User experience. How many clicks it takes. How annoying a task is to accomplish — because I'm not the one doing it. I speak declaratively to my agent and it goes and does the thing. It deals with the nuance: "it would be nice if this were one API call, but I actually have to make three." Unless you're really watching the logs, that's invisible to you now. You don't have to care.

What we're really doing is going back to the primary way people will engage with technology companies: through APIs. We build abstraction layers on top of problems people care about solving but don't have the specialization to do well themselves — and *especially* not well for a broader team.

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
