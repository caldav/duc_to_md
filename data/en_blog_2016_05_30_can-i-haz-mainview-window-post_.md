





#  [Can I haz MainView in a Window?](/en/blog/2016/05/30/can-i-haz-mainview-
window-post/)

Apps are currently advised to use a [MainView](https://developer.ubuntu.com/ap
i/apps/qml/sdk-15.04.5/Ubuntu.Components.MainView/) as the root item, which
can have a width and a height used as the window dimensions in a windowed
environment - on phones and tablets by default all apps are always full
screen. As soon as users can freely resize the window, [some apps may not look
great anymore](https://bugs.launchpad.net/ubuntu/+source/ubuntu-ui-
toolkit/+bug/1483331) - [QtQuick.Window](https://developer.ubuntu.com/api/apps
/qml/sdk-15.04.5/QtQuick.Window.Window/) solves this by providing
minimum/maximum/Width/Height properties. Another question is [what title is
used for the window](https://bugs.launchpad.net/ubuntu/+source/ubuntu-ui-
toolkit/+bug/1341677) - as soon as there is more than one Page that's no
longer obvious and it's actually somewhat redundant.

## So what can we do now?

There’s two ways to sort this that we’ll be discussing here. One way is to in
fact go ahead and use MainView, which is just an Item, and put it inside a
Window. That’s perfectly fine to do and that’s a good stop-gap for any apps
affected now. To the user the outcome is almost the same, except the title and
sizing can be customized behind the scenes.

import QtQuick 2.4

import QtQuick.Window 2.2

import Ubuntu.Components 1.3

Window {

title: "Hello World"

minimumWidth: units.gu(30)

minimumHeight: units.gu(50)

maximumWidth: units.gu(90)

maximumHeight: units.gu(120)

MainView {

applicationName: "Hello World"

}

}

From here on after things work exactly the same way they did before. And this
is something that will continue to work in the future.

## A challenger appears

That said, there’s another way under discussion. What if there was a new
MainWindow component that could replace the MainView and provide the missing
features out of the box? Code would be simpler. Is it worth it, though, just
to save some lines of code you might wonder? Yes actually. It is worth it when
performance enters the picture.

As it is now, MainView does many different things. It displays a header for
starters - that is, if you’re not using AdaptivePageLayout to implement
convergence. It also has automaticOrientation API, something the shell does a
much better job of these days. And it handles actions, which are, like the
header, part of each Page now. It’s still doing a good job at things we need,
like setting up folders for confinement (config, cache, localization) and
making space for the OSK (in the form of anchorsToKeyboard). So in short,
there’s several internals to re-consider if we had a chance to replace it.

Even more drastic would be the impact of implementing properties in MainWindow
that right now are context properties. “units” and “theme” are very useful in
so many ways and at the same time by design super slow because of how QML
processes them. A new toplevel component in C++ could provide regular object
properties without the overhead potentially speeding up every single use of
those properties throughout the application as well as the components using
them behind the scenes.

Let’s be realistic, however, these are ideas that need discussion, API design
and planning. None of this is going to be available tomorrow or next week. So
by all means, engage in the discussions, maybe there’s more use cases to
consider, other approaches, it’s the one component virtually every app uses so
we better do a good job coming up with a worthy successor.

[Zoltán Balogh](/en/blog/authors/bzoltan/)

May 30, 2016

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





