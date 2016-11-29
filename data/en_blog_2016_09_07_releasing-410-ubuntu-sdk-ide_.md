





#  [Releasing the 4.1.0 Ubuntu SDK
IDE](/en/blog/2016/09/07/releasing-410-ubuntu-sdk-ide/)

The testing phase took longer than we have expected but finally we are ready.
To compensate this delay we have even upgraded the IDE to the most recent
4.1.0 QtCreator.

# Based on QtCreator 4.1.0

We have based the new IDE on the most recent QtCreator upstream release, which
brings a lot of new features and fixes. To see whats new there just check out:
[http://blog.qt.io/blog/2016/08/25/qt-
creator-4-1-0-released/](http://blog.qt.io/blog/2016/08/25/qt-
creator-4-1-0-released/).

# LXD based backend

The click chroot based builders are now deprecated. LXD allows us to download
and use pre built SDK images instead of having to bootstrap them every time a
new build target is created. These LXD containers are used to run the
applications from the IDE. Which means that the host machine of the SDK IDE
does not need any runtime dependencies.

# Get started

It is good to know that all existing schroot based builders will not be used
by the IDE anymore. The click chroots will remain on the host but will be
decoupled from the Ubuntu SDK IDE. If they are not required otherwise just
remove them using the Ubuntu dialog in Tools->Options.

If the beta IDE was used already make sure to recreate all containers, there
were some bugs in the images that we do not fix automatically.

To get the new IDE use:

`sudo add-apt-repository ppa:ubuntu-sdk-team/ppa`

`sudo apt update && sudo apt install ubuntu-sdk-ide`

Check our first blog post about the LXD based IDE for more detailed
instructions:

[https://developer.ubuntu.com/en/blog/2016/06/14/calling-testers-new-ubuntu-
sdk-ide-post/](https://developer.ubuntu.com/en/blog/2016/06/14/calling-
testers-new-ubuntu-sdk-ide-post/)

[Benjamin Zeller](/en/blog/authors/zeller-benjamin/), [Zoltán
Balogh](/en/blog/authors/bzoltan/)

Sept. 7, 2016

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





