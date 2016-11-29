





#  [Snapd 2.0.8: universal snaps and desktop
interfaces](/en/blog/2016/06/15/snapd-208-universal-snaps-and-desktop-
interfaces/)

Yesterday, the snapcore team released a new version of snapd for Ubuntu 16.04.
Snapd is the system service that enables developers and users to interact with
snaps.

![](https://assets.ubuntu.com/v1/bb7f0c54-snaps-hero%403x.png)

## Features in 2.0.8

  * `snap try`. This command mounts any folder containing an unpackaged snap as an editable installed snap, making testing and iterating on snaps much faster. For example, if you are using snapcraft, you can run `snap try prime/` in your working dir to mount `prime/` as a installed snap and edit it while the snap is mounted.
  * Use `os-release` instead of `lsb-release` for cross-distro use
  * Add support for an environment map inside snap.yaml, although the matching snapcraft syntax has not landed yet.

## Interfaces

New interfaces have been added with this release, giving more control to the
way your snaps interact and exchange with the underlying OS (gsettings,
pulseaudio, etc.). Their names are self explanatory, but for more details, you
can have a look at [the implementation](https://github.com/snapcore/snapd/tree
/master/interfaces/builtin). Note that some of these interfaces are “reserved”
and will trigger a manual review in the store. Here is a summary of all
changes:

  * Changes in the ‘`unity7`’ interface:
  * add DBUSMenu, Freedesktop and KDE notifications
  * allow AppMenu and launcher API
  * add fcitx and mozc input methods
  * add com.canonical.UrlLauncher.XdgOpen
  * Introducing the following interfaces:
  * ‘`network-manager`’: allows operating as the NetworkManager service
  * ‘`cups-control`’: allows access to cups control socket
  * ‘`location-control`’ and ‘`location-observe`’: allow operating as the location service
  * ‘`pulseaudio`’: allows access to audio (`/etc/pulse` and related paths)
  * ‘`gsettings`’: allows access to global gsettings of the user's session
  * Autoconnect the ‘`home`’ interface
  * ‘`firewall-control`’ can access the xtables lock file
  * Add `socketcall()` to the ‘`network`’ and ’`network-bind`’ interfaces
  * Allow using `sysctl` and `scmp_sys_resolver` for parsing kernel logs
  * Allow access to new ibus abstract socket path
  * Documentation updates

## Command line

  * Implement ``snap refresh --list`` and ``snap refresh`` to view and manually apply available updates
  * Have '`snap list`' display an helper message when no snaps are installed

The full changelog for this release [is
here](https://github.com/snapcore/snapd/blob/2.0.8/debian/changelog). Note
that the previous snapd update in 16.04 was 2.0.5, so this changelog extends
from 2.0.6 to 2.0.8.

## What’s next?

Here are some highlights from the list of features and fixes lined up for the
next snapd release in 16.04:

  * Add new ``snap run`` command with hook support
  * Create `SNAP_USER_DATA` and common dirs in ``snap run``
  * Have the installation of the core snap request a restart (on classic)
  * Install snaps in `devmode` on distributions without complete apparmor and seccomp support
  * Interfaces: miscellaneous policy updates for chromium, x86, opengl, etc.
  * Enable full confinement on Elementary 0.4 (Loki)

[David Callé](/en/blog/authors/davidc3/)

June 15, 2016

Filed under: [planet-ubuntu](/en/blog/tags/planet-ubuntu/)
[snap](/en/blog/tags/snap/)





## Comments

No comments yet.

## Add your comment

Name:

Email address:

URL:

Comment:

If you enter anything in this field your comment will be treated as spam:





