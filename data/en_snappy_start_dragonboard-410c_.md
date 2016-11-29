





## Getting started with a DragonBoard 410c

**From your Ubuntu desktop computer, you can download and flash a pre-built Ubuntu Core image on your DragonBoard 410c**

![](http://i.imgur.com/TtpfGKq.png)





### Prerequisites for booting Ubuntu Core

An Ubuntu SSO account is required to setup the first user on the board.

  1. Start by creating an [Ubuntu SSO account](https://login.ubuntu.com)
  2. Import an SSH Key into your Ubuntu SSO account [on this page](https://login.ubuntu.com/ssh-keys)

Instructions to generate an SSH Key can be found
[here](https://help.ubuntu.com/community/SSH/OpenSSH/Keys).

  3. You will need a keyboard, monitor or a serial cable plugged into the board to be able to go through the first boot process and complete device configuration.





## Hardware and software requirements

  * a DragonBoard 410c
  * an Ubuntu workstation running Ubuntu 14.04 (or later)
  * an [Ubuntu Core 16 image for DragonBoard 410c](http://cdimage.ubuntu.com/ubuntu-core/16/stable/ubuntu-core-16-dragonboard-410c.img.xz)
  * a microSD card
  * a monitor with an HDMI interface
  * an HDMI cable
  * a USB keyboard
  * an USB to RJ45 adaptor or a WiFi connection





## Installation Instructions

These instructions will drive you through getting Ubuntu Core running on your
DragonBoard 410c, using an Ubuntu desktop workstation.

  * 1. Create an installation media
  * 2. Ubuntu Core first boot





### 1. Create an installation media

During this step, you will flash Ubuntu Core on a microSD card from your
Ubuntu desktop workstation. Note that this step will erase and replace all the
content of the MicroSD card.

  1. Download the [Ubuntu Core 16 image for DragonBoard](http://cdimage.ubuntu.com/ubuntu-core/16/stable/ubuntu-core-16-dragonboard-410c.img.xz)
  2. Insert the microSD card into your workstation
  3. Make sure the MicroSD card unmounted by right clicking on the card icon in the left-hand launcher and choosing "Unmount"
  4. Locate the device address of your card by running the following command in a terminal: `lsblk`

It will give you a list of all plugged-in devices, the card is usually named
`mmcblk0`.

  5. To extract the image and flash Ubuntu Core on the card, run:
    xzcat ~/Downloads/ubuntu-core-16-dragonboard-410c.img.xz | sudo dd of=/dev/mmcblk0 bs=32M

  6. You can now extract the card from your computer





### 2. Ubuntu Core first boot

  1. Make sure the DragonBoard is unplugged from power 
  2. Set S6 switch to `0-1-0-0`, where 1 is the "SD boot" option
  3. Plug the monitor and keyboard to the board
  4. Insert the SDCard and plug the power adaptor into the board
  5. After the boot sequence, the device will display the prompt “Press enter to configure”
  6. Press enter then select “Start” to begin configuring your network and an administrator account. Follow the instructions on the screen, you will be asked to configure your network and enter your Ubuntu SSO credentials
  7. At the end of the process, you will see **your credentials to access your Ubuntu Core machine**:
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





