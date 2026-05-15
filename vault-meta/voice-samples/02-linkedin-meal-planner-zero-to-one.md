---
platform: linkedin
url: https://www.linkedin.com/feed/update/urn:li:share:7345508478037217280/
author: Giovanni Briggs
date_published: ~2025 (post id 7345508478037217280)
date_captured: 2026-05-14
form: long-form LinkedIn post (~400 words)
purpose: voice anchor — long-form LinkedIn / narrative-led technical voice
---

# Voice anchor — what to learn from this post

**Opening move:** a generalized observation followed by a sharper restatement — "people don't always pick the best tool for the job. They pick the one they can get from 0 to 1 fastest with. And really what that means is they pick the tool that makes debugging errors the least painful." The third sentence is the actual thesis; the first two earn the reader's attention.

**Narrative as evidence.** The whole middle is a side-by-side product comparison (v0 vs Claude) with verdicts. Not abstract; not hypothetical. Specific apps, specific failures.

**Concrete personal detail with bite.** "I'd rather listen to my son's battery-powered, light up coffee cup sing on repeat than think about what to make for dinner ('red, orange yellow... green and blue... put some purple in there too...')." This isn't a writerly flourish — it's lived-in. Makes the post feel like a person, not a brand.

**Vivid metaphors with attitude.**
- "V0's looked like a VC pitch deck where I'm asking for money to eliminate risk and increase revenue in every household in America."
- "Claude's looked like a website made by an intern in 2014 who just learned Bootstrap."
- "I'd be eating turkey meatballs into eternity."

These all land because they're *specific* — the year (2014), the framework (Bootstrap), the meatballs.

**Technical specifics assume reader can parse them.** Mentions hardcoded timers, code comments like "in a real app...", network requests, browser dev tools. Doesn't dumb it down for non-engineers.

**Numbered bullet break** after a long narrative — two failures, terse. Used as a structural pivot, not as the main scaffolding.

**Closing principle, quotable.** "Any tool is judged by how quickly users go from 'I have an idea' to 'here's a working version.' Feature checklists only get you from 0→0.3. How a tool handles errors determines if you make it the rest of the way."

The "0→0.3" specificity (instead of "almost there" or "halfway") is the kind of move that makes a line repeatable.

# Original post text (verbatim)

> In my experience, people don't always pick the best tool for the job. They pick the one they can get from 0 to 1 fastest with. And really what that means is they pick the tool that makes debugging errors the least painful. An example where this came up -- I hate meal planning. I'd rather listen to my son's battery-powered, light up coffee cup sing on repeat than think about what to make for dinner ("red, orange yellow... green and blue... put some purple in there too... swirl around... mix it up... pour a latte in my cup!"). So I asked Vercel's v0 and Claude's AI-powered app creator to build me a meal planning tool. Both created very reasonable looking apps on first pass. V0's looked like a VC pitch deck where I'm asking for money to eliminate risk and increase revenue in every household in America. Claude's looked like a website made by an intern in 2014 who just learned Bootstrap, but on the surface it checked all of the boxes. Then I tried to actually use them. Most of the functionality in the V0 app was a series of different hardcoded timers to simulate "thinking" and action; complete with comments in the code saying "in a real app..." Claude hardcoded sample data, so it kept returning the same 3 recipes over and over. I'd be eating turkey meatballs into eternity. What was extra interesting about Claude was that it built an app that could theoretically talk back to Claude - meaning I could ask my meal planner to generate new recipes on demand. But despite writing all the code for this feature, Claude never actually connected it to the user interface. So I was stuck with the same hardcoded recipes instead of the dynamic functionality it had promised. When I tried to fix Claude's app, it rapidly iterated on 7 versions on its own before I had the opportunity to actually try it. Then came "Unexpected errors" with zero context. I had to leave the desktop app and go into the browser dev tools to see what was happening and discover that there was an issue with a network request it was making. At one point Claude complained... about Claude not returning the right structure of data back in its responses.
>
> There were two failures here:
>
> 1. Beautiful vaporware with no guidance on how to test if it actually worked inline with the specification I had provided, or how to expand on the initial creation
> 2. Technical errors I couldn't access or reason about
>
> Any tool is judged by how quickly users go from "I have an idea" to "here's a working version." Feature checklists only get you from 0→0.3. How a tool handles errors determines if you make it the rest of the way.
