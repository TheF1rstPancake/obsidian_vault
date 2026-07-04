---
title: "Unlearning the five-paragraph essay"
slug: unlearning-the-five-paragraph-essay
status: shaping
target: ghost
created: 2026-05-22
updated: 2026-07-03
tags: [writing, communication, sales, careers]
ghost_url:
---

## The thesis

I'm classically trained in the five-paragraph essay. Intro, three body paragraphs that litigate every objection, conclusion. It served me well in school. It has been actively detrimental in sales and in internal progression at every company I've worked at.

The five-paragraph essay assumes you have to litigate all objections *before* getting to the conclusion. Businesses move on the exact opposite assumption: give me the conclusion first, and if I want to litigate or object, *then* I'll read the rest. Most of the time, I won't. The executive who reads your email decides whether to keep reading after the first sentence. The customer reading your follow-up decides after the subject line.

If your default writing posture is "build to the conclusion," you are losing readers, deals, and headcount fights to people whose default is "lead with the conclusion." It's not a small effect. It compounds across every email, every doc, every Slack thread.

## Documents aren't dead — the audience changed

This is getting more relevant, not less, and the reason is AI. There's a live back-and-forth right now about whether document writing is even a meaningful practice in a world of LLMs and agents. My answer is an emphatic yes. But the "we don't do documents anymore" position is misread. The people saying it don't actually want to stop documenting things. They don't want to be responsible for *reviewing* them anymore.

That's a fair thing to be exhausted by. There's a lot of bad document writing out there: PRDs, product readiness docs, internal briefs, strategy memos. As the person consuming one, you're often sitting there wondering why the fuck you're reading it. What's the purpose? Why am I putting effort into something that's going to get thrown away? There's real scar tissue here. Airtable was a deeply doc-heavy culture. Everything lived in a document, everything got reviewed. And editing is far easier than creating. So as the writer trying to build alignment, you'd put a doc out and just get shit on. A wall of comments, no clear finish line. When is the doc done? When I've resolved every comment? When we've had a meeting about it? What's the point?

None of that means the document was the problem. The OpenClaw experiment made that obvious to me: almost the entire architecture comes down to updating a handful of documents over and over. That shared set of markdown files is what lets agents collaborate and take on increasingly complicated tasks. You have to have *some* way of holding a shared understanding of what's meaningful and what isn't. Documents are that mechanism, and they aren't going anywhere.

What's changed is the *primary audience*. People hear that and jump to dead-internet theory — robots writing documents for robots. But in most cases these documents are still consumed by people too. A PRD is where a team goes to understand the goals, comment, and iterate. What used to happen is the PRD would sit there, engineers would wander off with whatever context lived in their heads from a dozen meetings, and a lot of that context never made it back into the document. What *should* happen now is that the PRD — the thing that was actually agreed to, with the back-and-forth and the reasoning baked in — becomes the artifact you hand to your agent when you start building. It carries the context. It's genuinely helpful to an LLM deciding how to prioritize and which problems to attack first.

So write accordingly. Every doc I produce internally now, I fully expect and encourage people to consume through an AI. I don't expect anyone to sit down and read it cover to cover. That's exactly why killing the five-paragraph essay matters: the way people consume documents is changing, and you have to change the document with them. An LLM can load the full thing, the full context, without breaking a sweat. A human can't. So you arrange the context differently for your human readers than for your LLM readers.

There's an upside hiding in that. LLMs don't care about raw thought. They're good at translating raw thought into something cleaner and more actionable. You can afford to be less polished, a worse writer even, because the model will smooth over the mistakes. The discipline moves from prose-craft to getting the thinking right.

So: document writing isn't dead. The primary audience is shifting, but not as much as the loudest takes claim.

## Nobody wants to review your requirements anymore

If building is cheap, the instinct that follows is reasonable: don't evaluate the requirements up front, evaluate the build when it's done. Rebuilding is cheap too, so why litigate the spec in advance when you can just look at the output and react? The feedback loop got fast enough that this mostly works.

But the time doesn't disappear. All the effort you used to spend reviewing a document before a decision gets readjusted to evaluating the output of what your system actually produced. You have to be deliberate about that, because evaluating output well is a skill a lot of people don't have. Deep inspection of a system, confirming it actually meets the requirements of real users, is harder than it sounds. Everyone says "we dogfood, we test it ourselves." Do you? Did you load the page, see some data on it, and call it done? Or did you actually walk through it as a user would?

For a lot of products you can't, because you're not the user. Unless you're building a productivity tool, you usually aren't. Think about legal AI — there are a hundred of them. If you're not a lawyer, how do you test that the thing meets what lawyers actually expect? You did some research, you built up some requirements. But nobody wants to review your requirements anymore. They only want to review the output.

That's the tension, and it's exactly where documents keep earning their place. The document is the touchpoint you go back to when you're staring at the output: why did we build it this way? Is it satisfying a requirement I'm not even aware of? If the people evaluating the result were never aligned on the goals and objectives up front, their feedback is going to be shit. The doc holds the context that isn't loaded into their head, the reasoning the output alone can't explain.

So no, documents aren't going away. If anything we'll produce more of them, and the organization and value around them will go up. Their value was never in the ceremony of reviewing them. It's in storing organizational context so the next person doesn't have to relearn or relitigate what's already been decided. I don't see how you do that without a document with words in it.

## Why the five-paragraph essay is now *more* of a liability

The real problem is that writing documents got trivially easy. A 500-word essay used to take an hour; now it takes seconds. Claude can spin up a PRD in under a minute if you give it the right guidance. That doesn't mean it's good. The ability to just *crank* documents has never been higher. And most LLMs default to a five-paragraph essay style. Most of the document is a buildup to a conclusion that only lands at the very end. You frame the problem, you explain why it matters, yada yada, and the reader is supposed to consume all of your rationale to earn the payoff.

People throw a TL;DR at the top to compensate, but it's usually a two-line throwaway, and the real expectation is still that you'll absorb the full argument to understand the decision. With documents this verbose and this cheap to produce, there's simply too much context to consume. And it's not just that more people are writing. People who historically wouldn't have written docs at all, because it was too time-consuming or they didn't know how, are now producing them by the dozen. If your job is to review these things, the pile keeps growing and your context budget doesn't.

So people adapt. They chuck the doc at an agent, say "summarize this and pull out the things I care about," and get the top-level answer instantly. Attention spans are waning. It is harder than ever to get someone to suffer through a thorough, comprehensive case for why your decision is correct, and you run a real risk that they don't read it at all, at which point your opinion isn't in the room.

The standard objection is that this is lossy: if you only read the summary, you miss the nuance, or the LLM gets something wrong and you end up saying yes to things you didn't understand, or no to things you didn't understand. Maybe. But the idea that the person who was going to read all ten pages wouldn't have made those same mistakes is naive. There's a lot of bad writing. There's also a lot of bad reading. Pretending the careful full-document reader is the norm is how you justify writing for a reader who doesn't exist.

## The IC trap

This is a trap a lot of ICs fall into. You feel like you don't have decision-making power, so you compensate with comprehensiveness: *look at everything I've done, look how much thought I put in.* The implicit pitch is that volume of work should signal expertise, and expertise should buy you trust.

It works a couple of times. Then it stops, because the energy required to actually parse what you're saying is too high. Here's the key point: you may not have decision-making power — even a mid-level manager often doesn't — but **you are always allowed to have an opinion.** An opinion on what the problem is, and an opinion on the solution. People are free to disagree. But if they're going to disagree, they'll probably disagree whether or not they slogged through your five paragraphs. The litigation didn't protect you; it just buried the opinion.

## So what does the document actually look like?

All of this is easy to nod along to and hard to do, because the five-paragraph instinct is to set everything up before you say anything. Flipping the model is concrete: you collapse the document down to three short sections, and you state your point first in each one. The goal is for your points to be clear, direct, opinionated, and unmissable.

> [!tip] The three-section doc
> 1. **The problem** — stated up front, in the first line.
> 2. **Goals and non-goals** — the outcomes you want, and explicitly what you're *not* solving.
> 3. **A recommended solution** (optional) — ideally a flowchart, not prose.
>
> Most of these should be under two pages. The only reason you hit a second page is a diagram. Everything else goes in a collapsible "other context" section at the bottom.

### Section 1: the problem

The mistake people make — again, because of how you were trained — is spending paragraphs on problem setup. *We've experienced this, and this, and the other, which leads to these issues, and the root cause of that is…* That's a lot of building and framing to arrive at the point. Flip it. State the problem in the first line, very clearly.

Don't write "we've experienced enterprise customers who get nervous about the product." Write it as an opening statement:

> Customers are increasingly asking for role-based access controls. We don't have them. That gap is causing friction in the sales cycle, because it's something enterprises expect and we can't confidently answer — which adds doubt. It also threatens renewals: as people use the product more, they want fine-grained controls we can't offer, which causes frustration and makes them evaluate alternatives.

That's the whole problem statement. Notice what it's *not* doing: it's not piling on qualitative or quantitative justification. The instinct is to reach for a number — "30% of deals stall" — but the moment you do, people either debate how you got the number, or, if you leave it out, ask how big the problem really is. **The more context you provide, the more opportunities for argument and disagreement you invite.** That's not the point here. The point is to say: this is a problem, and you need to trust me, as the person closest to it, that I've correctly identified it as one. The supporting detail is real and you'll likely need it in conversation — but it lives later in the document, as a follow-up, not as preamble.

One more discipline: **the presentation of the problem should not demand its prioritization.** You want people to agree that it's a problem. Whether and when it gets worked on comes second. A lot of people try to force problem identification, solution recommendation, *and* prioritization into one essay. Treat them as three distinct steps in a larger process. It feels slower up front, but it's the classic case where slowing down at the start lets you accelerate in the back half.

### Section 2: goals and non-goals

I prefer goals over requirements — they're close enough to lump together. The idea is to outline the outcomes you want, given that most problems are broad and have many ways to be solved. Goals shouldn't be "win more deals" — there are a hundred ways to win more deals, and you don't strictly need role-based access controls for any of them. Aim instead at what it actually means to solve *this* problem. User stories are the right register: users need to be able to do X, Y, and Z.

The most important and most underused part is **non-goals.** This is where you put things in a box and stop people from playing the thousand-question what-if game. You say, targetedly: I've reviewed this, I've thought about it, this is what I think is meaningful, and this is what can be meaningfully left out. If people are going to push back anywhere, it'll be here — and that's good, because this is what becomes the requirements for the technical solution downstream.

Don't get cute. One bad habit people pick up from SaaS writing is parading every assumption they made to bucket the solution together. That just invites more debate. The nice thing about goals and non-goals stated plainly is that they feel concrete and actionable — which is the point. Someone should be able to read this and either do it themselves or hand it to an LLM. Don't create more surface area for confusion.

### Section 3: the recommended solution (optional)

A recommended solution is nice to have, not the end of the world if it's missing. If you include one, frame it as a flowchart — the if-this-then-that logic you're going after. Building diagrams is an underrated skill, and I find it's a red flag when someone can't do it: it usually means they're good at spouting problems but have no framework for solving them. No framework for solving means no framework for prioritizing — no way to weigh cost against value, no way to ask whether the juice is worth the squeeze.

A flowchart also plays to different learning styles. Even the collapsed version of the doc might be too much for some readers; an image lets them glance and get a sense of how users are meant to use the product, or what internal systems you'd build to hit the goals. That's it. Those are the three sections.

### Everything else goes in a drawer

After the three sections, you probably have a lot more: customer anecdotes, a prototype you threw together, deeper analysis. Put all of it in a collapsible "other context" section at the bottom. People are welcome to open it and engage. Most won't — and that's fine. You don't want them to have to learn everything you learned in order to participate in the conversation. That's the entire reason you collapsed it down to three short sections in the first place.

## Reasonable beats correct

This is the part that's hardest to internalize. Leading with the conclusion feels like exposure — you've stated an opinion before you've earned it with evidence. But you are not trying to be unimpeachably *correct* in a way no one can disagree with. You're trying to be *reasonable*: to demonstrate that you're the person closest to the problem, that you've thought about it, and that you've made a clear call others can react to.

The five paragraphs of litigation were always a defense mechanism — an attempt to win the argument before anyone could have it. But people who are going to disagree will disagree regardless. Spend that energy stating a clear opinion someone can act on, and put the rest in the drawer.
