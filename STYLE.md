# STYLE.md — voice and editing guide for The Burnt Pancake

Canonical style guide for articles in this vault. Required reading before **shaping** or **editing** any `drafts/<slug>/article.md`, and the spine of the editor pass in `scripts/article_pipeline.py`.

This is grounded in two things: the verified voice samples in `vault-meta/voice-samples/`, and the recurring corrections Giovanni has left in `~/.hermes/annotations.json` and the editor voice audit. When the two conflict, the annotations win — they are the most direct signal of what he actually wants.

The blog is **The Burnt Pancake**. The posture is humility, not authority: experiments, mistakes, frameworks that held until they didn't. The reader should be able to follow the logic, disagree with a step, and still get value. Nothing here is doctrine. "Don't blindly follow this advice for all situations. Just most."

---

## 1. Core voice

- **State the punch upfront.** Lead with the claim or the problem, not a ramp. The AI-coding post opens "Software has always just been if-this-then-that thinking wrapped in special syntax." No throat-clearing.
- **Personality comes from specifics, not adjectives.** "Donut vodka into Pepsi turns into vanilla Pepsi." "Retro arcade vibes with neon colors." Never "I was a goofy kid" — show what the kid was actually doing. When you reach for an adjective ("powerful", "robust", "seamless"), replace it with the concrete thing that earned the adjective.
- **Conditional reasoning is the spine.** Giovanni's natural structure is "if X then Y." Vows: "In order to continue this successful partnership: I promise to…" Articles: "If a team does X without Y, the result tends to be Z." Authority comes from the reader following the chain, not from asserted confidence.
- **Name the default assumption before the chain.** Before any if/then, state the (usually uncontroversial) ground truth it rests on. These passages are load-bearing, not filler.
- **First person is honest, not unprofessional.** "I keep coming back to…", "Here's what gets me…" signal a real person thinking. Use them.
- **Write the same personally and professionally.** The wedding vows and the LinkedIn posts use the same moves. Don't put on a "business" register for articles.

## 2. Article shape

- **Open with the thesis or the problem.** For thought pieces, lead with the claim. For practical pieces, lead with what the reader walks away with.
- **Every section earns its place.** If a section or heading doesn't pay off in the body, cut it. Giovanni's most frequent note is some form of "Cut. It adds nothing" or "we never really come back to this idea."
- **Preserve the real conceptual hierarchy.** Don't swap the article's actual argument order for a plausible consulting-shaped substitute. When the source establishes an order — e.g. customer goals → solution-agnostic requirements → vendor solution, *then and only then* — keep it.
- **Land the close.** Don't trail off into a list or a red-flag line. Long pieces (1500+ words) need a short synthesis section before the closing paragraph; the closer concludes (what the framework makes possible) rather than re-summarizing.
- **Wrap; don't re-litigate.** The last section is allowed one concrete check or inversion the reader can steal. It is not a second pass over the Lego kit / three questions / architect tier. If the last ~200 words could vanish without losing a *new* claim, cut them or replace with a short wrap.
- **Quotable closing inversions are good.** "AI coding agents handle the syntax. You handle the outcomes." Parallel structure built to be quoted.

## 3. How Giovanni disagrees with AI framing

These are the corrections that come up again and again. An editor pass should treat each as a blocking issue, not a nicety.

- **Cut interstitial lead-ins and bland transitions.** Kill sentences whose only job is to announce the next paragraph: "There's a sharper version of that mistake worth calling out on its own.", "Start with the assumption underneath.", "X is, in retrospect, a case study in this.", "But there's a deeper problem that…", "Drawing the line here is useful mostly because…". Prefer the direct move: "We saw this at Airtable." / the claim itself.
- **Prefer the concrete claim over generic scaffolding.** If a sentence hedges around the point ("that sharpens where the line between the two teams falls; it doesn't erase that line so much as move it up a layer"), delete the scaffolding and say the thing: "More and more, that thing is an AI agent." / "Harness is core. Prompt engineering and tools development is FDE."
- **Say each load-bearing point once.** Remaking the same insight in punchier form three paragraphs later ("the team that needs the pain to be sharp…") makes the section *less* clear. If the point already landed, cut the remake.
- **Cut framing that doesn't advance the argument.** Dramatic headings, clever wrappers the piece never cashes, "throat-clearing" intros. If the heading reads like a directive ("Lead with which workflows break first") but the body delivers one example, fix the header or the body — don't ship the mismatch.
- **Reject invented ceremony.** Do not add revision histories, scope-drift logs, renewal-protection sections, "official"-looking process artifacts because they look professional. Real example: "Revision history is super optional. You get it for free in any web-based word processor." If email threads or a simpler artifact would do, prefer them. Practical guides should be useful and stealable, not inflated into bureaucratic templates.
- **Preserve load-bearing distinctions; don't synonym-swap.** "In scope / out of scope" is *not* "needs / wants." "Solution-agnostic requirements" is *not* "a high-level summary." If a term carries the argument, keep it exactly.
- **Prefer conditional/situational claims over universal doctrine.** Replace "most teams enormously underinvest" or "this is where X really earns its keep" with "if a team does X without Y, Z tends to happen." Avoid "always do X" unless the source genuinely supports it. Prefer "in most situations," "when X is true," "this tends to."
- **Don't compress the point past the reader.** If a sentence uses stacked metaphor, vague referents, or abstract phrasing that makes the reader reverse-engineer the claim, unpack it into direct prose.
- **Keep the weird, concrete analogies.** The "horoscope version" analogy survived because it worked. Don't sand memorable specifics into generic business prose to sound smarter.
- **Don't fabricate authority.** No "experts argue," "industry reports," "studies show" without a real, named source. No invented statistics or plausible-but-fake citations.
- **No leaked meta-commentary.** Nothing about the drafting process, earlier versions, or the recording ("as I mentioned", "the weakest-argued part of the earlier draft"). That belongs in `notes.md`.

## 4. Punctuation and rhythm

- **Reduce em dashes.** Overuse "screams written by AI, which causes a lot of people to take it less seriously." Rewrite most dashes as periods, commas, or parentheses.
- **Staccato is fine, often better.** Short declarative sentences. A two-word beat after a long setup ("Now it's gone.") is a deliberate move, not a problem.
- **Vary sentence length on purpose.** Escalating-then-falling lengths. Don't let every sentence land the same way — that reads as machine-paced.
- **Avoid "it's not X, it's Y."** Say the positive claim directly. "Isn't a downgrade; it's the point" is weak by default.
- **Repetition can replace intensifiers.** "Try really, really, really hard" reads more like a person than "try extremely hard."
- **Straight quotes, sentence-case headings, no decorative emoji, no mechanical boldface.** (See the humanizer skill for the full AI-tell checklist.)

## 5. Vulnerability

- **Restrained and analytical, not confessional.** The target is "not dramatically, but clinically." Admit uncertainty or a mistake when it serves the argument; don't turn the piece into emotional performance.
- **Specific admissions land; vague ones read as performance.** Not "I've probably missed people" but: name the failure mode → name what you missed → name the cost → name what you'd do differently (or admit you're still working on it).
- **Self-deprecation through distance works.** "21-year-old Gio had a lot of room for growth" creates comic distance without earnestness. Useful when a piece needs to be self-critical.
- **Name internal trade-offs instead of hiding them.** "At the risk of a slight contradiction…" When a framework has a tension, say so.

## 6. Tactical artifacts

- **Default to including something the reader can steal** — a decision matrix, checklist, question bank, framework, before/after example. The reframe earns attention; the artifact earns the share.
- **Don't strip a tactical section to sound punchier or more contrarian.** If both the thesis and the artifact fit, include both. Pure-thesis pieces are fine when the article genuinely is about the idea — but cutting tactical content *to sound smarter* is the wrong instinct.
- **Set artifacts off with typed callouts.** `> [!tip]` for a steal-this artifact, `> [!note]` for an aside too important to cut, `> [!warning]` for a caveat. Author the syntax, never hand-write callout HTML. (Thought pieces: prefer footnotes over `[!note]`; pick one format per article.)
- **Callouts add, they don't apologize.** If a callout says "to be fair" or "I don't mean X," the body needs editing, not a footnote.

## 7. Guide / playbook expectations

- **A guide is a stealable resource, not a bureaucratic template.** It should help the reader do the thing, not look impressive.
- **Customer-first, not vendor-first.** The recurring failure mode for the solution-design guide: it was organized around the vendor's solution from section 1, when the framework requires customer goals and solution-agnostic requirements *before* any product language appears. Define the problem before naming the solution.
- **Match the blueprint article.** Before building or rebuilding a guide, read the article that defines its framework and name the structural mismatch explicitly. A guide written without reading the article inherits the article's-substitute structure.
- **Cut the ceremony.** No revision-history sections, no scope-drift logs, no renewal-protection logs unless the user asks. Their presence doesn't add protection; the document existing is enough.

## 8. Editing checklist

Run this on any shaping → ready pass, or as the editor rubric.

**Voice & AI tells**
- [ ] Em dashes reduced; staccato where it helps.
- [ ] No "it's not X, it's Y." Positive claims stated directly.
- [ ] No invented "experts/studies/reports" or fake statistics.
- [ ] Specifics over adjectives; weird analogies preserved.
- [ ] No leaked meta-commentary about drafting or recordings.

**Argument integrity**
- [ ] Conceptual hierarchy matches the source; load-bearing distinctions intact (no synonym-swaps).
- [ ] Claims are conditional/situational, not universal doctrine, unless the source supports universality.
- [ ] Every default assumption is named before the if/then chain that needs it.
- [ ] Each claim supports itself — grounded or derivable from a stated premise.
- [ ] No compressed abstraction: stacked metaphors and vague referents are unpacked into direct prose.

**Structure**
- [ ] Every section and heading pays off in the body; cut what doesn't advance the argument.
- [ ] No interstitial lead-ins or bland transitions; next claim starts cold.
- [ ] No remakes of a point the section already established.
- [ ] No invented ceremony (revision history, logs, official process) where a simpler artifact would do.
- [ ] Sections connect; no hard stops. Long pieces have a synthesis section before the close.
- [ ] The close wraps with a new check/inversion; it does not re-litigate earlier sections.

**Tactical & vulnerability**
- [ ] A stealable artifact is present where it fits (and wasn't cut to sound punchier).
- [ ] Callouts add rather than apologize; one format per article.
- [ ] Vulnerability is clinical, not confessional; admissions are specific.

**Publish-readiness** (see `vault-writing` skill for the full list)
- [ ] `target: ghost`; `point:` populated (required >1500 words); `updated:` bumped.
- [ ] No `[?]` markers, no notes-to-self sections, no wikilinks in the body.
