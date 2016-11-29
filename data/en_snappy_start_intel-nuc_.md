





## Getting started with an Intel® Nuc

**From your desktop computer, you can download and flash a pre-built Ubuntu Core image on your Intel**®** Joule.**

Install Ubuntu Core

Install Ubuntu Core as a testing or

production environment for snaps.

Developer setup

Install Ubuntu Classic to develop

snaps directly on your device.

![](https://developer.ubuntu.com/static/devportal_uploaded/30cdcf68-db23-4828-
ac25-d1e6b10a2804-cms_page_media/1037/Thin_Canyon_NUC_Front_Angle_Board.png)





### Prerequisites for booting Ubuntu Core

An Ubuntu SSO account is required to setup the first user on the board.

  1. Start by creating an [Ubuntu SSO account](https://login.ubuntu.com)
  2. Import an SSH Key into your Ubuntu SSO account [on this page](https://login.ubuntu.com/ssh-keys)

Instructions to generate an SSH Key can be found
[here](https://help.ubuntu.com/community/SSH/OpenSSH/Keys).

  3. You will need a keyboard, monitor or a serial cable plugged into the board to be able to go through the first boot process and complete device configuration.





## Hardware and software requirements

  * an Intel® NUC

The NUC needs to have its BIOS updated to the latest version. For this, you
can follow [online instructions on the Intel
website](http://www.intel.com/content/www/us/en/support/boards-and-
kits/000005850.html).

  * an USB 2.0 or 3.0 flash drive (8GB min.)
  * an [Ubuntu Desktop 16.04.1 LTS image](http://releases.ubuntu.com/16.04.1/ubuntu-16.04.1-desktop-amd64.iso)
  * a monitor with an HDMI interface
  * a USB keyboard and a mouse
  * a network connection with Internet access





## Installation Instructions

These instructions will drive you through getting Ubuntu Core running on your
NUC.

  * 1. Create your installation media
  * 2. Flash Ubuntu Core on the NUC
  * 3. Ubuntu Core first boot





### 1. Create your installation media

During this step, you will create an Ubuntu Desktop Live USB flash drive.

Follow the instructions for the desktop OS you are using:

  * [Using Ubuntu](http://www.ubuntu.com/download/desktop/create-a-usb-stick-on-ubuntu)
  * [Using Windows](http://www.ubuntu.com/download/desktop/create-a-usb-stick-on-windows)
  * [Using Mac OS X](http://www.ubuntu.com/download/desktop/create-a-usb-stick-on-mac-osx)





### 2. Flash Ubuntu Core on the NUC

During this step, you will boot a Live USB Ubuntu Desktop on the NUC and use
it to flash Ubuntu Core.

#### Preparing the NUC (if using internal ROM as disk)

This step is only necessary in case you want to install Ubuntu Core on the
emmc Built-In Storage. If you wired an SSD drive to your NUC, this section can
be skipped.

  1. Start your NUC by pressing the On button while pressing F2 during the boot up, this will open the BIOS settings
  2. On the initial screen, open the "Advanced" tab, then open the "Devices and Peripherals" tab
  3. On the "Devices and Peripherals" menu, under the "On board devices" submenu, make sure that the emmc checkbox ("4GB emmc Built-in Storage") is checked.  
If you didn't find this option, this means that you need to update your NUC
BIOS to latest version. For this, you can follow [online instructions on the
Intel website](http://www.intel.com/content/www/us/en/support/boards-and-
kits/000005850.html).

  4. In the "Boot" menu, "Secure boot" submenu, make sure that the "secure boot" is not checked.

#### Booting from the Live USB flash drive

  1. Insert the Live USB Ubuntu Desktop flash drive in the NUC
  2. Start the NUC and push F10 to enter the boot menu.
  3. Select the USB flash drive as a boot option
  4. Select "Try Ubuntu without installing”

#### Flashing Ubuntu Core

Once the Ubuntu session is running, open a terminal with the key combination
Ctrl+Alt+t and download the Ubuntu Core image typing:

    wget http://people.canonical.com/~platform/snappy/havasu/uc-series16-beta-image/havasu-20161021070243.img.xz

Decompress the image and flash it onto the NUC:

  * Using the NUC emmc storage
    xzcat havasu-20161021070243.img.xz | sudo dd of=/dev/mmcblk0 bs=32M; sync

  * Using an SSD drive:
    xzcat havasu-20161021070243.img.xz | sudo dd of=/dev/sda bs=32M; sync 

You can now reboot your NUC, you will be prompted to remove the USB flash
drive, then it will boot using Ubuntu Core.





### 3. Ubuntu Core first boot

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

### Install Ubuntu Classic (server) on the Intel Nuc

Ubuntu Classic is Ubuntu as you know it, where you can use your favourite
development tools to create and run snaps.

  * 1. Create an installation media
  * 2. Install Ubuntu on the board
  * 3. Try the snap command





### Hardware and software requirements

  * an Intel® NUC

The NUC needs to have its BIOS updated to the latest version. For this, you
can follow [online instructions on the Intel
website](http://www.intel.com/content/www/us/en/support/boards-and-
kits/000005850.html).

  * an USB 2.0 or 3.0 flash drive
  * an [Ubuntu Server 16.04.1 LTS image](http://people.canonical.com/~platform/snappy/nuc/ubuntu-server-16.04.1-20160817-0.iso)
  * a monitor with an HDMI interface
  * a USB keyboard and a mouse
  * a network connection with Internet access





### 1. Create your installation media

During this step, you will create an Ubuntu Server Live USB flash drive.

Follow the instructions for the desktop OS you are using, with the Ubuntu
image you have downloaded previously:

  * [Using Ubuntu](http://www.ubuntu.com/download/desktop/create-a-usb-stick-on-ubuntu)
  * [Using Windows](http://www.ubuntu.com/download/desktop/create-a-usb-stick-on-windows)
  * [Using Mac OS X](http://www.ubuntu.com/download/desktop/create-a-usb-stick-on-mac-osx)





### 2. Install Ubuntu on the board

Booting the board from the flash drive will start the Ubuntu installer.

#### Preparing the NUC (if using internal ROM as disk)

This step is only necessary in case you want to install Ubuntu Core on the
emmc Built-In Storage. If you wired an SSD drive to your NUC, this section can
be skipped.

  1. Start your NUC by pressing the On button while pressing F2 during the boot up, this will open the BIOS settings
  2. On the initial screen, open the "Advanced" tab, then open the "Devices and Peripherals" tab
  3. On the "Devices and Peripherals" menu, under the "On board devices" submenu, make sure that the emmc checkbox ("4GB emmc Built-in Storage") is checked.  
If you didn't find this option, this means that you need to update your NUC
BIOS to latest version. For this, you can follow [online instructions on the
Intel website](http://www.intel.com/content/www/us/en/support/boards-and-
kits/000005850.html).

  4. In the "Boot" menu, "Secure boot" submenu, make sure that the "secure boot" is not checked.

#### Booting from the Live USB flash drive

  1. Insert the Live USB Ubuntu Server flash drive in the NUC
  2. Start the NUC and push F10 to enter the boot menu.
  3. Select the USB flash drive as a boot option
  4. The system will automatically execute the first stage of installation, including eMMC storage partitioning and image installation. After installation is complete, a prompt dialog will be shown and you will need to restart the system
  5. Boot the system on the eMMC storage and finish the install configuration
  6. Follow the instructions and enter appropriate options for language, WiFi, location (timezone), and keyboard layout
  7. Pick a hostname, user account and password
  8. Wait for the configuration to finish. If you connected to a WiFi network at step 4, it will take several minutes to download and apply additional updates. You can now reboot the system
  9. Ubuntu is installed. Use your account and password to log in





### 3. Try the snap command

You are all set up to get started with snaps. A good introduction is to follow
the [snaps usage guide](http://snapcraft.io/docs/core/usage).





