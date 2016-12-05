





#  [Return of the Ubuntu UI Toolkit](/en/blog/2015/03/30/ubuntu-components-1-2-release/)

Next month will be the release of Ubuntu 15.04 (Vivid Vervet) for desktop, and
this version of Ubuntu will soon become the version that will be installed on
Ubuntu phones as well. With the release of 15.04, we also release a new
version of our UI toolkit: _Ubuntu.Components 1.2_. Below are some of the new
features that it will have.

## **Hasta la vista, toolbar!**

In _Ubuntu.Components 1.1_, the bottom-edge toolbar was replaced by a new
header that can be used for navigating the app and trigger actions. Actions
that used to be in the toolbar were automatically moved to the header, and a
_useDeprecatedToolbar_ property was added to the _MainView_ for developers
that liked to keep the toolbar. In 1.2, the toolbar and _useDeprecatedToolbar_
property are definitely gone which enabled us to clean up the _MainView_ and
header code, so that we can give you a fresh new visual design and more
control over the looks and behavior of the header very soon.

## **One ListItem to rule them all**

![ListItem leading actions](/static/devportal_uploaded/ce68afb4-6309-4235-a80e-5d3faaa74acf-3523d58f-f6d0-4cb3-adf4-9b464ff265a0-media/2015/03/30/listitem-actions.png)

There are many different list items in _Ubuntu.Components.ListItems_, but they
are not always easy to customize and the performance when you use thousands of
them in your app is not optimal. Therefore, we now introduce the all-new
_ListItem_ component. It replaces all of the old list items, is super-fast
(even when you have ten thousands of them), you can swipe them left and right
to reveal actions, they offer selection mode (to quickly select a subset of
all the list items), and the user can re-order the items in a list. Awesome :)

## **Ubuntu Shape up (doo doo doo)**

**![Image with transparent background in UbuntuShape](/static/devportal_uploaded/67f40d5f-6a27-458b-bb2d-70e0e28c586c-acf7f762-cdcc-465f-aed2-e78a944781fa-media/2015/03/30/shape-colors.png)**

The _UbuntuShape_ is now in the best shape ever! It has been refactored to
optimize performance (for example, the rendering is now "batched" so even a
lot of them can be rendered fast), semi-transparent images and colored
backgrounds are supported, you can use all the fill modes and tiling that the
_Image_ component supports, there is 2D transformation support, and the
implementation was made extensible so that new features can be added more
easily.

Here is the code for the app that was used for the two screenshots above:

>

>     import QtQuick 2.4

>     import Ubuntu.Components 1.2

>

>     MainView {

>         width: units.gu(40)

>         height: units.gu(50)

>         //useDeprecatedToolbar: false // terminated

>

>         Page {

>             title: "Return of the UITK"

>

>             ListItemActions {

>                 id: _exampleLeadingActions_

>                 actions: [

>                     Action {

>                         iconName: "tick"

>                     },

>                     Action {

>                         iconName: "delete"

>                     }

>                 ]

>             }

>

>             ListView {

>                 anchors.fill: _parent_

>                 model: 10

>                 delegate: ListItem {

>                     id: _listItem_

>                     Label {

>                         anchors {

>                             left: parent.left

>                             leftMargin: units.gu(2)

>                             verticalCenter: parent.verticalCenter

>                         }

>                         text: "List item "+index

>                     }

>                     leadingActions: _exampleLeadingActions_

>

>                     UbuntuShape {

>                         anchors {

>                             right: _parent_.right

>                             top: _parent_.top

>                             bottom: _parent_.bottom

>                             margins: units.gu(0.5)

>                         }

>                         backgroundMode: _listItem_.highlighted ?

>                                             UbuntuShape.VerticalGradient :

>                                             UbuntuShape.SolidColor

>                         backgroundColor: _listItem_.highlighted ?

>                                              UbuntuColors.blue :

>                                              UbuntuColors.lightGrey

>                         secondaryBackgroundColor: UbuntuColors.green

>                         source: Image {

>                             source: "logo.png"

>                         }

>                         sourceFillMode: UbuntuShape.PreserveAspectFit

>                     }

>                 }

>             }

>         }

>     }

>

Besides these new features, we fixed a whole bunch of bugs and we are working
hard on the next version of the UI toolkit that we will be blogging about in
the near future, so stay tuned for more good stuff!

[Tim Peeters](/en/blog/authors/tpeeters/)

March 30, 2015

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





