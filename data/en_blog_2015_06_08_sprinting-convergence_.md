





#  [Sprinting for convergence](/en/blog/2015/06/08/sprinting-convergence/)

Convergence is all around. Our deeply loved UI Toolkit, what was primarily
targeting touch environments is converging to where users might have keyboards
and pointer devices. But that is just one point. The innovative track for
Ubuntu is called Snappy and at the same time the SDK is converging to the
desktop. We move to the direction where frameworks and applications are
packaged and distributed in a new model. It is exciting to see how the
different development tracks do move in the same direction.

Last week the SDK team has spent quality time with the creative folks from the
design team and with master ninjas from the QA team to put down the
foundations of a converged UI Toolkit and SDK.

We had two major questions when we entered the sprint:

* * *

### How UI Components will look and behave when pointer and keyboard devices
become available even during runtime?

### How can we enable scope and application development for literally any kind
of Ubuntu device?

* * *

Our offering is not only for smartphones. The UI components are as good on a
big screen desktop as on a tablet sized device or on any small device with a
screen. I totally can imagine the UI Toolkit on a car’s infotainment dash or
on a control panel of an intelligent house. But before the bold dreams we
focus on bringing the components to the classic desktop environment.

## **Application convergence**

When we talk about convergence we mostly mean application convergence. The
“definition of done” is when one can start an application on a touchscreen
phone and the application scales and adapts automatically to a bigger screen
with keyboard and mouse when plugged into the device.

The driving applications are Ubuntu browser, dekko email client, music player,
calendar, document viewer, messaging, address book, snap decisions/alerts and
Telegram.

As an addition the toolkit will provide API to control window and page sizing,
a component to easily transition from a one column pagestack to a multi-column
view, supporting 2 or more columns. A detachable header component is also
planned, so applications can put headers in different views, not only in a
MainView. But more about these in the following.

## **Foundations and tools**

To make a converged SDK we do need a solid and sustainable foundation. Not
only the UITK depends on the Qt stack but our own IDE needs it. On the sprint
we already made working prototypes of distro decoupled Qt and IDE packages. In
other terms it means that we can produce the Qt, UI Toolkit and SDK Tools
snappy packages pretty much any time when needed. The cool thing in keeping
our eyes on snappy is that this new structure motivates us to cut the loose
ends from our packages and make the SDK more portable and easier to build.

The promise is that we will have distro independent (snappable) SDK tools and
UITK with Qt 5.4 for anything what is compatible with the 14.04 Ubuntu.

## **UI Toolkit 2.0 plans**

Improving the performance and the overall quality are the keywords for UITK
2.0. We will list those components what would perform better if they were
implemented in C++, starting with MainView as it is needed for the Convergence
story.

We want to upstream the UITK to Qt. Living close to our upstream foundation
brings great value. Refactoring the source tree to have a single
Ubuntu.Components module without submodules is the natural first step towards
upstreaming. It will make the UITK more compatible with other Qt modules.
Early bits might land on 1.3 depending on the needs. The detailed API planning
will start end of Ubuntu 15.09 and is planned to land on 16.04.

## **Scopes**

The scopes toolkit will slowly migrate from the Unity8 space to the UI
Toolkit. It means that the components used now for scope development will be
available for classic application development. Also the scopes APIs are under
heavy re-factoring. According to the present plans the UITK will be available
to the scopes and scopes will become more active aggregators than ever. The
key point with scopes is that we will put lots of effort on scopes development
as they are one of the most visible differentiation from other platforms.

## **Scrollbars**

An issue with the current version is the thumb is covering actions in the UI
because it can not be positioned outside the window and if users approach an
action on the right hand side the thumb is revealed. The scrolling user
experience will be the same as in Unity7 with the exception that the thumb
appears inside the window area. The thumb follows the mouse cursor position
and hides when the mouse does not move. The design team is currently
prototyping two different scrollbars, one with a thumb and one without, which
visually would look the same as in Qt Creator for example, and we will
evaluate which fits better to the designs and will release the most
appropriate and usable one.

## **Tooltips**

When mouse pointers are available the tooltip appears when hovering over a
component. With a touch interface a long press interaction is under
investigation which would invoke a tooltip on a component or action..

The tooltip appears under the mouse cursor after a timeout (1 second),
positioned the same way as popovers, and disappears after a timeout (10s) or
when the mouse is moved out of the component’s area.

## **Date and time pickers**

This is one of the components which got a heavy design facelift. The
components are no longer tumbler based Pickers, but composed of an editable
component, which when tapped/clicked opens a popup, in which there can be a
calendar component for date picking, or a picker for time picking. The main
component is a text input with no text cursor, when activated with keyboard,
the entire content will be selected, and can be edited at once, i.e. no
positioning will be possible. The popups will be full screen dialogs on
screens smaller than 40x71 GU, and popovers on bigger screens.

## **Dropdown Menus & popovers**

We are considering to reuse QtQuick Controls Menu components, adapting those
to the toolkit’s theming and actions. Keyboard shortcuts and accelerator will
only be visible with mouse/keyboard attached in any drop down menu. The
context menus will be single level menus in the first iteration and cascading
menus might come later if needed. The individual application menus are not
high priority but we will listen to the app developers and hear what they
need.

## **Expandables, ListItems module**

As now we have OptionSelector and ItemSelector what is confusing, and neither
of them is configurable enough. The old Ubuntu.Components.ListItems has a pile
of components which is just not flexible enough, and they are all
underperforming. Expansion will be introduced to the new ListItem, and new
layouts will be made which will be flexible enough to survive eventual design
changes. This is not a high priority for convergence, however it will serve as
a ground for phone and desktop layouts as well as the prerequisite for the
application menus. We will keep trying to separate the layout from the
ListItem, hopefully we will manage to do that performantly enough.

## **Accessing ListItem actions on desktop**

At first, a mouse right click will bring up a `contextual` menu which will
contain leading, trailing and default actions, as well as selection/drag
modes, without any API change on ListItem. After application menu will be
implemented, we will enable the context menu on the ListItem together with
other components.

## **Panels behaviour & MultiColumnView**

For the 2-column pagestack we still need to find out the best navigation
model, more precisely the way we handle the headers of the pages, cascading or
not. We gathered the tasks we have to complete in order to provide convergent
view handling:

  * PageStack cannot be adapted to the new UX without major API changes, therefore we will introduce a component called MultiColumnView, which can transition from one column to 2 or more columns. The component will put Pages side by side, and will maintain a stack depending on where the page is pushed, above the current page or next to it. Applications using this component must specify the minimum and maximum sizes for the page

  * Title, or header handling should be detached from MainView, and there will be a Header component which then can be used in bottom edge, or a ListView’s header component

  * The bottom edge will be used on the desktop, and there will be a component called BottomEdgeHint which provides a clickable component if there’s a mouse. The bottom edge swipe known from the touch environment will simply translate a new clickable component what will appear when the mouse is hovered on it. The content of the component (for example a pagestack) depends on what the developer wants.

## **Focus handling**

The focus handling concerns not only TAB/Shift+TAB navigation between
components, but also the keyboard navigation inside composite components, such
as ListView, ComboButton, text inputs, header, etc. The focus highlight is
more or less agreed, however there is a little prototyping ongoing to figure
out whether we can do some nice effects on it or not.

[Zoltán Balogh](/en/blog/authors/bzoltan/)

June 8, 2015

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





