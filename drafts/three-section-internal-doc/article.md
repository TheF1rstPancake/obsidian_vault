---
title: "The three-section internal doc"
slug: three-section-internal-doc
status: shaping
target: ghost
created: 2026-07-21
updated: 2026-07-21
tags: [writing, communication, templates, how-to]
visibility: public
related: ["unlearning-the-five-paragraph-essay"]
point: >
  Collapse any internal doc to three sections: the problem, stated in the
  first line with no quantified justification piled on as preamble; goals and
  non-goals, naming outcomes wanted and what's explicitly out of scope; and an
  optional recommended solution, framed as a flowchart rather than prose.
  Everything else (anecdotes, deeper analysis, a prototype) goes in a
  collapsible drawer at the bottom. Companion to Unlearning the five-paragraph
  essay; this piece is the mechanics and a worked example.
ghost_url:
---

# The three-section internal doc

*Companion to [Unlearning the five-paragraph essay](/unlearning-the-five-paragraph-essay/). That piece argues why leading with the conclusion beats litigating every objection first.*

## Section 1: the problem

The mistake people make is spending paragraphs on problem setup. *We've experienced this, and this, and the other, which leads to these issues, and the root cause of that is…* That's a lot of building and framing to arrive at the point. Flip it. State the problem in the first line, very clearly.

Don't write "we've experienced enterprise customers who get nervous about the product." Write it as an opening statement:

> Customers are increasingly asking for role-based access controls. We don't have them. That gap is causing friction in the sales cycle, because it's something enterprises expect and we can't confidently answer, which adds doubt. It also threatens renewals: as people use the product more, they want fine-grained controls we can't offer, which causes frustration and makes them evaluate alternatives.

That's the whole problem statement. Notice what it skips: qualitative or quantitative justification piled on as preamble. The instinct is to reach for a number ("30% of deals stall"), but the moment you do, people either debate how you got the number, or, if you leave it out, ask how big the problem really is. Extra context, piled on before the point lands, tends to invite argument rather than settle it. The point is to say: this is a problem, and you need to trust me, as the person closest to it, that I've correctly identified it as one. The supporting detail is real and you'll likely need it in conversation, but it lives later in the document, as a follow-up, not as preamble.

One more discipline: the presentation of the problem should not demand its prioritization. You want people to agree that it's a problem. Whether and when it gets worked on comes second. A lot of people try to force problem identification, solution recommendation, *and* prioritization into one essay. Treat them as three distinct steps in a larger process.

## Section 2: goals and non-goals

I prefer goals over requirements; they're close enough to lump together. The idea is to outline the outcomes you want, given that most problems are broad and have many ways to be solved. Goals shouldn't be "win more deals." There are a hundred ways to win more deals, and you don't strictly need role-based access controls for any of them. Aim instead at what it actually means to solve *this* problem. User stories are the right register: users need to be able to do X, Y, and Z.

The most important and most underused part is non-goals. This is where you put things in a box and stop people from playing the thousand-question what-if game. You say, explicitly: I've reviewed this, I've thought about it, this is what I think is meaningful, and this is what can be meaningfully left out. If people are going to push back anywhere, it'll be here, and that's good, because this is what becomes the scope the technical solution gets built against downstream.

Don't get cute. One bad habit people pick up from SaaS writing is parading every assumption they made to bucket the solution together. That just invites more debate. The nice thing about goals and non-goals stated plainly is that they feel concrete and actionable, which is the point. Someone should be able to read this and either do it themselves or hand it to an LLM. Don't create more surface area for confusion.

## Section 3: the recommended solution (optional)

A recommended solution is nice to have, not the end of the world if it's missing. If you include one, frame it as a flowchart: the if-this-then-that logic you're going after. Building diagrams is an underrated skill, and I find it's a red flag when someone can't do it. It usually means they're good at spouting problems but have no framework for solving them. No framework for solving means no framework for prioritizing: no way to weigh cost against value, no way to ask whether the juice is worth the squeeze.

Even the collapsed version of the doc might be too much for some readers; an image lets them glance and get a sense of how users are meant to interact with what you're building, or what internal systems you'd build to hit the goals. That's it. Those are the three sections.

## Everything else goes in a drawer

After the three sections, you probably have a lot more: customer anecdotes, a prototype you threw together, deeper analysis. Put all of it in a collapsible "other context" section at the bottom. People are welcome to open it and engage. Most won't, and that's fine. You don't want them to have to learn everything you learned in order to participate in the conversation. That's the entire reason you collapsed it down to three short sections in the first place.

> [!tip] The thirty-second test
> Try the collapse cold on your next internal doc. If a reader can't tell what you want from them within thirty seconds, it isn't done, no matter how much supporting material sits below the fold.
