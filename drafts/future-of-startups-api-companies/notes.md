---
slug: future-of-startups-api-companies
---

## 2026-06-15 10:57 — URecorder_20260615_115246.m4a

I just wandered around my apartment with a new idea and realized I didn't record any
of it.
So Ben Stensel on his Substack wrote an article about what does the future of startups look
like in an AI world, which I thought was really interesting.
This sort of thesis is that at every major jump in technology it has produced behemoth
enterprise orgs and household names and then a series of smaller but still meaningfully
large organizations that fall under those behemoths.
For example, you've got your Google and your Microsoft and your Amazon, but then think
of all of the SaaS tools underneath that, like a Stripe, Intercom, and Airtable, these
meaningfully large businesses that exist but haven't reached that full-scale state of a
large player.
And in the AI world, you know, it's the Anthropic and the OpenAI, but there is a fleet of smaller
organizations still doing meaningful work underneath that, and in a world where agent
harnesses become commoditized and anyone and everyone will have a harness that can manage
problems, then what is the role of software companies in that case?
If everyone has the harness and can build the software very specific to their needs
with little effort, why does someone need to pay for a service other than the harness
itself?
And in that case, what does it mean to be a startup in that world?
What service can you show up and offer that's like a boots on the ground, you know, net
new thing that people want to invest in and get on board on, again, in a world where anyone
can build the software that they need in one shot?
And I think it's an interesting problem to look at because nobody really seems to have
great answers for what it means.
At a minimum, it seems to mean that we will change how we evaluate the value of companies
based on how they can survive or whether this change.
I think there are some trends that we're already seeing that point to what that future
looks like.
And I think the biggest piece of this is in how you see so many applications moving to
what they call, you know, the headless experience, where all of the actions that you could take
and sort of the legacy, which is crazy that we're saying legacy web apps, all of the actions
that you can take in those, you can now take through an AI agent.
And so your interface for how you take action is...
Sorry, so the way that you take action now, right, it's not, hey, I go click around a
web browser.
I don't need to learn necessarily all of the nuanced mechanics of how to use some of these
SaaS tools.
I can just, you know, authenticate with my AI agent of choice and allow it to go and
take the action for me.
And I no longer care about things, and in many ways, I actually don't care about things
like user experience, like how many clicks does it take or how annoying is it to accomplish
a certain task because I'm not the one doing it.
I just issue, I speak declaratively to my AI agent of choice and it will go and do the
action for me.
It will deal with the nuance and the annoyance of, well, it would be really nice if this
was one API call, but I have to make three, really.
That is totally, unless you're like really paying attention to the logs, it's mostly
invisible to you and you no longer have to care about those things.
And I think the interesting part about this is really what you're doing is we're going
back to the primary way that people will engage with technology companies is through APIs.
We will build abstraction layers on top of problems that people care about solving, but
don't necessarily have the specialization to do well themselves or especially not well
for a broader team.
I think building software for yourself, hacking something on your laptop, that has been something
that people have continued to do and has always have done, and the problem has always been
how do I make this a collaborative team-based system?
How do I make something that is multiplayer-friendly, even if you're able to bootstrap your ork
to only being a handful of individuals?
You still want to consider the fact that two people might be trying to take action at the
same time and you need to understand how to resolve that state or keep track of those
things.
In software engineering, this is just Git, right?
Because everything is file-based, it goes into Git, there are entire processes for resolving
those conflicts, and we now have entire software companies that have built the specialization
around how to manage that problem very specifically.
Could you rebuild Git?
Probably.
You could rebuild an internal version of GitHub that is just what you need, and none of the
other bells and whistles.
Why would you?
That's kind of the open question, and maybe there is a point at which people actually
do that to a certain extent, but building that specialization or paying for that specialization
feels worth it.
So ultimately, what is it that we're paying for?
We're paying for abstraction of complicated problems that we probably could solve ourselves
if we were willing to devote the time, but we don't want to.
Because it will become mostly a want thing.
If our AI agents are technically capable, and building things like GitHub is very well
understood, there is no reason that your AI agent couldn't rebuild that for you.
But do you want to take on that specialization know-how for how to do that?
Probably not.
Could you rebuild Stripe?
Could you rebuild payment layers?
Maybe rebuild a very basic version of Stripe, but not that much time.
Now there's a ton of legal and compliance issues that are hard to abstract away, and
that is a lot of what Stripe gives you, is that abstraction layer to deal with that.
They have built that specialization into their payment layer, and that is what you were paying
them for.
I think another really fun one to look at is Security Pal, if you haven't been using
them for security reviews, highly recommend it, and again, if you break down a security
review process, it's not necessarily the most complicated thing in the world.
You get a questionnaire, you read the questionnaire, you know your posture and your answers, and
then you just kind of map the two together.
This is a problem that is ripe for translating the external security review document that
into the knowledge and postures that you already have, but there is like an incredible amount
of nuance to the right way to process those reviews.
When are different certifications meaningful as answers?
When can you get away with sort of like subverting an answer a little bit, not in a way that's
like slimy, but you know, not all security questionnaires are often like a blanket approach,
and it may not be applicable to your business, so how do you understand that context of knowing
what's applicable and what's not?
If you are not a security expert, understanding that level of specialization is hard, and
so yes, you'll probably push Claude to build something, but how do you have the framework
to evaluate whether or not it's doing the right job?
You can't.
You don't have the specialization context to be able to do that, and so what is security
palettes?
Functionally an API, right?
Ship them an email, they ship you back a completed questionnaire, and the entire process behind
how that questionnaire gets filled out is a black box to you.
Their internal teams have the agents, have their own harnesses, have their own setup
to be able to manage that complexity on your behalf, and so you pay them to deal with the
specialization of understanding how to answer a security questionnaire, but it's not a web
It is no longer the web applications of old for an implementation detail for dealing with
user requirements.
I think business intelligence is another really interesting thing to look at here.
If you look at something like Hex, which is very, very headless-friendly, you can spit
up entire reports and contexts and shared queries without ever having to go into the
application, but how does a BI tool work without reports?
We've all been very trained that business intelligence is about reports and dashboards
and pretty things that you can slap on a slide, but if you were to break down the core user
requirement that a BI tool represents, as a data analyst or an operations person, pick
I need to be able to generate data-driven answers to important business questions and
ensure that those answers can be shared and reused by others so that we are all working
from a shared definition and reduce confusion back and forth or misinformation that might
lead to bad judgments and outcomes.
Nowhere in that user story does it say, I need a UI to do that.
We have used the UI historically as the way to meet that user requirement.
You build the dashboard.
If people have answers, they go to the dashboard.
If someone wants to reuse your query, they look in the dashboard and they extract out
the SQL.
If you're lucky, your BI tool has the concept of shared queries, and so the queries from
the dashboard can be referenced in other places, and then if you make updates in one place
it updates everywhere, but even that's not necessarily a table takes feature in a lot
of places.
If you think about what does that mean now for how users request information, it is increasingly
less let me go to the dashboard and look.
I might still do that if I just want the top level summary and be able to go look, maybe
I want to drill and explore, but do I really want to be the one doing those actions?
No, I want to hand that off to my agent to go do that, and so what are you paying for
for a BI tool at that point?
You were paying for the shared multiplayer data substrate to say these are our queries,
this is the context around those queries, I want to manage those queries.
I think BI might be in a special case where ultimately isn't that all just code files
and this actually starts to look more like a software development issue of can I just
rebuild all of this in Git, then I have a repository that is our data hierarchy, and
in fact many of these BI tools actually allow you to store things in Git and then have them
loaded into the BI tool.
There's a lot of other things that BI provides that would be really challenging to specialize
on in Git, role-based access control being one of them, not all data needs to be visible
to everyone, and you will have some users that will have a mix of what they're allowed
to access and what they're not allowed to access, that is very hard to do, and just
text-based Git install, right, and so what are you paying for the specialization for
there?
You're paying for the specialization of how do updates work?
How do I get information repeatably and reliably to people and not just solve the on-demand
use case?
How do I manage connections to one or many databases in the event that I do need to generate
something visual?
How do I build, how do I have the tools that ensure that I can do that in a repeatable
process that matches my brand?
I actually think that visualization generation is probably the commodity that most of these
BI tools is no longer really a specialization, like those aren't hard to do, it's a very
well-understood problem, but really what you're paying for in those cases is what does shared
context look like, what do rules and permissions look like, what does access to certain information
look like and how do I segment those, how do I understand what source of truth is, how
do I litigate that, would different people have different sources of truth, how do we
combine those to a shared understanding?
Those are not trivial problems to solve, but now I am no longer constrained to having to
go through a UI to learn all of the nitty-gritty instances of how that UI wants to force me
to solve that problem.
I now have APIs that something else can figure out how to chain together in a way that achieves
my objective, and that is a very big paradigm shift in how users will engage with your tools,
but it is actually not necessarily a big paradigm shift in how you build those tools.
Building APIs, the well-understood practice, and because our AI friends have learned from
the internet, their understanding of best practices is very similar to what your average
developer would think were the best practices of interacting with an API.
That'll probably shift and change, and I think we're already seeing some of that of like,
is it an API or is it just command line arguments, right?
Are you making web requests or are you issuing commands via command line?
What is more ergonomically friendly to the LLMs, not to users, right?
No engineer would build an entire system necessarily on top of programmatic command line calls.
It's web-based, programmatic issuing.
The CLI calls are just issuing calls out to a web-bound API, but for the LLM, the CLI
is friendlier.
There's less overhead, right?
It already has access to your terminal.
It doesn't have to worry about, well, what library am I going to use to send the API call?
How do I capture errors and things when the terminal already has all of that wrapped up
for it, and so that tool alone is much better ergonomically friendly for your LLMs.
Anyway, case in point being, what do the startups of the future look like?
I think they look a lot more like building an API company where you build these API surface
areas that abstract away complicated problems that is not new.
I think the UI becomes secondary in many cases, and if anything, most of the UI is actually
internally facing.
Your internal team, if an agent is struggling or if there are requests that are not going
the way that you think they should be, the escalation and path to resolving those is
mostly within your internal team's control.
So you are building less and less customer-facing surface areas.
The customer-facing surface areas at ChatWindow where they get to be declarative about what
they want to accomplish.
You have the APIs to surface those actions to them, and then anything that isn't necessarily
done programmatically, Stripe Compliance and working with government agencies to make sure
that everything is above board, or internal reporting and metrics on security questionnaires
in the inbox and who's got what, that is all internal.
We're managing that almost entirely internally in a black box to your customer.
And so the companies of the future look like publicly facing APIs where the user experience
is secondary and internally there's a much bigger focus on internal operations and arming
your teams with the tools to sufficiently manage the edge cases of the product.
And what you were paying for in those cases is specialization.
You were paying for someone to think about the edge cases of the problems, to take an
idea from well it works on my machine to it works for my organization, that jump there
is still really hard.
The way we accomplish that now going forward though is going to look very, both like different
from what I think most people are used to, but also very familiar to companies that have
been building API for programmatic access to their tools for a very long time.

---

## 2026-06-24 07:46 — URecorder_20260624_083956.m4a

This is a different direction than I was originally going to take.
This might ultimately be related to a recent recording we did around, like, what are you
paying for?
You're paying for specialization.
I think not necessarily a new thought, but certainly one that's been circulating more
recently is that there's a very big difference between paying for a model and then paying
for the model hardness.
And that's because, if we go back to kind of the beginning here, why Claude Code, why
Codex, why some of these other frontier lab harnesses were so popular, they were kind
of the first to build them and build them well on top of their own proprietary models.
And so what that meant was, if you wanted to get the most out of the application, the
two were very tightly coupled.
Buying into Claude meant buying into their harness and their models.
And there was some argument to be made that the model did at least help the harnesses
perform better, smarter models do better for high complex tasks, and harnesses are certainly
complex.
And so you're paying for that specialization of someone, of both the model provider and
for someone to help you understand how to, like, take advantage of it.
But more and more, things we've seen with, like, OpenClaw, Hermes, even tools like Gumloop,
you know, the harness is becoming more and more of a place where the battle is being
fought.
You know, Fin didn't buy, or Salesforce didn't just buy Fin because Intercom had created
a new model that was particularly good in managing support, they built a harness that
allows any organization to build a really robust support engine on top of availability
of my models.
The interesting thing about Intercom, right, is the model is totally opaque, right, you
have no idea what they're using, you have no choice.
They get to kind of pick and choose, and that's fine, right, they can pick whatever model
they want to drive their costs as long as it delivers the outcomes that you need.
Whereas, again, tools like Hermes or OpenClaw, or Gumloop, you know, sort of bring your own
model, bring your own keys, so you get to pick and choose, you know, what model you
think is best for the task.
I think, again, the interesting part in that, and sort of the admission in that, is like
the models themselves are replaceable, right, they're like, with the right harness, with
the right prompts, and context, and tool, most of these models can get you to a similar
outcome.
The path that they take might be very different, and you might disagree, and you might agree
with the path that one model takes more regularly than another, but the harness itself is really
what you're paying for.
And so, you know, what does it mean when...
But I think the, so like, why aren't these, like, generalized frameworks like, again,
like Hermes, but if it is this sort of generalized agent that can do everything, why is it not?
Probably well, right, its revenue should be booming, it should be, like, amassing a ton
of users, a ton of revenue as a result, and I think it's because setting up those, the
general purpose frameworks still require a lot of setup, but there's like a dozen legal
AI startups right now, and a dozen, you know, AI support harnesses right now, and it's because
that specialization, when you're able to limit the scope of what it is that these harnesses
need to work on, they perform significantly better, the setup is much easier, and users
can just get in and sort of solve the one job that they want, but does that mean that
we're gonna live in a world where you have, like, 17 harnesses, right, and we're gonna
go back from tech sprawl of having purchased, you know, dozens of pieces of software to
now having dozens of different agent harnesses, one year towards each team, that doesn't feel
like a great future living either, and sort of a repeat of this into the past, that's what we think.
Specialization is certainly what you want to be looking for right now, it does this tool
provide something that I am not able to build out of the box myself,
I think where this is coming from, like, a new trend in software evaluations is, you know,
buyers getting kind of cute and asking, like, what's to prevent me from rebuilding
your product and quad code for nothing?
And the answer is, like, if you could, you would have, I think at a certain point, right,
motivation and prioritization skill are still a very large barrier to entry for a lot of these
problems, and so just because you have the technical skill now, or the technical toolbox
with Clon, your technical toolbox is expanded because you have an LLM coding agent at your disposal,
does not mean that you will actually be able to successfully deploy, and I think the other part is,
you know, apps designed for singular users, for singular people
in a vacuum, yes, are quite easy, and we've had citizen developers building one-off
applications for themselves, maybe like a very, very small group of individuals,
forever, shadow IT, citizen developers, whatever you want to call it, it has always sort of existed
as a concept of people with the technical skill and know-how.
You don't want to prevent those people from doing things because often the things that they go
and do unlock a lot of productivity and value for your organization,
and so instead, we gave them a name, sort of permanent corner, and said they were special.
Now the number of people that can do that is expanding, but like,
not really, right? Building a multiplayer collaborative system requires a certain set
of skills. It requires a certain amount of infrastructure and deployment and maintenance
and monitoring, and I think one of the aspects of the technical skill here, and that we probably
have overlooked, is knowing what questions to ask and knowing when you don't know
the answer. Well, the LLMs have gotten very good at you being able to like speak things into existence.
They do sometimes do things that are overkill. They do sometimes will push you in directions
you were uncomfortable with or you were not of course correct, and so you can earn a ton of time
where it's trying to, you know, solve a problem. The fundamental question that you asked was wrong.
Right, everything goes back to LLMs are a force multiplier. If you know the right things to ask
and the right things to do, yes can make you substantially more effective. If you don't,
it can just cause you to waste more time than you otherwise would have, and so this idea of, well,
why can't I rebuild it? Maybe this is like, this is the article that we need to tackle. It was like,
why can't you rebuild? Why can't I rebuild your product myself? Why am I paying you for this?
It's because you aren't the specialist. You were the specialist in your business, but you want to
be a specialist in how to create a shared inbox with real-time understanding of who's picking up
tickets, status tracking. Do you want to be a specialist in building webhooks and event-driven
workflows? Do you want to be a specialist in creating
the contact libraries and understanding the right way to
manage those contact libraries in an optimal way for an LLM? Because here's the biggest irony
of it, right? Because the LLMs only have access to so much information. Web searches definitely
improve this, but because LLM development changes so quickly, the LLMs themselves are not often very
good at solving, help me build LLM-based applications. They struggle, or will be using
tools from a year ago, and the market has moved considerably since then. And so its understanding
of what's right often gets boiled down to, well, what are the first five pages it read on Google,
and that's not necessarily the best way to solve your problem.
Right, the sort of massive weighting knowledge that it has about building
20 years worth of Stack Overflow answers about how to build
web applications that doesn't exist for LLM application development. And so all of the
specialization around how to make it work, how to monitor it, how to understand if it's performing
well, all of that stuff you likely will build in some capacity for yourself, very bespoke
to your business, but you will not build it in a generalized way that every part of your organization
will be able to use it. Because, as we've seen, the generalized harnesses are really hard to set
right. There are layers and additional things that you want to build on top of them and you
need to manage. And so what you're paying for is the specialization to understand the infrastructure,
the right way to deploy the system in a way that dozens of people can operate within it.
Seamlessly, you're paying for specialized understanding.
The infrastructure is kind of the big one of really what you're paying for,
is the infrastructure to understand how to fine-tune
an LLM and build surrounding support systems to manage it effectively within the context
of a specific problem. And so yes, you could, but it would take you significantly longer
and probably be worse, right? My team of 20 engineers working exclusively on this problem
can likely do better, get farther, build more than your single-claw terminal instance
with a surface-level understanding of the infrastructure required to support the
problem. And you might know the end outcome the best of how you want to use it for your business.
But we shouldn't be conflating, you know,
rapid configuration of an existing product with the ability to replace that product wholesale.

---

## 2026-07-07 07:27 — URecorder_20260707_082226.m4a

So if we keep up with the, you know, data model layer cake and why this means that more
companies are going to be ad companies, right, so you've got your database, your APIs, and
your presentation or interface layer, and the infrastructure that wraps all of that,
again, infrastructure is the one place where a lot of people struggle, but anyway, this is an aside
for the interface layer. Historically it's been a very big focus because that is really what your
users see and interact with, right, so you could have the coolest database set up and some pretty
nifty APIs and nobody really gives a shit because all of those are in service of presenting some
sort of application to a user. Even, you know, there's an exception here for like historically
truly API-based companies, right, so they have like a scrape as an example, but even they have some
user interface elements that people engage with more from like an admin dashboard or precanned UI
that you can insert and embed on your website, but really the interface is what most users engage
with, and so everything is in service of providing a good user experience, user interface for people
to engage with, and then there's, you know, whole schools of thought around design and, you know,
what makes a good user interface, how do you make it intuitive, how do you anticipate users' needs,
how do you build systems, instructors, and guardrails that guide them to a certain way
of accomplishing tasks that allow them to get value out of your platform, and I think what we're
seeing is that model has worked, but there's always been this tension of, again, the user
has to look at their problem, look at your software, and look at your user interface,
and then kind of like morph their mental model into the model of your application in order to
accomplish things that you've done. There's this sort of invisible translation layer that happens
between the user's desired outcomes and how to use your software to get to them, and this is why,
you know, solutions engineering teams exist, this is why implementation teams exist, is because
that layer is there, and some users are better at working through that than others, but it all
like you have your champion users, your advocates are very often people that like understood your
product, they got on board, they self-serve, they don't really need you to do the translation,
they kind of push the bounds, and you use them sort of a model citizen going forward, and someone
you want, you know, promoting your product. Others is like, hey, look how easy this is,
look how powerful it can be. You know, the air table we used to say, you know, just because
anyone could use the platform doesn't mean everyone will, and over time, what that really
evolved to was just because everyone can doesn't mean that they'll be motivated to or have the
capacity to. There's some people who just like doing that translation of their goals and objectives
into solution here software, they're just not going to do it, they don't have the framework,
they don't have the framework, they don't have the skills to be able to manage that, and what
LLMs are changing in terms of user interface is the fact that users can speak outcomes,
and the LLM does that translation layer for them. And the right way for it to do that for them is
not for it to use a browser, it is not to be constrained by clicks in your UI. If the answer,
if you think the answer is, well, we'll just give Claude access to Chrome, and then it'll
log in, it'll click things until it accomplishes the task. Like maybe, maybe there's some value
in being able to do that in some cases, but again, that's the user interface is backed by,
API is backed by endpoints that drive the logic that you do in the interface, and so the right
interface for an LLM is a programmatic one. And this also isn't necessarily new, right? Most SaaS
applications, even ones with pretty constrained UIs, offer some sense of API access, where you
can take actions outside of the interface.
And the reason you allow that access is, again, historically the reason you've allowed that access
twofold. One is because it allows an escape hatch for, well, let's make that one second. The first
is bulk action. Almost always, why do you give someone access to your API? It's because there
is some sort of import bulk data manipulation that they want to be able to do, and the thought
of manually keying things one by one is a big turn off, a barrier to entry that is too high. So you
build API to basically say, like, if you want to do those bulk actions, you can do it. And the other
is sort of, is similar, but is a more generic escape hatch. Right, having an API allows you to say,
the user comes to you with a really whack idea that kind of fits your application, but kind of
doesn't. The APIs give you the opportunity to say, like, well, you could, right, you could do that on
your own if you real custom code and use their APIs. And again, just because they can doesn't mean
they have the capacity to. And so they're, you know, it's very classic objection handling for
weird requirements that somebody gives you and says, well, you know, if this comes back up,
we can explore using the APIs. It allows you to sort of handle the objection and say yes,
but halfheartedly because you know that they're not actually going to take you up on that offer
at any point. And so this API layer, I think we had started drifting away from
or more and more applications were demanding, or we were at least even smarter about how to build
things and products so that you could do everything in the application. And if you think about,
you know, when everyone's respond, their own, you know, chat in the app,
agent and all of a sudden we're chatting like 17 different things at once.
Those are all backed by those institutions or those applications APIs.
And the GIF now with headless, I'd basically say you're using the APIs, but the orchestrator
and interface is your local LLM of choice, right? We've moved the user interface away
from the application UI to a terminal window because that terminal window, that text box
that you get allows you to speak outcomes and something else translates it and actions on it.
And the way that they action on it is through APIs. And so I think this isn't, again, this isn't
new, right? Like the whole reason you allow for APIs in the first place is the escape patch.
It's the escape patch for I don't totally know how to make this product do what I want,
but it seems to have the bare bones. Let me string together some API calls to make it happen.
I mean, every Salesforce deployment is functionally, well, I think Salesforce
can do what I want, but I got to customize it. And that customization and that ability
to do that customization is a value add, not a tractor. And so for the foreseeable future,
I think if your product is not exposing an API, if it is not exposing at a minimum,
MCP, then it is not long for this world because users are more and more moving away from UI
where they have to understand your presentation and your constraints. And instead, they want to
be able to speak outcomes into existence and allow the LLM to deliver those results for them.
So another way of thinking about this is the primary user of your application is no longer
the user. The primary user of your application is an AI. And how you design your APIs
changes a little bit, right? You know, if you make the world's most complex data input
structure, they can do crazy amounts of, you know, I'm sure people have used APIs where you
look at the structure and there's so much like bloat that you have to put in just to like
give the API the metadata that's necessary to trigger a successful call.
You know, each piece of metadata that you ask the AI to provide is yet another place for it
to loosen it and get something wrong. On the flip side, if you're too constrained,
the number of ways that your AI can juggle and mix and match to deliver an outcome gets constrained.
And so a lot of the principles of user interface design, of trying to anticipate what users need,
building, you know, the right buttons that take the right actions in the right place at the right
time. All of that now gets moved back to your API design, command line interface design. Because
more and more you're going to see that the people who are actually engaging with your product are not
a CD, that the people who are actually engaging with your product are not humans and robots.
And that's because the robot is better at consuming large amounts of context
and doing translation. It can translate user desire into a solution on your product.
The easier you make that, the faster you can make it for an AI to be able to take those actions.
The better. I think really tackling what that looks like, again, these aren't new. It looks
like good API documentation with good examples. I remember one thing that sucked about our
documentation was half of the examples we had in our docs didn't run. You would take the example
payload, put it into our staging environment, which sort of mocked responses because you didn't
actually want to charge real cards while you were testing. Half of them didn't work. I spent
an entire summer writing a system that basically scraped our own doc pages, loaded them into
payloads and tested them and then flagged what was wrong so that I could go and
correct them because there's nothing more frustrating than prepping an example
and not having it work. Now you imagine an AI has to do that. It's going to look at the same
thing. It's going to be like, what the fuck? Why does an example not work? How does it triage
and troubleshoot that? Which goes back to principle number two, that what you live and die by really
are error codes. Your API ergonomics, I think are judged primarily by how quickly you need
to first call, like how hard do you make authentication and setup? And then secondly,
how quickly can the user resolve errors? Because if your LLM gets stuck on loop or I can't understand
why it's getting an error, the error message is unclear, the next steps are unclear.
It then can't course correct itself to help. And what it will report back to a user is,
yeah, this doesn't work. That is the worst outcome for you, because it probably does work if you just
load the robot with the context and you assumed that you were dealing with a human
that was willing to spend a lot of time troubleshooting and navigating issues,
which is also wrong. And so I think APIs have sort of been this like secondary layer escape
patch for a lot of products. And I think what we're going to see very rapidly here for the next year
is APIs are going to become more and more
once you live and die by Luna. Hey, come here.
Because you have to, because your user base is changing. Your user base is no longer humans.
It's their AI systems doing things on their behalf.

---

