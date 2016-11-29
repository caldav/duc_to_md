





#  [Snapcraft 2.12: an ecosystem of parts, qmake and
gulp](/en/blog/2016/06/29/snapcraft-212/)

Snapcraft 2.12 is here and is making its way to your 16.04 machines today.

This release takes Snapcraft to a whole new level. For example, instead of
defining your own project parts, you can now use and share them from a common,
open, repository. This feature was already available in previous versions, but
is now much more visible, making this repo searchable and locally cached.

Without further ado, here is a tour of what’s new in this release.

## Commands

2.12 introduces ‘`snapcraft update`’, ‘`search`’ and ‘`define`’, which bring
more visibility to the Snapcraft parts ecosystem. Parts are pieces of code for
your app, that can also help you bundle libraries, set up environment
variables and other tedious tasks app developers are familiar with.

They are literally parts you aggregate and assemble to create a functional
app. The benefits of using a common tool is that these parts can be shared
amongst developers. Here is how you can access this repository.

  * `snapcraft update : `refresh the list of remote parts
  * `snapcraft search : `list and search remote parts
  * `snapcraft define : `display information and content about a remote part

[![5273725bbff337eaf4eb07a81af97cd82051866b.png](https://lh4.googleusercontent
.com/YSyjeVig3XQBIOhmz3JmkTo48t155naOHHbb8EpDSKMyRRkVgyEcxumrwMB4oQxWQrw6UJY2g
UnhPAr5weFzV2vRQ7KYKpOjFNjzr8v20DjNXVrIk4ivRej5pyWu4-qEU8ruo9xj)](https://asci
inema.org/a/6xtbfnd4xb3rpw4rqkkrexozl?autoplay=1)

To get a sense of how these commands are used, have a look at the above
example, then you can dive into [details and what we mean by “ecosystem of
parts”](http://blog.sergiusens.org/posts/The-Snapcraft-Parts-Ecosystem/).

### Snap name registration

Another command you will find useful is the new ‘`register`’ one. Registering
a snap name is reserving the name on the store.

  * `snapcraft register`

[![6875784c98c671707e1de1b27bb0cdba4690d68e.png](https://lh6.googleusercontent
.com/HTM6WM-s5R_GeekeA_VgGUqdbf-2bW2U4R8UzxFc0ny03pzgqzC8dy-EeDyc9i7dioyWbc-JB
zq5PHfBjFdM3kCXdyRIs90EyVDTfz1spO5zjzOmwRswJnTDn-f8WfzeoJHwFBuZ)](https://asci
inema.org/a/6l28s5mwhtqkvwhsr2mdjcyyx?autoplay=1)

As a vendor or upstream, you can secure snap names when you are the publisher
of what most users expect to see under this name.

Of course, this process can be reverted and disputed. Here is what the store
workflow looks like when I try to register an already registered name:

![snap-name-register.png](https://lh6.googleusercontent.com/CUC7IHx3mtUMavzuEE
5nQgg6VAJtjdFZxjfnSlL_P7AUzzLhH7Fs_osKmyNOe1Ie1dc6XpA2TG0BINZkbtYHqXW2ZNgP4nWy
soVmdY_XKkZaDllrx8zNoBcT9Sa0EOT7UgViD9AM)

_On the name registration page of the
[store](https://myapps.developer.ubuntu.com), I’m going to try to register
‘my-cool-app’, which already exists._

![snap-name-register-
failed.png](https://lh6.googleusercontent.com/OtX6LcrmwuS6_mCpqdTYZJJvU-
vZaG6JzbjhL1DlmjVKxyz3kIZB4NiKHKMd-
nygDD7h9TU8xOdPTmca1-QmxMTRilSGxfhhF_f55uZYvihZqj-ZbWZA_bgDrU7iMVUh-w4IegxG)

_I’m informed that the name has already been registered, but I can dispute
this or use another name._

![snap-name-register-dispute.png](https://lh3.googleusercontent.com/y13zjOAJtQ
zpBXy6q1JpvKNblMXxSw1bXluvmQkZpRCsn2wHRMODX850vHqe3MU-
fWHq9h6rF-8twCb74-sW0v1wRBM7aXHsD7z6aOxsx8WsbnvyowL0xdeKuc4QOd_F-hIhaxH9)

_I can now start a dispute process to retrieve ownership of the snap name._

## Plugins and sources

Two new plugins have been added for parts building: **qmake** and **gulp**.

### qmake

The qmake plugin has been requested since the advent of the project, and we
have seen many custom versions to fill this gap. Here is what the [default
qmake plugin](https://github.com/snapcore/snapcraft/blob/master/snapcraft/plug
ins/qmake.py) allows you to do:

  * Pass a list of options to qmake
  * Specify a Qt version
  * Declare list of .pro files to pass to the qmake invocation

### gulp

The hugely popular nodejs builder is now [a first class citizen](https://githu
b.com/snapcore/snapcraft/blob/master/snapcraft/plugins/gulp.py) in Snapcraft.
It inherits from the existing nodejs plugin and allows you to:

  * Declare a list of gulp tasks
  * Request a specific nodejs version

### Subversion

SVN is still a major version control system and thanks to Simon Quigley from
the Lubuntu project, you can now use `svn:` URIs in the source field of your
plugins.

## Highlights

Many other fixes made their way into the release, with two highlights:

  * You can now use hidden .snapcraft.yaml files
  * ‘`snapcraft cleanbuild`’ now creates ephemeral LXC containers and won’t clutter your drive anymore

The full changelog for this milestone is available
[here](https://launchpad.net/snapcraft/%2Bmilestone/2.12) and the list of bugs
in sight for 2.13 can be found
[here](https://launchpad.net/snapcraft/%2Bmilestone/2.13). Note that this list
will probably change until the next release, but if you have a Snapcraft itch
to scratch, it’s a good list to pick your first contribution from.

## Install Snapcraft

### On Ubuntu

Simply open up a terminal with Ctrl+Alt+t and run these commands to install
Snapcraft from the Ubuntu archives on Ubuntu 16.04 LTS

    
    sudo apt update
    sudo apt install snapcraft

### On other platforms

[Get the Snapcraft source code › ](https://github.com/ubuntu-
core/snapcraft/releases/tag/2.12)

## Get snapping!

There is a thriving community of developers who can give you a hand getting
started or unblock you when creating your snap. You can participate and get
help in multiple ways:

  * Mailing list: a great place to collaborate and discuss features, bugs and ideas on   
snapcraft is the [Snapcraft mailing
list](https://lists.ubuntu.com/mailman/listinfo/snapcraft)

  * Talk live to other snaps developers on the [#snappy IRC channel on Freenode](https://webchat.freenode.net/?channels%3Dsnappy)
  * If something is not working for you or you’ve spotted a missing feature, feel free to [file a bug report](https://bugs.launchpad.net/snapcraft/%2Bfilebug)
  * Ask a question or check out the growing Snapcraft FAQs at [Ask Ubuntu](http://askubuntu.com/questions/tagged/snapcraft)

[David Callé](/en/blog/authors/davidc3/)

June 29, 2016

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





