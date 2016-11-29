





#  [How to create Snap packages of Qt
applications](/en/blog/2016/11/16/snapping-qt-apps/)

## Introduction

One of the advantages of snap packages is that they are self-contained. When
you install a snap, you know that you don’t need to install additional
dependencies (besides the automatically-installed core snap that provides the
basic operating system layer), and it will simply work on every Linux
distribution that supports snaps.

Here, we show how to create self-contained snap packages for Qt-based
applications, and we show an additional approach where some of the app
dependencies are provided by a separate snap: the Ubuntu app platform snap.
The platform snap provides an (optional) approach for the software provider,
and can save disk space in some cases. Below we will explain the two
approaches to building a snap for Qt-based software: a snap that is self-
contained and includes Qt, and one that uses the platform snap, and we show
the advantages of each approach. However, before showing these two approaches
that you can apply to your own QML code, we demonstrate how to create a snap
from deb packages in the Ubuntu archive so that you can get started right away
even before you write any code.

We assume that before reading this blog post, you have acquired knowledge
about how to use Snapcraft. So if you haven’t, we recommend reading the
documentation on [snapcraft.io](http://snapcraft.io/docs/) and the [snap-
codelabs](https://developer.ubuntu.com/en/blog/2016/09/27/learning-to-snap-
with-codelabs/) tutorials.

All the commands that are listed below are executed on an Ubuntu 16.04 LTS
machine with the [stable-phone-overlay](https://launchpad.net/~ci-train-ppa-
service/+archive/ubuntu/stable-phone-overlay/) PPA enabled. Some of the
snapcraft commands may run on other configurations, but for the “Ubuntu App
Platform Snap” section it is a hard requirement because the version of Qt -
upstream 5.6 long term support version - and other libraries used to build the
snap need to match the versions in the _ubuntu-app-platform_ snap. Installing
the snap packages works on different versions of Ubuntu and even different
Linux distributions. The examples were tested on amd64 architecture with Intel
graphics. If you are running this on a different CPU architecture, naturally
the architecture in the directory and snap file names listed below must be
modified. If you have an Nvidia GPU and use the Nvidia proprietary drivers
there can be [problems](https://bugs.launchpad.net/snappy/+bug/1588192) when
running some snapped applications, so in that case we currently recommend to
use the open source Nouveau drivers.

The examples are also available in a repository linked to from the Evaluation
section.

## Qt cloud parts - a simple use case

We will demonstrate how to build a simple app snap that includes the Qt
release and Ubuntu UI Toolkit (UITK) from the Ubuntu archives. For this
example, we use the UITK gallery which is part of the _ubuntu-ui-toolkit-
examples_ deb package on classic Ubuntu systems, so no additional code is
needed. Because of that, we can simply use the _nil_ plugin and pull in the
examples as _stage-packages_. We create a directory called _uitk-gallery_
which contains only a _snapcraft.yaml_ file with the following contents:

    
    name: uitk-gallery
    version: '0.1'
    summary: Showcase gallery that demonstrates the components in the Ubuntu UI Toolkit.
    description: |
      See https://developer.ubuntu.com/api/qml/ for the API documentation of the components.
    
    grade: devel
    confinement: strict
    
    parts:
      ubuntu-ui-toolkit-examples:
        plugin: nil
        stage-packages:
          - qmlscene
          - qml-module-qtqml-models2
          - ubuntu-ui-toolkit-examples
        after: [desktop-qt5]
    
    apps:
      uitk-gallery:
        command: desktop-launch "qmlscene $SNAP/usr/lib/*/qt5/examples/ubuntu-ui-toolkit/examples/ubuntu-ui-toolkit-gallery/ubuntu-ui-toolkit-gallery.qml"
        plugs: [unity7, opengl]

(notes: the command line assumes you are on and targeting amd64 system. the
plugs line is needed so that you have access to graphical subsystem from your
confined app)

Under stage-packages we listed all the packages that need to be pulled from
the Ubuntu archive, including their dependencies. _ubuntu-ui-toolkit-examples_
contains all the QML code for the UITK gallery that we want to run using
_qmlscene_. We also included _qml-module-qtqml-models2_ because some pages of
the UITK gallery _import QtQml.Models_. The line _after: [desktop-qt5]_
fetches the _desktop-qt5_ part from the [remote parts
repository](https://wiki.ubuntu.com/snapcraft/parts). It will automatically
pull in Qt 5 from the Ubuntu archive, set-up environment variables, and
provide the _desktop-launch_ script that is called to start the app. The snap
file can be created simply by going to the _uitk-gallery_ directory which
contains the _snapcraft.yaml_ file, and running:

    
    snapcraft

Note that Snapcraft will ask for the sudo password to install the Qt5 dev
packages that are required to compile Qt apps, but can be left out if all the
dependencies are already present. Running snapcraft will create (on an amd64
machine) the file _uitk-gallery_0.1_amd64.snap_ which can then be installed
by:

    
    snap install --dangerous uitk-gallery_0.1_amd64.snap

where the _dangerous_ parameter is required because we are installing an
unsigned snap that does not come from the Ubuntu store. Note that you do not
need to use _sudo_ if you have logged in with _snap login_. The UITK gallery
can now be launched using:

    
    uitk-gallery

The _desktop-qt5_ cloud part pulls in the current stable version of Qt of the
Ubuntu 16.04 LTS release - 5.5.1 normally or 5.6.1 in the case of stable
overlay PPA. To uninstall the UITK gallery snap before going to the next
section, run:

    
    snap remove uitk-gallery

## QML project using parts from the cloud

If your existing QML code is not available as a deb package, then obviously
you cannot pull it in from the archive when creating the snap using _stage-
packages_. To show how to include your own QML code, we copy the UITK gallery
code to the _ubuntu-ui-toolkit-gallery_ directory inside the snapcraft (_uitk-
gallery_) directory. Go to the parent directory of the _uitk-gallery_ of the
previous section, and run:

    
    bzr branch lp:ubuntu-ui-toolkit
    cp -R ubuntu-ui-toolkit/examples/ubuntu-ui-toolkit-gallery uitk-gallery/

Alternatively, if you have the _ubuntu-ui-toolkit-examples_ package installed,
you can run:

    
    cp -R /usr/lib/*/qt5/examples/ubuntu-ui-toolkit/examples/ubuntu-ui-toolkit-gallery/ uitk-gallery/

You should now have both the _snapcraft.yaml_ and the copied _ubuntu-ui-
toolkit-gallery_ directory that contains the source code of the UITK gallery
under the _uitk-gallery_. We can now remove the _ubuntu-ui-toolkit-examples_
from the _stage-packages_ in the _snapcraft.yaml_ file. Because that line is
removed, the dependencies of the UITK gallery are no longer pulled in
automatically, and we must add them to the YAML file, which then becomes:

    
    name: uitk-gallery
    version: '0.2'
    summary: Showcase gallery that demonstrates the components in the Ubuntu UI Toolkit.
    description: |
      See https://developer.ubuntu.com/api/qml/ for the API documentation of the components.
    
    grade: devel
    confinement: strict
    
    parts:
      ubuntu-ui-toolkit-gallery:
        plugin: dump
        source: .
        stage-packages:
          - qmlscene
          - qml-module-qtqml-models2
          - qml-module-qt-labs-folderlistmodel
          - qml-module-qtquick-xmllistmodel
          - qml-module-ubuntu-components
          - ubuntu-ui-toolkit-theme
          - ubuntu-ui-toolkit-tools
        after: [desktop-qt5]
    
    apps:
      uitk-gallery:
        command: desktop-launch "qmlscene $SNAP/ubuntu-ui-toolkit-gallery/ubuntu-ui-toolkit-gallery.qml"
        plugs: [unity7, opengl]

Note that besides the changes in _stage-packages_, also the location of
_ubuntu-ui-toolkit-gallery.qml_ was updated in the _uitk-gallery_ command
because the QML files are no longer installed in usr/lib inside the snap, but
copied in the root of the snap filesystem. As before, the snap package can be
created by executing:

    
    snapcraft

inside the _uitk-gallery_ directory. The UITK gallery can then be installed
and started using:

    
    snap install --dangerous uitk-gallery_0.2_amd64.snap
    uitk-gallery

and uninstalled by:

    
    snap remove uitk-gallery

Now that you have seen how to package the UITK gallery from source into a
snap, you can do the same for your own QML application by using the _dump_
plugin with the dependencies as _stage-packages_. If your application includes
C++ code as well, you need to use another plugin, for example the _qmake_
plugin. For that we refer to the Snapcraft tutorials mentioned in the
introduction.

For those who like to experiment with newer versions of upstream Qt, we
provide _qt57_ and _qt58_ cloud parts in the parts repository for Qt 5.7.1 and
5.8 (in development). However, the _qt57_ and _qt58_ cloud parts do not yet
include a wrapper script similar to _desktop-launch_, so one must be included
with with snap configuration, see for example
[timostestapp2](https://github.com/tjyrinki/timostestapp2). When using these
cloud parts, you should usually omit any Qt/QML package from stage-packages,
as the ones compiled from newer Qt are used directly, and you should also omit
the _after: [desktop-qt5]_.

## Ubuntu app platform snap

The snap files we created in the previous sections contain everything that is
needed in order to run the UITK gallery application, resulting in a snap file
of 86MB. Here we will explain how to use the Ubuntu app platform snap when you
have multiple app snaps that all use the same Qt version.

Benefits of this approach include disk space saving, download time and
bandwidth usage if metered.

When your snap uses the _ubuntu-app-platform_ snap for Qt and other platform
libraries, we can remove the _stage-packages_ from the _snapcraft.yaml_ file
because (in this case), all the needed libraries are included in _ubuntu-app-
platform_. We must also replace _after: [desktop-qt5]_ by _after: [desktop-
ubuntu-app-platform]_. This will set-up your snap to use the global desktop
theme, icon theme, gsettings integration, etc. A more elaborate description of
the _desktop-ubuntu-app-platform_ is given in the [parts
list](https://wiki.ubuntu.com/snapcraft/parts) on the Ubuntu wiki. In the
_uitk-gallery_ directory we must currently create a directory where the files
from the platform snap can be mounted using the content interface:

    
    mkdir ubuntu-app-platform

and this empty directory (mount point) must be added in the YAML file as well.
At this point the directory structure is as follows:

    
    uitk-gallery/
     .. snapcraft.yaml
     .. ubuntu-ui-toolkit-gallery/
        .. [gallery contents]
     .. ubuntu-app-platform/

The whole YAML is:

    
    name: uitk-gallery
    version: '0.3'
    summary: Showcase gallery that demonstrates the components in the Ubuntu UI Toolkit.
    description: |
      See https://developer.ubuntu.com/api/qml/ for the API documentation of the components. ubuntu-app-platform snap must be installed for this snap to work.
    
    grade: devel
    confinement: strict
    
    plugs:
        platform: # plug name, to be used later
            interface: content
            content: ubuntu-app-platform1 # content being mounted and the version, currently 1
            target: ubuntu-app-platform # the mount directory created
            default-provider: ubuntu-app-platform # default content source snap, currently the only provider too
    
    parts:
      ubuntu-ui-toolkit-gallery:
        plugin: dump
        source: .
        after: [desktop-ubuntu-app-platform]
        snap: [ubuntu-ui-toolkit-gallery, ubuntu-app-platform]
    
    apps:
      uitk-gallery:
        command: desktop-launch "qmlscene $SNAP/ubuntu-ui-toolkit-gallery/ubuntu-ui-toolkit-gallery.qml"
        plugs: [platform, unity7, opengl]

Again, the new snap file can be created using:

    
    snapcraft

This time, before we can use the snap, the _ubuntu-app-platform_ snap must be
installed and connected to the new _uitk-gallery_ snap. So, execute the
following commands:

    
    snap install ubuntu-app-platform
    snap install --dangerous uitk-gallery_0.3_amd64.snap
    snap connect uitk-gallery:platform ubuntu-app-platform:platform
    uitk-gallery

Note that the snaps must be connected before running _uitk-gallery_ for the
first time. If _uitk-gallery_ has been executed before the _snap connect_ you
will see an error message. To fix the problem, uninstall the _uitk-gallery_
snap, then re-install it and run the _snap connect _command before executing
_uitk-gallery_. This is a known limitation in snapd which will be resolved
soon.

Another note: once support for the _default-provider_, already defined above,
will correctly be implemented in snap, there will no longer be a need to
install the platform snap separately - it will be pulled from the store
automatically and the interface connects automatically.

## Evaluation

We demonstrated three different approaches to creating a UITK gallery snap,
which we gave the version numbers 0.1, 0.2 and 0.3. For each of the
approaches, the table below lists the time needed for the different stages of
a snapcraft run, but the pull and build stages have been combined because when
doing pull, some of the prerequisites need to be built already. The _all
stages_ row shows the total time when running the _snapcraft_ command in a
clean directory, so that all stages are executed sequentially, so the value is
less than the sum of the previous rows in the table because in each stage it
is not necessary to check completion of the previous stages.

**Version (bzr revision)**

**0.1 (r1)**

**0.2 (r2)**

**0.3 (r3)**

build (includes pull)

1m49s

1m48s

3.6s

stage

7s

7s

1.5s

prime

33s

34s

1.8s

snap

1m11s

1m13s

1.7s

all stages

3m32s

3m20s

4.0s

install

2.2s

2.4s

1.2s

snap file size

86 MB

86 MB

1.3 MB

The measurements were done on a laptop with an Intel Core i5-6200U CPU with 8
GB RAM and an solid-state drive by running each command three times and
listing the average execution time. All build-dependencies were pre-installed
so their installation time is not included in the measurements. Note that this
table only serves as an illustration, and execution times will vary greatly
depending on your system configuration and internet connection, but it can
easily be tested on your own hardware by _bzr_ branching revisions r1, r2 and
r3 of _[lp:~tpeeters/+junk/blog-snapping-qt-
apps](https://code.launchpad.net/~tpeeters/+junk/blog-snapping-qt-apps)_.

The times and file size listed in the last column (version 0.3) do not include
downloading and installing the ubuntu-app-platform snap, which is 135 MB (it
includes more than just the minimal Qt and UITK dependencies of the UITK
gallery). It can be seen that (depending on the internet connection speed, and
which files were downloaded already), using the ubuntu-app-platform can speed
up the pull and build time when creating a new snap file. However, the most
important advantage is the reduction of the sum of the file sizes when
installing multiple app snaps that all depend on Qt or other libraries that
are part of the platform snap, because the libraries need to be installed only
once. The disadvantage of this approach is that the app snap must be built
using the exact same Qt (and other libraries) version as the ubuntu-app-
platform snap, so the choice whether the snap should be fully self-contained
or depend on the platform snap must be made individually for each use case.

## Future work

The UITK gallery snap is not yet available in the Ubuntu store, so our next
step will be to publish a UITK examples snap that includes the UITK gallery,
and to set-up automatic publishing of that snap to different channels when we
update the UITK or the examples. We will also evaluate what is the best way to
make newer versions of Qt available and determine whether we need to provide
prebuilt binaries to replace the _qt57_ and _qt58_ cloud parts.

Finally, we will determine which libraries need to be included in the _ubuntu-
app-platform_ snap. The plan is to include all APIs that are listed on
[https://developer.ubuntu.com/api/qml/](https://developer.ubuntu.com/api/qml/)
and if APIs are missing we will add them to that webpage as well as to the
platform snap. Of course, if you think we are forgetting a library that is
useful and used in many different applications, please leave a comment below.

[Tim Peeters](/en/blog/authors/tpeeters/), [Timo
Jyrinki](/en/blog/authors/timo-jyrinki/)

Nov. 16, 2016

Filed under: [planet-ubuntu](/en/blog/tags/planet-ubuntu/)
[sdk](/en/blog/tags/sdk/) [snap](/en/blog/tags/snap/)
[snapcraft](/en/blog/tags/snapcraft/) [ubuntu-sdk](/en/blog/tags/ubuntu-sdk/)





## Comments

No comments yet.

## Add your comment

Name:

Email address:

URL:

Comment:

If you enter anything in this field your comment will be treated as spam:





