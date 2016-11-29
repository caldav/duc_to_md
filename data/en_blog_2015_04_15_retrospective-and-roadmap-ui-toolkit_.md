





#  [Retrospective and roadmap of the UI
Toolkit](/en/blog/2015/04/15/retrospective-and-roadmap-ui-toolkit/)

## **14.04 - 1.0 release**

The 1.0 release of the UITK was built mostly for demonstrative purposes, but
works well to a certain extent, it is the LTS release after all. Available
from the Trusty archive ([0.1.46+14.04.20140408.1-0ubuntu1](http://packages.ub
untu.com/source/trusty/ubuntu-ui-toolkit)) and from the SDK PPA
([0.1.46+14.10.20140520-0ubuntu1~0trusty2](https://launchpad.net/~ubuntu-sdk-
team/+archive/ubuntu/ppa/+sourcepub/4190958/+listing-archive-extra)). The
“demonstrative purpose” in this context is a pretty serious thing. This
release was the ultimate proof of concept that the Qt (5.2 by then) and QML
technology with our design and components provides a framework for a
charmingly beautiful and killing fast user interface. Obviously there is no
commercial touch device with this UITK release, but it is good to make a
simple desktop application with the UX of a mobile app. If your desktop PC is
running 14.04 LTS Ubuntu and you have installed the Ubuntu SDK then the IDE is
using this release of the UITK.

![](/static/devportal_uploaded/83fb1edc-d5f3-47da-b486-a4e4e29c1cbd-59473339-3
5bc-48da-874f-0b8ff797194e-media/2015/04/15/sdk2-blog.jpg)

The available components and features are documented either online [_https://d
eveloper.ubuntu.com/api/qml/sdk-14.04/Ubuntu.Components/_](https://developer.u
buntu.com/api/qml/sdk-14.04/Ubuntu.Components/) or offline under the[
file:///usr/share/ubuntu-ui-toolkit/doc/html](file:///usr/share/ubuntu-ui-
toolkit/doc/html) local directory if the ubuntu-ui-toolkit-doc is installed.

* * *

## **14.10 - 1.1 release**

It was the base for the first real Ubuntu phone. Most mission critical
components and toolkit features were shipped with this edition. The highlights
of the goodies you can see on the Utopic edition of the UITK (version [1.1.127
9+14.10.20141007-0ubuntu1](http://packages.ubuntu.com/source/utopic/ubuntu-ui-
toolkit)):

  * Settings API

  * Ubuntu.Web

  * ComboButton

  * Header replaces bottom toolbar

  * PullToRefresh

  * Ubuntu.DownloadManager

  * Ubuntu.Connectivity

![](/static/devportal_uploaded/699d15f2-1a0d-454a-a5db-1ce63a3225a3-8630a41f-8
0e3-4ad1-b155-3e26f0ea5d66-media/2015/04/15/sdk1-blog.jpg)

The focus of the UITK development was to complete the component set and
achieve superb performance. It is important to note that these days, this
exact version you can find only on very few community ported Ubuntu Touch
devices, and even those early adaptations should be updated to 15.04. The most
common place to meet this edition of the UITK is the 14.10 Ubuntu desktop.
This UITK can be indeed used to build pretty nice looking desktop
applications. The Ubuntu specific UI extensions of the QtCreator IDE are built
on our very own UITK. So, the UITK is ported and available for desktop app
development with some limitations since 14.04.

* * *

## **14.09 - the RTM release**

The development of the RTM (Ready To Market) branch of the UITK was focusing
on bugfixes and final polishing of the components. Dozens of functional,
visual and performance related issues were tackled and closed in this release.

A few of relevant changes in the RTM branch:

  * Internationalization related improvements

  * Polishing the haptics feedback of components

  * Fixes in the ActivityIndicator

  * UX improvements of the TextField/TextArea

  * Dialog component improvements

This extended 1.1 release of the UITK is what is shipped with the bq Aquaris
E4.5 devices. This is pretty serious stuff. Providing the very building rocks
for the user experience is a big responsibility. During the development of
this release one of the most significant changes happened behind the scenes.
The release process of the UITK was renewed and we have enforced very strict
rules for accepting any changes.

To make sure that with the continuous development of the UITK we do not
introduce functional problems and do not cause regressions we not only force
to run about 400 autopilot test cases on the UITK, but an automatic test
script validates all core and system apps with the release candidates. It
means running thousands of automatic functional tests before each release.

* * *

## **15.04 - 1.2 release **

After the 14.09 aka RTM release was found good and the bq devices started to
leave the factory lines the UITK development started to focus on two major
areas. First of all we brought back to the development trunk all the fixes and
improvements landed on the RTM branch and we merged back the whole RTM branch
to the main line. The second area was to open the 1.2 queue of the toolkit and
release the new features:

  * ListItem

  * New UbuntuShape rendering properties

  * New Header

![](/static/devportal_uploaded/a04d0be4-20b5-4d0c-b99b-8c68b9cd2801-d29358e9-e
075-49d2-8c7c-902e3ee56191-media/2015/04/15/sdk3-blog.jpg)

Releasing the 1.2 UITK makes the first big iteration of the toolkit
development complete. In the last three cycles the Ubuntu application
framework went through three minor Qt upgrades (5.2 - 5.3 - 5.4) and
continuously adapted to the improving design and platform.

* * *

## **15.10 - 1.3 release**

The upcoming cycle the focus is on convergence. We have shipped a super cool
UI Toolkit for touch environment, now it is time to make it offer as complete
and as fast toolkit for other form factors and for devices with other
capabilities. The emphasis here is on capability. Not only form factor or
device mode. The next release (1.3) of the UITK will adopt to the host
environment according to its capabilities. Like input capabilities, size and
others.

The highlights of the upcoming features:

  * Resolution independence

  * Improve visual rendering (pixel perfectness at any device ratio)

  * Improve performance (CPU and GPU wise)

  * Convergence

    * Tooltips

    * Key navigation - Tab/Shift+Tab

    * Date and Time Pickers

    * Menus

      * Application and

      * context menus

  * Support Sub-theming

  * Support of ListItem expansion

  * Text input magnification on selection

  * Simplified Popovers

  * Text input context menu

  * Deprecate Dialer (Ubuntu.Components.Pickers)

  * Deprecate PopupBase (Ubuntu.Components.Popups)

  * Focused component highlight

  * Support for OSK to keep the focus component above the key rectangle

  * Integrate scope toolkit from Unity with the UI Toolkit

The 1.3 version of the UITK will be the first with the promise that
application developers can create both fully functional desktop and phone
applications. In practice it means that the runtime UITK will be the same as
in the build environment.

* * *

## **16.04 - 2.0 release**

Looking forward to our next LTS release our ambition is to polish together all
the features and tune the UI Toolkit for the next major release. This edition
of the toolkit will serve app developers for long time. The 2.0 will be the
“mission completed”. We expect few features to move from our original 15.10
plans to the 16.04:

  * Clean up deprecated components

  * Rename ThemeSettings to Theme

  * Toolbars for convergence

  * Modal Dialogs

  * Device mode (aka capability) detection

  * Complete scopes support

  * Backend for Alarm services

  * Separate service components from UI components

[Zoltán Balogh](/en/blog/authors/bzoltan/)

April 15, 2015

Filed under: [planet-ubuntu](/en/blog/tags/planet-ubuntu/)
[sdk](/en/blog/tags/sdk/)





## Comments

  1. ![Alan Bell](http://www.gravatar.com/avatar/cfec4484c1084c10022538ce73ca7caf?s=60&r=G) Alan Bell 04/15/2015 2:55 p.m.

What is the plan for allowing user customisable aspects to the theme, such as
a different primary or accent colour or different base font size and having
this consistent across QML apps, HTML5 apps and remote web apps?

  2. ![Zsombor Egri](http://www.gravatar.com/avatar/d776e581bed02e090f62047e227afec6?s=60&r=G) Zsombor Egri 04/16/2015 5:30 a.m.

Alan, I hope I got your question right, but we already offer customisable
themes. Apps can create their own themes, derive from one of the system themes
or create their own one. Themes offer palette customisation, and there we have
a small problem, that we have to make sure we use palette in every component -
there are few components which do not fully use palette colours. More, 1.3
brings the sub-theming which also allows you to change/override the palette
colours you want (more about that in a separate post). Fonts are also planned
to be configurable through themes. Either in 1.3 or latest in 2.0.

Now HTML5 toolkit will most probably follow these plans on theming and also on
convergence, but I may not be the best person to comment on that.

## Add your comment

Name:

Email address:

URL:

Comment:

If you enter anything in this field your comment will be treated as spam:





