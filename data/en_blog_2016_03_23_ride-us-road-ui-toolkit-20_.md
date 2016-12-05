





#  [Ride With Us: The Road To UI Toolkit 2.0](/en/blog/2016/03/23/ride-us-road-ui-toolkit-20/)

In 2012 we started the Ubuntu UI Toolkit development with QML-only components,
all logic being provided in Javascript. This allowed us to deploy components
quickly, to do fast prototyping, and tweak the behaviors and look-and-feel on
the fly without the need to re-package or rebuild the entire toolkit. With all
its benefits, this approach revealed its negative side, which is the impact on
the performance. Complex applications are the most affected, which use many
components, and their startup as well as rendering time is heavily affected by
the component performance.

Then came the theming, the grid units, and the i18n localization, which
introduced the plugin. The theming engine was the only component implemented
in C++ as we knew from the beginning that we needed to be fast on loading and
especially applying the styles on components. The style loading was done in
QML using loaders, which kept the flexibility on tweaking. After several
attempts on optimizing the engine, we decided to refactor it, and we managed
to come up with a theming that was little more than twice as fast as the
previous one. Although we started to gain speed on components initialization,
components were still too slow to be applicable in kinetic scrolling. List
views were still laggish, delegate creation of the simplest ListItem module
component was still 60 times slower than of an Item. Therefore we decided to
move components to C++ one by one, especially the ones on the critical path.
StyledItem was one of the first, followed by a new ListItem component, which
by now you are all familiar with. So it became crystal clear that, if we want
you guys to be able to play with full QML apps and still have decent
performance in your apps, we must provide at least the core logic of the
components in C++, and do the styling in QML. This thought was confirmed also
by the Qt developers, when they announced the start of the next generation of
the Qt Quick Controls.

But let’s take the biggest issues that brought us to press the reset button.

## API

When a person takes a toolkit in his/her hand, the first thing (s)he will
encounter is the API. Are the component names self-explanatory, is the API
easy to use, no ambiguities when using it, etc, etc. Many developers do not
read the API docs, they just jump in and start running the example codes,
copying the examples from the documentation without reading a line from it.
And next, they will try experimenting on the components, start changing
properties, add functionality to the code, and so they start shaping their
ideas for their apps.

I think API wise we are in a pretty good shape, we tried to be as close to the
declarative QML world as possible, and follow the practices imposed by the Qt
Company. I know, not everything is configurable in the components, and that is
mostly due to the policy we started with, which was to keep as much
configuration in the styling as possible, so we can keep consistency in
between components in the applications. But there are different ways to
achieve consistency and still keep configurability on a level that developers
will be happy to use the API. Both sides have their benefits: smaller API is
less complex than one which has plenty of configurations, even if those are
color values, on the other hand it is impossible to change its visuals. Some
of you may think the API is crap because we don’t provide enough
customization, or access to certain elements of the component. We do feel and
understand your pain, and we will try to come over it and compensate you in
the future.

## Behavior

When the developer starts using a component, he/she expects the component to
do what it is meant for. A Button is expected to be clickable, a text input to
accept text editing gestures, a list item to provide content layouting
functionality when used in views and a header to display a title and some
other vital functionality for the application. If a component can cooperate
with another one when placed side by side, without the developer doing
anything, that is the cherry on the cake. But that’s where the problem starts:
a component which must take into account its surroundings and change adapts
its behavior creates confusion. A much cleaner approach is to let the
developer do this rather than the components themselves, but components should
provide connectors and enablers so these interactions can be achieved. Yes,
application developers will have to do more, but now they will be in control.

## Context Properties as Singletons

Context properties are nice when an application wants to expose a model or
other logic to its QML UI layer. Those are pretty simple to implement, however
also provide unreadable code for those who read the two worlds (QML and C++ or
other non-QML code) separately. The problem gets even worse when these context
properties are representing singletons. QML has the notion of singletons but
those were not suitable for the functionality we needed for localization
(i18n) theming and grid units. The quickest decision was to provide them as
context properties, so whenever the locale, system theme or the screen’s grid
unit changes during the application’s lifetime, these will be automatically
updated, so when used in bindings, those will be automatically re-evaluated.
However these context properties cannot be used in [shared Javascriptlibraries](http://doc.qt.io/qt-5/qtqml-javascript-resources.html#shared-javascript-resources-libraries). And our measurements had proven that
importing a module which contains and uses [code-behind implementationjavascript](http://doc.qt.io/qt-5/qtqml-javascript-resources.html#code-behind-implementation-resource) libraries takes almost 3 times longer than one which
has shared libraries. In addition, now when convergence brings the multi-
monitor feature to Ubuntu, each monitor can have a different grid unit size,
which means the global units context property singleton is not usable in an
application which uses multiple windows. So we must get rid of these kinds of
interpretations of the singletons and provide proper ones which are naturally
supported by QML.

## Complex Theming

Now this is one of the biggest problems. The theming went through a complete
evolution: from CSS-like styling to a complete QML-based declarative styling,
and then to sub-theming, so each application can use multiple themes at the
same time. The performance increased dramatically when we dropped the first
version in favor of the declarative one, but it is still slower when compared
to a component which implements its visuals on top of a template that provides
the logic (see QtQuick Controls second generation).

## Performance

Oh, yes. All above are contributing to the slow performance of the components,
which results in bad performance in applications. Styling is still a
bottleneck. We’ve ported some components from QML to C++ to gain some speed in
both loading and UI response time, however we have still components entirely
written in QML and Javascript, and those are clearly performance eaters. And
these monsters are catching your eyes, because they are used the most:
AdaptivePageLayout turned to be the most loved component due to its support
for the converged application development, but there are the text inputs
(TextField and TextArea) which are again components taking too long to
instantiate. We have to make them performant, and the only solution is to make
them in C++. Of course, C++ is not the Holy Grail, one can make nasty things
there too. But so far, we’ve managed to get the components we’ve ported to C++
to behave really well and even provided performance gain to the components
derived from them. There was a reason why BlackBerry made its toolkit in C++
and exposed it to QML...

# The Plan

So we came up with a plan. And the plan includes you. The plan needs you to
succeed, it won’t work without you.

First we thought that we can introduce the new features and slowly turn all
the components into performant ones. But then came the DPR support, which
despite the fact that from Qt 5.7 onwards it will support floating point
value, QWidget based apps will still be broken, as those only support integer
sizes. This can be handled behind the scenes, however apps with multiple
windows must support different grid unit/DPR sizes when those windows are laid
out on different screens. This means that we must do something about the way
we handle the grid units, and that, unfortunately, cannot be done without an
API break.

But then, if we break it, let’s do it properly! This leads us to really go for
the second generation if the UI toolkit, which we were already dreaming of for
about a year. This means breaking the backwards compatibility in some APIs.
However, whenever is possible, we will keep the interface compatible, but that
may not apply to component inheritance.

## API design

We will start sharing all API designs with you, so you can contribute! We
don’t have a clear plan yet, but we could introduce a “labs” module where the
API can be tried out for each component before it lands to the stable module.
We must find a way to share the API documents with you so you can comment and
request interface changes/additions. (So later you can blame yourself for the
mistakes :) ) The policy will be the same, an API once released cannot be
revoked, only deprecated. By introducing the labs module, we could give a few
weeks or months of time for you to try it out, and provide fixes/comments. Of
course, components which were already designed will keep the API but will be
exposed for additional requests. And also, we will try to minimize the API to
the use cases we have.

## Styling

When it comes to component implementation we will follow the template+UI layer
design, so components will be implemented on top of templates. If your
application requires different layout, you will be free to implement it
yourself using the template. Therefore we can say that we will have two API
layers: the template layer APIs and the UI layer APIs, this last bringing
additional properties to the component customizing the look and feel of the
component itself, without modifying the logic of the component (i.e. colors,
borders, transitions). Both layers will be treated with the same stability
promise.

In addition, the theming will still be available, but will not contain
anything else but the palette, and the font of the theme. We don’t know yet
how will this be available to you, either through a component property of
attached properties, we have to benchmark both solutions and see which one is
more reliable. Both solutions have their pros and cons, let’s see which one
will be the winner.

## When Do We Start?

As soon as possible! First we need to open a repository and provide the
skeleton for it, and then move the former singletons so we have a clear API
for them. Then we need to get the components one by one from the 1.x into the
new base, and revisit each component’s API with you all. We will let you know
when the trunk is available so you can start playing with it.

## When Will It Be Available?

The journey will be a bit longer as we must keep UI Toolkit 1.3 up to date and
stable, and in parallel provide features to 2.0. The expectation is that by
the end of October we should have a few components in the labs module so those
can be tested. We expect to have components appearing in the labs written in
C++, so no QML first then move to C++ approach anymore, as the idea is once
the component API is seen to be stable enough, we move that to the released
package without any effort. Also, as all the major version changes used to be,
this version will not be backwards compatible nor usable with 1.x versions,
meaning that your QML application would not be able to import 1.x and 2.0 same
time.

## Shouldn’t We Take The Next Generation of QtQuick Controls as base?

That is a good point, and we’ve been considering that option too. However some
of our components’ behavior is so different that it may make sense to simply
follow a different path rather than take those as base. But we promise we will
consider it as an option. We’ve had a discussion back in last December when we
talked about the QtQuick Controls blending in with UI Toolkit, see it
[here](https://www.youtube.com/watch?v=d-LJFMoaHv0).

# Final words

It will be a long journey, a tough one, but finally it will be properly open.
Lots of IRC discussions, hangouts, videos, labs works… It’ll be fun! I cannot
promise pizza, or beer for you guys, but I promise it'll be hell of a good
ride!

[Zsombor Egri](/en/blog/authors/zsombi/)

March 23, 2016

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





