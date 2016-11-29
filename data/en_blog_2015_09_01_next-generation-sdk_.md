





#  [The Next Generation SDK](/en/blog/2015/09/01/next-generation-sdk/)

Up until now the basic architecture of the SDK IDE and tools packaging was
that we have packaged and distributed the QtCreator IDE and our Ubuntu plugins
as separate distro packages which strongly depend on the Qt available in the
same release.

Since 14.04 we have been jumping through hoops to provide the very same
developer experience from a single development branch of the SDK projects.
Just to give a quick picture on what we have available in the last few
releases (note that 1.3 UITK is not yet released):

14.04 Trusty

Qt 5.2.1

QtCreator 3.0.1

UI Toolkit 0.1

14.10 Utopic

Qt 5.3.

QtCreator 3.1.1

UI Toolkit 1.1

15.04 Vivid

Qt 5.4.1

QtCreator 3.1.1

UI Toolkit 1.2

15.10 Wily

Qt 5.4.2

QtCreator 3.5.0

UI Toolkit 1.3

Life could have been easier by sticking to one stable Qt and QtCreator and
base our SDK on it. Obviously it was not a realistic option as the phone
development needed the most recent Qt and our friend Kubuntu required a hot
new engine under its hood too. So Qt was quickly moving forward and the SDK
followed it. Of course it was all beneficial as new Qt releases brought us
bugfixes, new features and improved performance.

But on the way we came to realize that continuously backporting the UITK and
the QtCreator plugins to older releases and the LTS was simply not going to be
possible. It went fine for some time, but the more API breaks the new Qt and
QtCreator releases brought the more problems we had to face. Some people have
asked why we don’t backport the latest Qt releases to the LTS or to the stable
Ubuntu. As an idea it may sound good, but changing the Qt to 5.4.2 under an
application in LTS what was built against 5.2.1 Qt would certainly break that
application. So it is simply not cool to mess around with such fundamental
bits of a stable and long term supported release.

The only option we had was to decouple the SDK from the archive release of Qt
and build it as a standalone package without any external Qt dependencies.
That way we could provide the exact same experience and tools to all
developers regardless if they are playing safe on Trusty/LTS or enjoy the
cutting edge on the daily developed release of Wily.

The idea manifested in a really funny project. The source tree of the project
is pretty empty. Only cmake and the debian/rules take care of the job. The
builder pulls the latest stable Qt, QtCreator and UITK. Builds and integrates
the libdbusmenu-qt and appmenu-qt5 projects and deploys the SDK IDE. The
package itself is super skinny. Opposing the old model where QtCreator has
pulled most of the Qt modules as dependencies this package contains all it
needs and the size of it is impressing 36MB. Cheap. Just the way I like it.
Plus this package already contains the 1.3 UITK as our QtCreator plugin
(Devices Tab) is using it. So in fact we are just one step from enabling
desktop application development on 14.04 LTS with the same UI Toolkit as we
use on the commercial phone devices. And that is a super hot idea.

The Ubuntu SDK IDE project lives here: [_https://launchpad.net/ubuntu-sdk-
ide_](https://launchpad.net/ubuntu-sdk-ide)

If you want to check out how it is done:

`$ bzr branch lp:ubuntu-sdk-ide `

Since we considered such a big facelift on the SDK I thought why not to make
the change much bigger. Some might remember that there was a discussion on the
[Ubuntu Phone mailing list](http://lists.launchpad.net/ubuntu-
phone/msg11212.html) about the possibility to improve the Kit creation in the
IDE. Since then we have been playing with the idea and I think it is now a
good time to unleash the static chroots.

The basic idea is that creating the builder chroots runtime is a super slow
and fragile process. The bootstrapping of the click chroot already takes a
long time and installing the SDK API packages (all the libs and dev packages
with headers) into the chroot is also time consuming. So why not to create
these root filesystems in advance and provide them as single installable
packages.

This is exactly what we have done. The base of the API packages is the Vivid
core image. It is small and contains only the absolutely necessary packages,
we install the SDK libs, dev packages and development tools on the core image
and configure the Overlay PPA too. So the final image is pretty much
equivalent with the image on a freshly updated device out there. It means that
the developer can build and test against the same API set as it is available
on the devices.

These API packages are still huge. Their size is around 500MB, so on a slow
connection it still takes ages to download, but still it is way faster than
bootstrapping a 1.6GB chroot package by package.

This API packages contain a single tar.gz file and the post install script of
the package puts the content of this tar.gz to the right place and wires it
in, in the way it should be. Once the package is installed the new Kit will be
automatically recognized by the IDE.

One important note on this API package! If you have an armhf 15.04 Kit (click
chroot) already on your system when you install this package, then your
original Kit will not be removed but simply renamed to
backup-[timestamp]-[original name]. So do not worry if you have customized
Kits, they are safe.

The Ubuntu SDK API project is only a packaging project with a simple script to
take care of the dirty details. The project is hosted here:
[_https://launchpad.net/ubuntu-sdk-api-15.04_](https://launchpad.net/ubuntu-
sdk-api-15.04)

And if you want to see what is in it just do

`$ bzr branch lp:ubuntu-sdk-api-15.04 `

The release candidate packages are available from the Tools Development PPA of
the SDK team: [_https://launchpad.net/~ubuntu-sdk-team/+archive/ubuntu/tools-
development_](https://launchpad.net/~ubuntu-sdk-team/+archive/ubuntu/tools-
development)

How to test these packages?

`$ sudo add-apt-repository ppa:ubuntu-sdk-team/tools-development -y `

`$ sudo apt-get update`

`$ sudo apt-get install ubuntu-sdk-ide ubuntu-sdk-api-tools`

`$ sudo apt-get install ubuntu-sdk-api-15.04-armhf ubuntu-sdk-api-15.04-i386`

After that look for the Ubuntu SDK IDE in the dash.

[Zoltán Balogh](/en/blog/authors/bzoltan/)

Sept. 1, 2015

Filed under: [planet-ubuntu](/en/blog/tags/planet-ubuntu/)
[sdk](/en/blog/tags/sdk/)





## Comments

  1. ![M. Ángel](http://www.gravatar.com/avatar/1ef9b1727d0c3a32dd33a4532ee45c76?s=60&r=G) M. Ángel 09/21/2015 2:43 p.m.

Hi, Zoltán. Can I install Ubuntu phone beta ("daily build") in aquaris E4.5?
Thank you for this post, it's very good.

## Add your comment

Name:

Email address:

URL:

Comment:

If you enter anything in this field your comment will be treated as spam:





