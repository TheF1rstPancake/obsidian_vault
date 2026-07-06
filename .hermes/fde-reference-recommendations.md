# FDE citation recommendations

Goal: identify where external references would materially improve credibility in `drafts/fde-is-consulting/article.md` without turning the piece into a source dump.

## Best insertion points

1. **Opening Palantir reference**
   - **Anchor:** `# FDE is what happens when implementation engineering gets a better title.` → the paragraph starting `People cite Palantir as the model constantly.`
   - **Why a citation helps:** This is the article’s main external reference point, and it is currently asserted as shared context rather than supported fact. A link here makes the “Palantir as the model” claim feel grounded instead of vibe-based.
   - **Recommended source type:** Official Palantir role/model description, plus one reputable third-party analysis.
   - **Candidate sources:**
     - https://blog.palantir.com/dev-versus-delta-demystifying-engineering-roles-at-palantir-ad44c2a6e87 — *Dev versus Delta: Demystifying engineering roles at Palantir* — Palantir / hiring manager post. Clear primary-source description of Devs vs Deltas.
     - https://a16z.com/the-palantirization-of-everything/ — *The Palantirization of everything* — Marc Andrusko, Andreessen Horowitz. Directly about companies copying the Palantir FDE model.
     - https://blog.palantir.com/products-with-purpose-foundry-archetypes-27a8538df12a — *Products with Purpose: Foundry Archetypes* — Palantir. Shows the field-feedback/product-loop mechanism the article is discussing.
   - **Suggested insertion style:** Inline link on `Palantir`, or a short footnote after the sentence.

2. **The three-question framework**
   - **Anchor:** `## Three questions FDE has to answer` through the numbered list.
   - **Why a citation helps:** The list is an argument about who owns generalization, maintenance, and platform hygiene. Palantir’s own role descriptions and product posts make the Dev/Delta split explicit enough to support that framing.
   - **Recommended source type:** Official Palantir role descriptions and product examples.
   - **Candidate sources:**
     - https://blog.palantir.com/dev-versus-delta-demystifying-engineering-roles-at-palantir-ad44c2a6e87 — *Dev versus Delta: Demystifying engineering roles at Palantir* — Palantir. States Devs own platform components end to end and Deltas deploy to customers.
     - https://blog.palantir.com/products-with-purpose-foundry-archetypes-27a8538df12a — *Products with Purpose: Foundry Archetypes* — Palantir. Says field engineers can direct product development from first-hand field insight.
   - **Suggested insertion style:** One parenthetical source note after the first paragraph, not on every bullet.

3. **“What comes next is not a renamed version of the early model”**
   - **Anchor:** the paragraph in the closing section that starts `What comes next is not a renamed version of the early model. As I understand the Palantir setup...`
   - **Why a citation helps:** This is one of the most challengeable claims in the piece because it describes a specific operating model, not just an opinion about roles.
   - **Recommended source type:** Official company job/careers page or role explainer.
   - **Candidate sources:**
     - https://www.palantir.com/careers/ — *Careers* — Palantir. Current careers copy describes Devs as product architects and distinguishes them from Deltas.
     - https://blog.palantir.com/dev-versus-delta-demystifying-engineering-roles-at-palantir-ad44c2a6e87 — *Dev versus Delta: Demystifying engineering roles at Palantir* — Palantir. Best direct support for the split between product/platform engineering and forward deployment.
     - https://www.palantir.com/careers/students-and-early-talent/ — *Students and Early Talent* — Palantir. Public FAQ-style language on the Dev vs Forward Deployed distinction.
   - **Suggested insertion style:** Short footnote after `As I understand the Palantir setup`.

4. **Airtable scripting setup**
   - **Anchor:** `### The Airtable scripting example` → the opening paragraph starting `A version of this played out at Airtable when scripting shipped.`
   - **Why a citation helps:** This paragraph makes concrete claims about where the code lived and how it was triggered. That is factual product behavior and benefits from a product-doc citation.
   - **Recommended source type:** Official Airtable support docs.
   - **Candidate sources:**
     - https://support.airtable.com/docs/scripting-extension-overview — *Scripting extension overview* — Airtable Support. Describes the extension as a browser-based, user-triggered scripting surface.
     - https://support.airtable.com/docs/run-a-script-action — *How to Run a Script Action* — Airtable Support. Explains the automation path and the foreground/background distinction.
   - **Suggested insertion style:** Inline link on `scripting` or a short source note at the end of the paragraph.

5. **Foreground vs background script behavior**
   - **Anchor:** In the Airtable section, the sentence pair beginning `Scripting extension scripts run in the foreground of the base...` and `An automation's scripting action runs a script in the background of the base.`
   - **Why a citation helps:** This is the clearest factual distinction in the Airtable example and directly supports the article’s “button click vs scheduled/automatic” contrast.
   - **Recommended source type:** Official Airtable docs, possibly with a product blog explainer.
   - **Candidate sources:**
     - https://support.airtable.com/docs/run-a-script-action — *How to Run a Script Action* — Airtable Support. Exact wording for foreground/background and manual vs automatic use.
     - https://blog.airtable.com/what-is-scripting/ — *What is Scripting?* — Airtable Blog. Explains scripting as narrow, repetitive in-program work, which fits the article’s framing.
   - **Suggested insertion style:** Footnote on the first sentence of the pair, not both.

6. **Agent harness layer**
   - **Anchor:** `## What the split looks like once you're deploying agents` → the paragraph starting `Start with the assumption underneath.`
   - **Why a citation helps:** The article’s “harness” vocabulary is sharp but abstract. A product doc showing real systems that expose tools, permissions, context, and eval-like controls will make that layer feel concrete.
   - **Recommended source type:** Official AI platform / agent documentation.
   - **Candidate sources:**
     - https://palantir.com/docs/foundry/ai-fde/overview/ — *AI FDE • Overview* — Palantir. Explicitly frames AI FDE around tools, context, permissions, and Foundry operations.
     - https://palantir.com/docs/foundry/ai-fde/security-and-governance/ — *Security and governance* — Palantir. Shows the permissions/approval boundary the article is calling the harness.
     - https://palantir.com/docs/foundry/ai-fde/best-practices/ — *Best practices for using AI FDE* — Palantir. Mentions evals, tools, and iterative production work.
   - **Suggested insertion style:** Short parenthetical source note after the harness definition paragraph.

7. **Current FDE jobs as a cross-check on the “turn solutions into platform capabilities” claim**
   - **Anchor:** `## The roles and responsibilities problem` or the later sentence `The FDE pitch quietly proposes a different model...`
   - **Why a citation helps:** The article argues that a healthy FDE model needs a clean handoff from customer solutioning into platform work. A current job description from another serious company is useful corroboration here.
   - **Recommended source type:** Official job description from a company with an active FDE team.
   - **Candidate sources:**
     - https://stripe.com/jobs/listing/backend-engineer-forward-deployed-engineering/7249744 — *Backend Engineer, Forward Deployed Engineering* — Stripe. Says the team turns hard customer problems into platform capabilities that scale to everyone.
     - https://stripe.com/jobs/listing/forward-deployed-engineer-privy/7230452 — *Forward Deployed Engineer, Privy* — Stripe. Good example of customer-facing technical ownership for important customer problems.
   - **Suggested insertion style:** Inline link on the phrase `platform capabilities that scale to everyone` or a brief endnote.

## Claims that should probably stay unsupported

- The firsthand Airtable/Recurrency stories, especially the parts about what happened inside those teams, should stay mostly in first person unless you want to add a source note for product behavior. They read best as lived experience, not externally verified history.
- `customers are not always rational nor capable of implementing your solution` is opinionated framing, not a fact claim. It does not need a citation.
- `That isn't how SaaS has typically worked` is a broad industry generalization. Unless you want to introduce a survey or history reference, it is cleaner left as analysis.
- `The duct tape is evidence` and the product-feedback-loop argument are the essay’s own logic. They should stay uncited unless you want to anchor them with a separate product-management source.

## Recommended first-pass citations

1. The opening Palantir reference in `Three questions FDE has to answer`.
2. The Airtable scripting paragraph that explains the browser/manual vs automation/background split.
3. The agent-harness paragraph in `What the split looks like once you're deploying agents`.
