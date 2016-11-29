





## Pick your device

Ubuntu Core runs everywhere: on development boards, IoT devices, or even
locally. Where do you want to install it?

![](http://i.imgur.com/MtSazih.png)

Ubuntu Core allows you to install apps on your board in just a few clicks.

Get started on a

[Raspberry Pi 2 or 3 ›](/snappy/start/raspberry-pi-2)

![](http://i.imgur.com/NoshHIW.png)

Ubuntu Core lets you interact and control complex hardware and modules.

Get started on an

[Intel® Joule ›](/snappy/start/intel-joule)

![](http://i.imgur.com/Hd2gRBo.png)

Ubuntu Core helps you harness the power of boards tailored for the IoT
ecosystem.

Get started on a

[DragonBoard 410c ›](/snappy/start/dragonboard-410c)

![](http://i.imgur.com/wB6bD81.png)

Ubuntu Core can be easily installed on other architectures like Intel® 64
bits.

Get started on an

[Intel® NUC ›](/snappy/start/intel-nuc)

![](http://i.imgur.com/tZ619Fm.png)

Ubuntu Core runs smoothly on both small and large footprint boards.

Get started on a

[Samsung ARTIK 5 or 10 ›](/snappy/start/samsung-artik-iot-modules)

![](http://i.imgur.com/SYwbSCl.png)

Develop on target or on your Linux desktop, run Ubuntu Core in a virtual
environment.

Get started

locally with KVM ›

Ubuntu Core can also be installed on the PandaBoard, BeagleBone, Gumstix and
Odroid boards... [See all enabled devices ›](/snappy/start/gadget-snaps)





Back to top

### Launch Ubuntu Core locally with KVM on Linux

The current release of Ubuntu Core is available as a KVM virtual machine. On
Ubuntu, you can install KVM and verify that your hardware can run virtual
machines like this:

#### 1. Install KVM

Install the qemu-kvm package with the following command:

    sudo apt install qemu-kvm

Then, run the kvm-ok command to check KVM status and your hardware:

    kvm-ok
    INFO: /dev/kvm exists
    KVM acceleration can be used

This is the best outcome — it means that Ubuntu Core will run fast on your
system, taking advantage of hardware acceleration in your CPU.

#### 2. Download Ubuntu Core

Next, download the Ubuntu Core 16 compressed image and uncompress it:

    wget http://releases.ubuntu.com/ubuntu-core/16/ubuntu-core-16-amd64.img.xz
    unxz ubuntu-core-16-amd64.img.xz

You now have an image ready to boot.

#### 3. Setup your Ubuntu SSO account

An Ubuntu SSO account is required to setup the first user.

  1. Start by creating an [Ubuntu SSO account](https://login.ubuntu.com)
  2. Import an SSH Key into your Ubuntu SSO account [on this page](https://login.ubuntu.com/ssh-keys)

Instructions to generate an SSH Key can be found
[here](https://help.ubuntu.com/community/SSH/OpenSSH/Keys).

#### 4. First boot

You can now launch a virtual machine with KVM, using the following command:

    kvm -smp 2 -m 1500 -netdev user,id=mynet0,hostfwd=tcp::8022-:22,hostfwd=tcp::8090-:80 -device virtio-net-pci,netdev=mynet0 -drive file=ubuntu-core-16-amd64.img,format=raw

Note that this command also sets up port redirections:

  * **`localhost:8022`** is redirecting to port 22 of the virtual machine for accessing it through SSH
  * **`localhost:8090`** is redirecting to its port 80

You should now see a window, with your Ubuntu Core virtual machine booting
inside it.

  1. The system will display the prompt "Press enter to configure"
  2. Press enter, select “Start”, then follow the instructions on the screen: you will be asked to configure your network and enter your Ubuntu SSO credentials to create the administrator account
  3. At the end of the process, you will see **your credentials to access your Ubuntu Core machine**:
    This device is registered to <Ubuntu SSO email address>.
    Remote access was enabled via authentication with the SSO user <Ubuntu SSO user name>
    Public SSH keys were added to the device for remote access.

#### 5. Login

Once setup is done, you can login with SSH into Ubuntu Core using the
following command:

    ssh -p **8022** <Ubuntu SSO user name>@**localhost**

The user name is your Ubuntu SSO user name, it has been reminded to you at the
end of the account configuration step. You also need to specify port 8022 of
your localhost, as this is where we are redirecting port 22 of the virtual
machine.

##### First login tips

  * During setup,` console-conf` will download the SSH key registered with your Store account and configure it so you can log into the device via `ssh -p 8022 <Ubuntu SSO user name>@<device address>` without a password.
  * There is no default `ubuntu` user on these images, but you can run `sudo passwd <Ubuntu SSO user name>` to set a password in case you need a local console login.





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





