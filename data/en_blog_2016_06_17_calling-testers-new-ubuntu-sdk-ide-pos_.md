





#  [新的Ubuntu SDK IDE开放测试](/en/blog/2016/06/17/calling-testers-new-ubuntu-sdk-
ide-pos/)

## Ubuntu SDK IDE 的下一个迭代

### 简单来说︰LXD 来了

经过一段漫长的开发过程，我们很高兴地宣布，Ubuntu SDK IDE 的下一个版本从今天起进入 Beta 测试阶段。新版本包含全新的构建器
(Builder) 和运行时后端，最终消除了 SDK IDE 目前存在的最大问题。

之前已经有传闻说基于 [LXD](http://www.ubuntu.com/cloud/lxd) 的新构建器将会取代基于 schroot
的构建器。没错，这些传闻都是真的。在几位值得信赖的测试人员对概念验证版本进行了一段时间的内部测试后，我们认为向更多人展示新版本 IDE 的时机已经到来。

下面，在直接介绍新软件包前，我们先来回顾一下不得不放弃 schroot 构建器的一些原因：

最大的问题无疑在于安装 SDK 后立即创建新的 chroot。从实时档案文件启动引导 (Bootstrapping) 完整的 Ubuntu
根文件系统非常缓慢，而且容易出错。每当档案文件或 Overlay PPA 存在打包问题时，就无法创建新的构建目标。这基本上导致 SDK
在打包问题修复前将一直不可用。LXD
已经解决了这个问题。新容器以现成可用的压缩映像文件形式下载，下载速度比以往快得多，而且得到的容器肯定可用，因为容器在发布前已经过我们的测试，而不是像
Overlay PPA 那样不断改变。映像下载完毕后将被缓存，而从缓存启动一个新容器只需要几秒钟！

第二个要强调的问题是，我们需要在桌面本地执行应用程序，但仍支持目前官方支持的所有 Ubuntu 版本。这意味着必须解决不同 Qt 和 UITK
版本的问题。我们曾经尝试过通过提供单独的 Qt+UITK 软件包来解决这个问题。但事实证明，这种方法需要破解和重构太多的软件包，因此是不可行的。而且，这不仅
仅是构建时的问题，还是一个运行时的问题。那么如何既能在桌面上运行应用，使用最新、最流行的组件，同时又能保持 LTS 兼容性呢？

答案其实很简单：使用容器作为运行时目标，并在主机的 X 服务器上显示 UI。

此外还有一些问题，例如整体速度缓慢、挂载点泄漏（每个曾经因 schroot 而设置了数百个挂载的人都能明白我的意思）以及 ecryptfs 的问题等。

现在说够了过去，我们来聊聊将来，看看新版本有了哪些变化。在开始前需要指出的是，我们已经停止了对默认桌面套件的支持。默认已不再支持在主机上构建和运行应用。除了
qmake 和 cmake 插件自动创建的配置以外，SDK IDE 不会创建其他桌面运行配置。当然，我们还是有办法在主机上构建和运用应用的，但是需要手动创建
运行配置。今后，我们需要创建一个与主机架构一致的容器来执行应用程序。这意味着，在主机系统上，几乎不需要使用额外的软件包作为依赖项。

IDE 将不再使用任何现有的基于 schroot 的构建器。click chroot 仍然留在主机上，但是将与 Ubuntu SDK IDE 分离。

## 开始

做法很简单，我们只需添加 SDK 发行版和适用于 Ubuntu SDK 工具的 Tools Development PPA：

`sudo add-apt-repository ppa:ubuntu-sdk-team/tools-development`

`sudo apt update && sudo apt install ubuntu-sdk-ide`

`![](http://people.canonical.com/~bzoltan/blog-decoration/sdk-ppa-added-ide-
installed-bigger.png)`完成上面的操作后，IDE 现在完全可用。它会按照过去使用 click chroot
时相同的方式来发现容器。从各个方面看，开发者的体验并不会有太大变化。需要注意的是，目前我们还在 Beta 测试阶段，因此容器映像或 IDE
本身很有可能存在一些 Bug。请直接在 IRC 上或通过邮件列表向我们报告 Bug，更好的方式是通过 launchpad 中的官方 ubuntu-sdk-
ide 项目来报告 Bug：[https://bugs.launchpad.net/ubuntu-sdk-
ide](https://bugs.launchpad.net/ubuntu-sdk-ide)

## 已知问题和故障排除

### **lxd 组成员资格**

通常，LXD 安装进程会配置必要的组成员资格。但如果该进程未配置成员资格，我们就需要确保当前用户属于 lxd 组。请发出以下命令：

`sudo useradd -G lxd `whoami``

之后，重新登录将新组通知给登录会话。

### **重置 QtCreator 设置**

有时，在不同版本间来回切换时，QtCreator（Ubuntu SDK IDE 的 Qt
应用程序）的设置会发生损坏。当发现已损坏或无法使用的套件、配置上可能有误的设备或者任何不寻常的问题时，按下 Qtcreator
上的重置按钮可能会有帮助。注意，这是一种相当激进的修复方法。操作上很简单，只需执行下面这条命令即可：

`$ rm ~/.config/QtProject/qtcreator ~/.config/QtProject/QtC*`

### **清理旧的 click chroot**

前面提到，旧的 schroot 已与 SDK IDE 分离，但是仍留在文件系统中。使用以下命令可清理 click chroot：

`$ sudo click chroot -a armhf -f ubuntu-sdk-15.04 destroy`

`$ sudo click chroot -a i386 -f ubuntu-sdk-15.04 destroy`

这两个命令将释放大约 1.4GB 的磁盘空间。click chroot 位于 /var/lib/schroot/chroots
下。最好检查一下该文件夹是否为空，并且没有挂载任何内容。

`$ mount|grep schroot`

### **NVIDIA 显卡驱动程序**

在使用 NVIDIA 显卡驱动程序的主机上，无法从 LXD 容器本地部署应用。如果主机具有双图形处理器，一种变通的方法是使用另一个图形处理器。

检查系统是否具有备用显卡

`$ sudo lshw -class display`

如果列表显示除 NVIDIA 以外的其他条目，则激活另一个显卡。prime-select 工具是一个简单易用的工具。

`$ sudo prime-select intel`

注意，你的系统上可能未安装这个工具，而且它不能与 bumblebee 一起使用。如果主机已安装 bumblebee 且缺少 prime-select 工具：

`$ sudo apt-get remove bumblebee`

`$ sudo apt-get install nvidia-prime`

如果主机除 NVIDIA 以外没有其他显卡，可以尝试 Nouveau
驱动程序，该驱动程序也许能用。不管怎样，这是一个非常严重的已知问题，我们目前正在着手解决。

## 启动新的 IDE

首先备份一些设置，以防在极少数情况下我们需要恢复回当前的 IDE。

`$ tar zcvf ~/Qtproject.tar.gz ~/.config/QtProject`

然后，在 Dash 中找到 Ubuntu SDK IDE 并启动它。

![](http://people.canonical.com/~bzoltan/blog-decoration/sdk-start-ide-from-
dash.png)

Ubuntu SDK IDE 首先会检查环境是否已正确设置。除非你是 LXC/LXD 超级用户，否则安全的做法是选择此对话框中的“Yes（是）”。

![](http://people.canonical.com/~bzoltan/blog-decoration/sdk-fixing.png)

如果 Ubuntu SDK 是第一次启动，会打开一个欢迎向导帮助你设置套件和设备。

![](http://people.canonical.com/~bzoltan/blog-decoration/sdk-
welcome-1.png)接下来，最好的建议是阅读向导的每个页面，并按照上面的说明操作。整个过程相当简单。

在下一页上，向导将帮助你创建套件。

![](http://people.canonical.com/~bzoltan/blog-decoration/sdk-
welcome-2.png)按下“Create new Kit（创建新套件）”按钮，查看目标创建对话框。

![](http://people.canonical.com/~bzoltan/blog-decoration/sdk-welcome-target-
creation.png)

在这一步中，可以在 3 种类型的目标间进行选择︰

  * Build to run on the desktop（构建以便在桌面上运行）- 筛选出所有与桌面兼容的映像
  * Build to run on device or emulator（构建以便在设备或模拟器上运行）- 筛选出所有可用于设备的映像
  * Show all available images（显示所有可用的映像）- 显示所有可用映像

我们选择“Show all available images”，查看所有现有映像的概览。

下一步，选择首选的目标架构。Ubuntu 手机和平板电脑是 armhf，主机 PC 是 i386 或 amd64。因此，要创建适用于手机的 click
包，需要 armhf 目标；要在桌面上测试应用程序，需要原生的 amd64 或 i386 目标。

![](http://people.canonical.com/~bzoltan/blog-decoration/sdk-welcome-select-
image.png)我们可以为套件使用默认命名。

![](http://people.canonical.com/~bzoltan/blog-decoration/sdk-welcome-create-
target-name.png)

创建 LXD 容器需要系统管理员权限，所以下面我们需要验证自己的身份。

![](http://people.canonical.com/~bzoltan/blog-decoration/sdk-welcome-
authentication.png)

输入正确的密码后，LXD 映像下载将开始。

![](http://people.canonical.com/~bzoltan/blog-decoration/sdk-welcome-create-
target-progress.png)

下载需要些时间，具体取决于网络的带宽。每个映像大约为 400MB。在向导下载和配置 LXD 映像期间，我们刚好有足够时间来看一篇简短的博客文章，了解一下到底
什么是套件：[你想了解却又羞于发问的关于套件的一切](https://developer.ubuntu.com/en/blog/2015/03/18/eve
rything-you-always-wanted-know-about-kits-were-afraid-ask/)
。毫不夸张地说，花时间阅读这篇博客文章并了解开发套件是什么，是最佳的选择。

容器创建完毕后，会弹出一个简单的对话框显示一些基本详情。

![](http://people.canonical.com/~bzoltan/blog-decoration/sdk-welcome-armhf-
target-created.png)向导的下一页将帮助你设置目标设备。在我们的例子中，我们已经有了一个 BQ (krillin) 手机和一个来自 rc-
proposed 通道的模拟器。

![](http://people.canonical.com/~bzoltan/blog-decoration/sdk-welcome-
devices.png)但是，即使没有可用的手机、平板电脑或模拟器设备，结束向导肯定也是安全的。

在这个阶段，IDE 将自动发现 LXD 容器，并提示我们可以更新它。

![](http://people.canonical.com/~bzoltan/blog-decoration/sdk-start-update-kit-
dialog.png)

这并不是一个必须要做的步骤，取消该对话框完全没有问题。

完成该向导后，IDE 将打开。

![](http://people.canonical.com/~bzoltan/blog-decoration/sdk-ide-started.png)

[liam zheng](/en/blog/authors/tmacyunn1/)

June 17, 2016

Filed under: [Scope](/en/blog/tags/Scope/) [Ubuntu
Phone](/en/blog/tags/Ubuntu%20Phone/) [ubuntu-sdk](/en/blog/tags/ubuntu-sdk/)





## Comments

No comments yet.

## Add your comment

Name:

Email address:

URL:

Comment:

If you enter anything in this field your comment will be treated as spam:





