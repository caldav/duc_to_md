





#  [Adaptive page layouts made easy](/en/blog/2015/08/10/adaptive-page-layouts/)

![Adaptive page layouts made easy](/static/devportal_uploaded/5f519c74-5718-474e-9196-eea21644bd4a-uploads/zinnia/100gu-right.png)

## Convergent applications

We want to make it easy for app developers to write an app that can run on
different form factors without changes in the code. This implies that an app
should support screens of various sizes, and the layout of the app should be
optimal for each screen size. For example, a messaging app running on a
desktop PC in a big window could show a list of conversations in a narrow
column on the left, and the selected conversation in a wider column on the
right side. The same application on a phone would show only the list of
conversations, or the selected conversation with a back-button to return to
the list. It would also be useful if the app automatically switches between
the 1-column and 2-column layouts when the user resizes the window, or
attaches a large screen to the phone.

To accomplish this, we introduced the _AdaptivePageLayout_ component in
Ubuntu.Components 1.3. This version of Ubuntu.Components is still under
development (expect an official release announcement soon), but if you are
running the latest version of the Ubuntu UI Toolkit, you can already try it
out by updating your import Ubuntu.Components to version 1.3. Note that you
should not mix import versions, so when you update one of your components to
1.3, they should all be updated.

## AdaptivePageLayout

_AdaptivePageLayout_ is an _Item_ with the following properties and functions:

  * _property Page primaryPage_
  * _function addPageToCurrentColumn(sourcePage, newPage)_
  * _function addPageToNextColumn(sourcePage, newPage)_
  * _function removePages(page)_

To understand how it works, imagine that internally, the _AdaptivePageLayout_
keeps track of an infinite number of virtual columns that may be displayed on
your screen. Not all virtual columns are visible on the screen. By default,
depending on the width of your _AdaptivePageLayout_, either one or two columns
are visible. When a _Page_ is added to a virtual column that is not visible,
it will instead be shown in the right-most visible column.

The _Page_ defined as _primaryPage_ will initially be visible in the first
(left-most) column and all the other columns are empty (see figure 1).

Figure 1: Showing only primaryPage in layouts of 100 and 50 grid-units.

[![Showing only primaryPage at 100 grid units.](/static/devportal_uploaded/06c6dd6b-39b5-41b8-b86f-f3aae72570fa-8fbf7abc-3c25-454d-879c-35deda1adf2e-media/2015/08/10/100gu-root.png)](/static/devportal_uploaded/06c6dd6b-39b5-41b8-b86f-
f3aae72570fa-8fbf7abc-3c25-454d-879c-35deda1adf2e-media/2015/08/10/100gu-
root.png)

[![Showing primaryPage at 50 grid units.](/static/devportal_uploaded/76a3ad66-03e6-49c6-ac1b-e50bc7d31fd5-e59ebaf4-6ba9-4ac9-aee5-4864edf62051-media/2015/08/10/50gu-root.png)](/static/devportal_uploaded/76a3ad66-03e6-49c6-ac1b-e50bc7d
31fd5-e59ebaf4-6ba9-4ac9-aee5-4864edf62051-media/2015/08/10/50gu-root.png)

To show another _Page_ in the first column, call _addPageToCurrentColumn()_
with as parameters the current page (_primaryPage_), and the new page. The new
page will then show up in the same column with a back button in the header to
close the new page and return to the previous page (see figure 2). So far,
_AdaptivePageLayout_ is no different than a _PageStack_.

Figure 2: Page with back button in the first column.

[![Page with back button in the first column at 100 grid units.](/static/devportal_uploaded/9802256d-fd6b-449c-93fb-94aaa2d7cdd4-88646788-665a-4bd1-a859-edbb6764acd4-media/2015/08/10/100gu-left.png)](/static/devportal_uploaded/9802256
d-fd6b-449c-93fb-94aaa2d7cdd4-88646788-665a-4bd1-a859-edbb6764acd4-media/2015/
08/10/100gu-left.png)

[![Page with back button in first column at 50 grid units.](/static/devportal_uploaded/587a8db9-37f9-42a7-8fbe-f456b6b6735f-6de5840a-e5e3-4e0f-986b-b1600acd871e-media/2015/08/10/50gu-left.png)](/static/devportal_uploaded/587a8db9-37f9
-42a7-8fbe-f456b6b6735f-6de5840a-e5e3-4e0f-986b-b1600acd871e-media/2015/08/10/
50gu-left.png)

The differences with _PageStack_ become evident when you want to keep the
first page visible in the first column, while adding a new page to the next
column. To do this, call _addPageToNextColumn()_ with the same parameters as
_addPageToCurrentColumn()_ above. The new page will now show up in the
following column on the screen (see figure 3).

Figure 3: Adding a page to the next column.

[![Added a page to the next column at 100 grid units.](/static/devportal_uploaded/fe372d9b-d8df-426f-a0de-84c36b0d9e5e-602d0540-804b-45ad-befc-960b2ddf3c60-media/2015/08/10/100gu-right.png)](/static/devportal_uploade
d/fe372d9b-d8df-426f-a0de-84c36b0d9e5e-602d0540-804b-45ad-
befc-960b2ddf3c60-media/2015/08/10/100gu-right.png)

[![Added a page to the next column at 50 grid units.](/static/devportal_uploaded/0cffbb91-eef0-4f19-846d-a5424a89d342-5ca06439-ec4f-4217-b321-5a765fbb9ada-media/2015/08/10/50gu-right.png)](/static/devportal_uploaded/0cffbb91-eef0-4f1
9-846d-a5424a89d342-5ca06439-ec4f-4217-b321-5a765fbb9ada-
media/2015/08/10/50gu-right.png)

However, if you resize the window so that it fits only one column, the left
column will be hidden, and the page that was in the right column will now have
a back button. Resizing back to get the two-column layout will again give you
the first page on the left, and the new page on the right. Call
_removePages(page)_ to remove _page_ and all pages that were added after
_page_ was added. There is one exception: _primaryPage_ is never removed, so
_removePages(primaryPage)_ will remove all pages except _primaryPage_ and
return your _AdaptivePageLayout_ to its initial state.

_AdaptivePageLayout_ automatically chooses between a one and two-column layout
depending on the width of the window. It also automatically shows a back
button in the correct column when one is needed and synchronizes the header
size between the different columns (see figure 4).

Figure 4: Adding sections to any column increases the height of the header in
every column.

[![Added a page with sections to the right column at 100 grid units.](/static/devportal_uploaded/4991f692-2bf4-4951-a2d1-4659d83f269b-455b5bb3-b9d6-41b1-bccc-b3857ab2de94-media/2015/08/10/100gu-sections.png)](/static/devportal_uploade
d/4991f692-2bf4-4951-a2d1-4659d83f269b-455b5bb3-b9d6-41b1-bccc-b3857ab2de94-me
dia/2015/08/10/100gu-sections.png)

[![Added a page with sections at 50 grid units.](/static/devportal_uploaded/29edb73b-7f29-44e3-8ce6-3974ef600b31-dfef5024-4573-4d20-8cd5-d6b37ed2f540-media/2015/08/10/50gu-sections.png)](/static/devportal_uploaded/29edb73b-7f29-44e3-8
ce6-3974ef600b31-dfef5024-4573-4d20-8cd5-d6b37ed2f540-media/2015/08/10/50gu-
sections.png)

## Future extensions

The version of _AdaptivePageLayout_ that is now in the UI toolkit is only the
first version. What works now will keep working, but we will extend the API to
support the following:

  * Layouts with more than two columns
  * Use different conditions for switching between layouts
  * User-resizable columns
  * Automatic and manual hiding of the header in single-column layouts
  * Custom proxy objects to support Autopilot tests for applications

Below you can read the full source code that was used to create the
screenshots above. The screenhots do not cover all the possible orders in
which the pages left and right can be added, so I encourage you to run the
code for yourself and discover its full behavior. We are looking forward to
see your first applications using the new _AdaptivePageLayout_ component soon
:). Of course if there are any questions you can leave a comment below or ping
members of the SDK team (I am t1mp) in #ubuntu-app-devel on Freenode IRC.

>

>     import QtQuick 2.4

>     import Ubuntu.Components 1.3

>

>     MainView {

>         width: units.gu(100)

>         height: units.gu(70)

>

>         AdaptivePageLayout {

>             id: layout

>             anchors.fill: parent

>             primaryPage: rootPage

>

>             Page {

>                 id: rootPage

>                 title: i18n.tr("Root page")

>

>                 Column {

>                     anchors {

>                         top: parent.top

>                         left: parent.left

>                         margins: units.gu(1)

>                     }

>                     spacing: units.gu(1)

>

>                     Button {

>                         text: "Add page left"

>                         onClicked: layout.addPageToCurrentColumn(rootPage,
leftPage)

>                     }

>                     Button {

>                         text: "Add page right"

>                         onClicked: layout.addPageToNextColumn(rootPage,
rightPage)

>                     }

>                     Button {

>                         text: "Add sections page right"

>                         onClicked: layout.addPageToNextColumn(rootPage,
sectionsPage)

>                     }

>                 }

>             }

>

>             Page {

>                 id: leftPage

>                 title: i18n.tr("First column")

>

>                 Rectangle {

>                     anchors {

>                         fill: parent

>                         margins: units.gu(2)

>                     }

>                     color: UbuntuColors.orange

>

>                     Button {

>                         anchors.centerIn: parent

>                         text: "right"

>                         onTriggered: layout.addPageToNextColumn(leftPage,
rightPage)

>                     }

>                 }

>             }

>

>             Page {

>                 id: rightPage

>                 title: i18n.tr("Second column")

>

>                 Rectangle {

>                     anchors {

>                         fill: parent

>                         margins: units.gu(2)

>                     }

>                     color: UbuntuColors.green

>

>                     Button {

>                         anchors.centerIn: parent

>                         text: "Another page!"

>                         onTriggered:
layout.addPageToCurrentColumn(rightPage, sectionsPage)

>                     }

>                 }

>             }

>

>             Page {

>                 id: sectionsPage

>                 title: i18n.tr("Page with sections")

>                 head.sections.model: [i18n.tr("one"), i18n.tr("two"),
i18n.tr("three")]

>

>                 Rectangle {

>                     anchors {

>                         fill: parent

>                         margins: units.gu(2)

>                     }

>                     color: UbuntuColors.blue

>                 }

>             }

>         }

>     }

>

[Tim Peeters](/en/blog/authors/tpeeters/)

Aug. 10, 2015

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





