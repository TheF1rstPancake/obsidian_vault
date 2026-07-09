---
slug: decomposing-software-apps
---

## 2026-06-24 12:31 — URecorder_20260624_132612.m4a

Mini-Rant time, so had a conversation today about, you know, why can't I just rebuild
that in Claude?
Why is it so hard?
Right?
And there's sort of two different flavors of this.
One is customers coming to you and debating the usefulness of your tool, because why pay
for your system if they could just in theory rebuild it on their own using Claude?
Or any agentic coding setup?
Let's call it reference Claude since that's my tool of choice.
The other side of that is internally, right, the question gets asked of engineering teams,
why can't you just move faster, why does this take so long, what is the problem with building
this?
I think it is increasingly being asked of your sort of pseudo-technical groups of why
are you submitting, like a solutions engineering team or a forward deployed engineering team,
why are you submitting tickets or making, you know, bug requests or features, like why
don't you just go fix it yourself, right, you have Claude, make Claude do it.
And I think, you know, all of this portrays a fundamental lack of understanding of what
it means to build production systems, right?
And I think it is worth breaking down, like, what fundamentally goes into any application
and that where does Claude work really well and where does it need to be prodded and
where do people's sort of lack of understanding mean that they can't actually get Claude
to do the things that it needs to be able to go and do.
Even if you look at things like, you know, how people have used, like, fable and some
of the more powerful models where they're like, you know, we told it to do a thing and
it did it in one shot, you know, what's often missing from those posts is, well, what was
the full prompt that you said, what were all of the instructions that went into it?
If you just said, build me Minecraft clone, right, like, what, is that really all that
it takes?
No, there's additional context that you put in and based on your understanding of the
technical tree, the amount of context that you are able to insert to increase the odds
of having a one shot success go up.
But at service level, right, if you just leave it totally up to chance, the LLM is going
to pick the shortest path to resolving.
The shortest path to resolving is often not a full grade production application, right?
And so in any production app, you have three layers, right?
You have a data layer.
So what are the attributes or data elements that you want to store that define your application's
universe?
And so if you think about any of the LLM apps that you're using right now, let's take
cloud or JGBT, right, like, fundamentally, what does that data layer look like at a very,
very basic level?
It's users, right, who is signing up for the platform, and then it's users' conversations.
The conversation gets stored, the text related to it gets stored, and then there are other
things, right?
There are your preferences, there are memories, all of that stuff becomes additional data
that you build on top of that.
But at its core, right, you know, rebuilding JGBT is users' conversations and maybe a
password.
We'll check a password in there.
Passwords aren't probably stored in their own table, but implementation detail, right?
So data layer is just, what do I need to store to have a functional application that defines
the universe of how people are going to engage with my product?
Then there's the application layer.
This is where APIs generally sit, application programming interfaces, and the application
layer or the logic layer is how you interface with the data.
At a minimum, you need to support create, read, update, and delete operations for every
data element that you store, right?
So again, for users and conversations, I need a way to create new users, I need a way to
update them, update a password, update a preference, update their name, update their email, I
need a way to delete users, right, delete users will request deletions, and I need a
way to read users.
When a user logs in, I can read their details.
Same thing on conversations, right, as a user engages with the product, they will create
applications or create conversations, they will update them.
The system will read the existing conversations or any given conversation, and then I need
the ability to delete them, right, so CRUD actions are the base of your application and
logic layer.
The interesting thing about, you know, the relationship between data and application
here just on like the CRUD surface area is we've known how to automate that process forever.
There's tons of libraries out there where, you know, you define the data layer, you define
those, you know, like Express or some of the Python backends, right, have always had
libraries where you define the class of data models, so what are the tables and their objects
and the relationships between them, and it will automatically generate, without LLM,
it will procedurally generate the CRUD endpoints to interface with that data layer.
The logic layer then expands to have more than just CRUD, right, you start chaining
those operations together to do more complex things, right, so again, in our, hey, let's
chat GPT clone, there's often, you know, a summarize this conversation or a, you know,
how it inserts the title of your conversation, right, whenever you create a new conversation
is generally created, you know, with an empty title and then based on reviewing the prompt
that you gave it, it goes and updates that title, but the logic for how does it, you
read the initial message, summarize it, interpret it, and then store it, that block of actions
then becomes a dedicated, you know, piece of your logic layer, so the specific logic
that then starts to actually make this application function, and then the final piece is the
interface layer, how do people actually engage with your product, you know, for most tools
that we think about right now, that's going to be a web-based, you go to a web page, as
you're on that web page, it fires off calls to the logic layer, which then takes action
within the data layer, and then presents things back to you, now, in sort of modern web programming,
where your logic lives is often a highly debated thing, not the point of this simple summary,
yes, your web page can have logic that lives within it, that doesn't take away from the
fact that there is this sort of layer cake that every application follows, where the
code runs, where it is stored is separate, and so that brings us to our final point,
the sort of fourth layer that I think a lot of people don't talk about is the infrastructure,
so for any one of those layers, you have many, many decisions about where that code runs,
how it's accessed, the cost for how much compute you want your application to have, so think
of a single-page web app, what is its data layer, does everything in the browser, it
stores data in the browser's local session, all of the logic is different, JavaScript
functions that run and call upon each other, maybe it makes an outbound request somewhere
within that, and then the browser is entirely responsible for rendering the application
to you, so in a chat GBT though that's not the case, some things probably get stored
locally in browser, but most things are stored in a database somewhere, there are endpoints
that then pull that data and then you have a web UI that presents it, or you use a desktop
app, there's a ton of different ways to build the infrastructure that supports those three
layers, and this is the piece that like Claude, or at least I have found, that most of our
LLM friends are the worst at is that infrastructure component, because the decision for what you
want to do there depends a lot on requirements that a lot of people don't think about, right?
If you want something that is collaborative, real-time collaboration, it's sort of become
a pretty table-sakes feature for most applications, thank you Google Docs, you can't have a single
page web app, do that, right?
I can't have something that runs just in my browser and be collaborative with other people
who are running it in their browser, our browsers do not talk to one another without there being
some semblance of a middleman that can facilitate that communication to each other, before people
come for me in the comments I'm sure there are some frameworks that allow sort of peer
connection on this, but like, that is a complicated setup, and if you think that Claude is going
to be able to one-shot that, and even if it does one-shot it, the fact that, like, are
you actually going to be able to understand what it did, and then take further action
when needed, and not break everything with your next prompt thereafter, like I don't
think, I don't think that's realistic, right?
So very simple requirements change the way you think about the infrastructure behind
your data application and user interface that colors a lot of the code that you write and
the way that you ultimately will bring something to people and market, building something on
your laptop is trivial, it always has been, it is becoming increasingly more trivial to
do so. Building something that works for one person has always been trivial. This is why
so many enterprise organizations have, you know, the monster spreadsheet that Sally,
who's been there for 20 years, runs, and that's her only job, is because building something
that works for one person, that one person understands really well and one person executes
on, has always been easy. What has not necessarily gotten any easier is building what I refer
to as multiplayer applications, applications where you need multiple people to be engaging
with the system. That comes with a host of additional complexities that most people do
not think through, and because you are not thinking through it, you are not injecting
that context and that requirement into your CLOD prompts, which means CLOD has not taken
those into account, which means that what CLOD ultimately spits out works for you and
only for you. Even if, even if you use something like ngrok or tailscale, publish the thing
working on your laptop for other people to engage with, it probably won't work. It'll
run, but it won't meet the objectives that you need it to. And so like, why, and so one
part of why it is still so hard for engineering teams to run fast, even with CLOD, why it's
so hard for, you know, internal, highly, fairly technical, but not, you know, principal software
engineers to work on things within your production application is because infrastructure and
environment choices color so much of the code that we write, and it is often one of the
least understood parts of writing code. And so it is very difficult to go from it works
on my machine to it works for my entire team.

---

## 2026-07-09 07:46 — URecorder_20260709_084258.m4a

So I want to keep harping on the three layers of software application article because I
think this is, I don't know, that work is becoming more and more, because I think it's
helpful in kind of understanding where AI sits in a lot of applications today and then
depending on how you're using it, what that means about you as a business. And so you
have data, logic, and interface, right? And so most of where AI is going to sit is in the,
actually not most, where AI sits very specifically is in the logic layer, right? These AI tools that
we're calling or the AI models that we're interacting with are all done via API calls,
right? You make a request out to something, to some service, to someone that is then packaging
it up into a response to an LLM and then feeding you back the information. Even if you're self-hosting,
right? You are making that request out and that is a telltale sign that this is all existing within
your logic layer, right? And the reason I think that matters is because ultimately what is the
logic layer is the collection of APIs. And so what you expose to your interface is a series of
APIs which then call another set of APIs. And so if, you know, today users are primarily engaging
with these front-end interfaces, these web interfaces, the interface, but machines don't
like that. Machines don't want to interact with a web browser. They're much better at interacting
with code and code interfaces, which actually means calling your APIs directly. And so the big
change that I think we're going to see for a lot of people is, you know, API development is going
to become a first-party experience again. I think for a long time APIs have been used as like this
escape hatch for, it's like, well, you're a more technical user and you have requirements that we
don't really touch. Like here's the API, knock yourself out. And that's fundamentally changing
because the primary users of your applications now are not people. They are people directing LLMs to
do things in your product. And so the user's interface is their chat bot that they're using,
and that chat bot's interface into your product is an LLM, or the chat bot's interface into your
product is your APIs. And you might use a CLI, you might use, you know, there's REST APIs,
you might use GraphQL API. I think the conversation becomes very interesting in terms of like,
what is the best interface for AI? Like REST has sort of been the dominant API framework for a very,
very long time. That doesn't mean that it's what's best for an LLM to interact with. Is it MCPs? Is
that the only way to do this? You see a lot of people, Jesus Christ, doing, you see a lot
more people developing command line arguments, right? Like do you next actually have it right
all along that that's the, you know, the best way for developers to interact with tools is through
the command line and the ability to chain commands together, you know, self-documenting,
or documentation all comes along with it. So you never have to leave that environment that's
actually very nice for an LLM. And so NetNet APIs are very much making a comeback here. And so I
think a lot of product managers and a lot of engineering teams care a lot about the front-end
interface, right? The dashboards and applications that users engage with in order to use your
product. And I think what needs to change is that focus is actually needs to go back to the APIs
because the UI is not actually how users are going to use it. Now that UI might need to be
more of a control plane, which I don't think is like a trivial problem for how you understand
what agents are doing. You know, how do you understand what actions your agent took within
that application? If something's wrong or there are errors, how do you like investigate those? Is
that done entirely within, you know, a given chat context? If you start doing these things
programmatically, where do those get raised? I think these are all like very different user
interface questions than most people are accustomed to. And I think it's going to be a very unnatural
feeling for a lot of PMs because for so long, you know, the inner the web interface is what we care
about. I think we're just going to start caring about that less and less. You in theory, right,
an LLM can generate an arbitrary web interface on top of your APIs. And so why, right, like they can,
customer has an outcome and a objective, the LLM can translate that outcome and objective into a UI
that work for that user that doesn't diminish the value of your product as long as the AI needs to
use your product to power the logic behind that UI. So I think, yeah, I think it's just like a very
interesting read frame of where organizations should be sending their time in terms of the
application that they're providing. And I think also James, a lot of how you think about your value
on a product and engineering team in terms of like, what am I working on? I think if you are
working on the UI, if you are working on, you know, that's no longer the primary customer touch
point or won't be the primary customer touch point very soon. And so teams need to really
reevaluate how do I design good APIs? How do I expose those APIs to my users, to my LLMs? How do we
document those and make sure the tools make sense? I think there is an interesting thing of, you know,
REST really likes everything to be very modular, right? So developers can then package up and mix
and match things into Intelligent. You leave it to the developer to understand, okay, well, here are
all the building blocks I have. Here's how I'm going to combine them all into what I need. And I think
that's actually not what our AI friends like. It is in some cases. But each decision point that you want the LLM to make
is an opportunity for it to get something wrong, right? And so it's actually that there are often
discrete actions that are probably a combination of APIs under the hood. And you just want the LLM to
be able to make that one request, right? The layers of abstraction here, they're going to be very
different compared to what we've seen people do historically. Like, at a minimum, you have to provide
create, read, update, and delete endpoints, right? Otherwise, nobody can do anything
programmatically. But I don't think that's efficient, right? That leaves too much room for
interpretation or too much room for error on the LLM side. And so just as you would build, you know,
pages in your interface to guide users to the behavior that you want, I think we are going to have to start
building, you know, endpoints and tools that are very explicit and clear and targeted so that your
LLMs can't falsely interpret or you give the LLM a greater chance of understanding what it needs to do
as opposed to trying to invent some combination of API inputs and getting it wrong. Of everything I
said, I think that maybe that's more the salient points again. So product managers and developers
are really going to have to change where their focus area is. And B, I suspect we will see some
sort of new API framework. I don't know that MCP is actually it. I think it's like
a very interesting start. But you do see in the MCPs, it's not just, you know, create,
read, update, and delete for every type of resource. You have these like dedicated,
more action-oriented tools that you provide the LLM, which under the hood,
you know, have abstracted away some of the complexities of your system. And I think that
doing that right and doing that intelligently, it's actually going to be pretty hard.
But there are best practices we can pull from, right? We've been building APIs in the SaaS world
for years, decades even. And so a lot of those old learnings we shouldn't just try to throw away.
There's a lot that we can use there. Because again, that is going to be the primary interface
for most of your users going forward, because they're going to chat with an LLM that then
chats with your APIs.

---

## 2026-07-09 07:50 — URecorder_20260709_084546.m4a

This one's going to be short, still on the interface data or interface logic data article.
Maybe the clearest way of saying this is that historically it's been web interface, APIs,
database, right?
And I think what's going to change for most users is its LLM chat, APIs, database.
And I do think that material really changes how you think about the APIs that you need to build
and surface to individuals.
I think it changes how you think about how users are going to engage and interact with
your product.
I think it changes how you think about how users are going to understand the value that
they are gaining from your product because we are fundamentally shifting the UI away
from something that you control to something you don't control at all, actually.
We are moving from deterministic control over I render you a page and user actions on that
page aren't always deterministic, but they're constrained and you're going to move it to
system that is totally open-ended and it can choose to use you, it can choose to use someone
else.
And so how do you build these things such that you are the tool of choice and that it
is an intelligent choice and that users understand that you are better than other tools that
it could have picked.
This is a very interesting problem that is fundamentally shifting, should be fundamentally
shifting how people build products today.

---

