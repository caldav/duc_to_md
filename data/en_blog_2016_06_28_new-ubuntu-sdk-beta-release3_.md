





#  [New Ubuntu SDK Beta Version](/en/blog/2016/06/28/new-ubuntu-sdk-beta-
release3/)

A few days ago we have released the first Beta of the Ubuntu SDK IDE using the
LXD container solution to build and execute applications.

The first reports were positive, however one big problem was discovered pretty
quickly:

Applications would not start on machines using the proprietary Nvidia drivers.
Reason for this is that indirect GLX is not allowed by default when using
those. The applications need to have access to:

  1. The glx libraries for the currently used driver
  2. The DRI and Nvidia device files

Luckily the snappy team already tackled a similar problem, so thanks to
Michael Vogt (a.k.a mvo) we had a first idea how to solve it by reusing the
Nvidia binaries and device files from the host by mounting them into the
container.

However it is a bit more complicated in our case, because once we have the
devices and directories mounted into the containers they will stay there
permanently. This is a problem because the Nvidia binary directory has a
version numbering, e.g. /usr/lib/nvidia-315, which changes with the currently
loaded module and would stop the container from booting after the driver was
changed and the old directory on the host is gone, or the container would use
the wrong nvidia dir if it was not removed from the host.

The situation gets worse with optimus graphics cards were the user can switch
between a integrated and dedicated graphics chip, which means device files in
/dev can come and go between reboots.

Our solution to the problem is to check the integrity of the containers on
every start of the Ubuntu SDK IDE and if problems are detected, the user is
informed and asked for the root password to run automatic fixes. Those checks
and fixes are implemented in the “usdk-target” tool and can be used from the
CLI as well.

As a bonus this work will enable direct rendering for other graphics chips as
well, however since we do not have access to all possible chips there might be
still special cases that we could not catch.

So please report all problems to us on one of those channels:

  * Launchpad ([https://bugs.launchpad.net/ubuntu-sdk-ide](https://bugs.launchpad.net/ubuntu-sdk-ide))
  * Telegram ( [https://telegram.me/joinchat/A2RODQhY9iLbe_WNeRMK_w](https://telegram.me/joinchat/A2RODQhY9iLbe_WNeRMK_w))!
  * or IRC (#ubuntu-app-devel on freenode)

We have released the new tool into the [Tools-development
PPA](https://launchpad.net/~ubuntu-sdk-team/+archive/ubuntu/tools-development)
where the first beta was released too. However existing container might not be
completely fixed automatically. They are better be recreated or manually
fixed. To manually fix an existing container use the maintain mode from the
options menu and add the current user into the “video” group.

To get the new version of the IDE please update the installed Ubuntu SDK IDE
package:

`$ sudo apt-get update && sudo apt-get install ubuntu-sdk-ide ubuntu-sdk-
tools`

[Benjamin Zeller](/en/blog/authors/zeller-benjamin/), [Zoltán
Balogh](/en/blog/authors/bzoltan/)

June 28, 2016

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





