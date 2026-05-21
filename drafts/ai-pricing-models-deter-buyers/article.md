---
title: "Your AI Pricing Model Is Scaring Off the Buyers You Need"
slug: ai-pricing-models-deter-buyers
status: raw
target: substack
created: 2026-05-21
updated: 2026-05-21
tags: [ai, pricing, saas, go-to-market]
substack_url:
---

There's a theme I keep coming back to: if you're not the tool people pick, you're whatever tool they can get up and running first — not necessarily the one that's best for the job. And right now, pricing is one of the biggest things keeping people from even getting to the "try it" step with AI products.

## The conversation everyone's having

The CEO of Pylon recently posted on LinkedIn about how nobody has figured out their AI cost model. Is it usage-based? Per seat? Per outcome? Who decides what counts as an outcome? It's all over the place, and that's true.

But the conversation has been framed almost entirely around the vendor: *how do I as a business price this in a way that makes sense for me?* The customer has been cut out of that conversation almost entirely.

## Price as a barrier to entry

If you think of price as one of the barriers to entry for why someone will choose your product, an unintelligible pricing model is one of the single biggest deterrents to someone even exploring your tool. If a buyer can't rationalize what they'll spend, they won't pick you — they'll go pick someone else. You can have everything else right, and they will never explore it. Even a generous free tier doesn't fix this, because nobody wants to invest time into something they think they'll have to rip out later when the bill lands.

## "But the numbers look great"

A lot of AI companies are posting big headline numbers — total customers, total payments, total revenue. And those numbers are probably real. AI products are ubiquitous right now, and the pool of potential users is so large that you can throw a rock and hit someone willing to try the thing.

The question is whether that growth is durable. I don't think it is. Today's adopters are people who know how to successfully navigate AI spend conversations internally — they say "we're adding agentic AI capabilities to X" and someone in finance says "wow, cool, do it." That window closes. Budgets tighten. And the moment cold outbound starts replacing PLG, price sensitivity shows up as the reason deals stall.

We saw exactly this at [?] — Airtable changed its pricing several times, and as the PLG motion thinned out, price sensitivity became a real reason people wouldn't even try the freemium tier. The lower tier didn't have the features they wanted, and they didn't want to commit to (or couldn't rationalize) the long-term cost of the enterprise offering.

## Per-token pricing is a trap for the buyer

Per-token pricing is uniquely bad for buyer confidence:

- **You can't estimate it up front.** Until you've actually run a workflow and watched it spend, you have no idea what a workflow costs.
- **The buyer can see your margin.** Most people already understand what a token costs from the AI provider directly. So they can see exactly what premium you're charging on top — and immediately ask, "is that premium worth it?"
- **It moves under you.** A new model drops, your token math changes, your price changes. There's too much variability to control or predict.

Compare that to compute-time billing, which is how Cursor prices its cloud agents. Engineering teams *get* compute time — that's how AWS has priced things forever. You can reason about a worst case (this runs 24/7), a best case, an average case. There's a mental model.

Per token has none of that.

## When a flat-fee tool quietly becomes metered: the Claude Code change

Anthropic recently changed how Claude Code [?] (I think it's the Claude-P [?] tier specifically — worth pulling other articles to confirm) counts against API usage. I think they're going to regret it, and it's a clean example of everything above playing out in real time.

The reason the fixed $100/month Claude Code plan is *so* nice is that you know what you're going to pay. Plenty of people exceed the $20 tier. Far fewer exceed the $100 one. I use Claude a ton — professionally and personally — and even on my personal account, doing custom projects, I'm nowhere near the $100 ceiling.

So something I catch myself wanting to do constantly is use Claude Code as the intelligent layer behind little custom apps I'm building for myself. I'm already paying the $100. Running Claude through the command line and piping output out of it was a way to keep using Anthropic — to stay in their ecosystem — without stacking API costs on top of a subscription I wasn't even maxing out.

Now those calls start counting. My bill stops being $100. It's $100 plus the interstitial usage. And the second that happens, I start looking at other tools.

Claude Code has been winning on intelligence. But intelligence is commoditizing. It's not a strong enough moat to hold people through a pricing change that *adds* anxiety to something that used to feel safe. So this will push me — and I'd guess plenty of others — to look elsewhere. Codex picks up share. Will Codex eventually make the same move? Probably. But in the meantime there's a real window. Cursor too: for $20/month their usage is permissive, the CLI is included, and they're not nickel-and-diming the side-channel uses.

Anthropic is making so much money right now that the churn probably looks acceptable internally. But it's another barrier to entry on a product whose addressable market is way bigger than just engineers. None of these AI tools have captured their market — the universe of potential users is enormous if you believe non-engineers can use this stuff too. Pricing changes that quietly turn predictable subscriptions into metered ones work directly against that expansion.

It's the same pattern as the rest of this piece: the vendor optimized for vendor economics and didn't ask what the change does to buyer confidence.

## The build-vs-buy conversation has shifted

People say the build-vs-buy debate is overworked right now. Maybe. But something real has changed underneath it.

The whole reason you pay for SaaS is to avoid building expertise in something that isn't your core competency, and to avoid maintaining it as the market moves. That's the deal. LLM coding agents have made building targeted, custom features dramatically cheaper. So when a buyer looks at your tool and thinks, *I only need three of these features* — building those three things themselves now feels viable. They're already paying for the coding agent.

So when your pricing layers a platform fee *and* a token premium on top of that, the dissonance gets loud: "Why would I pay you the overhead when I can build the slice I actually need?"

## What actually works

The classic per-seat flat model still works, partly because we've trained the market on it, but mostly because users can rationalize it. "For $40/month I get access to these things, which unlock these workflows, which let me build this for the business." Done.

This also works once you accept that not everyone in the org will actually build in the tool — just because everyone *can* doesn't mean everyone *will*. Citizen developers, operators, internal-tool builders — that's the real audience for a lot of these platforms.

Gumloop's model is the best I've seen in this space. It's effectively a platform fee: $X/month gets you Y credits which gets you roughly Z workflows. And — crucially — **bring your own key**. The most variable, scariest part of the cost (the AI spend) gets offloaded onto infrastructure the buyer's org already pays for and already monitors.

That matters because most orgs at this point have an OpenAI, Gemini, or Anthropic account. They've picked one or two providers, and they're willing to issue keys to people with a good use case. BYOK piggybacks on a budget conversation that's already been won. It dissolves the token anxiety.

So you look at Gumloop and you go: *for forty bucks a month I can build dozens of workflows across my team, I don't have to bug engineering every time I want to change agent behavior, and I'm not on the hook for runaway token spend.* That is a real unlock in willingness to even explore the product. Pair it with a free tier generous enough that you can actually run your workflows on it — long enough to know roughly what your real-world spend will look like before you upgrade — and you've removed almost every reason to say no.

Tools whose free tier doesn't give you enough credits to actually see the cost shape of your workflow are betting on something brutal: that you get to a V0, it's *almost* working, and you'll pay to push it over the line. That's a death move. What actually happens is "I got kind of close, I learned some stuff, now let me pour this work into a tool with a more forgiving pricing model."

## The outcome-based version of the same problem

Finn's outcome-based pricing — roughly a dollar per resolved ticket — has the same defect dressed differently. In the abstract it sounds fair. In practice, an early-stage buyer can't size it. They don't know how many tickets they'll resolve. They just see a path to suddenly owing $100K+/year, and a voice in their head asking: *could Pylon have done this? Could Plain? Could a traditional chatbot? Do I really need to pay this premium?*

That doubt at the decision-making stage is exactly what you don't want with an early buyer.

## The real argument

Right now this is a land grab. The winners will be whoever gets the most users locked in and building the earliest, because migrations are painful — people only switch when there's a security incident that makes the vendor untenable, or when the cost stops being justified by the benefit.

If you want to capture users at this stage, your pricing model cannot make people fearful of the long-term cost. That's the whole job. And it's not just the initial pricing model — it's every change you make to it afterward. The Claude Code shift is the cautionary tale: a predictable subscription that quietly becomes metered is the same betrayal of buyer confidence as an unintelligible price tag on day one. Both push people to look at what else is out there.

Otherwise they won't even sign up — or they'll leave the second the math stops feeling safe — and all the clever per-token, per-outcome, per-whatever math in the world won't matter, because the deal died before it started.

The conversation about AI pricing has been about what makes sense for the vendor. The conversation that's missing is whether your pricing is letting buyers in the door — and keeping them there — at all.
