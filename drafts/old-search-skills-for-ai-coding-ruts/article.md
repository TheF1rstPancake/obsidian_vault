---
title: "Old Search Skills for When AI Coding Hits a Rut"
slug: old-search-skills-for-ai-coding-ruts
status: raw
target: substack
created: 2026-06-04
updated: 2026-06-04
tags: [ai-coding, claude, workflow, debugging]
---

This is a smaller one than some of my other ramblings. [?] I still need to figure out how this folds into the blog — where the line sits between long-form content and the daily, narrower stuff that might help a few people and be old news to everyone else. Maybe this is all obvious. But here it is anyway.

## The spiral

I was working on a problem today and found myself spiraling with Claude.

Don't get me wrong — Claude Code is great. It lets me do a lot of things I was never able to do before. But today it just could not get around a class of problems we kept running into. And I've noticed there's a very particular failure mode when this happens: Claude starts writing extremely targeted, one-off code aimed at the specific example in front of it. The logic is essentially, "How do I make this exact thing go away? I'll write custom code for this one case, declare it done, and move on."

The problem is obvious in hindsight. Sure, it works for that one example. Then you hand it the next case and you're sitting there going, *what the hell, why am I still struggling with this?* You've got a system that needs to be generic, and instead you're accumulating onesie-twosie fixes that don't generalize.

## Falling back to old skills

What I've found myself doing is reaching back for old Google and Stack Overflow skills.

Once upon a time, when you hit a problem — an error, or just the general shape of a problem — you'd Google it. And the *absence* of an answer told you something. If nothing came back, you were in one of two places:

1. You were onto something genuinely new and novel, worth exploring.
2. You were completely out in left field and needed to re-evaluate what you were even doing.

Our AI friends never give you that signal for free. They are *always* willing to try. They will always generate the code. They never come back empty-handed and force you to stop and reconsider.

## Forcing the signal back

You can say: just add a skill, just tell it not to do that. Fair — and honestly that's probably something I'll do, add some skill or gate that forces it to re-review its answers. But the deeper problem is that *everyone* would have to do that. By default these coding agents don't enforce it. So what we're going to end up with is a lot of people generating a lot of code that fits very few examples and never generalizes into a real skill or abstraction.

So when I'm in that rut, here's what's worked for me: I just ask it to go look online. "Will you please research this and find other people who have approached similar problems?"

And then the old signal comes back. If it returns and says *no one else seems to have approached this problem* — that's the same fork you used to get pre-Claude:

- Either you're onto something novel that's actually worth pursuing, and you can use the coding agent to build something that didn't exist before — frameworks for a problem that are genuinely easy to use.
- Or you're approaching the whole thing incorrectly and it's time for an architectural reset.

In my experience it is *far* more often the latter. Usually some earlier part of the conversation — some context you fed the bot — sent it down a path it now feels it can't recover from. And you probably aren't even aware of which requirement set it down that path in the first place.

That's the real value of forcing it to search. When you make it say "this doesn't seem like a unique problem, other people should have been able to do this," you force a reset. You re-evaluate your own requirements and what a *good* outcome from the conversation should even look like. More often than not, the bug is in how I framed the thing — either my own fault, or wires crossed somewhere with Claude.

## Stack Overflow isn't dead, the interface changed

This isn't earth-shattering or life-changing. But I keep coming back to it: the old tactics for navigating the web to find answers to programming problems still work.

We talk a lot about how the world has moved on — Stack Overflow is dead, etc. I don't think that's true. I think the *way we interface* with that information has changed.

Although it raises a real question. None of these questions and answers are getting reposted anywhere. So will the LLMs ever actually grow and learn from this new work? [?] Is there a world where Claude — or Anthropic — partners with Stack Overflow, and you opt into an experience where your questions and answers flow back into the public record for the good of internet code review and debugging at large? I think a lot of people would actually opt into that.

But for now, the skill that matters is the old one: *am I finding answers to my query?* Because if I'm not, it's one of two things — either my query is wrong (wrong context, wrong language, wrong framing to tee up the problem), or I'm onto something genuinely novel.

In my line of work, it is almost always the former. I've framed it incorrectly. And re-checking that expectation early is what keeps me making real progress instead of burning hours going back and forth on one-off fixes for a system that needed to be generic all along.
