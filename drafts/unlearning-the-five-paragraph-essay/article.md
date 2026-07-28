---
title: "Unlearning the five-paragraph essay"
slug: unlearning-the-five-paragraph-essay
status: shaping
target: ghost
created: 2026-05-22
updated: 2026-07-28
tags: [writing, communication, sales, careers]
visibility: public
related: ["three-section-internal-doc"]
point: >
  School trains you to litigate every objection before the conclusion. Business
  readers (and now LLMs summarizing for them) decide after the first sentence.
  If your default is "build to the conclusion," you lose attention before the
  opinion lands. Collapse internal docs to three short sections (problem,
  goals/non-goals, optional recommended solution), state the point first in
  each, and put the rest in a drawer. The companion piece walks through each
  section with a worked example. Aim to be reasonable and actionable, not
  unimpeachably correct.
ghost_url:
---

# Unlearning the five-paragraph essay

I'm classically trained in the five-paragraph essay. Intro, three body paragraphs that litigate every objection, conclusion. It served me well in school. It has been actively detrimental in sales, and in the promo packets and internal memos that were supposed to make the case for me, at every company I've worked at.

The five-paragraph essay assumes you have to litigate all objections *before* getting to the conclusion. In my experience, business readers move on the exact opposite assumption: give me the conclusion first, and if I want to litigate or object, *then* I'll read the rest. Most of the time, I won't. If an executive is deciding whether to keep reading your email, that decision is usually made by the first sentence. If a customer is deciding whether to open your follow-up, that decision is the subject line.

If your default writing posture is "build to the conclusion," you are losing readers, deals, and headcount fights to people whose default is "lead with the conclusion."

## Documents aren't dead. The audience changed

This is getting more relevant, not less, and the reason is AI. There's a live back-and-forth right now about whether document writing is even a meaningful practice in a world of LLMs and agents. My answer is an emphatic yes. But the "we don't do documents anymore" position is misread. The people saying it don't actually want to stop documenting things. They don't want to be responsible for *reviewing* them anymore.

That's a fair thing to be exhausted by. There's a lot of bad document writing out there: PRDs, product readiness docs, internal briefs, strategy memos. As the person consuming one, you're often sitting there wondering why the fuck you're reading it. What's the purpose? Why am I putting effort into something that's going to get thrown away? There's real scar tissue here. Airtable was a deeply doc-heavy culture. Everything lived in a document, everything got reviewed. And editing is far easier than creating. So as the writer trying to build alignment, you'd put a doc out and just get shit on. A wall of comments, no clear finish line. When is the doc done? When I've resolved every comment? When we've had a meeting about it? What's the point?

None of that means the document was the problem. The OpenClaw experiment made that obvious to me: almost the entire architecture comes down to updating a handful of documents over and over. That shared set of markdown files is what lets agents collaborate and take on increasingly complicated tasks. You have to have *some* way of holding a shared understanding of what's meaningful and what isn't. Documents are that mechanism, and they aren't going anywhere.

What's changed is the *primary audience*. People hear that and jump to dead-internet theory (robots writing documents for robots). But in most cases these documents are still consumed by people too. A PRD is where a team goes to understand the goals, comment, and iterate. What used to happen is the PRD would sit there, engineers would wander off with whatever context lived in their heads from a dozen meetings, and a lot of that context never made it back into the document. What *should* happen now is that the PRD (the thing that was actually agreed to, with the back-and-forth and the reasoning baked in) becomes the artifact you hand to your agent when you start building. It carries the context. It's genuinely helpful to an LLM deciding how to prioritize and which problems to attack first.

Every doc I produce internally now, I fully expect and encourage people to consume through an AI. I don't expect anyone to sit down and read it cover to cover. That's exactly why killing the five-paragraph essay matters: the way people consume documents is changing, and you have to change the document with them. An LLM can load the full thing, the full context, without breaking a sweat. A human can't. So you arrange the context differently for your human readers than for your LLM readers.

LLMs don't care about raw thought. They're good at translating raw thought into something cleaner and more actionable. You can afford to be less polished, a worse writer even, because the model will smooth over the mistakes. The discipline moves from prose-craft to getting the thinking right. The *shape* of the document matters more than whether documents survive.

## Nobody wants to review your requirements anymore

If building is cheap, the instinct that follows is reasonable: don't evaluate the requirements up front, evaluate the build when it's done. Rebuilding is cheap too, so why litigate the spec in advance when you can just look at the output and react? The feedback loop got fast enough that this mostly works.

But the time doesn't disappear. All the effort you used to spend reviewing a document before a decision gets readjusted to evaluating the output of what your system actually produced. Deep inspection of a system, confirming it actually meets the requirements of real users, is harder than it sounds, and it's a skill most reviewers never had to build under the old model. Everyone says "we dogfood, we test it ourselves." Do you? Did you load the page, see some data on it, and call it done? Or did you actually walk through it as a user would?

For a lot of products you can't, because you're not the user. Unless you're building a productivity tool, you usually aren't. Think about legal AI: there are a hundred of them. If you're not a lawyer, how do you test that the thing meets what lawyers actually expect? You did some research, you built up some requirements. But nobody wants to review your requirements anymore. They only want to review the output.

The document becomes the touchpoint you go back to when you're staring at the output: why did we build it this way? Is it satisfying a requirement I'm not even aware of? If the people evaluating the result were never aligned on the goals and objectives up front, their feedback is going to be shit. The doc holds the context that isn't loaded into their head, the reasoning the output alone can't explain, so the next person doesn't have to relearn or relitigate what's already been decided.

## Why the five-paragraph essay is now *more* of a liability

The real problem is that writing documents got trivially easy. A 500-word essay used to take an hour; now it takes seconds. Claude can spin up a PRD in under a minute if you give it the right guidance. That doesn't mean it's good. The ability to just *crank* documents has never been higher. And most LLMs default to a five-paragraph essay style. Most of the document is a buildup to a conclusion that only lands at the very end. You frame the problem, you explain why it matters, yada yada, and the reader is supposed to consume all of your rationale to earn the payoff.

People throw a TL;DR at the top to compensate, but it's usually a two-line throwaway, and the real expectation is still that you'll absorb the full argument to understand the decision. With documents this verbose and this cheap to produce, there's simply too much context to consume. And it's not just that more people are writing. People who historically wouldn't have written docs at all, because it was too time-consuming or they didn't know how, are now producing them by the dozen. If your job is to review these things, the pile keeps growing and your context budget doesn't.

So people adapt. They chuck the doc at an agent, say "summarize this and pull out the things I care about," and get the top-level answer instantly. If attention was already scarce, this makes it scarcer. It is harder than ever to get someone to suffer through a thorough, comprehensive case for why your decision is correct, and you run a real risk that they don't read it at all, at which point your opinion isn't in the room.

The standard objection is that this is lossy: if you only read the summary, you miss the nuance, or the LLM gets something wrong and you end up saying yes to things you didn't understand, or no to things you didn't understand. Maybe. But the idea that the person who was going to read all ten pages wouldn't have made those same mistakes is naive. There's a lot of bad writing. There's also a lot of bad reading. Pretending the careful full-document reader is the norm is how you justify writing for a reader who doesn't exist.

There's a subtler failure hiding under that objection, though, and it's worth naming directly. Writers under pressure to be concise for a senior audience already trim the context out of the document: the prior decisions, the company goals, the reasoning trail. That's fine if the reader was in the room for all of it. It stops being fine once the reader is an LLM summarizing the document for someone who wasn't, because even a well-prompted model doesn't carry the context a senior leader carries around in their head. Cut the context from the document and you're not risking a bad summary, you're guaranteeing one, and now that leader is making a call off a summary of a document that was already missing the reasoning. That's worse than the original problem. The fix isn't to stop cutting for length. It's to stop confusing "short" with "missing information": keep the reasoning in the document, just stop putting it up front.

## The IC trap

This is a trap a lot of ICs fall into. You feel like you don't have decision-making power, so you compensate with comprehensiveness: *look at everything I've done, look how much thought I put in.* The implicit pitch is that volume of work should signal expertise, and expertise should buy you trust.

It works a couple of times. Then it stops, because the energy required to actually parse what you're saying is too high. Here's the key point: you may not have decision-making power (even a mid-level manager often doesn't), but you are allowed to have an opinion. An opinion on what the problem is, and an opinion on the solution. People are free to disagree. But if they're going to disagree, they'll probably disagree whether or not they slogged through your five paragraphs. The litigation buried the opinion instead of protecting it.

## So what does the document actually look like?

Flipping the model is concrete: you collapse the document down to three short sections, and you state your point first in each one. The goal is for your points to be clear, direct, opinionated, and unmissable.

> [!tip] The three-section doc
> 1. **The problem**: stated up front, in the first line.
> 2. **Goals and non-goals**: the outcomes you want, and explicitly what you're *not* solving.
> 3. **A recommended solution** (optional): ideally a flowchart, not prose.
>
> Most of these should be under two pages. The only reason you hit a second page is a diagram. Everything else goes in a collapsible "other context" section at the bottom.

"Other context" doesn't mean throwaway. It means buried. A human reviewer skims past it, fine, they already have the conclusion. But when the reader is an LLM, and it increasingly is, that section is exactly what lets it do its job. An LLM that only sees your conclusion can't tell a decision you actually thought through from one you didn't. Don't let it mistake lack of context for lack of decision-making.

Inside the problem section, that means stating the negative consequences of not solving it, not just the problem statement. Inside goals and non-goals, that means stating the solution-agnostic capabilities you actually need, not just a bullet list of outcomes. And if you did market research or competitive analysis to get to your recommendation, that's what belongs in the drawer: the evidence that got you from capabilities to conclusion. Structured that way, an LLM reviewing the document reads your conclusion, then walks backward through problem, consequences, capabilities, evidence, in that order. That's usually what someone's actually asking the model to do when they hand it your doc: find the holes, find where your thinking doesn't hold up. A document that walks its own reasoning in order is a lot harder to flag as inconsistent, because the model can actually follow how you got there. It might still come back with something you missed, a competing approach, research you didn't find. Good, that's a real conversation worth having. What you're avoiding is the model calling your thinking inconsistent simply because it never had enough of it to check.

If the context lives in other documents, link out to them, and make sure your org has the out-of-the-box connectors turned on so a reviewing LLM can actually follow the link instead of guessing.[^1]

The mechanics of each section, plus a worked example and where the leftover material goes, are laid out in the companion piece: [The three-section internal doc](/three-section-internal-doc/).

## Reasonable beats correct

Leading with the conclusion feels like exposure. You're trying to be reasonable: the person closest to the problem, who's thought about it, and made a clear call others can react to. That's the bar that actually holds up in the room.

The drawer in the three-section form was never a place to hide things you didn't want read. It's for the reader who actually needs the full case: the rare human chasing every objection, and the LLM summarizing you for someone who wasn't in the room. Bury the context. Don't cut it. Everyone else, human or agent, was already skipping straight to the conclusion. Five paragraphs of litigation just made them work for it first.

[^1]: This means you can effectively prompt-inject your own document. Put a line near the top, right after the conclusion: "before reviewing the rest of this, pull in these linked documents first." Reviewer LLMs following your org's standard connectors tend to actually do it.
