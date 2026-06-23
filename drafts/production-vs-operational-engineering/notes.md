---
slug: production-vs-operational-engineering
---

## 2026-06-15 11:45 — URecorder_20260615_124419.m4a

Just stub this article out for me. I think there's a big difference between
production engineering and what I call like operational engineering. I think
historically that's been referred to as like software engineers and then citizen
developers. I think in an AI world the idea of a citizen developer is actually
getting collapsed a lot more. There's just so many more people that fit that
description that I think is worth revisiting and we talk about it but you
know I think related to some of our for deployed engineering conversations
there's just there's a difference in quality and a difference in what's
acceptable I would say like where we're allowed to draw the cut line between a
production engineering team that's trying to build a solution that means a
lot of people's needs versus you know this operational engineering that you
still don't want to be sloppy but we're much more comfortable cutting corners to
get to an end state faster and just know there's gonna be some downstream pain
that you're gonna have to revisit. The example that brought this on in our
software right now we're dealing with the problem of duplicates. What happens
if you know we reached out to one org to establish a relationship and then
through our discovery process we actually rediscover that org under a
different name. How does the system resolve that? This through my production
engineering team for a loop because it's like actually a very hard problem to
solve how do you know you know subsidiaries do we need to buy a tool
do we need to do all of these things. Where my like operational engineering
lens is well we'll know if it's the same company if we attempt to reach out to
the same person twice under different names so we reached out to company A
you know generic support email and then company B also directed us to generic
support email. That's all we need that should cover most cases that should
cover the cases that we like can reasonably feel comfortable that we'll
even be able to detect so like don't worry about all of the other edges and
variations we're not concerned with that we don't have to be concerned with
those right now it's okay to just like at least have the logic and process in
place that we can expand upon later rather than just like sticking our head
in the sand and ignoring it. I think that's another difference between the
two or two ways you know production versus operational. I'm thinking about it
is your production teams if you can't do it well don't do it at all operations
teams say a little bit more like I just want to cover the 80% or even the 70%
right that is still meaningful and beneficial to me so just do it and note
there's gonna be cases where we run into issues and we'll we'll deal with those
and I think a lot of that comes from the fact that you know operational teams are
used to being a little bit more customer-facing in which case they
understand that like shit happens and as long as they have the tools to go find
those and resolve those they can get it done or I think a lot of engineers don't
want to retouch things that they've already built they don't want to be have
to take that manual action to result which is totally fair and that's
exactly the right place that you want them thinking about those things but it
is materially different ways of looking at it but another reason why you need
two different teams to balance each other out if you only ever had an
operations team you would only ever cover the 80% then you would always be
bogged down by the 20% of errors and edge cases you'd probably just end up
with this like hodgepodge system where production engineering teams gonna
really standardize and force you to own something a hundred percent that becomes
the backbone that lets you then continue to grow and expand and take on more
without burying yourself under the weight of your own hacks so they related
forward-deployed engineering but a slightly different lens to it which is
why I think it's worth another article is just the difference here between like
production engineering and operational engineering and the ways they evaluate
what an acceptable trade-off is

---

## 2026-06-23 08:31 — URecorder_20260622_133643.m4a

New article idea was having a conversation with someone about, you know, the difference
between go-to-market and engineering.
This might actually fit in with our operational engineering article.
I leave that up to you, but anyway, ultimately, I made a comment that I get frustrated with
our engineering teams because it sometimes feels like they are willing to pass complex
it off to go-to-market when there are things that are more complicated than they want to
deal with.
They just say, oh, well, that's a go-to-market problem, and assume that the go-to-market
team will figure out how to implement a system that they don't get buried under the workload.
And I think that, like, there is some responsible, you know, delineation and accountability,
and I think there is a certain degree of benefit in making the people you want to be
primarily responsible for a job feel the pain of doing that job.
Otherwise, they'll never improve it.
The classic example of this is if you look at, traditionally, security reviews, a lot
of engineering teams would say, well, that's the go-to-market team's responsibility.
You know, it's interfacing with customers.
The reality is a go-to-market team doesn't know all of the information necessary to fill
out a security review.
You need your engineering team to help assist with that, and when they are unable or unwilling
to do that, it actually makes it very difficult for the go-to-market team to build that system.
And so what do you do?
You push it back onto engineering, and you say, like, no, you guys are going to fill
these out.
And once they start feeling the pain of having to do them manually and not having a standard
repository of answers and having to answer everything ad hoc, because they're the owners
of the information, they become incentivized to build that system, to be able to hand it
back to go to market in a better place.
And so this tension is useful in applying pressure in the right areas forces your teams
to build systems that allow for repeatability, scalability, and better business margins.
In having this recent conversation, what someone pointed out to me is it shouldn't be necessarily
go to market versus engineering.
That's like a proxy for do you want to have to hire humans to do this job, or do you want
it to be done in software?
Because that delineation functionally tells you which team should then do it.
I need to hire bodies to manage this product experience, and yes, it's going to be some
function of the go to market team.
It might be support, it might be customer success, it might be sales, it might be BDRs.
But when you decide that you are committing to hiring bodies, that becomes a go to market
problem.
How many bodies you have to hire, well, there's a ton of flexibility there, and I think especially
in the AI world, how much your go to market team can technically arm themselves and build
their own systems will determine how many bodies you have to go hire.
But once you make the commitment that you need bodies to manage that experience, you
are committing to the idea that it's going to be a go to market thing.
And you're going to have to keep hiring bodies.
And there is, it doesn't necessarily have to be linear, but as your business grows,
there will be new bodies that you have to continue to hire.
Which means some amount of your revenue will have to be eaten up by these people that you
hire to support it.
The other option is you say, well, we want software to manage it.
And you say, well, software requires people, and that's true, but again, we don't need
to scale linearly anymore.
And once you build that software system, it can grow and grow and grow and support significantly
more individuals than one person can.
And so the economies of scale and doing it with software is very different than choosing
to hire people.
And so then you say, well, why not make software do everything?
Well, that becomes down to tradeoffs and prioritization.
Maybe it's people today, software later.
It's a very acceptable answer to a lot of this.
And some problems just aren't great solves for software.
And sometimes it's like, you know, if you think of, well, support is not this anymore.
Support is definitely leaning more and more towards it is solvable as software.
But traditionally, it wasn't.
Traditionally, support was you needed bodies because there were so many idiosyncrasies
that would come up with support, even in a world of chatbots and flowcharts, you know,
choose your own adventure style.
Select this option and get routed into the right place.
There was always a fleet of humans behind that in order to manage the things that trickled
through. And there was such high volume of it that your teams continued to grow and expand.
But more and more of that flowchart driven process, even with some of the dynamicism
is something that software can solve.
And so I think this is redefining how much of the customer experience your go to market
teams or your engineering team is actually responsible for managing, because you make
the conscious decision that you don't want to hire armies and armies of people to manage
a task that you want to operate leaner, that you want to get to a larger customer base
and a larger amount of scale with less headcount.
And you say we need in order to do that, you have to build software.
So there are certainly problems today that you would say, well, we need to hire salespeople,
we need to hire support people, we need to hire forward deployed engineers.
There are cases for which we still want to hire.
Then the question is just like how much and how many tools and systems do we give them
to decrease the amount that we need to hire?
On the flip side, there are plenty of problems when you look at them and you say, if we were
to hire the number of people that we'd have to hire is way more than we want.
It is an overhead cost that we are not willing to take on.
In that case, you have to go to software.
And there are more and more of those types of problems that are coming up now.
That engineering teams need to get more comfortable with owning.
And you can no longer just punt because something is complex.
Complexity is no longer.
Complexity and cost honestly are no longer good enough for reasons to say we don't want
software, even though traditionally that is where most teams drew the line.

---

