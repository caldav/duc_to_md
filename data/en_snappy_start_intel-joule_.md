





## Getting started with an Intel® Joule

**From your Ubuntu desktop computer, you can download and flash a pre-built Ubuntu Core image on your Intel**®** Joule.**

Install Ubuntu Core

Install Ubuntu Core as a testing or

production environment for snaps.

Developer setup

Install Ubuntu Classic to develop

snaps directly on your device.

![](http://i.imgur.com/NgG2WWZ.png)





### Prerequisites for booting Ubuntu Core

An Ubuntu SSO account is required to setup the first user on the board.

  1. Start by creating an [Ubuntu SSO account](https://login.ubuntu.com)
  2. Import an SSH Key into your Ubuntu SSO account [on this page](https://login.ubuntu.com/ssh-keys)

Instructions to generate an SSH Key can be found
[here](https://help.ubuntu.com/community/SSH/OpenSSH/Keys).

  3. You will need a keyboard, monitor or a serial cable plugged into the board to be able to go through the first boot process and complete device configuration.





## Hardware and software requirements

  * an Intel® Joule board

The board needs to have its BIOS updated to version #131, which is available
[here](https://downloadmirror.intel.com/26206/eng/Joule-Firmware-2016-09-23-131_Public.zip).

  * an Ubuntu workstation running Ubuntu 14.04 (or later)
  * 2 USB 2.0 or 3.0 flash drives (2GB min.)

The first one will let you boot a full fledged Ubuntu Desktop on your board,
the second one will allow you to flash the board with Ubuntu Core.

  * an [Ubuntu Core 16 beta image for Intel Joule](http://people.canonical.com/~platform/snappy/tuchuck/tuchuck-20161014085519.img.xz)
  * an [Ubuntu Desktop 16.04.1 LTS image](http://releases.ubuntu.com/16.04.1/ubuntu-16.04.1-desktop-amd64.iso)
  * a monitor with an HDMI interface
  * a Mini HDMI to HDMI cable
  * a USB keyboard and a mouse
  * a USB Hub for all the above USB pieces (4)
  * an 802.11 a/b/g/n WiFi network with Internet access





## Installation Instructions

These instructions will drive you through getting Ubuntu Core running on your
Joule board, using an Ubuntu desktop workstation.

  * 1. Create installation medias
  * 2. Flash Ubuntu Core on the Joule
  * 3. Ubuntu Core first boot





### 1. Create installation medias

During this step, you will create an Ubuntu Desktop Live USB flash drive and
an Ubuntu Core flash drive on your Ubuntu desktop workstation.

  1. Download the [Ubuntu Desktop 16.04.1 LTS iso image](http://releases.ubuntu.com/16.04.1/ubuntu-16.04.1-desktop-amd64.iso)
  2. Insert the first USB flash drive into your workstation
  3. Start “Startup Disk Creator” application. It can be found by typing “Startup Disk Creator” in the Unity Dash (icon with Ubuntu logo located in the upper left corner of the screen)

    1. Select “ubuntu-16.04.1-desktop-amd64.iso” in the top pane “Source disk image (.iso)”. If the .iso file is not listed there, click on "Other..." to locate and select the .iso file.
    2. In the lower pane, make sure the USB disk is selected properly.
    3. Click on “Make Startup Disk” button and click “Yes” when a prompt dialog appears.
    4. The message “Installation is complete.” will be displayed.

Note: these instructions are based on Ubuntu 16.04. If you are using a
different version, the messages may be different.

  4. Unmount (right click on the USB device icon on Unity launcher, choose “Safely Remove”) and remove the USB flash drive
  5. Download the [Ubuntu Core 16 beta image for Intel Joule](http://people.canonical.com/~platform/snappy/tuchuck/tuchuck-20161014085519.img.xz)
  6. Insert the second USB flash drive and copy the img.xz file you just downloaded onto it
  7. Unmount and remove the second USB flash drive





### 2. Flash Ubuntu Core on the Joule

During this step, you will boot a Live USB Ubuntu Desktop on the Joule and use
it to flash Ubuntu Core on the board.

  1. Connect your USB hub, keyboard, mouse, LCD monitor to the Joule board
  2. Insert the Ubuntu Desktop Live USB flash drive
  3. Power-up the Joule board, boot-up the device from USB and select “Try Ubuntu without installing” in the GRUB menu
  4. After the system is ready, insert the second USB flash drive
  5. Open a terminal and type the following command:
    xzcat /media/ubuntu/DISKLABEL/tuchuck.img.xz | sudo dd of=/dev/mmcblk0 bs=32M status=progress; sync

Change `DISKLABEL` to the name of the USB flash drive.

  6. Remove the USB flash drive and reboot the system





## 3. Ubuntu Core first boot

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





## Developer setup

### Install Ubuntu Classic (desktop) on the Intel Joule

Ubuntu Classic is Ubuntu as you know it, where you can use your favourite
development tools to create and run snaps.

  * 1. Create an installation media
  * 2. Install Ubuntu on the board
  * 3. Try the snap command





### Hardware and software requirements

  * a Joule board 

The board needs to have its bios updated to version #131, which is available
[here.](https://downloadmirror.intel.com/26206/eng/Joule-Firmware-2016-09-23-131_Public.zip)

  * an Ubuntu workstation running Ubuntu 14.04 (or later)
  * 1 USB 2.0 or 3.0 flash drive (4GB min.)
  * an [Ubuntu Desktop 16.04 classic image for Intel Joule](http://people.canonical.com/~platform/snappy/tuchuck/tuchuck-20161014085519.img.xz)





### 1. Create an installation media

During this step, you will create an Ubuntu Desktop Live USB flash drive and
an Ubuntu Core flash drive on your Ubuntu desktop workstation

  1. Download the [Ubuntu Desktop 16.04 classic image for Intel Joule](http://people.canonical.com/~platform/snappy/tuchuck/tuchuck-20161014085519.img.xz)
  2. Extract the image with the `unxz tuchuck-20161014085519.img.xz` command
  3. Insert the USB flash drive into your workstation
  4. Start “Startup Disk Creator” application. It can be found by typing “Startup Disk Creator” in the Unity Dash (icon with Ubuntu logo located in the upper left corner of the screen) 
    1. Select “`tuchuck-20161014085519.img`” in the top pane “Source disk image”. If the .img file is not listed there, click on "Other..." to locate and select the .img file.
    2. In the lower pane, make sure the USB disk is selected properly.
    3. Click on “Make Startup Disk” button and click “Yes” when a prompt dialog appears.
    4. The message “Installation is complete.” will be displayed.

Note: these instructions are based on Ubuntu 16.04. If you are using a
different version, the messages may be different.

  5. Unmount (right click on the USB device icon in the Unity launcher, choose “Safely Remove”) and remove the USB flash drive





### 2. Install Ubuntu on the board

Booting the board from the flash drive will start the Ubuntu installer.

  1. Boot the system from the USB flash drive
  2. The system will automatically execute the first stage of installation, including eMMC storage partitioning and image installation. After installation is complete, a prompt dialog will be shown and you will need to restart the system
  3. Boot the system on the eMMC storage and finish the install configuration
  4. Follow the instructions and enter appropriate options for language, WiFi, location (timezone), and keyboard layout
  5. Pick a hostname, user account and password
  6. Wait for the configuration to finish. If you connected to a WiFi network at step 4, it will take several minutes to download and apply additional updates. You can now reboot the system
  7. Ubuntu is installed. Use your account and password to log in





### 3. Try the snap command

You are all set up to get started with snaps. A good introduction is to follow
the [snaps usage guide](http://snapcraft.io/docs/core/usage).

RealSense libraries can also be installed as a snap, using this command:

    sudo snap install --devmode --edge librealsense-chenhan





