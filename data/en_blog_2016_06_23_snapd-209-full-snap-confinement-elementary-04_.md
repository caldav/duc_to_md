





#  [Snapd 2.0.9: full snap confinement on Elementary0.4](/en/blog/2016/06/23/snapd-209-full-snap-confinement-elementary-04/)

As of today and part of our weekly release cadence, a new snapd is making its
way to your 16.04 systems. Here is what’s new!

### Command line

  * `snap interfaces` can now give you a list of all snaps connected to a specific interface:  
[![1a42fb817c663169453b0c7c5e24302d24ecb376.png](https://asciinema.org/a/1kavfus9fe32z9v5q8p06wkie.png)](https://asciinema.org/a/1kavfus9fe32z9v5q8p06wkie?a
utoplay=1)

  * Introduction of `snap run <app.command>`, which will provide a clean and simple way to run commands and hooks for any installed revision of a snap. As of writing this post, to try it, you need to wait for a newer core snap to be promoted to the stable channel, or alternatively, switch to the _beta_ channel with `snap refresh --channel=beta ubuntu-core`

### Ecosystem

  * Enable full confinement on [Elementary 0.4 (Loki)](http://blog.elementary.io/post/145881464631/loki-beta)
  * If a distribution doesn’t support full confinement through `Apparmor` and `seccomp`, snaps are installed in [devmode](http://askubuntu.com/questions/783945/what-is-devmode-for-snaps) by default.

### Misc

  * Installing the core snap will now request a restart
  * Rest API: added support to send apps per snap, to allow finer-grained control of snaps from the Software center.

Have a look at the full [changelog](https://launchpad.net/ubuntu/%2Bsource/snapd/2.0.9&sa=D&ust=1466692417623000&usg=AFQjCNEq-XhwBht99hF8OS0m6PGIFVdVIA) for
more details.

## What’s next?

Here are some of the fixes already lined up for the next snapd release:

  * New interfaces to enable more system access for confined snaps, such as “`camera`”, “`optical-drive`” and “`mpris`”. This will give a lot more latitude for media players (control through the mpris dbus interface, playing DVDs, etc.) and communication apps. You can try them now by building snapd [from source](https://github.com/snapcore/snapd).
  * Better handling of snaps on nvidia graphics
  * And much more to come, watch the new Snapcraft social channels ( [twitter](https://twitter.com/snapcraftio), [google+](https://plus.google.com/+SnapcraftIo), [facebook](https://www.facebook.com/snapcraftio)) for updates!

[David Callé](/en/blog/authors/davidc3/)

June 23, 2016

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





