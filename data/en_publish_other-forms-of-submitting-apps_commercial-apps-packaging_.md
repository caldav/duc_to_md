





# Packaging commercial desktop applications

This guide will take you through the steps of packaging new software.

## Getting and checking the example app

The first stage in packaging is to check that the code of your app compiles
and runs. This guide will take you through packaging a simple application
called GNU Hello which has been posted on
[GNU.org](http://www.gnu.org/software/hello/). If you don’t have the build
tools lets make sure we have them first. Also if you don’t have the required
dependencies lets install those as well.

First if all, you'll need to install the build tools:

    $ sudo apt-get install build-essential

Then download the example hello app:

    $ wget -O hello-2.9.tar.gz "http://ftp.gnu.org/gnu/hello/hello-2.9.tar.gz"

You can now uncompress the contents of the archive you downloaded:

    $ tar xf hello-2.9.tar.gz
    $ cd hello-2.9

This application uses the autoconf build system so we want to run the
./configure script to prepare for compilation. This will check for the
required build dependencies. As hello is a simple example, build-essential
should provide everything we need. For more complex programs, the command will
fail if you do not have the needed libraries and development files. Install
the needed packages and repeat until the command runs successfully.:

    $ ./configure

Now you can compile the source:

    $ make

If compilation completes successfully you can install and run the program:

    $ sudo make install
    $ hello

## Creating the package from scratch

bzr-builddeb includes a plugin to create a new package from a template. The
plugin is a wrapper around the dh_make command. You should already have these
if you installed packaging-dev. Run the command providing the package name,
version number, and path to the upstream tarball:

    $ sudo apt-get install dh-make
    $ cd ..
    $ bzr dh-make hello 2.9 hello-2.9.tar.gz

When it asks what type of package type s for single binary. This will import
the code into a branch and add the debian/ packaging directory. Have a look at
the contents. Most of the files it adds are only needed for specialist
packages (such as Emacs modules) so you can start by removing the optional
example files:

    $ cd hello/debian
    $ rm *ex *EX

You should now customise each of the files. In debian/changelog change the
version number to an Ubuntu version: 2.9-0ubuntu1 (upstream version 2.9,
Debian version 0, Ubuntu version 1). Also change unstable to the current
development Ubuntu release such as saucy. Much of the package building work is
done by a series of scripts called debhelper. The exact behaviour of debhelper
changes with new major versions, the compat file instructs debhelper which
version to act as. You will generally want to set this to the most recent
version which is 9. control contains all the metadata of the package. The
first paragraph describes the source package. The second and following
paragraphs describe the binary packages to be built. We will need to add the
packages needed to compile the application to Build-Depends:. For hello, make
sure that it includes at least:

    Build-Depends: debhelper (>= 9)

You will also need to fill in a description of the program in the Description:
field. copyright needs to be filled in to follow the licence of the upstream
source. According to the hello/COPYING file this is GNU GPL 3 or later. docs
contains any upstream documentation files you think should be included in the
final package. README.source and README.Debian are only needed if your package
has any non-standard features, we don’t so you can delete them. source/format
can be left as is, this describes the version format of the source package and
should be 3.0 (quilt). rules is the most complex file. This is a Makefile
which compiles the code and turns it into a binary package. Fortunately most
of the work is automatically done these days by debhelper 7 so the universal %
Makefile target just runs the dh script which will run everything needed. All
of these file are explained in more detail in the _[overview of the debian
directory](http://packaging.ubuntu.com/html/debian-dir-overview.html)_
article. Finally commit the code to your packaging branch:

    $ bzr commit -m "Initial commit of Debian packaging."

## Building the package

Now we need to check that our packaging successfully compiles the package and
builds the .deb binary package:

    $ bzr builddeb -- -us -uc
    $ cd ../../

bzr builddeb is a command to build the package in its current location. The
-us -uc tell it there is no need to GPG sign the package. The result will be
placed in ... You can view the contents of the package with:

    $ lesspipe hello_2.9-0ubuntu1_amd64.deb

Install the package and check it works:

    $ sudo dpkg --install hello_2.9-0ubuntu1_amd64.deb

## Next steps

Even if it builds the .deb binary package, your packaging may have bugs. Many
errors can be automatically detected by our tool lintian which can be run on
both the source .dsc metadata file and the .deb binary package:

    $ lintian hello_2.9-0ubuntu1.dsc
    $ lintian hello_2.9-0ubuntu1_amd64.deb

A description of each of the problems it reports can be found on the [lintian
website](http://lintian.debian.org/tags.html). After making a fix to the
packaging you can rebuild using -nc “no clean” without having to build from
scratch:

    $ bzr builddeb -- -nc -us -uc

Having checked that the package builds locally you should ensure it builds on
a clean system using pbuilder. Since we are going to upload to a PPA (Personal
Package Archive) shortly, this upload will need to be _signed_ to allow
Launchpad to verify that the upload comes from you (you can tell the upload
will be signed because the -us and -uc flags are not passed to bzr builddeb
like they were before). For signing to work you need to have set up GPG. If
you haven’t set up pbuilder-dist or GPG yet, _[do so
now](http://packaging.ubuntu.com/html/getting-set-up.html)_:

    $ bzr builddeb -S
    $ cd ../build-area
    $ pbuilder-dist precise build hello_2.9-0ubuntu1.dsc

This will build the package and leave the built files in
~/pbuilder/precise_result/. You can install and test them with sudo dpkg -i
*.deb now.

## Publishing commercial apps

### Basic DOs and Dont's for Commercial Applications packging

#### DOs

  1. Please use /opt/<application_name>/ as your application root directory
  2. Please use /usr/share/applications/<application_name>.desktop for your application desktop file
  3. Please use /home/$USER/.cache/<application_name>/ for application data storage (eg game scores, level/game saves)
  4. Please use /home/$USER/.config/<application_name>/ for application configs (eg screen resolutions and other application data)
  5. Please use /home/$USER/<application_name>/ for saving data output from the user (eg. Saved files from a text editor)

#### DONTs

  1. Please do not let the application run under root, this is strictly not allowed and your application will be sent back to you. All applications must be able to run as a standard user.
  2. Please do not use Maintainer scripts unless absolutely essential. Please add a note as to why it is required in the feedback tab.
  3. Please do not try and save data to the /opt/<application_name/ it will fail on testing and be sent back to you.
  4. Please do not use an external source to install a script, your application will be rejected if you do.

## Packaging a PDF

If you have a book or magazine in PDF format, the pkgme package available from
the universe repository should do the bulk of the work for you.

## Contacting an external Contractor to package your application for you

There are external packaging contractors available to package your application
for you if you are not sure on what to do. You can contact [
](mailto:hyperair@ubuntu.com)[Loong Jin Chow](mailto:hyperair@ubuntu.com)
directly for packaging services.

**Note:**

This article refers to publishing third-party desktop applications packaged
with the traditional .deb format.

Ubuntu is migrating to the new .snap format to easily and securely distribute
apps.

If you are looking for information on how to publish an app for mobile or IoT
devices, [check out the current documentation instead
›](https://developer.ubuntu.com/en/publish)





