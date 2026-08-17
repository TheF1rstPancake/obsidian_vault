---
title: "I built a voice-memo-to-Substack pipeline so I'd actually publish"
slug: voice-to-substack-pipeline
status: shaping
target: ghost
created: 2026-05-07
updated: 2026-08-17
tags: [build-in-public, ai, writing]
---

# I built a voice-memo-to-Substack pipeline so I'd actually publish

## The thesis

I had article ideas for years and never published them. The bottleneck wasn't writing, it was capture. By the time I sat down at a keyboard, the spark was gone. So I built a pipeline: voice memo whenever an idea hits → Whisper transcribes it on a homebrew server → an agent shapes a draft → I rewrite and argue with it → publish. Building the pipeline taught me more about my own bottleneck than years of "I should write more" ever did.

Then I published the Airtable article, someone posted it on Twitter, and the reaction taught me something else: most of the resistance to this workflow isn't really about AI quality. It's about what AI makes visible.

## Why people don't publish, and how the pipeline gets around each one

Three things kept me from putting ideas out before this existed, and I don't think I'm unusual here.

**Perfectionism.** Writing takes effort, and it's very easy to get caught in a loop of constant tweaking. Every time you reread a draft there's one more thing you could change, one more idea that could be sharper. Some posts on this blog sat as drafts for months before I published them. That loop convinces you the piece isn't ready, when really it's just never going to feel ready.

**"Hasn't someone already said this?"** You assume some other, sharper person has already put the thought to paper, so what are you really adding? I don't want to add junk to a pile that's already full of junk, so figuring out whether what you're pulling together is actually your own perspective, and not just a repackage of something already well understood, is its own kind of paralysis.

**Fear of the reaction.** It's easy to point out inconsistencies or failures in someone else's writing. Imagining people think you're an idiot, or that they'll vehemently disagree, or that it exposes real gaps in your own understanding, that's uncomfortable, even when there's genuine learning on the other side of it.

The pipeline doesn't solve any of these by making me a better writer. It solves them by lowering the cost of finding out whether the idea was worth having in the first place.

## What actually happened when I published

The Airtable article got real pushback. Someone posted it on Twitter, and the loudest reaction was some version of "this is AI slop somebody threw together." What's interesting is where the positive reactions landed: I got messages that were genuinely thoughtful, "this was really helpful," but they came in privately, DMs and texts from people I know, while the public reaction skewed toward dismissiveness. I don't think that gap reflects the quality of the piece so much as how much easier it is to publicly dunk on something than to publicly say it helped you.

Someone ran two paragraphs of it through an AI detector. The result: not enough characters to confirm, but it also looks like AI. Sure. Any short snippet has a decent shot at reading as AI, because I *am* using AI to fill in the gaps I struggle to articulate on my own, especially openings. That's the part of my writing I'm weakest at, and the part I lean on the agent for the most. Read the first couple lines of most of these pieces and that's probably the most "AI" thing on the page.

## The actual stack

A voice recording on a walk gets forwarded to a homebrew server running Whisper, which transcribes it [?] (the capture app itself is still fuzzy in the recording, need to confirm the exact tool). Traditionally, the hardest part of sitting down to write something is figuring out where to start. It spawns from some tangential thought, and if you're doing that from a keyboard you're trying to brain-dump and structure at the same time. Talking into my phone for fifteen minutes strips that apart. It doesn't mean every recording is usable. Sometimes I read the transcript back and think "what the fuck was I talking about," and just rerecord. But at its best, a recording is a fully contained thought, and that thought, my actual voice, feelings, reasoning, is the backbone of the article.

From there a prompt feeds the transcript, plus any smaller related transcripts, into an agent. Its job is to find the common thesis across the disparate thoughts and build a first draft using my style guide.

This is where a lot of people stop. They get a draft, it's got a clean five-paragraph structure, and they ship it. I don't. I treat that draft almost like a shared doc: I rewrite significant chunks myself, and I leave comments in the margins, "interesting idea, explore further," "this is dogshit, cut it," "you latched onto a side quest here." Those edits and comments get fed back into the agent and we go back and forth until the article actually encapsulates the idea, not just a passable imitation of it.

The other thing that loop does is research. Part of the agent's job on the first pass is checking whether other people have said something similar, and if so, whether my angle is actually different. Plenty of times it's come back and told me I'm just regurgitating something the rest of the market already understands, it's just new to me. That's useful validation, not a failure. It means the fifteen minutes of talking did its job of clarifying my own thinking, even if the piece never gets published.

> [!tip] The loop, if you want to steal it
> - Record whenever the idea hits. One contained thought per recording, not a running list.
> - Self-hosted Whisper transcribes it.
> - An agent takes the transcript(s) plus a style guide and produces a first draft: finds the common thesis, imposes structure.
> - Treat that draft as a starting point, not a finished one. Rewrite the weak parts yourself, leave comments on the rest, feed it back, repeat until the piece says what you actually mean.
> - Have the same agent do a research pass: has this already been said, and by whom? If yes and you're not adding anything, shelve it. The recording still did its job.

The real benefit isn't the words the agent generates, it's that it gets me over the writer's block hump. It's almost always easier to react to something than to generate it from nothing, and giving feedback on a draft is a much lower barrier than staring at a blank page. That's what makes me willing to keep doing this instead of letting the idea die in a voice memo I never transcribe.

> [!warning] The one-shot trap
> Skip the rewrite-and-comment loop and just ship the agent's first draft, and you get a poor impersonation of your own ideas. Grammatically fine, decent structure, and empty. That's the legitimate half of the "AI slop" critique, and it's earned by people who treat the tool as a vending machine instead of a collaborator.

## Where the "AI slop" critique breaks down

You can't say, on one hand, "this is a genuine reflection of someone's experience," and on the other, "this is AI crap." It has to be one or the other. A piece can be poorly written. It can fail to communicate anything new. You can just not care about the person's experience. But wholesale dismissing something as fake because parts of it read as AI-assisted is a different claim, and most people making it haven't actually thought about which one they mean.

There's also a real irony here: a lot of the same people calling something AI slop went and used AI to summarize a document or answer a question thirty minutes later. That's functionally the same use of the tool, just pointed at consumption instead of production. I think a chunk of the reaction is a kind of superiority complex, "I don't use AI for that, I'm still cool and edgy," which is the same energy as "I don't use Google, I read the encyclopedia." It doesn't hold up.

One thing that is genuinely interesting about AI-assisted writing: if you hand it your rambling and it takes the idea somewhere you didn't expect, that's information. It means you weren't as clear a communicator as you thought you were. Comparing what I meant to what the agent actually understood has been a useful, if uncomfortable, way to see where my own communication is fuzzy.

> [!note] The version I'm not building
> There's a tempting, different version of this: train an AI to think like me, feed it current events, let it generate a constantly-growing library on autopilot. That's an interesting scale-and-efficiency problem, but it's not this project. That's throwing words into the void. This is about getting a genuine personal thought out of my head and into something someone else can actually engage with, not replacing the thought.

## The thesis, more precisely

There is a way to take a genuine, personal, half-formed thought and have AI help iterate, expand, and translate it into something other people can understand and want to engage with. Plenty of the barriers that keep people from sharing ideas, and from the reactions that follow, aren't really about the underlying idea. They're activation energy. AI can strip most of that away, but only if you actually understand the tool and hold yourself accountable for reading, editing, and iterating on everything it produces instead of treating it as one-shot. Treat it as one-shot and you get a poor impersonation of your own ideas: empty, and ultimately unhelpful, no matter how clean the paragraph structure looks.

## What to flesh out in future recordings

- The motivation collapse the first time around: built the pipeline, didn't use it for two months, what changed
- Full stack details beyond Whisper: Syncthing, Obsidian, cron, and why each piece earned its spot
- Confirm the actual capture app name (marked [?] above)
- The "many recordings, one article" mechanic in more concrete terms: notes.md as the lossless source, article.md as the polished output
- A LinkedIn-friendly hook: "I built a voice-memo-to-Substack pipeline. The first thing it taught me wasn't about writing."
