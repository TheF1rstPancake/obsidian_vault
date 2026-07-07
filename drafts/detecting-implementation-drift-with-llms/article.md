---
title: "No plan survives contact with implementation"
slug: detecting-implementation-drift-with-llms
status: raw
target: ghost
created: 2026-07-07
updated: 2026-07-07
tags: [product-management, engineering, go-to-market, llms]
visibility: public
point: >
  Design docs get written upfront, then implementation drifts as engineers make
  judgment calls the requirements never anticipated. That drift isn't anyone's
  fault, but it turns toxic when it stays invisible until a customer hits the
  edge case nobody flagged. The fix isn't a more perfect spec, it's a
  project-completion debrief that compares what got built against what was
  agreed. LLMs finally make that comparison cheap enough to actually run, but
  only if someone makes it a standing part of the process instead of one more
  report nobody reads.
ghost_url:
---

One of the more frustrating parts of being an early-stage employee is watching your product move fast across a lot of areas at once. This isn't really a function of company size. It's a function of how long the company has been around. Anthropic and OpenAI have thousands of employees and things still move incredibly fast internally. In an early-stage company, or an early-stage team inside a bigger one, there's just a lot of motion.

As someone on a go-to-market team, you get pulled into conversations about goals, objectives, and the trade-offs an engineering team is allowed to make. Those are good conversations. You should keep having them, and there should be documentation: design docs, architectural decisions, the whole record.

The problem shows up in the gap between when those decisions get made and when the thing actually gets built. During implementation, the engineer makes additional trade-offs, additional assumptions, and learns things the design doc never addressed. No one did anything wrong here. Plans don't survive contact with implementation. The original goals usually stay the same. The path to them drifts.

## Where the drift actually hurts

That drift is invisible to the go-to-market team by default. It usually stays invisible until a customer starts probing around the exact area where a trade-off was made, which forces someone to go dig through the system to understand what happened. That's the moment you learn someone decided a particular behavior was acceptable, quietly, while building.

Technically, the goal was still met. The engineer can point out that the customer's specific condition wasn't part of the original ask. But from the outside it doesn't read as "goal met." It reads as a silent trade-off that got made without anyone flagging it, and it casts doubt on the rest of the system. If this was overlooked, what else was?

That's what actually damages trust between go-to-market and engineering. Not that trade-offs get made. Trade-offs always get made. It's that they're discovered instead of disclosed. The go-to-market team feels like they've been lying to customers. The engineering team feels ambushed for a decision that felt reasonable at the time.

Weekly project updates don't fix this. The gap between "what we agreed to build" and "what got built" is made up of dozens of micro-decisions, and keeping all of that context front-loaded across a team is genuinely hard. Historically, catching the drift required someone to sit down and manually compare a design doc against every implementation detail that backed it up. That's a lot of unglamorous reading, so it mostly didn't happen.

## The kind of drift that shows up most

In my experience, the most common source of drift isn't the headline feature. It's the logic and gates that quietly preclude certain activity.

Take a data ingestion pipeline: a user uploads a file, the system processes it, things happen. Generic, on purpose. One of the first real problems with file upload is dedupe. How do you know if a user uploaded the same thing twice? Was that ever stated as an explicit goal? Usually not, because it has nothing to do with the stated purpose of the system. The system's job is "user uploads something, something happens."

So the engineering team either skips dedupe entirely and treats every file as independent (a mistake in most cases), or they build dedupe logic and quietly decide it's not worth telling users that the old data gets overwritten. Then a customer says, "I had all this data, and now it's gone."

It gets worse from there. It turns out the dedupe logic doesn't just overwrite the uploaded file, it also resets the item's status to "new," which invalidates all the downstream data that had already been processed against it, because a "new" item can't have processed metadata. The system assumed a deduped file was something the user wanted to act on again, so it wiped everything downstream.

That's a decision an engineer made because the upfront requirements were ambiguous about dedupe, and dedupe wasn't something anyone thought to make explicit. Whether it was a person or an LLM that made the call doesn't really matter. Something decided this behavior was acceptable, and now the go-to-market team is looking at a system that isn't "done," while the engineering team is being told to reopen work they believed was finished.

## The debrief, and why LLMs finally make it cheap

The fix isn't a more perfect spec. Unknowns come up. Decisions get made in the day-to-day that nobody could have front-loaded. The fix is running a debrief once a project is declared complete: pull the original job to be done, pull the initial understanding of the workflow (even if it was high level), pull the actual code, and compare them. Where did we drift? Are we comfortable with that drift?

This won't catch everything, and it won't stop bad decisions. Sometimes you'll look at a drift, decide it's fine, ship it, and then customers hit it and you realize it wasn't fine. That's okay. The difference is there are no hard feelings, because everyone looked at the decision together and agreed to move forward with it. It's known. It's understood. It might get revisited. What's actually corrosive isn't a bad trade-off, it's a surprise.

This kind of review used to be expensive. It meant someone reading every implementation detail and tracing it back to a design doc, which is exactly the kind of tedious cross-referencing that gets skipped under deadline pressure. In the age of LLMs this should be a lot more tractable. It's not a per-PR review, a single PR is usually too granular to see the shape of a drift. It's closer to something done at project completion: take the epic or the project from Linear or Jira, take the original context document and the conversations that shaped it, and compare that against everything the code actually does.

> [!tip] The drift debrief
> Run this once a project is marked "done," before it's actually closed:
> - Pull the original ask: the job to be done, and the initial (even if high-level) description of how the workflow would work.
> - Pull everything that got built: commits, PRs, tickets grouped under the project.
> - Compare them and name every place they diverge, especially logic and gates (dedupe, validation, edge-case handling) rather than headline features.
> - For each divergence, decide explicitly: are we comfortable with this trade-off? Who needs to know?
> - Write the decision down. Not to protect anyone, just so it's known instead of discovered.

## The part that's easy to get wrong: nobody reads the digest

If you automate this as a weekly report, be careful about notification fatigue. In practice, the number of people who actually read a recurring digest is low, even though everyone says they want it. If a project takes a month, you'll get three weeks of digests with no action taken on any of them, and the notification gets seen and ignored, because it's rarely the week something meaningful actually changed.

An LLM can help here too, not by sending more updates, but by judging when a divergence is actually worth surfacing and to whom. That still requires someone to do the unglamorous work outside the tool: define the project, define who cares about it, define who should be notified when something drifts. That's not something ticketing gives you for free. Most PMs also don't want a thousand cooks in the kitchen; if you ask people whether they want to be looped in, they'll say yes, and then largely ignore it.

## Making it someone's job

This has to be a deliberate part of the process, because most engineering teams, not unlike LLMs, default to the path of least resistance. They want to finish the thing and move to the next thing. Asking "are you actually done?" after they've already called it done is inherently unwelcome, so it has to be enforced structurally, not left to goodwill.

Tactically, this is a PM-owned part of the launch checklist. Before a project moves from "built" to "done," the PM runs the debrief. On the go-to-market side, the model I've seen work best is a pod: SEs, including pre- and post-sales, paired with specific PMs, acting as the reviewer on that PM's work and the conduit back to the team on anything they're building. This works with a small team. I've done it with three people covering three engineering teams split roughly into core, platform, and infrastructure. If you're a team of one, you're just the default point of contact, which is still better than nothing.

Budget real time for it. Somewhere between an hour and a week per team per project, depending on the size of your engineering and product org relative to your go-to-market team. That doesn't feel like customer-facing time, but it is. These are the milestones that determine how well you can actually speak to customers about what's shipping, and the relationships built doing this work pay off in ways that don't show up on a calendar.

## Where this is heading

People try to front-load every risk and requirement into the initial doc, and that's unrealistic. Unknowns come up. Decisions get made in a vacuum by engineers working day to day, and I think LLMs are going to make that worse before they make it better, because it's now so easy to just accept a PR by its output and skip inspecting the actual code. Some of the nuance in how a user will really use a feature, and the intuition for where errors tend to hide, isn't something an LLM is particularly good at either.

Sticking your head in the sand and assuming perfect upfront requirements will prevent drift is wrong. So is deciding this kind of review is too hard to ever do well. It's actually not hard. It takes discipline, and that discipline comes from building it into your organizational process rather than hoping someone remembers to ask.
