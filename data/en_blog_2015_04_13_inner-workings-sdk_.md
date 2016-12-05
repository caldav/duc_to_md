





#  [Inner workings of the SDK](/en/blog/2015/04/13/inner-workings-sdk/)

![Inner workings of the SDK](/static/devportal_uploaded/fe934c07-8efa-41c2-b68e-ea5069aacee5-uploads/zinnia/Bildschirmfoto_vom_2015-04-13_112105.png)

From time to time app developers ask how to manually build click packages from
their QMake or CMake projects. To understand the answer to that question,
knowing about how the SDK does things internally and the tools it uses helps a
lot.

First we have to know about the _click_ command. It is one of the most
important tools we are about to use, because it provides ways to:

  * create a build environment
  * maintain the build environment
  * execute commands in the build environment
  * build click packages
  * review click packages
  * query click packages

Issuing _click --help_ will show a complete list of options. The _click_
command is not only used on the development machines but also on the device
images, as it is also responsible for installing/removing click packages and
to provide informations about the frameworks a device has to offer.

Assuming that the project source is already created, probably from a SDK
template, and ready to be packed up in ~/myproject, creating a click package
requires the following steps:

  1. Create a build target for the device that should be targeted 
    click chroot -a armhf -f ubuntu-sdk-15.04 create

  2. Run qmake/cmake on the project to create the Makefiles 
    
    mkdir ~/myproject-build
    cd ~/myproject-build
    click chroot -a armhf -f ubuntu-sdk-15.04 run cmake ../myproject #for cmake
    click chroot -a armhf -f ubuntu-sdk-15.04 run qt5-qmake-arm-linux-gnueabihf ../myproject #for qmake

  3. Run make to compile the project and run custom build steps 
    
    click chroot -a armhf -f ubuntu-sdk-15.04 run make

  4. Run make install to collect all required files in a deploy directory 
    
    rm -rf /tmp/deploy-myproject #make sure the deploy dir is clean
    click chroot -a armhf -f ubuntu-sdk-15.04 run make DESTDIR=/tmp/deploy-myproject install #for cmake
    click chroot -a armhf -f ubuntu-sdk-15.04 run make INSTALL_ROOT=/tmp/deploy-myproject install #for qmake

  5. Run click build on the deploy directory 
    
    click build /tmp/deploy-myproject

We will look into each step at a greater detail and explain the tools behind
it starting with:

#### _Creating a build chroot and what exactly is that:_

When building applications for a different architecture as the currently used
development machine , for example x86 host vs armhf device, cross build
toolchains are required. However toolchains are not easy to maintain and it
requires a good deal of effort to make them work correctly. So our decision is
to use "build chroots" to ease the maintenance of those toolchains. A build
chroot is in fact nothing else as the normal Ubuntu you are using on your host
machine. Probably its a different version, but it is still coming from the
archive. That means we can make sure the toolchains, libraries and tools that
are used to build click packages are well tested and receive the same updates
as the ones on the device images.

To create a build chroot the following command is used:

    
    click chroot -a armhf -f ubuntu-sdk-15.04 create

Grab a coffee while this is running, it will take quite some time. After the
chroot was created for the first time, it is possible to keep it up to date
with:

    
    click chroot -a armhf -f ubuntu-sdk-15.04 upgrade

But how exactly does this work? A chroot environment is another complete
Ubuntu root filesystem put inside a directory. The "chroot" command makes it
possible to treat exactly this directory as the "root directory" for a login
shell. Commands running inside that environment can not access the outer
filesystem and do not know they are actually inside a virtualized Ubuntu
installation. That makes sure your host file system can not be tainted by
anything that is done inside the chroot.

To make things a bit easier, /home and /tmp directories are mounted into the
chroot. That means those paths are the same inside and outside the chroot. No
need to copy files around. But that also means projects can only be in /home
by default. It is possible to change that but thats not in the scope of this
blog post (hint: check /etc/schroot/default/fstab).

#### _Run qmake/cmake on the project to create the Makefiles_

In order to compile the project, CMake or QMake need to create a Makefile from
the project description files. The SDK IDE always uses a builddirectory to
keep the source clean. That is the recommended way of building projects.

Now that we have a chroot created, we need a way to actually execute commands
inside the virtual environment. It is possible to log into the chroot or just
run single commands. The click chroots have 2 different modes, one of them is
the production mode and one is the maintenance mode.

Everything that is changed on the chroot filesystem in production mode will be
reverted when the active session is closed to make sure the chroot is always
clean. The maintenance mode can be used to install build dependencies, but its
the job of the user to make sure those dependencies are available on the phone
images as well. Rule of thumb is, if something is not installed in the chroot
by default it is probably not officially supported and might go away anytime.

    
    
    click chroot -a armhf -f ubuntu-sdk-15.04 run  #production
    click chroot -a armhf -f ubuntu-sdk-15.04 maint #maintenance

Running one of these commands without specifying which command should be
executed inside the chroot will open a login shell inside the chroot
environment. If multiple successive commands should be executed it is faster
to use a login shell, because the chroot is mounted/unmounted every time a
session is opened/closed.

For QMake projects usually the IDE takes care of selecting the correct QMake
binary, however in manual mode the user has to call the _qt5-qmake-arm-linux-
gnueabihf_ in armhf chroots instead of the plain _qmake_ command. The reason
for this is that qmake needs to be compiled in a special way for cross build
targets and the "normal" qmake can not be used.

#### _Run make to compile the project and run custom build steps_

This step does not need much explanations, it triggers the actual build of the
project and needs to be executed inside the chroot again of course.

#### _Run make install to collect all required files in a deploy directory_

Now that the project build was successful, step 4 collects all the required
files for the click package and installs them into a deploy directory. When
building with the IDE the directory is located in the current build dir and is
named ".ubuntu-sdk-deploy".

It is a good place to check if all files were put into the right place or
check if the manifest file is correct.

In order for that step to work correctly all files that should be in the click
package need to be put into the INSTALL targets. The app templates in the SDK
should give a good hint on how this is to be done.

The deploy directory now contains the directory structure of the final click
package.

#### _Run click build on the deploy directory_

The last step now is to build the actual click package. This command needs to
be executed outside the chroots, simply because of the fact that the click
command is not installed by default inside the chroots. What will happen now
is that all files inside _/tmp/deploy-myproject_ will be put inside the click
package and a click review is executed. The click review will tell if the
click package is valid and can be uploaded to the store.

If all went well, the newly created click package should show up in the
directory where _click _was executed, it can now be uploaded to the store or
installed on a device.

[Benjamin Zeller](/en/blog/authors/zeller-benjamin/)

April 13, 2015

Filed under: [planet-ubuntu](/en/blog/tags/planet-ubuntu/)
[sdk](/en/blog/tags/sdk/)





## Comments

No comments yet.

## Add your comment

Name:

Email address:

URL:

Comment:

If you enter anything in this field your comment will be treated as spam:





