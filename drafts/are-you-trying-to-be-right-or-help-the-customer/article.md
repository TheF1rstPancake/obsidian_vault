---
title: "Are You Trying to Be Right, or Help the Customer?"
slug: are-you-trying-to-be-right-or-help-the-customer
status: ready
target: ghost
created: 2026-05-18
updated: 2026-06-21
tags: [sales-engineering, solutions-consulting, customer-discovery]
point: >
  The default SE posture of "being right" loses deals; solution-agnostic
  requirements gathering — a four-part discovery framework plus a solution
  bridge — is what actually helps customers and builds the artifact that
  protects the relationship downstream.
---

## The question that stuck

I was a newly minted sales engineer with no real concept of what the job entailed.  My manager was [Chris Hecht](https://www.linkedin.com/in/checht) — still one of the best solutions leaders I've ever had the opportunity to work with.

Coming out of school, I feel like I had been trained to approach every problem as if there's one right answer. You look at the test, you're given a problem, there are discrete things people are looking for in your answer. That doesn't translate to the work environment very well. When working with customers, there are any number of correct answers to the problem they are trying to solve at any given moment. There's no partial credit in sales — it's closed won or closed lost. You either met the objectives or you didn't.[^learning]

But I didn't know that yet. I thought my job as a sales engineer was to *have the right answer*. To be prescriptive. To know the tech the best. If a customer disagreed with our answer, they probably weren't a good fit.

Then came my first large opportunity. I don't remember the full context of what was unique about the customer's problem, but I do remember spending a lot of time documenting a solution I thought was *right*. Objectively, based on our experience, it was the correct answer. Technically, it would have worked.

About five minutes into presenting it, the customer called out some unique constraints on their side that they felt rendered the whole thing moot.

Instead of stepping back to listen — instead of asking, *can you tell me more about that? Why does that requirement exist?* — I just pushed back. I fell back on the technical. I read the spec sheet at them. *Here's what we can do and... and... and...*

The problem with word-vomiting the spec sheet is that the customer is responsible for translating their problem space into a solution on your platform. You are no longer leading them to a solution, you are forcing them to connect the dots. If they wanted to (or were capable of) doing that, they could have read the docs themselves. Today, you could just chuck Claude at it.[^headless] But this was a group of people who had already taken a phone call, gone the extra mile, seen enough to warrant a conversation — and there I was, re-reading the documentation back to them as justification for why my solution was right.

Needless to say, the call was a pretty spectacular fucking failure.  A very skilled AE managed to salvage a follow up call.

I walked out of that meeting feeling indignant. *They just didn't understand.* Up until this point in my career I had felt like I had a natural intuition for how to navigate customer conversations well. This one was hard to walk out of.

Word got back to Chris. The opportunity was a big price tag and was a highlight in pipeline reviews. He pulled me up to figure out what was going on, and in that conversation he got frustrated with me because I wasn't getting it. He said:

> *Are you trying to be right? Or are you trying to help the customer?*

I don't even know if he remembers saying it. But to this day, across all of the roles I've had in sales, implementation, engineering, etc, when I catch myself reading the spec sheet, or catch myself in a spiral where it just doesn't feel like the customer is getting it, this is the question I ask myself -- am I trying to be right? 

## Why we default to "being right"

There is a real, material difference between the two postures. And the way most teams are built, trained, and rewarded pushes you toward "being right" as the default.

Being right is usually about what's right *for you*. Teams create standards. We definitely had this at WePay — there were archetypes we really wanted to bucket people into. Marketplace, crowdfunding, and a third one I've clearly forgotten.  Airtable had simiarly attempted to reduce most customer problems into a few buckets.  And the reason you do that is sound: when you standardize, you scale. You develop reusable assets, reusable talk tracks, the keywords and catchphrases that make people go *aha, I get it*. Standards let you take on more customers and turn them into durable revenue faster. It is important to do this.

But you build those standards for yourself. Your workload and desires to scale are not something a customer cares about. "But Gio it lets us get them to value faster!" Uh huh. You could just work longer hours or throw more people at the problem. But we don't.  We standardize.

In every org I've worked in, implementation has been the function most allergic to this. A lot of their frustration with presales stems from the fact that sales teams are willing to be fuzzier about how someone fits into an archetype. Implementation doesn't like that. If the customer doesn't fit cleanly in the box, it means more work for them. There's a kind of organ-rejection response to those opportunities.

For presales specifically, the "being right" instinct tends to look like defaulting to the talk track that worked for someone else. You're spread thin across a lot of opportunities and want to reach a solution with the least friction. You're not especially open to debate — or you tip the other way entirely and just agree to everything and figure it out later. Either path means you're not really listening to this customer.

If you really are trying to help, you have to be much more open to the idea that they have requirements unique to them. Unique to their business, their market, even their working style. Yes, there are patterns you can grab and latch onto. But if all these businesses were the same, there would be no differentiation — they'd collapse into each other. They don't, because they operate differently and have found different niches. They compete over some of the same users, but not all of them. So you have to assume every customer is unique in some capacity.

## What "being helpful" actually looks like

Being helpful means being curious and exploratory. But that's a platitude someone pulled out of Ted Lasso.

What actually puts this into practice is **solution-agnostic requirements gathering** — and doing it well.

I took a sales training years ago with Skip Miller, who wrote a book called [*ProActive Selling*](https://www.amazon.com/ProActive-Selling-Control-Process-Sale/dp/0814407641). Skip had a lot of things to say, but the one line he repeated over and over was: *don't talk about the dog.* Weird metaphor, but clearly it worked because I still talk about it. The point was: don't talk about your own product too early. The customer doesn't care. They have a problem, they want to know how it gets solved, and before they can hear you on that, they need to know you understood the problem.

A lot of people roll their eyes at this. *Yeah, of course, I always summarize the customer back to them.* That's table stakes — and it's not enough. Any AI can summarize a conversation. If reciting the customer's tape back is your only skill as a seller, you are ripe for replacement. So let's assume you need to do a little more to keep your job.

Solution-agnostic means you aren't just parroting back the problem. You are taking the time to help the customer clarify what *they* think their ideal solution and requirements are. How would they approach it if they could? Their answer might be a shrug — *that's why I'm talking to you* — and that's fine. But you have to pause and ask. When people don't, they fall back on reading the spec sheet, which forces the customer to interpret your product and map it to their problem. The role of a "solutions" team in any capacity is to help the customer *do that mapping of their problem, to your solution.* You can give the most technically accurate, robust description of your platform and still lose, because the customer was confused about how it connected to what they actually needed. If you leave it up to the customer, you are rolling the dice, and not in your favor.

The best test here is -- can they take your solution agnostic requirements and use them to evaluate your solution *and* others in the market. That's how you know you've documented what they need, not just what's right for you.

### The four boxes

People say "discovery is so important" all the time and like most things, it's _good_ discovery that matters. There are four data points that, together, form a problem statement. These four boxes have *nothing to do with you*. They have everything to do with the customer:

1. **Current state.** What are you doing today?
2. **Problems.** What's not working about it? Why are you taking this call?
3. **Goals and objectives.** What are you trying to achieve?
4. **Ideal solution.** If you had a magic wand, what would the solution look like?

In my experience, asking the fourth question scares people, because what if the customer's ideal state is incongruous with what you offer? What if they ask for things you can't deliver? Then how can you win the opportunity? What if they can't tell me what their ideal is?

If the prospect is already imagining an ideal state that doesn't match your product, *you need to know that now*. You need to get out ahead of it, reframe it, address it head-on. If you never ask, you never get the chance. The customer just quietly disqualifies you later.

This is also where the distinction between *understanding the customer's problem* and *understanding the customer* shows up. The problem is easy — what's broken today. The customer is harder — their idiosyncrasies, motivations, rationale, context. People flounder here because the prospect throws out a string of whacky requirements, and the seller feels pressure to show, one by one, how the product checks each box. So they fall back to the spec sheet, walking through every button on the page, hoping the customer will connect the dots.

It's very unlikely that any single button on the page exactly attacks the problem. It's almost always a *combination* — a workflow, a sequence, a process. You can't show the right combination if you don't understand what the customer expects to have happen.

Those four boxes are the anchor point of the entire relationship. Your AEs will reference them. Other SEs will. Your CSMs will. They'll come up in QBRs. They're the essential thesis for why this customer is working with you. Until you have them dialed, you have not understood the customer, and you can't actually help them.

### The fifth box: your bridge

Only once the four boxes are solid do you move to the fifth: a solution-agnostic summary of the technical requirements they'd need to solve their problem — generalized, not tied to your platform yet. This is where you reframe their ideal solution in your terms. It's the bridge. From there you get into the nitty-gritty of what you can and can't do, and you start negotiating between what the customer *thinks* they need and what they *actually* need.  This is solution-agnostic requirements.

As an SE you're already good at documenting requirements for using your own system. Apply the same skills to the customer's stated ideal solution. *In order for that to work, you would need X, Y, Z.* Take, for example, a customer who says: *I want an application where people log tickets, the system automatically prioritizes and assigns them to the right team member, connects to Salesforce so I can see which accounts need help at any moment, and lets me see bandwidth and resource allocation across team members.*

There are any number of tools in the market that can hit most of that. The one that wins is the one that convinces the buyer fastest that *it* is the right answer. The easiest way to do that is to know exactly which boxes the customer is trying to check, and then build the artifact that proves you've checked them.

Boxes you *can't* check are fine. That's not a deal-killer. What you have to do is convince the customer those are nice-to-haves rather than need-to-haves. Most buyers don't come in with a clean need-vs-want list. They come in with a pie-in-the-sky want list. Part of your job is playing it back: *Here's what I've understood your wants to be. In my experience working in this industry, here are the critical things people actually need — and here are some things people don't usually consider that I'd add.*

That last part is where you seed the list with your differentiators. If you can rewrite the customer's want-and-need list for them, then when they go evaluate other tools, they'll have a harder time selecting others, because the list now contains needs that are very specific to you. Be upfront and honest about what you can't do, and steer the requirements in those areas from need-to-have to nice-to-have.[^reframe]

Tactically: I almost never offer a solution on the first call. If someone really pushes, sure, you can move into it. But it's not the default posture. The first call is for current state, problems, goals, ideal solution. Then the fifth box. *Then* the product.

When you do offer the solution, if you've done the four boxes well, the customer's want-and-need list will already align with what you have — and what you're planning to build. (Which assumes you have some semblance of a roadmap. How you communicate roadmap in an early-stage product without locking yourself into commitments or accidentally lying to customers is a topic for another day.)

## Package it into a document

This whole framework I commonly wrap up into a **solution design document**.There's plenty of examples and templates online.  Feed this article to Claude and I'm sure it will give you something very workable. 

The format of the document is less important to me.  It can be a presentation, sometimes it's an Excel sheet, or you can be extra hardcore and its an amendment to the contract. My preferred form is a long-form document. It looks official. It feels comprehensive. It gives the sense that you've turned over every rock, that there are no unknown unknowns.

The contents:

- The four boxes (current state, problems, goals, ideal solution)
- The fifth box (your high-level summary of how you help)
- Requirements, split into in scope (need-to-have) and out of scope (nice-to-have)
- Timelines, implementation responsibilities, onboarding scope
- An explicit call-out of what your system does and does not do

A side note on onboarding and hand-holding: that *is* a differentiator. Not every company offers it. It is completely fair to list "implementation support" or "white-glove onboarding" as a need-to-have requirement. Most customers don't think they need it, but it's easy to make the case that they do — and if they go to a competitor and ask whether they can match it, you've set a bar that's hard to clear.

Internally, you should know which requirement maps to which objective. I've tried explicitly tagging every row with an objective in the past. It looks comprehensive and fancy. It's confusing for customers, because not every requirement maps cleanly to one objective, and you end up in a debate about *is this objective one or objective two?* Who cares. The traceability is a filtering function for you, not a deliverable for them. If you have a requirement that you cannot trace back to an objective, get rid of it.

The last step is sending the document and getting acceptance — *explicit*, a written confirmation, or *implicit*, they sign the contract without responding directly.

Acceptance does two things. It gives you accountability and traceability: the artifact becomes the shared agreement that proves you understood the customer's problem intimately and were the only one capable of solving it with them — which is what protects your implementation team and the downstream renewal revenue. And forcing everything into a form someone can sign off on sharpens how you communicate what your product does and how it's different from everyone else.

## Where do demos fit?

Demos are a wrinkle, especially the very early-stage ones where someone just wants to sniff-test the product. A lot of buyers have been trained to think that a demo is the first step and that it will give them clear signal on what tools will and will not work for them. A lot of teams meet that with show-up-and-throw-up demos — what I've heard called a "harbor cruise," meandering through features hoping to surface what the customer reacts to.

If you don't have the chance to do proper discovery before a demo, you have to be more vague in general. You get roughly three to five questions before the customer gets antsy and says *show me the fucking product*. So spend those questions well.

Counterintuitively, in this scenario you don't want to lead with *goals and objectives*. It's too esoteric, too high-level. Someone came to you wanting a tactical demo — meet them there. Get the tactical *what's wrong* and *what are you looking for*. Skip current state, skip the deep *why*. You can reverse-engineer those.

It is okay in sales to assume. Rather than throwing spaghetti at the product wall and forcing the customer to decide whether it solves their goals, have them tell you tactically what they're looking for, and then vocalize back the goal you think they're chasing. Think of it like a horoscope — goals and objectives pattern-match across customers even when specific requirements don't. You don't have to wait for the customer to clearly articulate their goals before you put one on the table. Give them the general version back: vague enough that they agree, specific enough that they expand. (Time saved is the weakest goal to build a relationship on long-term — but it's the most universal one. Everyone wants time back.) They will correct you, fast. It's a two-minute exercise that way. Start with *what are your goals?* and you get ten minutes of unstructured ranting and now you have twenty minutes left and no idea where to go.

So the early demo flow looks like: three to five tactical questions about what's broken and what they want to see, then assumptions about *why* that you offer back for correction. Something like: *In my experience, the reason one team member gets overloaded compared to others is usually round-robin distribution that doesn't account for project difficulty — one person ends up with all the hard tickets. Is that what you're seeing?* That's vague enough to horoscope onto — they'll either latch on or correct you (*no, we pod people*). Either way, you've learned more in two exchanges than you would have in ten minutes of *tell me about your goals*.

> [!note]
> This is one tactic for the early demo — and it works in most situations. But the ultimate goal is always a next call, and sometimes the person just wants the fucking spec sheet, and that's what will get them back on the phone. Don't follow this approach blindly. Just most of the time.

The hard part: this means your demos aren't canned and repeatable. That scares leaders who want to operate at scale. *How do I train the team to do these well if they're different every time?* That's the nature of the beast — especially if you're the first SE pancake at any org. You have to roll with the punches and accept you'll get some things wrong. But if you do the framing up front and capture even a little of the negative consequences and the goals they're after, you generally build enough trust to earn a second conversation.

And there is a way to do this scalably... if you know what goals/outcomes a customer wants that lead you to recommend certain solutions... then you should also know the reverse, what package of requirements ladder back up to which goals/outcomes — which is the foundation of an [[ai-native-se-stack]] [?-update to Ghost URL when live].

And that second conversation is where the leverage is. When a customer demands a demo, *they* are in the driver's seat. You don't really have a choice. But once they've agreed to a follow-up, you take the wheel. You schedule more time. You set the agenda ahead of it. You send an email beforehand to capture more context. From there you're back in the four-boxes framework and the document starts taking shape.

## How to spot it

It's very telling when you have a team or a team member who is more interested in being right than in helping the customer. It almost always comes down to how they frame the very first conversations they choose to have.

Are they reading the spec sheet? Word-vomiting what the product is capable of? Or do they take a beat to actually understand what the customer is trying to do — package it back to them in the customer's own language — before moving forward into the 7,000 ways we can help?

Are they skipping the fourth box because they're afraid of what the customer might say? Are they running harbor-cruise demos because that's easier than asking three sharp tactical questions?

Are they trying to be right? Or are they trying to help the customer?

[^headless]: Headless product experiences are changing this dynamic considerably. People can now just ask "implement using X solution" — an agent like Claude reads the docs and wires up the integration, with nobody on your side reading the spec sheet at the customer. That shift makes solution-agnostic requirements matter even more, not less: when the customer can just tell an AI what to build, the vendor who arrives with a crisp requirements doc already scoped to their stack wins faster.

[^learning]: You should always be learning — and showing your work internally, for your own development and your team's, is a necessity. Your customers just don't care what you learned. They care whether they got what they needed.

[^reframe]: Phrasing like "when we've worked with other customers with similar objectives, we've recommended..." does a lot of the heavy lifting here. It frames your judgment as pattern recognition across clients rather than personal opinion, which makes it easier for the customer to accept a requirement being scoped down.
