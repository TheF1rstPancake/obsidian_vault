# Article clustering — recent recordings (2026-07-14)

Scan of pending thought threads from the last ~5 days of transcripts. Grouping only — no shaping pass.

## Sources reviewed

| File | Date | Already landed in |
|---|---|---|
| `transcripts/URecorder_20260709_084258_2026-07-09_074501.md` | Jul 9 | `decomposing-software-apps/notes.md` |
| `transcripts/URecorder_20260709_084546_2026-07-09_075001.md` | Jul 9 | `decomposing-software-apps/notes.md` |
| `transcripts/URecorder_20260710_113734_2026-07-10_104001.md` | Jul 10 | `capabilities-not-guesses-agentic-requirements/` (notes + raw article) |
| `transcripts/URecorder_20260711_091713_2026-07-11_082001.md` | Jul 11 | **misfiled** into `ai-native-se-stack/notes.md` (published SE-org piece — wrong home) |

**Same window, not yet transcribed** (excluded from grouping until they land):

- `recordings/URecorder_20260713_082704.m4a`
- `recordings/URecorder_20260713_084910.m4a`
- `recordings/URecorder_20260713_163132.m4a`
- `recordings/URecorder_20260714_082230.m4a`

No other Jul 10–14 transcripts exist beyond the four above.

---

## Distinct threads in the recordings

1. **Agentic requirements without users** — founding team freezes on "what to make agentic"; capabilities stay stable across current→future state; LLM fills ordering/intent at runtime. (Jul 10)
2. **"AI-native" means AI is the primary interface** — trap is "build for humans, then augment with AI"; execution should be LLM-first with human escalation; discovery of *what work to do* may still be human-led. (Jul 11)
3. **Three-layer lens applied to AI** — AI sits in the *logic* layer (API calls); interface swap is web UI → LLM chat. (Jul 9 both)
4. **APIs become first-party again** — action-oriented tools beat CRUD soup for LLMs; UI becomes control plane / observability, not the primary touchpoint. (Jul 9 long)
5. **Win as the tool of choice** when the LLM can pick you or a competitor. (Jul 9 short, closing beat only)

---

## Proposed groups

### A. Keep / finish — `capabilities-not-guesses-agentic-requirements` (exists, `raw`)

- **Type:** practical
- **Working title:** Capabilities, Not Guesses: Requirements in the Agentic Era
- **Owns:** thread 1 only
- **Why alone:** Different job than the AI-native thesis. This answers "how do we decide what to build when we have no users?" with a stealable requirements stance (current state → capabilities → agent fills combinations → observability decides what to harden). Stuffing it into a philosophy piece would bury the artifact.
- **Bridge, don't merge:** the closing beat ("capabilities become APIs, not pages") is a handoff to Group C/D, not a reason to combine articles.
- **Status:** already drafted from Jul 10. Ready for a shaping pass.

### B. New thought piece — candidate slug `ai-is-the-primary-interface`

- **Type:** thought piece
- **Working title:** AI-native means your primary user is the model
- **Owns:** thread 2 (Jul 11)
- **Why alone / why new:** This is the parent claim Giovanni himself names as the headline that *spawns* the three-layer and API articles. It is not SE-org content — do not leave it on `ai-native-se-stack`. It is also not the same article as A: A is "how to gather requirements"; B is "what product you are building."
- **Do not mega-merge** B + decomposing + API company into one. Jul 11 flirts with that ("maybe all of these need to get combined") — resist. One thesis piece that points at sibling articles stays readable; a kitchen-sink "AI product manifesto" will not.
- **Still thin:** the "how users discover what work needs doing" half (human-led intake vs tables/filters vs something smarter). Needs another recording before this is more than a crisp opener + one distinction (intake vs execution).

### C. Fold into existing — `decomposing-software-apps` (exists, `shaping`)

- **Type:** thought / framework
- **Owns:** thread 3 (AI lives in logic; chat replaces web as the interface layer)
- **Why here:** Both Jul 9 recordings explicitly say they're harping on this article. The short Jul 9 formula — *historically web/APIs/DB → now LLM chat/APIs/DB* — is the cleanest punchline the piece still needs.
- **Boundary:** keep this the *lens* article. Do not let it become the full API-design playbook (that's D). Cross-link, don't absorb.

### D. Keep separate — `future-of-startups-api-companies` (exists, `raw`)

- **Type:** thought / strategy (with room for a tactical "what good agent tools look like" callout later)
- **Owns:** thread 4 (APIs as primary product surface; action-oriented tools vs CRUD; UI as control plane)
- **Why not merge into C:** Same facts, different question. C asks "how do you see an app?" D asks "what kind of company / product surface wins?" Merging recreates the mega-article problem. Jul 9 long is already sitting in C's notes — editorially, most of the API/control-plane material should feed D (or be duplicated lightly with a link), not inflate C past a framework piece.
- **Related stub:** `llm-apps-personalize-saas` overlaps ("LLMs as personalization over APIs"). Do not revive it as a third sibling yet — treat as legacy seed; fold any useful line into D or kill later.

### E. Wait — too thin

| Thread | Why wait |
|---|---|
| Tool-of-choice when LLM can pick competitors (5) | One paragraph of intuition, no examples or criteria |
| Intake UX for "what work needs doing" (half of 2) | Named but not argued |
| Concrete action-oriented API / MCP design patterns (part of 4) | Asserted; needs a worked example recording |
| Anything in the Jul 13–14 m4as | Not transcribed yet — re-cluster after they land |

---

## What should stay separate (summary)

| Pair | Reason |
|---|---|
| A vs B | Practical requirements method vs product philosophy |
| B vs C/D | Parent thesis vs supporting lenses (Giovanni's own spawn map) |
| C vs D | Architecture lens vs company/API-surface thesis |
| A/B vs `ai-native-se-stack` | SE-org headcount piece is published and orthogonal; Jul 11 was a routing mistake |

## What should merge / land together

- Jul 10 → already A. Done.
- Jul 9 short punchline → C (shaping pass).
- Jul 9 long API/control-plane meat → prefer D; leave only the layer-placement claim in C.
- Jul 11 → new B; remove from `ai-native-se-stack` mental queue (notes are append-only — don't rewrite; just don't shape it there).

---

## Recommended next-action order

1. **Transcribe Jul 13–14 recordings** before creating more drafts — four sizable m4as may reshuffle B/D.
2. **Shape A** (`capabilities-not-guesses-agentic-requirements`) — densest, already drafted, clearest practical payoff.
3. **Stand up B as a stub** (`ai-is-the-primary-interface`) once Jul 13–14 are in (or sooner if you want the claim parked correctly); one more recording on the intake/discovery side before shaping.
4. **Shaping pass on C** — pull in the chat/APIs/DB formula; keep API-design depth out.
5. **Feed D from Jul 9 long** — align with existing `future-of-startups-api-companies` notes; decide later whether `llm-apps-personalize-saas` gets absorbed or archived.
6. **Park E** until a recording supplies examples.

---

## React checklist

- [ ] Agree A stays independent and goes first?
- [ ] Approve candidate slug `ai-is-the-primary-interface` (or rename)?
- [ ] Agree C = lens only, D = API/company surface?
- [ ] Wait for Jul 13–14 transcripts before creating B's folder?
