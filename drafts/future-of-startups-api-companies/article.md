---
title: "The Future of Startups Is API Companies"
slug: future-of-startups-api-companies
status: raw
target: substack
created: 2026-06-15
updated: 2026-06-15
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

## The thing you can't one-shot is multiplayer

Building software for yourself — hacking something together on your laptop — is something people have always done. The hard part has never been that. The hard part has always been: how do I make this collaborative? How do I make it multiplayer-friendly?

Even if you bootstrap your org down to a handful of people, you still have to consider that two of them might try to take action at the same time, and you need to resolve that state, or keep track of it.

In software engineering, this is just Git. Everything is file-based, it goes into Git, there are entire processes for resolving conflicts — and we have entire software companies built around the specialization of managing that problem.

Could you rebuild Git? Probably. Could you rebuild an internal version of GitHub that's just what you need and none of the bells and whistles? Probably. *Why would you?* That's the open question. Maybe at some point people do, to an extent. But building — or paying for — that specialization still feels worth it.

So what are we actually paying for? We're paying for the abstraction of complicated problems we *could* solve ourselves if we were willing to devote the time — but we don't want to. It becomes mostly a *want* thing. If our agents are technically capable, and building something like GitHub is well understood, there's no reason your agent couldn't rebuild it for you. But do you want to take on that specialization know-how? Probably not.

Could you rebuild Stripe? Maybe a very basic version, in not that much time. But there's a ton of legal and compliance baggage that's hard to abstract away — and that *is* a lot of what Stripe gives you. They've built that specialization into the payment layer. That's what you're paying them for.

> [!note] The pattern
> In every one of these cases the software is rebuildable. What isn't easily rebuildable is the specialization baked into it — conflict resolution, compliance, the accumulated judgment about edge cases. That's the moat, and it survives commoditized harnesses.

## SecurityPal: the service that's secretly an API

A fun one to look at is SecurityPal. (If you're not using them for security reviews — highly recommend.)

Break down a security review and it doesn't seem that complicated. You get a questionnaire, you read it, you know your posture and your answers, and you map the two together. It's a problem that's ripe for translating an external security review document into the knowledge and posture you already have.

But there's an incredible amount of nuance in doing it *right*. When are different certifications meaningful as answers? When can you get away with sort of subverting an answer a little — not in a slimy way, but because a questionnaire is often a blanket approach that may not be applicable to your business? How do you understand what's applicable and what's not?

If you're not a security expert, that level of specialization is hard. Yes, you could push Claude to build something — but how do you have the framework to evaluate whether it's doing the right job? You can't. You don't have the specialization context to judge it.

So what is SecurityPal, functionally? An API. You ship them an email, they ship you back a completed questionnaire, and the entire process behind how it gets filled out is a black box. Their internal teams have the agents, the harnesses, the setup to manage that complexity on your behalf. You pay them to deal with the specialization of *understanding how to answer a security questionnaire* — and it's no longer a web application as an implementation detail for dealing with user requirements.

## Business intelligence: a UI we mistook for the product

BI is another interesting one. Look at something like Hex, which is very headless-friendly — you can spin up entire reports, contexts, and shared queries without ever going into the application.

But how does a BI tool work without reports? We've all been trained to think business intelligence *is* reports and dashboards and pretty things you can slap on a slide. Break down the core user requirement, though. As a data analyst or operations person:

> I need to generate data-driven answers to important business questions, and ensure those answers can be shared and reused by others, so we're all working from a shared definition — reducing the back-and-forth and the misinformation that leads to bad judgments and outcomes.

Nowhere in that user story does it say *I need a UI*. We've historically used the UI as the way to meet that requirement. You build the dashboard. People with questions go to the dashboard. Someone who wants to reuse your query digs in and extracts the SQL. If you're lucky, your BI tool has shared queries, so a query can be referenced elsewhere and updates propagate — but even that's not table stakes everywhere.

Now think about how users request information. Increasingly it's *not* "let me go to the dashboard and look." I might still do that for a top-level summary, or if I want to drill and explore. But do I really want to be the one doing those actions? No — I want to hand that off to my agent.

So what are you paying a BI tool for at that point? You're paying for the shared, multiplayer data substrate: these are our queries, this is the context around them, this is how I manage them.

BI might actually be a special case, because — isn't that all just code files? It starts to look more like a software development problem: can I just rebuild this in Git, where the repo *is* our data hierarchy? Many BI tools already let you store things in Git and load them in.

> [!tip] What to actually charge for in BI
> Visualization generation is probably the commodity now — it's a well-understood problem, not a specialization. The defensible specializations are the multiplayer/governance layer:
> - **Shared context** — what are our queries and what surrounds them?
> - **Rules and permissions** — role-based access control; not all data should be visible to everyone, and that's very hard to do in a plain text-based Git setup.
> - **Source of truth** — how do you litigate it when different people have different answers, and combine them into a shared understanding?
> - **Repeatable delivery** — how do updates work? How do you get information reliably to people, not just solve the on-demand case? How do you manage connections to one or many databases when you *do* need something visual, on-brand, repeatable?

These are not trivial problems. But now I'm no longer constrained to going through a UI to learn all the nitty-gritty of how that UI wants to force me to solve them. I have APIs that something else can chain together to achieve my objective. That's a big paradigm shift in how users engage with your tools — but, crucially, *not* a big shift in how you build them.

## Building APIs is the well-understood part

Building APIs is well-understood practice. And because our AI friends learned from the internet, their sense of best practices is very similar to what your average developer would consider best practice for interacting with an API.

That'll shift, though. We're already seeing it: is it an API, or is it just command-line arguments? Are you making web requests, or issuing commands via CLI? The question becomes *what's more ergonomically friendly to the LLM* — not to the user.

No engineer would build an entire system on top of programmatic CLI calls. Under the hood it's web-based; the CLI calls are just issuing requests out to a web-bound API. But for the LLM, the CLI is friendlier. There's less overhead. It already has access to your terminal. It doesn't have to worry about which library to use to send the call, or how to capture errors — the terminal already wraps all of that up. So that interface alone is much more ergonomic for the agent. [?]

## So what does the startup of the future look like?

It looks a lot more like an API company. You build API surface areas that abstract away complicated problems — which is not new.

The UI becomes secondary. And where there *is* a UI, most of it is internally facing. When an agent is struggling, or requests aren't going the way you'd expect, the escalation and resolution path lives mostly within your internal team's control. So you build less and less customer-facing surface area.

The customer-facing surface is a chat window, where the customer gets to be declarative about what they want to accomplish. You have the APIs to surface those actions to them. And anything that *isn't* done programmatically — Stripe-style compliance, working with government agencies to keep everything above board, internal reporting on which security questionnaires are in the inbox and who has what — that's all internal. You manage it in a black box to your customer.

So the companies of the future look like **publicly facing APIs where the user experience is secondary, and internally there's a much bigger focus on operations** — arming your teams with the tools to manage the edge cases of the product.

And what you're paying for, in every one of these cases, is specialization. You're paying for someone to think about the edge cases. To take an idea from "it works on my machine" to "it works for my organization." That jump is still really hard.

The way we make that jump going forward will look both very different from what most people are used to — and very familiar to the companies that have been building APIs for programmatic access to their tools for a very long time.
