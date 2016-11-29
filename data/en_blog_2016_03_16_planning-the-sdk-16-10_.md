





#  [SDK Planning for 16.10](/en/blog/2016/03/16/planning-the-sdk-16-10/)

# **On your mark!**

We have a clear commitment for the upcoming cycle: We will make it faster! One
might ask what exactly we want to make faster and how much faster? From the
point of SDK the most important place for performance improvements are the
applications and all the consumers of the UI Toolkit. So we will make the
applications start up faster, respond faster, use less memory and less power.
The starting point for this is to profile and refactor some of the components
we know could use some boosting. We will migrate the following components from
QML to C++:

  * AdaptivePageLayout

  * Page 

  * Picker

  * DateTimePicker

  * TextField

  * TextArea

In addition to improving the components we will check out the most critical
core applications and consult with their developers on how to get the most out
of the UITK. We all know how easy it is to create and develop apps in QML, but
when it comes to performance, every millisecond matters.

# **Closing the feature gaps**

The groundwork for convergence in the UI Toolkit was successfully put in place
but it is not complete yet. We have a few more components to implement and
hand over to application developers:

  * header subtitle 

  * keyboard control for the header

  * toolbar scrolling

  * exclusive group

  * radio buttons 

  * popup window

  * context menus 

  * new dialog component 

  * context menu

  * application menu

These components will land as part of Ubuntu.Components 1.3.

# **APIs and Frameworks**

Frameworks and framework versions are not the easiest part of the application
development story, to put it mildly. It is clear that we must have a framework
definition that specifies the APIs (platform package, name, import version)
that are supported on that particular device and each released framework must
have a public definition of the APIs it supports.

The most fundamental requirements for the API and framework control are:

  * Each platform module that provides application or platform development APIs must have an API definition and an API change tracker.

  * Each platform module that provides an API must have a version number bumping mechanism when it changes its API.

  * Each platform module that provides an API must have a blocking mechanism for API deprecation to prevent API breakage.

  * For application developers it must be trivial to learn what version of each QML module is available in a framework version and what QML import they can use.

  * For application developers there must be an API scanner that checks if the application is using only supported APIs; maybe that tool could help the developer figure out what minimum framework is required by the app.

In the following development cycles we are going to implement and release an
API tracker and framework management system to address all these (and many
more) related problems.

In short, we will have a simple and consistent framework management solution
that will be almost transparent for application developers.

# **UITK v2.0**

Even if the v1.3 of the UI Toolkit still receives new APIs and fixes we better
start working on the next major release. It is still way too early to talk
about detailed plans, but we already know that for example the multi-screen
DPR support will land on 2.0. Other than that this work is still in the
brainstorming and planning phase. Stay tuned and expect a blog post about this
topic from Zsombor. All in all, now is the time to step forward and join the
discussion!

# **Development Tools and IDE**

In the last few months we have changed a lot around the development tools and
the IDE. Finally the IDE is decoupled from the system Qt packages, so we can
offer a consistent developer experience regardless of what Ubuntu release the
SDK is installed on. This compact and confined packaging gives us more freedom
and flexibility, plus finally we can be as close to the upstream QtCreator and
Qt as possible.

The next steps will be to improve the application build process and the app
runtime testing. We are prototyping a new builder and runtime container that
is based on LXD. It will be much faster, lighter and more reliable than the
present schroot based builder. As a bonus we can move the app and scope
runtime from the host desktop to the LXD container. It means that developers
can see their apps and scopes in a native Unity8 shell in a container without
the overhead of the full system emulator.

In the following weeks we will be releasing the Pocket PC edition of the IDE
and we will add more and more Snappy support to our tools.

# **Integration and releases**

We will keep up the pace we have set in the last cycle. The goal is to push
out a new UI Toolkit release twice a month. Each release takes about a week to
be validated. Releasing a new Toolkit is a complex process. We need to make
sure that all the visual changes are inline with the design guidelines and we
need to run thousands of functional tests (automatic, thanks to autopilot) and
check if the new Toolkit blends in with the whole system. Just recently we
have added a new feature to our CI. Each merge request can be tested from a
simple installable click package. So if somebody wants to follow the UITK
development it can be safely done without messing up the system.

# **Keeping it all open**

Even under all the pressure to deliver the UI Toolkit and the SDK we will not
forget that what we do is not only open source software but we do it in an
open way. It is obvious that the UI Toolkit and the IDE projects are all open,
but we need to ensure that how we work is open, too. We will keep publishing
technical blog posts and videocasts about what is going on in the SDK
workshops. We welcome all contributions to our projects and we are going to
participate in various events to hear developers and to share information.

[Zoltán Balogh](/en/blog/authors/bzoltan/)

March 16, 2016

Filed under: [planet-ubuntu](/en/blog/tags/planet-ubuntu/)
[sdk](/en/blog/tags/sdk/)





## Comments

No comments yet.

## Add your comment

Name:

Email address:

URL:

Comment:

If you enter anything in this field your comment will be treated as spam:





