





#  [Calling for testers of the new Ubuntu SDKIDE](/en/blog/2016/06/14/calling-testers-new-ubuntu-sdk-ide-post/)

## The next iteration of the Ubuntu SDK IDE

### or: here comes LXD

After a long development process we are pleased to announce that the next
version of the Ubuntu SDK IDE will go into beta testing phase as of today and
it comes packed with a completely new builder and runtime backend to finally
get rid of the biggest issues the SDK IDE has today.

Some people already heard rumours about new
[LXD](http://www.ubuntu.com/cloud/lxd) based builders that should replace the
schroot based ones. Well, the rumours are true and after some time of internal
testing of our proof of concept version with just a few trusted testers we
think it is time to show the new IDE to a bigger audience.

Now, before jumping right on the new packages let’s revisit some of the
reasons why we had to move away from the schroot based builders:

The biggest issue is for sure the creation of new chroots right after
installing the SDK. Bootstrapping a full Ubuntu root file system from live
archives is very slow and error prone. Whenever there is a packaging issue in
the archives or overlay PPA it is not possible to create new build targets.
Which basically makes the SDK unusable until the packaging issues are fixes.
LXD already has solved that problem, new containers are downloaded as
compressed and ready-to-go image files, downloading is much faster and the
resulting container will work for sure since it was tested by us before
releasing it as opposed to the continuously changing Overlay PPA. Once an
image has been downloaded it is cached, and spinning up a new container from
the cache is a matter of seconds!

The second issue I want to highlight is our requirement to execute the
applications locally on the desktop, but still supporting all Ubuntu versions
that are currently officially supported. Which means we had to deal with a
list of different Qt and UITK versions. We tried to solve that problem by
providing a separate Qt+UITK package but it turned out we’d have to hack and
rebuild so many packages to make that work that it was just not feasible. And
this is not only a build time problem, but also a runtime problem. How should
we continue to make it possible to run apps on the Desktop, using the hottest
and newest components while maintaining LTS compatibility?

The answer was actually very simple: Use the containers as runtime targets and
show the UI on the host’s X server.

There were a few more issues, like overall slowness and leaking mount points
(everyone who ever had hundreds of mounts because of schroot, knows what I’m
talking about), issues with ecryptfs and more.

Now, enough with the past, let’s look into the future and what has changed. It
is good to know before starting that we have dropped support for the default
Desktop Kit. Building and running on the Host is not supported by default
anymore. The SDK IDE will not create other desktop run configurations than
what automatically created by the qmake and cmake plugins. It is of course
still possible to build and run on the host, but the run configuration needs
to be created manually. Instead from now on it’s required to create a
container that matches the host architecture where the application is executed
in. It means that on the host system almost no additional packages are
required as dependencies.

All existing schroot based builders will not be used by the IDE anymore. The
click chroots will remain on the host but will be decoupled from the Ubuntu
SDK IDE.

## Get started

Its simple, all that needs to be done is to add the SDK Release and the Tools
Development PPA for the Ubuntu SDK tools:

`sudo add-apt-repository ppa:ubuntu-sdk-team/tools-development`

`sudo apt update && sudo apt install ubuntu-sdk-ide`

![](http://people.canonical.com/~bzoltan/blog-decoration/sdk-ppa-added-ide-installed-bigger.png)

##

And we are done, the IDE is now be fully usable. It will discover the
containers just as it used to do with the click chroots. From all aspects, the
developer experience will not change much. Please keep in mind we are still
beta testing so there will be most likely some bugs, either with the container
images or with the IDE itself. Please report them to us either directly on IRC
or via mailing list, or even better on the official ubuntu-sdk-ide project in
launchpad: [https://bugs.launchpad.net/ubuntu-sdk-ide](https://bugs.launchpad.net/ubuntu-sdk-ide)

## Known issues and troubleshooting

### **The lxd group membership**

Normally the LXD install process takes care of configuring the necessary group
membership. But if it does not then we have to make sure the current user is
part of the lxd group issue this command:

`sudo useradd -G lxd `whoami``

After that please relogin to make the new group known to the login session.

### **Reset QtCreator settings**

Sometimes the settings of QtCreator (the Qt application of the Ubuntu SDK IDE)
break when switching back and forth between different version. When you see
broken or ghost Kits, or possible misconfigured devices, or in general
anything what is weird it is possible that pushing the reset button on
Qtcreator helps. Note, that it is a rather radical fix. It can be easily done
with a single command:

`$ rm ~/.config/QtProject/qtcreator ~/.config/QtProject/QtC*`

### **Clean up old click chroots**

As mentioned before the old schroots are detached from the SDK IDE, but they
remain on the file system. With the following commands it is possible to clean
up the click chroots:

`$ sudo click chroot -a armhf -f ubuntu-sdk-15.04 destroy`

`$ sudo click chroot -a i386 -f ubuntu-sdk-15.04 destroy`

These commands will free about 1.4GB disk space. The click chroots live under
the /var/lib/schroot/chroots/ It is a good idea to check if that folder is
empty and nothing is mounted there

`$ mount|grep schroot`

### **NVIDIA video driver**

Deploying apps locally from the LXD container i snot possible on hosts using
NVIDIA graphics driver. If the host has dual graphic processor then one
workaround is to use the other one.

Check if you have a backup graphics card

`$ sudo lshw -class display`

If that list shows other entries than the NVIDIA the activate the other video
card. The prime select tool is a simple and easy tool to use.

`$ sudo prime-select intel`

Note that this tool might not be installed on your system and it does not work
together with bumblebee. In case the host has bumblebee installed and missing
the prime-select tool

`$ sudo apt-get remove bumblebee`

`$ sudo apt-get install nvidia-prime`

If the host has no other video card then the NVIDIA it is possible to use the
Nouveau driver what might work. Anywhow, this is a known and very sever issue
what we are working on.

## Let start the new IDE

But first back up some settings for the very unlikely case that we want to
move back to the present IDE

`$ tar zcvf ~/Qtproject.tar.gz ~/.config/QtProject`

Then find the Ubuntu SDK IDE in the Dash and start it

![](http://people.canonical.com/~bzoltan/blog-decoration/sdk-start-ide-from-dash.png)

The first thing the Ubuntu SDK IDE will do is checking if the environment is
properly set up. Unless you are an LXC/LXD power user it is safe to choose
'Yes' in this dialog.

![](http://people.canonical.com/~bzoltan/blog-decoration/sdk-fixing.png)

If the Ubuntu SDK is started for the first time, it will open a welcome wizard
to help with setting up kits and devices

![](http://people.canonical.com/~bzoltan/blog-decoration/sdk-welcome-1.png)

The best advice after this point is to read each page of the wizard and follow
the instructions. It is a fairly easy process.

On the next page the wizard will offer you help to create kits

![](http://people.canonical.com/~bzoltan/blog-decoration/sdk-welcome-2.png)

Push the "Create new Kit" button and read the target creation dialog

![](http://people.canonical.com/~bzoltan/blog-decoration/sdk-welcome-target-creation.png)

At this step we can choose between 3 types of targets:

  * "Build to run on the desktop", will filter for all images compatible with the desktop
  * "Build to run on device or emulator", will filter for all images that can be used for devices
  * "Show all available images", will show all available images

Let's select "Show all available images" to get an overview of all existing
images.

As next we choose the preferred target arch. The Ubuntu phones and tablets are
armhf and the host PC is either i386 or amd64. So for creating click packages
for the phone we will need an armhf target and testing the application on the
desktop we will need a native amd64 or i386 target

![](http://people.canonical.com/~bzoltan/blog-decoration/sdk-welcome-select-image.png)

We can use the default naming for the kits.

![](http://people.canonical.com/~bzoltan/blog-decoration/sdk-welcome-create-target-name.png)

Creating an LXD container requires system administrator rights, so at this
point we need to authenticate ourself

![](http://people.canonical.com/~bzoltan/blog-decoration/sdk-welcome-authentication.png)

Once we have entered the right password the download of the LXD image will
start

![](http://people.canonical.com/~bzoltan/blog-decoration/sdk-welcome-create-target-progress.png)

It will take some time, depending on our network bandwidth. Each image is
about 400MB. While the wizard downloads and configures the LXD image we have
just enough time to read a quick blog post about what the Kits actually are:
[Everything You Always Wanted to Know About Kits But Were Afraid toAsk](https://developer.ubuntu.com/en/blog/2015/03/18/everything-you-always-wanted-know-about-kits-were-afraid-ask/) . It is not an exaggeration to say
that the best way to invest the time is to read that blogpost and understand
what the development kits are.

Once the container creation is done a simple dialog will show us some basic
details

![](http://people.canonical.com/~bzoltan/blog-decoration/sdk-welcome-armhf-target-created.png)

The next page of the wizard will help to set up target devices. In our case we
already had a bq (krillin) phone and an emulator from the rc-proposed channel.

![](http://people.canonical.com/~bzoltan/blog-decoration/sdk-welcome-devices.png)

But even if there is no phone, tablet or emulator device available it is safe
to finish the wizard.

At this stage the IDE will automatically discover the LXD container and offer
us to update it.

![](http://people.canonical.com/~bzoltan/blog-decoration/sdk-start-update-kit-dialog.png)

It is not a mandatory step and perfectly safe to cancel that dialog.

After finishing the wizard the IDE will open up

![](http://people.canonical.com/~bzoltan/blog-decoration/sdk-ide-started.png)

[Benjamin Zeller](/en/blog/authors/zeller-benjamin/), [ZoltánBalogh](/en/blog/authors/bzoltan/)

June 14, 2016

Filed under: [planet-ubuntu](/en/blog/tags/planet-ubuntu/)
[sdk](/en/blog/tags/sdk/) [ubuntu-sdk](/en/blog/tags/ubuntu-sdk/)





## Comments

No comments yet.

## Add your comment

Name:

Email address:

URL:

Comment:

If you enter anything in this field your comment will be treated as spam:





