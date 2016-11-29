





## Getting started with a Samsung ARTIK 5 or 10

**From your desktop computer, you can download a pre-built Ubuntu Core image for your Samsung ARTIK 5 or 10 and copy it to an SD card ready to boot.**

Install Ubuntu Core

Install Ubuntu Core as a testing or

production environment for snaps.

Developer setup

Install Ubuntu Classic to develop

snaps directly on your device.

![](http://i.imgur.com/C9gK1z9.png)





### Prerequisites for booting Ubuntu Core

An Ubuntu SSO account is required to setup the first user on the board.

  1. Start by creating an [Ubuntu SSO account](https://login.ubuntu.com)
  2. Import an SSH Key into your Ubuntu SSO account [on this page](https://login.ubuntu.com/ssh-keys)

Instructions to generate an SSH Key can be found
[here](https://help.ubuntu.com/community/SSH/OpenSSH/Keys).

  3. You will need a keyboard, monitor or a serial cable plugged into the board to be able to go through the first boot process and complete device configuration.





### Install from Ubuntu

![](https://developer.ubuntu.com/static/devportal_uploaded/f4804533-1dcb-4cd5-
81af-61191e9309e5-cms_page_media/1014/ubupi.png)

Download the Ubuntu Core image, insert your SD Card and get started in a snap
with any Ubuntu computer.

Ubuntu instructions ›

### Install from Windows

![](https://developer.ubuntu.com/static/devportal_uploaded/a4327be8-178b-4ed9-
b3fe-54b821008714-cms_page_media/1014/winpi.png)

Download the Ubuntu Core image, insert your SD Card and get started in a snap
with any Windows computer

Windows instructions ›

### Install from a Mac

![](https://developer.ubuntu.com/static/devportal_uploaded/f8953f48-da90-481b-
9ed3-49cd7335861f-cms_page_media/1014/macpi.png)

Download the Ubuntu Core image, insert your SD Card and get started in a snap
with any Mac OS computer

Mac instructions ›





Back to top

## Install from Ubuntu

### Requirements

  * Ubuntu desktop (or any OS with `xzcat`, `dd`, and `sync` or equivalents available)

### Install commands

Start by downloading the [Ubuntu Core 16 developer image for Samsung ARTIK
5](http://people.canonical.com/~platform/snappy/artik/uc-series16-beta-
image/artik5.img.tar.xz) or your [Ubuntu Core image for Samsung ARTIK
10](http://people.canonical.com/~platform/snappy/artik/uc-series16-beta-
image/artik10.img.tar.xz) in your `~/Downloads` folder.

Insert your SD card, unmount it and run:

    # Note: replace /dev/sdX with the device name of your SD card (e.g. /dev/mmcblk0, /dev/sdg1 ...)
    #For the ARTIK 5
    xzcat ~/Downloads/artik5.img.tar.xz | sudo dd of=/dev/sdX bs=32M
    sync
    #For the ARTIK 10
    xzcat ~/Downloads/artik10.img.tar.xz | sudo dd of=/dev/sdX bs=32M
    sync

You’re done, you can now extract the SD card and boot your board with it.

First boot

#### Notes

  * If your SD card is mounted when you insert it into your computer (you will know it if the file manager automatically opens a window showing the card's contents), you must manually unmount it before writing the snappy image to it. Either eject your SD card from the file manager, or from the command line: `sudo umount /media/$USER/*`
  * You must specify the path to the disk device representing your SD card in the `dd` command above. Common device paths for the SD card disk device are either of the form /dev/sdX (such as /dev/sdb, not /dev/sdb1!) or /dev/mmcblk0 (not /dev/mmcblk0p1!)
  * Ensure there is no data you care about on the SD card before running the `dd` command above.





Back to top

## Install from Windows

Start by downloading the [Ubuntu Core 16 developer image for Samsung ARTIK
5](http://people.canonical.com/~platform/snappy/artik/uc-series16-beta-
image/artik5.img.tar.xz) or your [Ubuntu Core image for Samsung ARTIK
10](http://people.canonical.com/~platform/snappy/artik/uc-series16-beta-
image/artik10.img.tar.xz) in your `Downloads` folder.

Once the download is finished, you’ll have a zip file named
`artik5.img.tar.xz` or `artik10.img.tar.xz`.

Extract the downloaded zip file into your `Downloads` folder (you might have
to install archive extractor software, like [7-zip](http://www.7-zip.org/) or
similar as the standard tools do not support xz) you will now have a file
called `artik5.img` or `artik10.img`.

Insert the MicroSD Card on your computer, you can use an external card reader
or the SD slot if your computer has one.

Download and install Win32DiskImager.

Launch the [Win32DiskImager](http://sourceforge.net/projects/win32diskimager/f
iles/latest/download) application.

Find out where what drive your SD card is mounted to. Open a File Explorer
window to check which drive your SD card is listed under. Here is an example
of a card listed under `E:` and the setup in Diskimager.

![](https://developer.ubuntu.com/static/devportal_uploaded/9242b67a-987c-4181-
a9aa-59b1767fd2d1-cms_page_media/1014/Drives.png)

`Win32DiskImager` will need 2 elements:

  * `An Image File` which is the file you want to copy on your SD Card. Navigate to your `Downloads` folder and select the `.img` file you have extracted.
  * `A Device` which is the location of your SD card. Select the Drive in which your SD card is mounted.

![](https://developer.ubuntu.com/static/devportal_uploaded/b295bfa0-9546-4997-
9a7f-8ee4d5f8b800-cms_page_media/1014/Diskimager_setup.png)

To be safe, unplug every External USB Drive you may have connected to your PC.

When ready click on Write and wait for the process to complete.

Exit from `Win32DiskImager` and eject the SD card from the File Explorer
window.

You’re done, you can now extract the SD card and boot your board with it.

First boot





Back to top

## Install from a Mac

Start by downloading the [Ubuntu Core 16 developer image for Samsung ARTIK
5](http://people.canonical.com/~platform/snappy/artik/uc-series16-beta-
image/artik5.img.tar.xz) or your [Ubuntu Core image for Samsung ARTIK
10](http://people.canonical.com/~platform/snappy/artik/uc-series16-beta-
image/artik10.img.tar.xz) in your `Downloads` folder.

Save the file in your Download folder. Unarchive the file `artik5.img.tar.xz`
or `artik10.img.tar.xz` by double clicking on it. You should now have a
`artik10.img` or `artik5.img` file in your Download folder. In order to
uncompress the file you might need to download a new un-archiving application
like [The Unarchiver](https://itunes.apple.com/gb/app/the-
unarchiver/id425424353?mt=12).

Insert your SD card into your MAC (note that you will need an adapter for your
Micro-SD card)

Open a terminal window (Go to Application -> Utilities you will find the
Terminal app there). Run the following command:

    diskutil list

In the results identify your SD card, it will probably an entry like the one
below:

    /dev/disk0
      #:                       TYPE NAME                    SIZE       IDENTIFIER
      0:      GUID_partition_scheme                        *500.3 GB   disk0
    /dev/disk2
      #:                       TYPE NAME                    SIZE       IDENTIFIER
      0:                  Apple_HFS Macintosh HD           *428.8 GB   disk1
                                    Logical Volume on disk0s2
                                    E2E7C215-99E4-486D-B3CC-DAB8DF9E9C67
                                    Unlocked Encrypted
    /dev/disk3
      #:                       TYPE NAME                    SIZE       IDENTIFIER
      0:     FDisk_partition_scheme                        *7.9 GB     disk3
      1:                 DOS_FAT_32 NO NAME                 7.9 GB     disk3s1

Note that your SD Card must be DOS_FAT_32 formatted. The SIZE will be the size
of your SD card, in this example an 8GB SD Card.

Write down the number after /dev/disk that is associated with your SD card, in
this case 3.

Unmount your SD card, for this you will need the number you just wrote down by
entering the command:

    diskutil unmountDisk /dev/disk<disk number you wrote down above>

in our example we used:

    diskutil unmountDisk /dev/disk3

When successful you should see a message similar to this one:

    Unmount of all volumes on disk# was successful

This effectively made the SD card ready to receive a copy of Ubuntu Core. The
next step is to copy Ubuntu Core to the SD card, using the following command:

    sudo dd if=~/Downloads/artik10.img of=/dev/rdisk<disk number you noted above> bs=32MB

In our example:

    sudo dd if=~/Downloads/artik10.img of=/dev/rdisk3 bs=32MB

You will be prompted to enter your Apple password after this command.

Note that this operation will take between 15 and 30 minutes, during which you
will not see any progress! Be patient, get a cup of coffee. You can check the
progress by sending a SIGINFO signal pressing Ctrl+T.

When finalised you will see the following message:

    3719+1 records in
    3719+1 records out
    3899999744 bytes transferred in 642.512167 secs (6069924 bytes/sec)

You’re done, you can now extract the SD card and boot your board with it.

First boot

This section uses content from the eLinux wiki page RPi_Easy_SD_Card_Setup and
from the Raspberry Pi Foundation, which is shared under the Creative Commons
Attribution-ShareAlike 3.0 Unported license.





## Ubuntu Core first boot

Before you can boot your ARTIK with Ubuntu Core you need to set it to boot
from the SD card. To do so use the "SW2" switches and set them to 1:on and
2:on.

  1. Insert the SD card in your Samsung ARTIK
  2. Connect the 5V power supply to the board, then use the power button on the board to switch on your Samsung ARTIK
  3. The system will boot then become ready to configure
  4. The device will display the prompt “Press enter to configure”
  5. Press enter then select “Start” to begin configuring your network and an administrator account. Follow the instructions on the screen, you will be asked to configure your network and enter your Ubuntu SSO credentials
  6. At the end of the process, you will see **your credentials to access your Ubuntu Core machine**:
    This device is registered to <Ubuntu SSO email address>.
    Remote access was enabled via authentication with the SSO user <Ubuntu SSO user name>
    Public SSH keys were added to the device for remote access.

#### Login

Once setup is done, you can login with SSH into Ubuntu Core, from a machine on
the same network, using the following command:

    ssh <Ubuntu SSO user name>@**<device IP address>**

The user name is your Ubuntu SSO user name, it has been reminded to you at the
end of the account configuration step.

##### First login tips

  * During setup,` console-conf` will download the SSH key registered with your Store account and configure it so you can log into the device via `ssh <Ubuntu SSO account name>@<device IP address>` without a password.
  * There is no default `ubuntu` user on these images, but you can run `sudo passwd <account name>` to set a password in case you need a local console login.





* * *

### Next steps

You're all set up to get started with the next generation of Ubuntu. It's now
time for the fun to start and try Ubuntu Core and snaps.

[Snaps usage guide](http://snapcraft.io/docs/core/usage)

### Grow the ecosystem

Learn how to snap your apps or make your own custom image with preloaded snaps
for a family of devices.

  * [How to build snaps ›](http://snapcraft.io)
  * [Make a custom Ubuntu Core image ›](http://docs.ubuntu.com/core/en/guides/build-device/image-building)

### Need help?

Thanks to our active community, you can find support from a variety of sources
such as Ask Ubuntu, our mailing lists or IRC channel.

  * [Ask us a question ›](http://snapcraft.io/community/)
  * [Browse the documentation ›](http://docs.ubuntu.com/core)





## Developer setup

### Install Ubuntu Classic (server) on the Artik 5 or 10

Ubuntu Classic is Ubuntu as you know it, where you can use your favourite
development tools to create and run snaps.

  * 1. Create an installation media
  * 2. Install Ubuntu on the board
  * 3. Try the snap command





### 1. Create your installation media

During this step, you will create an Ubuntu Server 16.04 SD Card.

Follow the instructions for the desktop OS you are using:

  * Create your installation media from Ubuntu
  * Create your installation media from Windows
  * Create your installation media from Mac OS X





### Create your installation media from Ubuntu

#### Requirements

  * Ubuntu desktop (or any OS with `xzcat`, `dd`, and `sync` or equivalents available)

#### Install commands

Start by downloading the [Ubuntu Server 16.04 image for Samsung ARTIK
5](http://people.canonical.com/~platform/snappy/artik/artik5-ubuntu-
server.img.tar.xz) or your [Ubuntu Server 16.04 image for Samsung ARTIK
10](http://people.canonical.com/~platform/snappy/artik/artik10-ubuntu-
server.img.tar.xz) in your `~/Downloads` folder.

Insert your SD card, unmount it and run:

    # Note: replace /dev/sdX with the device name of your SD card (e.g. /dev/mmcblk0, /dev/sdg1 ...)
    #For the ARTIK 5
    xzcat ~/Downloads/artik5-ubuntu-server.img.tar.xz | sudo dd of=/dev/sdX bs=32M
    sync
    #For the ARTIK 10
    xzcat ~/Downloads/artik10-ubuntu-server.img.tar.xz | sudo dd of=/dev/sdX bs=32M
    sync

You’re done, you can now extract the SD card and boot your board with it.

Install Ubuntu on the board

##### Notes

  * If your SD card is mounted when you insert it into your computer (you will know it if the file manager automatically opens a window showing the card's contents), you must manually unmount it before writing the snappy image to it. Either eject your SD card from the file manager, or from the command line: `sudo umount /media/$USER/*`
  * You must specify the path to the disk device representing your SD card in the `dd` command above. Common device paths for the SD card disk device are either of the form /dev/sdX (such as /dev/sdb, not /dev/sdb1!) or /dev/mmcblk0 (not /dev/mmcblk0p1!)
  * Ensure there is no data you care about on the SD card before running the `dd` command above.





### Create your installation media from Windows

Start by downloading the [Ubuntu Server 16.04 image for Samsung ARTIK
5](http://people.canonical.com/~platform/snappy/artik/artik5-ubuntu-
server.img.tar.xz) or your [Ubuntu Server 16.04 image for Samsung ARTIK
10](http://people.canonical.com/~platform/snappy/artik/artik10-ubuntu-
server.img.tar.xz) in your `Downloads` folder.

Once the download is finished, you’ll have a zip file named `artik5-ubuntu-
server.img.tar.xz` or `artik10-ubuntu-server.img.tar.xz`.

Extract the downloaded zip file into your `Downloads` folder (you might have
to install archive extractor software, like [7-zip](http://www.7-zip.org/) or
similar as the standard tools do not support the xz format) you will now have
a file called `artik5-ubuntu-server.img` or `artik10-ubuntu-server.img`.

Insert the MicroSD Card on your computer, you can use an external card reader
or the SD slot if your computer has one.

Download and install Win32DiskImager.

Launch the [Win32DiskImager](http://sourceforge.net/projects/win32diskimager/f
iles/latest/download) application.

Find out where what drive your SD card is mounted to. Open a File Explorer
window to check which drive your SD card is listed under. Here is an example
of a card listed under `E:` and the setup in Diskimager.

![](https://developer.ubuntu.com/static/devportal_uploaded/9242b67a-987c-4181-
a9aa-59b1767fd2d1-cms_page_media/1014/Drives.png)

`Win32DiskImager` will need 2 elements:

  * `An Image File` which is the file you want to copy on your SD Card. Navigate to your `Downloads` folder and select the `.img` file you have extracted.
  * `A Device` which is the location of your SD card. Select the Drive in which your SD card is mounted.

![](https://developer.ubuntu.com/static/devportal_uploaded/b295bfa0-9546-4997-
9a7f-8ee4d5f8b800-cms_page_media/1014/Diskimager_setup.png)

To be safe, unplug every External USB Drive you may have connected to your PC.

When ready click on Write and wait for the process to complete.

Exit from `Win32DiskImager` and eject the SD card from the File Explorer
window.

You’re done, you can now extract the SD card and boot your board with it.

Install Ubuntu on the board





### Create your installation media from Mac OS X

Start by downloading the [Ubuntu Server 16.04 image for Samsung ARTIK
5](http://people.canonical.com/~platform/snappy/artik/artik5-ubuntu-
server.img.tar.xz) or your [Ubuntu Server 16.04 image for Samsung ARTIK
10](http://people.canonical.com/~platform/snappy/artik/artik10-ubuntu-
server.img.tar.xz) in your `~/Downloads` folder.

Save the file in your Download folder. Unarchive the file `artik5-ubuntu-
server.img.tar.xz` or `artik10-ubuntu-server.img.tar.xz` by double clicking on
it. You should now have a `artik10-ubuntu-server.img` or `artik5-ubuntu-
server.img` file in your Download folder. In order to uncompress the file you
might need to download a new un-archiving application like [The
Unarchiver](https://itunes.apple.com/gb/app/the-unarchiver/id425424353?mt=12).

Insert your SD card into your MAC (note that you will need an adapter for your
Micro-SD card)

Open a terminal window (Go to Application -> Utilities you will find the
Terminal app there). Run the following command:

    diskutil list

In the results identify your SD card, it will probably an entry like the one
below:

    /dev/disk0
      #:                       TYPE NAME                    SIZE       IDENTIFIER
      0:      GUID_partition_scheme                        *500.3 GB   disk0
    /dev/disk2
      #:                       TYPE NAME                    SIZE       IDENTIFIER
      0:                  Apple_HFS Macintosh HD           *428.8 GB   disk1
                                    Logical Volume on disk0s2
                                    E2E7C215-99E4-486D-B3CC-DAB8DF9E9C67
                                    Unlocked Encrypted
    /dev/disk3
      #:                       TYPE NAME                    SIZE       IDENTIFIER
      0:     FDisk_partition_scheme                        *7.9 GB     disk3
      1:                 DOS_FAT_32 NO NAME                 7.9 GB     disk3s1

Note that your SD Card must be DOS_FAT_32 formatted. The SIZE will be the size
of your SD card, in this example an 8GB SD Card.

Write down the number after /dev/disk that is associated with your SD card, in
this case 3.

Unmount your SD card, for this you will need the number you just wrote down by
entering the command:

    diskutil unmountDisk /dev/disk<disk number you wrote down above>

in our example we used:

    diskutil unmountDisk /dev/disk3

When successful you should see a message similar to this one:

    Unmount of all volumes on disk# was successful

This effectively made the SD card ready to receive a copy of Ubuntu Core. The
next step is to copy Ubuntu Core to the SD card, using the following command:

    sudo dd if=~/Downloads/artik10-ubuntu-server.img of=/dev/rdisk<disk number you noted above> bs=32MB

In our example:

    sudo dd if=~/Downloads/artik10-ubuntu-server.img of=/dev/rdisk3 bs=32MB

You will be prompted to enter your Apple password after this command.

Note that this operation will take between 15 and 30 minutes, during which you
will not see any progress! Be patient, get a cup of coffee. You can check the
progress by sending a SIGINFO signal pressing Ctrl+T.

When finalised you will see the following message:

    3719+1 records in
    3719+1 records out
    3899999744 bytes transferred in 642.512167 secs (6069924 bytes/sec)

You’re done, you can now extract the SD card and boot your board with it.

Install Ubuntu on the board

This section uses content from the eLinux wiki page RPi_Easy_SD_Card_Setup and
from the Raspberry Pi Foundation, which is shared under the Creative Commons
Attribution-ShareAlike 3.0 Unported license.





### 2. Install Ubuntu on the board

Booting the board from the SD Card will start the Ubuntu installer.

Before installing Ubuntu, you need to set your Artik to boot from the SD card.

To do so use the "SW2" switches and set them to 1:on and 2:on.

  1. Insert the SD card in your Samsung ARTIK
  2. Connect the 5V power supply to the board, then use the power button on the board to switch on your Samsung ARTIK
  3. The system will automatically execute the first stage of installation
  4. Follow the instructions and enter appropriate options for language, WiFi, location (timezone), and keyboard layout
  5. Pick a hostname, user account and password
  6. Wait for the configuration to finish. If you connected to a WiFi network at step 4, it will take several minutes to download and apply additional updates. You can now reboot the system
  7. Ubuntu is installed. Use your account and password to log in





### 3. Try the snap command

You are all set up to get started with snaps. A good introduction is to follow
the [snaps usage guide](http://snapcraft.io/docs/core/usage).





