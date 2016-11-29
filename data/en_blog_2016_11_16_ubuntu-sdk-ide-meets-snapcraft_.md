





#  [Ubuntu SDK meets snapcraft](/en/blog/2016/11/16/ubuntu-sdk-ide-meets-
snapcraft/)

Everyone who has followed Ubuntu lately for sure stumbled across the snappy
technology, which does not only bring the new cross-distro packaging format
“snap” but also a sandboxing technology for apps, as well as transactional
updates that can be rolled back in case of an update going wrong and a new way
of installing and upgrading Ubuntu called “Ubuntu Core”.

Together with all those new technologies came new tools that make it possible
for app developers to build and pack their applications to target Snappy and
Core. The central tool for that is snapcraft and it aims to unite a lot of
tasks that were separate before. It can set up your build environment, build
your projects and even package it with just one call in the project directory:
“snapcraft”.

We took the last few weeks to start the work on supporting those new tools and
now we have the first release of the IDE with direct support for building with
snapcraft, as well as a basic template to get you started.

New technologies usually come with certain limitations. This one is not an
exception and we hope that these issues will be eliminated in the near
future.:

  * Snapcraft uses sudo when it needs to install build packages, however that does not work when run from the QtCreator, simply because sudo does not have a console to ask the password on. So make sure build dependencies are installed before building.

  * “Out of source” builds are not yet implemented in snapcraft, but since QtCreator always uses a extra build directory we had to work around that problem. So for now we rsync the full project into a build directory and run the build there.

  * Also incremental builds are yet not supported, so every build is a complete rebuild.

Snapcraft projects are described in a snapcraft.yaml file, so it made sense
for us to use it as the project file in the IDE as well, so instead of opening
a .pro or CMakeList.txt file the snapcraft.yaml is opened directly. Naturally
implementing a completely new project type manager is not a trivial task, so
many key features are still missing.

  * Code model support: while completion does work in the file scope, it does not for the full project.

  * Debugging mode: currently the profiling and debugging run modes do not work, so snap projects can only be executed normally.

Those limitations aside it can be already used to create snap packaged
applications.

With this new release we consider the IDE as feature complete for the time
being. Since the development of snapcraft is moving in a very fast pace we
need to let it evolve to a certain degree to be sure new features added to the
IDE represent the future way of building with snapcraft.

[Benjamin Zeller](/en/blog/authors/zeller-benjamin/)

Nov. 16, 2016

Filed under: [planet-ubuntu](/en/blog/tags/planet-ubuntu/)
[qtcreator](/en/blog/tags/qtcreator/) [snap](/en/blog/tags/snap/)
[snapcraft](/en/blog/tags/snapcraft/) [snaps](/en/blog/tags/snaps/) [ubuntu-
sdk](/en/blog/tags/ubuntu-sdk/) [ubuntu-sdk-ide](/en/blog/tags/ubuntu-sdk-
ide/)





## Comments

No comments yet.

## Add your comment

Name:

Email address:

URL:

Comment:

If you enter anything in this field your comment will be treated as spam:





