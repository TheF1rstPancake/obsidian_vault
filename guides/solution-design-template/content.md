---
title: "The solution design template"
slug: guide-solution-design-template-content
status: ready
target: ghost-page
visibility: paid
created: 2026-06-19
updated: 2026-07-11
tags: [sales-engineering, customer-success, implementation, template]
point: >
  A worked example of the solution design template for a fictitious support
  triage problem, plus a blank copyable version alongside it.
---

# The solution design template

This page is the worked example. If you want the empty version, use the [blank solution design template](/guide-solution-design-template-blank/).

The fictional customer is Northstar Cloud, a mid-market software company with a 55-person support team. They already know they need better triage. What they do not have yet is a document that turns that problem into something another vendor could read and respond to.

## The customer's problem

### Box 1: Current state

Northstar Cloud receives support requests through support@northstarcloud.com, an in-app form, and the occasional Slack ping from account managers when an enterprise customer is stuck. One support operations manager opens the queue in the morning, scans for urgent issues, and assigns tickets by hand.

The team already uses Salesforce for account data and a ticketing system for cases, but those systems do not line up cleanly. Reps bounce between tabs to check account tier, renewal date, and open escalations before they answer a ticket. If the support manager is out, the queue keeps moving, but the triage judgment disappears with them.

### Box 2: Problems

The support manager is the single point of failure. P1 incidents can sit next to password resets. Enterprise accounts do not always get the attention they should. The team spends two to three hours a day on routing instead of resolving cases.

Leadership also does not have a clean view of what is happening. By the time someone asks about backlog or SLA risk, the numbers have to be stitched together by hand from spreadsheets and reports that are already stale.

### Box 3: Goals and objectives

The support team wants a few specific outcomes:

- P1 incidents should be acknowledged within 10 minutes.
- Manual triage should drop to under 30 minutes a day.
- Reps should see account tier, renewal date, and open escalations without leaving the ticket.
- Managers should be able to rebalance the queue without touching every ticket one by one.
- Leadership should get a weekly view of backlog, first response time, and SLA risk by account tier.

They are not trying to replace Salesforce. They are trying to make support routing reliable enough that the whole process stops depending on one person.

### Box 4: Ideal solution

If Northstar could design the answer without thinking about vendors, it would look like this:

- one shared queue for all inbound requests
- automatic routing for urgent tickets and enterprise accounts
- visible account context in the case view
- clear escalation for high-priority incidents
- reporting that shows where the queue is getting stuck

They do not want a custom portal in phase one. They do not want a CRM replacement. They want the routing problem solved without turning the project into a platform rebuild.

## Box 5: Solution-agnostic requirements

This is the bridge. The rows below turn the customer story into requirements that another vendor could answer without translating your product terminology.

| Scope | Requirement |
|---|---|
| In scope | All inbound customer requests must enter one queue within 60 seconds, regardless of source. |
| In scope | P1 incidents and enterprise accounts must be flagged automatically and routed to the on-call rep. |
| In scope | Reps must see account tier, renewal date, and open escalations in the ticket view before they respond. |
| In scope | Managers must be able to rebalance ownership without rekeying tickets or rebuilding the queue. |
| In scope | Weekly reporting must show backlog, first response time, and SLA risk by account tier. |
| Out of scope | Replacing Salesforce or changing the CRM of record. |
| Out of scope | Building a custom self-service portal in phase one. |
| Out of scope | Auto-generated customer replies with no human review. |

Use the table to force a decision, not to list every idea anyone mentioned on the call. If a row does not change the recommendation, cut it.

> [!tip] Seed requirements with judgment
> Customers often start with a want list. Convert that into a need list by asking which items actually change the solution. If a capability is a real differentiator and the customer needs it, say so. If it is just nice to have, keep it out of scope.

## Recommended solution

For this example, the recommendation is a Zendesk-based support workspace with Salesforce sync, rules-based routing, and Slack escalation for urgent issues. That keeps Salesforce as the system of record, gives the support team one queue to work from, and handles the routing problem without forcing a CRM replacement or a custom portal build.

### Requirements mapping

| In-scope requirement | Recommended approach | Gap or constraint |
|---|---|---|
| All inbound customer requests must enter one queue within 60 seconds, regardless of source. | Connect email, in-app form, and manual intake into a single Zendesk queue. | Phone voicemails stay manual in phase one. |
| P1 incidents and enterprise accounts must be flagged automatically and routed to the on-call rep. | Use routing rules that combine issue type and account tier, then trigger Slack escalation for P1s. | Routing depends on clean tier data in Salesforce. |
| Reps must see account tier, renewal date, and open escalations in the ticket view before they respond. | Surface key Salesforce fields in the ticket sidebar and link to the open escalation history. | Renewal date sync is nightly, not real time. |
| Managers must be able to rebalance ownership without rekeying tickets or rebuilding the queue. | Use queue ownership, reassignment, and bulk update tools. | Historical tickets stay with their original owner unless moved. |
| Weekly reporting must show backlog, first response time, and SLA risk by account tier. | Schedule built-in dashboards and exports for leadership review. | No custom executive scorecard in phase one. |

### Responsibilities and timing

| Work | Owner | Timing |
|---|---|---|
| Confirm the P1 definition and VIP account list. | Customer support leadership | Before configuration starts |
| Approve Salesforce field mapping and connection details. | Customer IT/admin | Week 1 |
| Configure intake channels, routing, and escalation rules. | Our team | Week 1 |
| Train managers on reassignment and report review. | Our team | Week 2 |
| Validate the pilot against live tickets and adjust the queue rules. | Customer support ops + our team | End of Week 2 |

### Open questions

| Question | Owner | Needed by |
|---|---|---|
| Which accounts count as VIP for routing priority? | Customer support ops | Before week 1 |
| Should phone calls enter the same queue in phase one? | Customer support leadership | Before week 1 |
| Who owns routing rule changes after go-live? | Customer admin | Before week 2 |

The sequence is the safeguard. Understand the customer's world, translate it into solution-agnostic requirements, and only then make the case for the solution you recommend.
