





#  [New PageHeader.subtitle with framework 15.04.5 inOTA-11](/en/blog/2016/05/10/new-pageheadersubtitle-framework-15045-ota-11/)

With OTA-11 on the horizon, rc-proposed now has a new framework. If you want
to use the latest UI Toolkit API, that is part of Ubuntu.Components 1.3, you
should bump your framework to 15.04.5 - in QtCreator you can find your
manifest.json.in under Other Files and simply select the new version. Now you
can use the new subtitle property with PageHeader which complements the
existing title and shows a smaller label at the bottom of the header.
PageHeaderStyle gains subtitleColor which can be used via StyleHints to
customize the looks of the new subtitle. disabledForegroundColor further more
now allows changing the color of the actions when the header is disabled. For
example

`Page {

header: PageHeader {

id: pageHeader

title: i18n.tr("Hello World")

subtitle: i18n.tr('Lorem ipsum dolor sit amet')

StyleHints {

backgroundColor: UbuntuColors.inkstone

foregroundColor: UbuntuColors.blue

// The color of disabled actions

disabledForegroundColor: UbuntuColors.red

// The divider at the bottom

dividerColor: UbuntuColors.red

// The new subtitle

subtitleColor: UbuntuColors.green

}

trailingActionBar.actions: [

Action {

iconName: 'list-add'

onTriggered: console.log('Hello world')

},

Action {

iconName: 'list-remove'

enabled: false

}

]

}

}`

"`enabled: false`" in the Action turns it red as it no longer responds to
touch, mouse or keyboard input (the same can be done for all actions by
disabling PageHeader).

## Remember OTA-10 and framework 15.04.4?

Already shipping on most if not everyone’s Ubuntu devices now is OTA-10 which
brought with it new API for the BottomEdge component: preloadContent. This new
boolean property when set to true causes all contents to preload in the
background even before the hint is being used to reveal it - the default is
false, which means contents are loaded on demand like before. This can speed
things up a great deal in some cases.

`BottomEdge {

id: bottomEdge

height: parent.height - units.gu(20)

hint.text: “My bottom edge”

preloadContent: true

contentComponent: Rectangle {

color: UbuntuColors.green

width: page.width

height: page.height

}

}`

[Christian Dywan](/en/blog/authors/kalikiana/)

May 10, 2016

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





