





## Get started with a Raspberry Pi 2 or 3

**From your desktop computer, you can download an Ubuntu Core image for your Raspberry Pi 2 or 3 and copy it to an SD card ready to boot.**

![](https://developer.ubuntu.com/static/devportal_uploaded/072a3783-6b14-4c65-
a2aa-f9e2b4d282db-cms_page_media/376/raspberry-pi.png)





### Prerequisites for booting Ubuntu Core

An Ubuntu SSO account is required to setup the first user on the board.

  1. Start by creating an [Ubuntu SSO account](https://login.ubuntu.com)
  2. Import an SSH Key into your Ubuntu SSO account [on this page](https://login.ubuntu.com/ssh-keys)

Instructions to generate an SSH Key can be found
[here](https://help.ubuntu.com/community/SSH/OpenSSH/Keys).

  3. You will need a keyboard, monitor or a serial cable plugged into the board to be able to go through the first boot process and complete device configuration.





### Install from Ubuntu

![](/static/devportal_uploaded/f4804533-1dcb-4cd5-81af-61191e9309e5-cms_page_m
edia/1014/ubupi.png)

Download the Ubuntu image, insert your SD Card and get started in a snap with
any Ubuntu computer.

Ubuntu instructions ›

### Install from Windows

![](/static/devportal_uploaded/a4327be8-178b-4ed9-b3fe-54b821008714-cms_page_m
edia/1014/winpi.png)

Download the Ubuntu image, insert your SD Card and get started in a snap with
any Windows computer

Windows instructions ›

### Install from a Mac

![](/static/devportal_uploaded/f8953f48-da90-481b-9ed3-49cd7335861f-cms_page_m
edia/1014/macpi.png)

Download the Ubuntu image, insert your SD Card and get started in a snap with
any Mac OS computer

Mac instructions ›





Back to top

## Install from Ubuntu

### Requirements

  * Ubuntu desktop (or any OS with `xzcat`, `dd`, and `sync` or equivalents available)

### Install commands

Start by downloading the [Ubuntu Core 16 image for Raspberry Pi
2](http://releases.ubuntu.com/ubuntu-core/16/ubuntu-core-16-pi2.img.xz) or the
one [for Raspberry Pi 3](http://releases.ubuntu.com/ubuntu-core/16/ubuntu-
core-16-pi3.img.xz) in your `~/Downloads` folder.

Insert your SD card, unmount it and run:

    # Note: replace /dev/sdX with the device name of your SD card (e.g. /dev/mmcblk0, /dev/sdg1 ...)
    xzcat ~/Downloads/ubuntu-core-16-pi3.img.xz | sudo dd of=/dev/sdX bs=32M
    sync

Eject the SD card physically from your PC and Insert the SD card in your
Raspberry Pi.

#### Notes

  * If your SD card is mounted when you insert it into your computer (you will know it if the file manager automatically opens a window showing the card's contents), you must manually unmount it before writing the Ubuntu Core image to it. Either eject your SD card from the file manager, or from the command line: `sudo umount /media/$USER/*`
  * You must specify the path to the disk device representing your SD card in the `dd` command above. Common device paths for the SD card disk device are either of the form /dev/sdX (such as /dev/sdb, not /dev/sdb1!) or /dev/mmcblk0 (not /dev/mmcblk0p1!)
  * Ensure there is no data you care about on the SD card before running the `dd` command above.

First boot





Back to top

## Install from Windows

Start by downloading the [Ubuntu Core 16 image for Raspberry Pi
2](http://releases.ubuntu.com/ubuntu-core/16/ubuntu-core-16-pi2.img.xz) or the
one [for Raspberry Pi 3](http://releases.ubuntu.com/ubuntu-core/16/ubuntu-
core-16-pi3.img.xz) in your `Downloads` folder.

Once the download is finished, you’ll have a zip file named `ubuntu-
core-16-pi3.img.xz`.

Extract the downloaded zip file into your Downloads folder (you might have to
install an archive extractor software, like [7-zip](http://www.7-zip.org/) or
similar as the standard tools do not support the `xz` format), and you will
now have a file called `ubuntu-core-16-pi3.img` .

Insert the MicroSD Card on your computer, you can use an external card reader
or the SD slot if your computer has one.

Download and install [Win32DiskImager](http://sourceforge.net/projects/win32di
skimager/files/latest/download), then launch it.

Find out where your SD card is mounted by opening a File Explorer window to
check which drive your SD card is listed under.

Here is an example of a card listed under `E:`.

![](http://i.imgur.com/QXLkLsa.png)

In order to flash your card with the Ubuntu image, **Win32DiskImager** will
need 2 elements:

  * an Image File: navigate to your `Downloads` folder and select the `ubuntu-core-16-pi3.img` image you have just extracted.
  * a Device: the location of your SD card. Select the drive on which your SD card is mounted.

![](http://i.imgur.com/ebeQHKT.png)

To be safe, unplug every External USB Drive you may have connected to your PC.

When ready click on **Write** and wait for the process to complete.

Exit from Win32DiskImager and eject the SD card from the File Explorer window.

Eject the SD card physically from your PC and insert the SD card in your
Raspberry Pi.

First boot





Back to top

## Install from a Mac

Start by downloading the [Ubuntu Core 16 image for Raspberry Pi
2](http://releases.ubuntu.com/ubuntu-core/16/ubuntu-core-16-pi2.img.xz) or the
one [for Raspberry Pi 3](http://releases.ubuntu.com/ubuntu-core/16/ubuntu-
core-16-pi3.img.xz) in your `Downloads` folder.

Save the file in your Download folder. Unarchive the file `ubuntu-
core-16-pi3.img.xz` by double clicking on it. You should now have an `ubuntu-
core-16-pi3.img` file in your `Downloads` folder. In order to uncompress the
file you might need to download a new un-archiving application like [The
Unarchiver](https://itunes.apple.com/gb/app/the-unarchiver/id425424353?mt=12).

Insert your SD card into your MAC (note that you will need an adapter for your
Micro-SD card)

Open a terminal window (Go to Application -> Utilities, you will find the
Terminal app there). Run the following command:

    diskutil list

In the results identify your SD card, it will probably look like an entry like
the ones below:

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
running the command:

    diskutil unmountDisk /dev/disk<disk number you wrote down above>

in our example we used:

    diskutil unmountDisk /dev/disk3

When successful you should see a message similar to this one:

    Unmount of all volumes on disk# was successful

This effectively made the SD card ready to receive a copy of Ubuntu. The next
step is to copy Ubuntu to the SD card, using the following command:

    sudo dd if=~/Downloads/ubuntu-core-16-pi3.img of=/dev/rdisk<disk number you noted above> bs=32MB

In our example:

    sudo dd if=~/Downloads/ubuntu-core-16-pi3.img of=/dev/rdisk3 bs=32MB

You will be prompted to enter your Apple password after this command.

Note that this operation will take between 15 and 30 minutes, during which you
will not see any progress! Be patient, get a cup of coffee. You can check the
progress by sending a SIGINFO signal pressing Ctrl+T.

When finalised you will see the following message:

    3719+1 records in
    3719+1 records out
    3899999744 bytes transferred in 642.512167 secs (6069924 bytes/sec)

Extract the card and slot it in your Raspberry Pi to give it a spin!

First boot

This section uses content from the eLinux wiki page RPi_Easy_SD_Card_Setup and
from the Raspberry Pi Foundation, which is shared under the Creative Commons
Attribution-ShareAlike 3.0 Unported license.





## Ubuntu Core first boot

  1. The system will boot then become ready to configure
  2. The device will display the prompt “Press enter to configure”
  3. Press enter then select “Start” to begin configuring your network and an administrator account. Follow the instructions on the screen, you will be asked to configure your network and enter your Ubuntu SSO credentials
  4. At the end of the process, you will see **your credentials to access your Ubuntu Core machine**:
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





