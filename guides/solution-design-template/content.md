---
title: "The solution design template"
slug: guide-solution-design-template-content
status: ready
target: ghost-page
visibility: paid
created: 2026-06-19
updated: 2026-07-03
tags: [sales-engineering, customer-success, implementation, template]
point: >
  A fill-in-the-blank solution design document that starts with four boxes
  about the customer's world, turns them into solution-agnostic requirements,
  and only then maps those requirements to a recommended solution. The order
  keeps discovery focused on what the customer needs before any vendor's
  product enters the document.
---

# The solution design template

This is the companion artifact to *Are you trying to be right, or help the customer?* The structure is deliberate:

1. Capture the customer's current state, problems, goals, and ideal solution.
2. Turn that understanding into requirements that do not mention your product.
3. Bridge those requirements to the solution you recommend.

If your product appears before the recommendation, go back and rewrite. The customer should be able to hand the first five boxes to another vendor and ask how they would solve the same problem.

Copy everything below into your own document and replace the bracketed prompts.

---

## The customer's problem

*Complete these four boxes in the customer's language. Describe their world without mentioning your company, product, features, or implementation.*

### Box 1: Current state

[What is the customer doing today? Describe the workflow, tools, people, and relevant constraints as they would describe them.]

### Box 2: Problems

[What is not working? Why are they taking this call now? Capture the cost, risk, friction, or delay in their words.]

### Box 3: Goals and objectives

[What should be different when the problem is solved? Use a measurable or observable outcome where one exists.]

### Box 4: Ideal solution

[If the customer could design the answer without regard to any vendor, what would it let them do? Preserve their preferences even when they do not match what you sell.]

## Box 5: Solution-agnostic requirements

*Translate the first four boxes into a requirements table. This is the bridge between the customer's problem and your recommendation. Every requirement should describe what a suitable solution must do without naming your company, product, feature names, or architecture.*

| Scope | Requirement |
|---|---|
| In scope | [A solution must...] |
| In scope | [A solution must...] |
| In scope | [A solution must...] |
| Out of scope | [A capability the customer considered but does not need for this engagement] |
| Out of scope | [A preference that should not determine the recommendation] |

Use **in scope** for requirements your recommendation must satisfy and **out of scope** for items you recommend excluding. The distinction records a recommendation, not an abstract debate over what the customer needs or wants.

Before moving on, check each row:

- Can you trace it back to the current state, a problem, a goal, or the ideal solution?
- Could another vendor respond to it without translating your product terminology?
- Does it describe an outcome or constraint instead of a feature?

Delete any row that fails those checks.

> [!tip] Seed requirements with judgment
> Customers may begin with a list of wants. Use what you learned in the first four boxes to recommend what belongs in and out of scope. You can add requirements customers with similar goals often miss, including onboarding or implementation support. Be direct about capabilities you cannot provide.

## Recommended solution

*Only now introduce your product. Show how the recommendation satisfies the in-scope requirements and be explicit about gaps.*

### Recommendation

[In one short paragraph, explain the solution you recommend and why it fits the customer's goals and requirements.]

### Requirements mapping

| In-scope requirement | Recommended approach | Gap or constraint |
|---|---|---|
| [Copy a requirement from Box 5] | [Specific capability, workflow, or configuration] | [None, or state the limitation plainly] |
| [Copy a requirement from Box 5] | [Specific capability, workflow, or configuration] | [None, or state the limitation plainly] |
| [Copy a requirement from Box 5] | [Specific capability, workflow, or configuration] | [None, or state the limitation plainly] |

### Responsibilities and timing

| Work | Owner | Timing |
|---|---|---|
| [What your team will provide] | [Owner] | [Date or phase] |
| [What the customer must provide] | [Owner] | [Date or phase] |

## Open questions

| Question | Owner | Needed by |
|---|---|---|
| [An unresolved decision or missing fact] | [Owner] | [Date] |

---

The sequence is the safeguard. Understand the customer's world, agree on solution-agnostic requirements, and then make the case for your solution.
