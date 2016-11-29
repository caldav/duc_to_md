





#  [Snapd 2.11/Snapcraft 2.13: downgrade installed snaps, release to users
from the command line](/en/blog/2016/08/04/snapd-211-snapcraft213/)

The latest version of snapd, the service powering snaps, has just landed in
Ubuntu 16.04, here are some of the highlights of this release.

## New commands: buy, find private, disable, revert

A lot of new commands are available, allowing you, for example, to downgrade,
disable and buy snaps:

  * When logged into a store, `snap find --private` lets you see snaps that have been shared with you privately.
  * The new `buy` command presents you a choice of payment backends for non-free snaps.  
[![](https://asciinema.org/a/e3sb63e8t0lidyqx0npncgerc.png)](https://asciinema
.org/a/e3sb63e8t0lidyqx0npncgerc)

  * `snap disable` allows you to disable specific snaps. A disabled snap won't be updated or launched anymore. It can be enabled with the `snap enable` command.
  * `snap revert` allows you to revert a snap to its previous installed version.  
[![](https://asciinema.org/a/akdrasv0juprlp21zca1ufhkm.png)](https://asciinema
.org/a/akdrasv0juprlp21zca1ufhkm)

  * The `refresh` command now works with snaps installed in `devmode`.

## Snap try and broken states handling

When using the `snap try` command to mount a folder containing a snap tree as
an installed snap, you can end up with a broken snap if you happen to delete
the folder without removing the snap first.

This "broken" state is now acknowledged as a potential snap state and handled
gracefully by the system. The `broken` tag now appears next to the snap in the
`snap list` output and you can remove it with `snap remove`.

## Interfaces changes

  * `getsockopt` has been allowed for connected `x11` plugs.
  * `/usr/bin/locale` access is now part of the default confinement policy.
  * A new `hardware-observe` interface that gives snaps read access to hardware information from the system. See [the implementation](https://github.com/snapcore/snapd/blob/master/interfaces/builtin/hardware_observe.go#L28) for details.

## Snapcraft 2.13

Snapcraft has also seen a new release (2.13) that brings:

  * Enhanced Ubuntu Store integration with the introduction of `snapcraft push` (which deprecates `upload`) and `snapcraft release`. These are very important pieces to the Continuous Integration aspect of snapcraft, you will have more to read on this front very soon!
  * A new `plainbox` plugin which allows parts containing a Plainbox test collection.
  * Many improvements on sanitizing cloud parts declarations.

### Java plugins

There has also been a strong focus on improving Java plugins with, for
example:

  * Improvements to the `ant` and `maven` plugins (support for targets).
  * Introduction of a `gradle` plugin

To learn how to use these plugins, the easiest way is to run `snapcraft help
ant`, `snapcraft help maven` and `snapcraft help gradle`.

Usage examples can be found in [the Playpen
repository](https://github.com/ubuntu/snappy-playpen/) and guidance in the
[snapcraft documentation](http://snapcraft.io/docs).

[David Callé](/en/blog/authors/davidc3/)

Aug. 4, 2016

Filed under: [planet-ubuntu](/en/blog/tags/planet-ubuntu/)
[snap](/en/blog/tags/snap/) [snapcraft](/en/blog/tags/snapcraft/)





## Comments

No comments yet.

## Add your comment

Name:

Email address:

URL:

Comment:

If you enter anything in this field your comment will be treated as spam:





