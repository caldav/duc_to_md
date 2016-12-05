





#  [Announcing new snap desktop launchers](/en/blog/2016/07/06/announcing-new-snap-desktop-launchers/)

## Background

Integrating desktop applications with snaps has been a little bit challenging
in terms of getting them looking and behaving as part of the system. This
means following general desktop theming, having global application menu
integration, getting the icon caches, getting configuration keys and such.
Also, the technologies and toolkits like GTK, Qt, demand a little bit of
expertise on that front.

![](http://core1.staticworld.net/images/article/2016/05/ubuntu-snappy-100658857-large.png)

That's the reason why we saw flourishing some desktop helpers like gtkconf or
qtconf as [cloud snapcraft parts](https://wiki.ubuntu.com/snapcraft/parts) for
this. However, they were sharing little code and some part of the integration
was working for one flavor and not the other flavor and vice-versa.

## New desktop launchers to the rescue!

This is the reason why we are announcing new destkop launchers! The goal was
to streamline the experience and ensuring that all following user visible
features are working, independent of the toolkit or technology you are using:

  * Bind with current desktop theme if shipped by default (GTK & Qt)
  * Icons theme available for decoding (with the right decoders automatically shipped)
  * Application menu integration (in Unity)
  * Icon cache and images generated on first launch (no more need to ship pre-compile GSettings and Gio caching modules) after a new upgrade
  * Keep previous xdg-based data, even after upgrade
  * GSettings keys available for reading (not only writing)
  * Most of the code is shared between the launchers, so any fix in one will benefit others, and we assemble them at build time.
  * Avoid erratic behavior like _cd $SNAP_ that some launchers were doing and not others (we don't change the current working directory anymore)

![Ristretto before applying desktop/gtk3](http://i.imgur.com/j2rPrf0.png)
![Ristretto with desktop/gtk3](http://i.imgur.com/FgqfzZT.png)

Those new cloud parts also ship with default package set configuration to
ensure all features are enabled, this is overridable as well, as explained [bySergio in his blog post](http://blog.sergiusens.org/posts/The-Snapcraft-Parts-Ecosystem/).

Qt-based applications also show those drastic improvements. Note that the
[appmenu fix for Qt applications](https://github.com/snapcore/snapd/pull/1463)
will only work starting with snapd 2.0.10.

![SMPlayer before using desktop/qt5](http://i.imgur.com/BtevDNV.png)
![SMPlayer using desktop/qt5](http://i.imgur.com/4RyzCrP.png)

## Definition and usage

We currently have 5 launchers, depending on the technology you want to
support: **gtk2**, **gtk3**, **qt4**, **qt5** and **glib-only** for a
lightweight, non graphical app, but needing basic integration like GSettings
and MIME types.

Those are grouped under the "desktop" namespace from the snapcraft cloud part
functionality, with extensive help on how to use them:

$ snapcraft define desktop/qt5

Maintainer: 'Snapcraft community <snapcraft@lists.snapcraft.io>'

Description: |

Helpers for gtk2, gtk3, qt4 and qt5 or glib minimal launchers.

It brings the necessary code and exports for binding and using those

desktop technologies in a relocatable fashion, enabling binding with

global desktop theme, icon theme, image caching, fonts, mimetype handlers

application global menu and gsettings integration.

It also brings basics ubuntu dependency packages.

.

Usage:

1. add "after: [desktop/<technology>]" to your launcher:

- gtk2, gtk3, qt4 and qt5 corresponds to their respective toolkit  
main dependencies and default choices.

- glib-only enables to compile mime types and gsettings infos. If you  
added your own graphical drivers, it will link them as well.

2. prepend your command with "desktop-launch", like:

commands: "desktop-launch foo" if foo is in $PATH. You can as well

specify: "desktop-launch $SNAP/foo".

3. add needed plugs to your application:

- for graphical application:  
plugs: [x11 (or unity7 for appmenu integration)]. Think about adding

opengl if you need hw acceleration.

- if your application needs access to sound:  
plugs: [pulseaudio]

- accessing to user's home directory:  
plugs: [home]

- read/write to gsettings:  
plugs: [gsettings, home]

(note that the home plug is needed to read new value)'

desktop/qt5:

build-packages:

- qtbase5-dev  
- dpkg-dev  
make-parameters:

- FLAVOR=qt5  
plugin: make

source: https://github.com/ubuntu/snapcraft-desktop-helpers.git

source-subdir: qt

stage-packages:

- libxkbcommon0  
- ttf-ubuntu-font-family  
- dmz-cursor-theme  
- light-themes  
- shared-mime-info  
- libqt5gui5  
- libgdk-pixbuf2.0-0  
- libqt5svg5  
- appmenu-qt5

(Note that the descriptions are for now common to any namespaces launchers)

## Migrating from gtkconf/qt4conf/qt5conf

As part of this journey, I wanted to see this applied in the real world and
migrated all [snappy playpen examples](https://github.com/ubuntu/snappy-playpen) to this new launchers. I was delighted to see that some of the goals,
like having smaller snapcraft.yaml was a success. Also, broken examples are
now fully integrated to the desktop (see some of the pictures above).

Migrating is the existing **gtkconf/qt4conf/qt5conf** (we plan to deprecate
them after a while) is a 2 minutes job:

  1. Replace: _after: [<xxx>conf]_ with_ after: [desktop/<xxx>]_ where <xxx> is the targeted toolkit.
  2. Change _command: gtk-launch (or qt-launch) foo_ with _commands: desktop-launch foo_. For simplicity, all launchers are now called "desktop-launch". Note that foo needs to be in $PATH for your snap, if it's not, replace it to $SNAP/foo.
  3. You can (not mandatory) clean up any build-packages or stages-packages that are shipped and expose in the desktop launcher definition.

By following those simple steps, you can get from an unthemed, no matching
icons and no appmenu VLC to a fully integrated one!

![](http://i.imgur.com/TXwdNVX.png)

Happy snap desktop integration! :)

[Didier Roche](/en/blog/authors/didrocks/)

July 6, 2016

Filed under: [Snappy](/en/blog/tags/Snappy/) [planet-ubuntu](/en/blog/tags/planet-ubuntu/) [snap](/en/blog/tags/snap/)
[snapcraft](/en/blog/tags/snapcraft/)





## Comments

No comments yet.

## Add your comment

Name:

Email address:

URL:

Comment:

If you enter anything in this field your comment will be treated as spam:





