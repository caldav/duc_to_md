





#  [Using the ubuntu-app-platform content interface in appsnaps](/en/blog/2016/11/29/using-ubuntu-app-platform-content-interface-in-app-snaps/)

Recently the ubuntu-app-platform snap has been made available in the store for
application developers to build their snaps without bundling all their
dependencies. The ubuntu-app-platform snap includes standard Qt libraries
(version 5.6.1 as of this writing) and QML runtime, the ubuntu UI toolkit and
related dependencies, and oxide (a web engine based on the chromium content
API and its QML bindings).

This allows app developers to declare a dependency on this snap through the
content sharing mechanism, thus reducing dramatically the size of the
resulting app snaps.

I went through the exercise with the webbrowser-app snap. This proved
surprisingly easy and the size of the snap (amd64 architecture) went down from
136MB to 22MB, a sizeable saving!

For those interested in the details, here are the actual changes in the
snapcraft.yaml file: [https://bazaar.launchpad.net/~phablet-team/webbrowser-app/staging/revision/1576](https://bazaar.launchpad.net/~phablet-team/webbrowser-app/staging/revision/1576).

Essentially they consist in:

  * Using the ‘platform’ plug (content interface) and specifying its default provider (‘ubuntu-app-platform’)

  * Removing pretty much all stage packages

  * Adding an implicit dependency on the ’desktop-ubuntu-app-platform’ wiki part

  * Adding an empty ‘ubuntu-app-platform’ directory in the snap where snapd will bind-mount the content shared by the ubuntu-app-platform snap

Note that the resulting snap could be made even smaller. There is a known bug
in snapcraft where it uses ldd to crawl the dependencies, ignoring the fact
that those dependencies are already present in the ubuntu-app-platform snap.

Also note that if your app depends on any Qt module that isn’t bundled with
ubuntu-app-platform, you will need to add it to the stage packages of your
snap, and this is likely to bring in all the Qt dependencies, thus duplicating
them. The easy fix for this situation is to override snapcraft’s default
behaviour by specifying which files the part should install, using the “snap”
section (see what was done for e.g. address-book-app at
[https://code.launchpad.net/~renatofilho/address-book-app/ubuntu-app-platform/+merge/311351](https://code.launchpad.net/~renatofilho/address-book-app/ubuntu-app-platform/+merge/311351)).

[Olivier Tilloy](/en/blog/authors/osomon/)

Nov. 28, 2016

Filed under: No tags





## Comments

No comments yet.

## Add your comment

Name:

Email address:

URL:

Comment:

If you enter anything in this field your comment will be treated as spam:





