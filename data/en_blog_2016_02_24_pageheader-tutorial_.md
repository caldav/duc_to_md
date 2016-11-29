





#  [PageHeader tutorial](/en/blog/2016/02/24/pageheader-tutorial/)

## The new header property

This is a tutorial on how to use the new _PageHeader_ component. So far, we
had one header per application, implemented in the _MainView_, and
configurable for each page using the_ Page.head_ property (which is an
instance of _PageHeadConfiguration_). We deprecated that approach, and added
the _[_Page.header_](https://developer.ubuntu.com/api/apps/qml/sdk-15.04.1/Ubu
ntu.Components.Page/)_ property, which can be set to be any _Item_ so that
each page has its own header instance. When it is set, two things happen:

  1. The (deprecated) application header is disabled and any configuration that may be set using the old _Page.head_ property is ignored,

  2. The _Page.header_ item is parented to the page.

Because the header is parented to the page, inside the header you can refer to
its parent, and other items inside the page can anchor to the header.

![Example 1](/static/devportal_uploaded/13e3757e-f4bf-45a5-8056-620b975bd7d4-8
f7106b5-dc41-4737-aab2-b9c2f520fa76-media/2016/02/24/example1.png)

>

>     import QtQuick 2.4

>     import Ubuntu.Components 1.3

>     MainView {

>         width: units.gu(50)

>         height: units.gu(30)

>         Page {

>             id: _page

>     _        header: Rectangle {

>                 color: UbuntuColors.orange

>                 width: _parent_.width

>                 height: units.gu(8)

>                 Label {

>                     anchors.centerIn: _parent

>     _                text: "Title"

>                     color: "white"

>                 }

>             }

>             Rectangle {

>                 anchors {

>                     left: parent.left

>                     right: parent.right

>                     bottom: parent.bottom

>                     top: _page_.header.bottom

>                 }

>                 color: UbuntuColors.blue

>                 border.width: units.gu(1)

>                 Label {

>                     anchors.centerIn: _parent

>     _                text: "Hello, world!"

>                     color: "white"

>                 }

>             }

>         }

>     }

>

## Use PageHeader for an Ubuntu header

In order to get a header that looks like an Ubuntu header, use the _[_PageHead
er_](https://developer.ubuntu.com/api/apps/qml/sdk-15.04.1/Ubuntu.Components.P
ageHeader/)_ component. This component provides properties to set the title
and actions in the header and shows them the way you are used to in Ubuntu
apps. Below I will show how to customize the header styling, but first an
example that uses the default visuals:

![Example 2](/static/devportal_uploaded/a85e15ee-1dc8-4372-a554-b29f20d8f9de-6
d44ae5a-541c-4b52-bc15-7cbbf0395b14-media/2016/02/24/example2.png)

>

>     import QtQuick 2.4

>     import Ubuntu.Components 1.3

>     MainView {

>         width: units.gu(50)

>         height: units.gu(20)

>         Page {

>             header: PageHeader {

>                 title: "Ubuntu header"

>                 leadingActionBar.actions: [

>                     Action {

>                         iconName: "contact"

>                         text: "Navigation 1"

>                     },

>                     Action {

>                         iconName: "calendar"

>                         text: "Navigation 2"

>                     }

>                 ]

>                 trailingActionBar.actions: [

>                     Action {

>                         iconName: "settings"

>                         text: "First"

>                     },

>                     Action {

>                         iconName: "info"

>                         text: "Second"

>                     },

>                     Action {

>                         iconName: "search"

>                         text: "Third"

>                     }

>                 ]

>             }

>         }

>     }

>

The _leadingActionBar_ and _trailingActionBar_ are instances of _[_ActionBar_]
(https://developer.ubuntu.com/api/apps/qml/sdk-15.04.1/Ubuntu.Components.Actio
nBar/)_, and can thus be configured in the same way any action bar can be
configured. The default settings for the leading action bar configures the
number of slots as 1, sets the overflow icon to "navigation-menu", and the
default value for _actions_ is _navigationActions_, which is a property of the
_PageHeader_ set by the _[_PageStack_](https://developer.ubuntu.com/api/apps/q
ml/sdk-15.04.1/Ubuntu.Components.PageStack/)_ or _[_AdaptivePageLayout_](https
://developer.ubuntu.com/api/apps/qml/sdk-15.04.1/Ubuntu.Components.AdaptivePag
eLayout/)_ to show a back button when needed. If _leadingActionBar.actions_ is
explicitly defined as in the example above, the back button added by a
_PageStack_ or _AdaptivePageLayout_ is ignored. The trailing action bar
automatically updates its number of slots depending on the space available for
showing actions. On a phone it will show 3 actions by default, but on a tablet
or desktop more. When _actions.length > numberOfSlots_ for the leading or
trailing action bar, an overflow button will automatically be shown that shows
the other actions when tapped.

## Automatic show/hide behavior

The examples above show a static header where the page contents is anchored to
the bottom of the header. When the page contains a _Flickable_ or _ListView_,
this can be linked to the header so that it automatically moves with the
flickable:

>

>     import QtQuick 2.4

>     import Ubuntu.Components 1.3

>     MainView {

>         width: units.gu(50)

>         height: units.gu(40)

>         Page {

>             header: PageHeader {

>                 title: "Ubuntu header"

>                 flickable: _listView

>     _            trailingActionBar.actions: [

>                     Action {

>                         iconName: "info"

>                         text: "Information"

>                     }

>                 ]

>             }

>             ListView {

>                 id: _listView

>     _            anchors.fill: _parent

>     _            model: 20

>                 delegate: ListItem {

>                     Label {

>                         anchors.centerIn: _parent

>     _                    text: "Item " + index

>                     }

>                 }

>             }

>         }

>     }

When _PageHeader.flickable_ is set, the header automatically scrolls with the
flickable, and the _topMargin_ of the _Flickable_ or _ListView_ is set to
leave enough space for the header, so the flickable can fill the page. Besides
using the flickable to scroll the header in and out of the view, the
_PageHeader.exposed_ property can be set to show or hide the header. The
_PageHeader_ will automatically become more slim on a phone in landscape
orientation to make better use of the limited vertical screen space.

## Extending the header

Some applications require more functionality in the header besides the actions
in the leading and trailing action bars. For this, we have the _extension_
property which can be any _Item_ that will be attached at the bottom of the
header. For changing what is 'inside' the header, there is the _contents_
property which will replace the default title label. The following example
shows how to use the extension and contents properties to implement search
mode and edit mode that can be switched between by clicking the action buttons
in the default header:

![Example 4a](/static/devportal_uploaded/dac64158-6751-4210-91c7-f01065322f0e-
ef4d6fd4-fe0e-40ec-ab6b-f45aa7c8dde6-media/2016/02/24/example4a.png)

>

>     import QtQuick 2.4

>     import Ubuntu.Components 1.3

>     MainView {

>         width: units.gu(50)

>         height: units.gu(20)

>         Page {

>             id: _page

>     _        header: _standardHeader

>     _        Label {

>                 anchors {

>                     horizontalCenter: parent.horizontalCenter

>                     top: _page_.header.bottom

>                     topMargin: units.gu(5)

>                 }

>                 text: "Use the icons in the header."

>                 visible: _standardHeader_.visible

>             }

>             PageHeader {

>                 id: _standardHeader

>     _            visible: _page_.header === _standardHeader

>     _            title: "Default title"

>                 trailingActionBar.actions: [

>                     Action {

>                         iconName: "search"

>                         text: "Search"

>                         onTriggered: _page_.header = _searchHeader

>     _                },

>                     Action {

>                         iconName: "edit"

>                         text: "Edit"

>                         onTriggered: _page_.header = _editHeader

>     _                }

>                 ]

>             }

>             PageHeader {

>                 id: _searchHeader

>     _            visible: _page_.header === _searchHeader

>     _            leadingActionBar.actions: [

>                     Action {

>                         iconName: "back"

>                         text: "Back"

>                         onTriggered: _page_.header = _standardHeader

>     _                }

>                 ]

>                 contents: TextField {

>                     anchors {

>                         left: _parent_.left

>                         right: _parent_.right

>                         verticalCenter: _parent_.verticalCenter

>                     }

>                     placeholderText: "Search..."

>                 }

>             }

>             PageHeader {

>                 id: _editHeader

>     _            visible: _page_.header === _editHeader

>     _            property Component delegate: Component {

>                     AbstractButton {

>                         id: _button

>     _                    action: modelData

>                         width: _label_.width + units.gu(4)

>                         height: _parent_.height

>                         Rectangle {

>                             color: UbuntuColors.slate

>                             opacity: 0.1

>                             anchors.fill: _parent

>     _                        visible: _button_.pressed

>                         }

>                         Label {

>                             anchors.centerIn: _parent

>     _                        id: _label

>     _                        text: action.text

>                             font.weight: _text_ === "Confirm"

>                                          ? Font.Normal

>                                          : Font.Light

>                         }

>                     }

>                 }

>                 leadingActionBar {

>                     anchors.leftMargin: 0

>                     actions: Action {

>                         text: "Cancel"

>                         iconName: "close"

>                         onTriggered: _page_.header = _standardHeader

>     _                }

>                     delegate: _editHeader_.delegate

>                 }

>                 trailingActionBar {

>                     anchors.rightMargin: 0

>                     actions: Action {

>                         text: "Confirm"

>                         iconName: "tick"

>                         onTriggered: _page_.header = _standardHeader

>     _                }

>                     delegate: _editHeader_.delegate

>                 }

>                 extension: Toolbar {

>                     anchors {

>                         left: parent.left

>                         right: parent.right

>                         bottom: parent.bottom

>                     }

>                     trailingActionBar.actions: [

>                         Action { iconName: "bookmark-new" },

>                         Action { iconName: "add" },

>                         Action { iconName: "edit-select-all" },

>                         Action { iconName: "edit-copy" },

>                         Action { iconName: "select" }

>                     ]

>                     leadingActionBar.actions: Action {

>                         iconName: "delete"

>                         text: "delete"

>                         onTriggered: print("Delete action triggered")

>                     }

>                 }

>             }

>         }

>     }

>

## Customize the looks

Now that we covered the basic functionality of the page header, let's see how
we can customize the visuals. That can be done by creating a theme for your
app that overrides the _[_PageHeaderStyle_](https://developer.ubuntu.com/api/a
pps/qml/sdk-15.04.1/Ubuntu.Components.Styles.PageHeaderStyle/)_ of the
Ambiance theme, or by using _[_StyleHints_](https://developer.ubuntu.com/api/a
pps/qml/sdk-15.04.1/Ubuntu.Components.StyleHints/)_ inside the _PageHeader_.
To change the looks of the header for every page in your application, it is
recommended to create a custom theme, but the example below shows how to use
_StyleHints_ to change the properties of _PageHeaderStyle_ for a single
_PageHeader_ instance:

![Example 5](/static/devportal_uploaded/499a8e72-1124-45e5-9be7-49f6d3368f6d-9
9e82422-1c80-4d46-be87-981e05f9ad9c-media/2016/02/24/example5.png)

>

>     import QtQuick 2.4

>     import Ubuntu.Components 1.3

>     MainView {

>         width: units.gu(50)

>         height: units.gu(20)

>         Page {

>             header: PageHeader {

>                 title: "Ubuntu header"

>                 StyleHints {

>                     foregroundColor: "white"

>                     backgroundColor: UbuntuColors.blue

>                     dividerColor: UbuntuColors.ash

>                     contentHeight: units.gu(7)

>                 }

>                 trailingActionBar {

>                     actions: [

>                         Action {

>                             iconName: "info"

>                             text: "Information"

>                         },

>                         Action {

>                             iconName: "settings"

>                             text: "Settings"

>                         }

>                     ]

>                 }

>             }

>         }

>     }

>

If the header needs to be customized even further, use the _contents_
property, as is demonstrated in the example above for the search mode, or use
any _Item_ for _Page.header_, as was shown in the first example. For a fully
custom header that will still show and hide automatically when the user
scrolls in the page, use the _Header_ component which is the parent component
of _PageHeader_, and set its _flickable_ property.

That’s all. I am looking forward to see what you will do with the new and
often-requested flexibility of the new header in the Ubuntu UI Toolkit.

[Tim Peeters](/en/blog/authors/tpeeters/)

Feb. 24, 2016

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





