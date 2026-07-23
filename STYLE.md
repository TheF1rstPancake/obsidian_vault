# STYLE.md — voice and editing guide for The Burnt Pancake

Canonical style guide for articles in this vault. Required reading before **shaping** or **editing** any `drafts/<slug>/article.md`, and the spine of the editor pass in `scripts/article_pipeline.py`.

This document is for **writing and editing judgment**. It is not the full publishing or ops manual. Workflow mechanics, Ghost quirks, annotation plumbing, and project-specific tooling live in `CLAUDE.md` and the project references. Keep STYLE.md focused on how the prose should think and sound.

This guide is grounded in two things: the verified voice samples in `vault-meta/voice-samples/`, and the recurring corrections Giovanni has left in `~/.hermes/annotations.json` and the editor voice audit. When the two conflict, the annotations win — they are the most direct signal of what he actually wants.

The blog is **The Burnt Pancake**. The posture is humility, not authority: experiments, mistakes, frameworks that held until they didn't. The reader should be able to follow the logic, disagree with a step, and still get value. Nothing here is doctrine. "Don't blindly follow this advice for all situations. Just most."

---

## 0. Operator layer — the non-negotiables

Use this as the fast pass before you touch prose.

1. **Lead with the claim or the problem.** No throat-clearing.
2. **Preserve the real conceptual hierarchy.** Do not replace the article's actual argument order with a cleaner consulting-shaped substitute.
3. **Prefer conditional logic over doctrine.** If the claim depends on an `if`, keep the `if`.
4. **Cut interstitial lead-ins.** Do not announce the next paragraph; just make the move.
5. **Say each load-bearing point once.** If it already landed, cut the remake.
6. **Prefer direct concrete claims over scaffolding.** Say the thing instead of circling it.
7. **Name the actual referent.** If two products/systems are in play, no mushy bare `the product`.
8. **No invented ceremony.** Do not add revision histories, scope-drift logs, renewal-protection sections, or official-looking process for its own sake.
9. **Wrap; don't re-litigate.** The close gets one new check, inversion, or implication — not a second tour.
10. **Preserve recognizability over perfection for live pieces.** Fix blockers with the smallest edit that clears them.

If an edit violates one of those, it is probably wrong even if it sounds cleaner.

---

## 1. Core voice

- **State the punch upfront.** Lead with the claim or the problem, not a ramp. The AI-coding post opens "Software has always just been if-this-then-that thinking wrapped in special syntax." No throat-clearing.
- **Personality comes from specifics, not adjectives.** "Donut vodka into Pepsi turns into vanilla Pepsi." "Retro arcade vibes with neon colors." Never "I was a goofy kid" — show what the kid was actually doing. When you reach for an adjective ("powerful", "robust", "seamless"), replace it with the concrete thing that earned the adjective.
- **Conditional reasoning is the spine.** Giovanni's natural structure is "if X then Y." Articles should earn authority by logic the reader can follow, not by asserted confidence.
- **Name the default assumption before the chain.** Before any if/then, state the ground truth it rests on. These passages are load-bearing, not filler.
- **First person is honest, not unprofessional.** "I keep coming back to…", "Here's what gets me…" signal a real person thinking. Use them.
- **Write the same personally and professionally.** The wedding vows and the LinkedIn posts use the same moves. Don't put on a fake business register for articles.

---

## 2. Blocking issues — fix these, do not hand-wave them

These are not preferences. They are the recurring ways AI edits miss Giovanni's voice or break the article's logic.

### 2.1 Structure and argument integrity

- **Every section earns its place.** If a heading or section doesn't pay off in the body, cut it.
- **Preserve the real conceptual hierarchy.** When the source establishes an order — e.g. customer goals → solution-agnostic requirements → vendor solution, *then and only then* — keep it.
- **One clear lens beats bloated total theory.** If the article is trying to explain the whole domain, cut scope or split it.
- **Split essay vs playbook when both are load-bearing.** A thought piece plus a Monday-morning operating manual in one file is usually two posts.
- **Publish from stable observations, not final beliefs.** Ship what is defensible and useful now. New nuance can become the next post.

### 2.2 AI-shaped prose failures

- **Cut interstitial lead-ins and bland transitions.** Kill sentences like "There's a sharper version of that mistake worth calling out on its own," "Start with the assumption underneath," or "X is, in retrospect, a case study in this." Prefer the direct move.
- **Prefer the concrete claim over generic scaffolding.** If a sentence is hedging around the point, delete the scaffolding and say the thing.
- **Say each load-bearing point once.** Repeating the same insight in punchier words usually makes the section less clear, not more emphatic.
- **No leaked meta-commentary.** Nothing about the drafting process, earlier versions, or the recording belongs in `article.md`.
- **Don't compress the point past the reader.** If a sentence uses stacked metaphor, vague referents, or abstract phrasing that forces the reader to reverse-engineer the claim, rewrite it into direct prose.

### 2.3 Precision of terms and claims

- **Preserve load-bearing distinctions; don't synonym-swap.** `In scope / out of scope` is not `needs / wants`. `Solution-agnostic requirements` is not `high-level summary`.
- **Name dual products when both are in play.** If the customer-facing paid offering and an internal system share the stage, define short names up front and use them consistently.
- **Keep load-bearing if-conditionals.** Do not promote a conditional claim into a universal prescription by stripping the `if`.
- **Prefer conditional or situational claims over doctrine.** Replace unsupported universals with mechanism the reader can follow: "If a team does X without Y, Z tends to happen."
- **Don't fabricate authority.** No fake experts, reports, studies, or plausible-looking statistics.
- **Each claim must support itself.** Every statement should be factually grounded or logically derivable from a stated premise.

### 2.4 Ending and recognizability

- **Wrap; don't re-litigate.** The ending should not take a second lap through the framework.
- **Long pieces need synthesis before the close.** If the article is long and multi-section, add a short synthesis section before the final paragraph.
- **Preserve recognizability over structural purity for live pieces.** If a fix would make a published or flagship piece feel like a different article, prefer the smaller fix. Keep the memorable bits.

---

## 3. Strong preferences — default to these unless the article gives you a reason not to

### 3.1 Rhythm and punctuation

- **Reduce em dashes.** Overuse reads as AI-coded. Prefer periods, commas, parentheses, and cleaner sentence boundaries.
- **Staccato is fine, often better.** Short declarative sentences are not a bug.
- **Vary sentence length on purpose.** Don't let every sentence land the same way.
- **Avoid `it's not X, it's Y`.** State the positive claim directly.
- **Repetition can beat intensifiers.** "Try really, really, really hard" sounds more human than a flattened adverb.
- **Straight quotes, sentence-case headings, no decorative emoji, no mechanical boldface.**

### 3.2 Personality and specificity

- **Keep the weird, concrete analogies.** If a memorable analogy works, don't sand it down into generic business prose.
- **Specifics over adjectives.** Replace abstract praise words with the thing that earned them.
- **Self-awareness should be restrained and analytical, not confessional.** The tone is clinical, not dramatic.
- **Specific admissions land; vague admissions read as performance.** Name the failure mode, what was missed, the cost, and what changes.
- **Name internal trade-offs instead of hiding them.** If the framework has a tension, say so.

### 3.3 Publish posture

- **Useful enough to ship beats permanently unfinished.** If the draft is being held because the model might keep updating, that is usually a ship signal, not a rewrite signal.
- **New nuance → next post.** Do not suppress a good article because the model is still growing.
- **A quotable closing inversion is good.** If it lands the thesis cleanly, keep it.

---

## 4. Tactical artifacts and practical guidance

- **Default to including something the reader can steal.** A framework, question bank, checklist, decision matrix, or before/after example often earns the share more than the abstract thesis alone.
- **Don't strip a tactical section just to sound smarter.** If both the thesis and the artifact fit, keep both.
- **Set artifacts off cleanly.** Use typed callouts like `> [!tip]`, `> [!note]`, or `> [!warning]` where appropriate. Thought pieces should usually prefer footnotes to note callouts; pick one format per article.
- **Callouts add; they don't apologize.** If a note says "to be fair" or "I don't mean X," the body needs editing.

---

## 5. Guide and playbook expectations

- **A guide is a stealable resource, not a bureaucratic template.** It should help the reader do the thing, not look impressive.
- **Customer-first, not vendor-first.** Define the problem and the solution-agnostic requirements before naming the vendor solution.
- **Match the blueprint article.** Before building or rebuilding a guide, read the article that defines its framework and make sure the structures agree.
- **Cut the ceremony.** No revision-history sections, scope-drift logs, or renewal-protection logs unless explicitly requested.

---

## 6. Editing checklist

### 6.1 Blocking checks
- [ ] Opens with the claim or problem; no throat-clearing.
- [ ] Conceptual hierarchy matches the source; no consulting-shaped substitutions.
- [ ] No interstitial lead-ins or bland transition sentences.
- [ ] No point remakes; each load-bearing point lands once.
- [ ] Direct claims replace generic scaffolding where the prose was circling the point.
- [ ] If two products or systems are in play, each has a clear short name.
- [ ] Load-bearing `if` clauses are preserved; claims are not overstated into doctrine.
- [ ] No synonym-swaps on terms carrying the argument.
- [ ] No leaked meta-commentary, fake authority, or fabricated statistics.
- [ ] The close wraps with a new check or implication instead of re-litigating earlier sections.

### 6.2 Strong-preference checks
- [ ] Em dashes reduced; punctuation and rhythm feel human.
- [ ] Specifics beat adjectives; memorable analogies are preserved.
- [ ] Vulnerability is restrained, analytical, and specific.
- [ ] Tactical artifacts are present where they genuinely help.
- [ ] Callouts add value instead of apologizing for the body.

### 6.3 Publish checks
- [ ] `target: ghost`; `point:` populated when required; `updated:` bumped.
- [ ] No `[?]` markers, no notes-to-self sections, no wikilinks in the body.
- [ ] The article ships from stable observations, not a need to become a final manifesto.
- [ ] Scope is clear: one lens, or a clean split if both essay and playbook are load-bearing.
- [ ] For live or flagship pieces, edits preserved recognizability while clearing the blocker.
