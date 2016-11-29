





# Author archives: April Wang





#  [程序猿Ubuntu北京黑客松回忆录分享篇](/en/blog/2015/07/10/ubuntu/)

[ ![程序猿Ubuntu北京黑客松回忆录分享篇](/static/devportal_uploaded/84036537-a507-4250-8e1c-8
ce961b8dda9-uploads/zinnia/Ubuntu设计-ol-01.jpg) ](/en/blog/2015/07/10/ubuntu/)

2015年7月4-5日，我们聚集北京一起经历了Ubuntu手机在中国的首场黑客松。[@DawnDIY](http://weibo.com/dawndiy)最
近发布了一篇细心记录下的活动回忆录， 在这里和大家分享。

### **[Ubuntu Hackathon](http://dawndiy.com/2015/07/08/ubuntu-
hackathon.html)**

2015年07月08日 DawnDIY

* * *

### 前言

很早就知道["黑客松"(Hackathon)](https://zh.wikipedia.org/wiki/%E9%BB%91%E5%AE%A2%E6%9D
%BE)，也关注过一些国内的 Hackathon 活动，只是一直都没有去尝试参与过。以前是没有美工前端，所以自己变成了个野生渣前端。最近很长时间都在关注
Ubuntu Touch 的进度，得知有在北京举办 Hackathon 活动，也就迅数报名了。好吧，我的第一次 Hackathon 献给 Ubuntu 了。

### 准备

当然这次 Ubuntu Hackathon 是为 Ubuntu Touch 开发应用。Ubuntu Touch 上的开发基本分三类。

一是 Scope，Scope 目前在中文也没有很合适的翻译，官方也没有给出中文名称我们都以 Scope 来叫它就好了。开发
Scope，官方给出了一个框架并提供了各类API，可以快速的做出一个不错的 ...

[Continue reading](/en/blog/2015/07/10/ubuntu/)

[April Wang](/en/blog/authors/aprilswang/)

July 10, 2015

Filed under: [Hackathon](/en/blog/tags/Hackathon/) [Ubuntu phone
hackathon](/en/blog/tags/Ubuntu%20phone%20hackathon/)
[黑客松](/en/blog/tags/%E9%BB%91%E5%AE%A2%E6%9D%BE/)

#  [博文转发之-清理Scope Settings](/en/blog/2015/06/26/-scope-setting/)

Pawel Stolowski于2015年6月11日发布一篇名为“Cleaning up scopes
settings”的博文，我们在这里简单翻译转发和大家分享一下。

Unity 7（在当前桌面上提供Ubuntu shell和默认UX体验）和Unity
8（支持手机且很快将支持融合桌面）在数据源可见性方面存在很大程度的差异。未来Unity
8版本将废弃过去遗产的隐私标记，会更偏向于一种更加清晰的方式，让用户自己决定将数据发送到哪里。

## Unity 7中的Scope搜索并保存隐私

![](/static/devportal_uploaded/d33b6bd2-826e-48ea-a0c0-88b796a97a7c-7aab8d61-1
6fe-4976-9b3a-bffbf3938d24-media/2015/06/26/guhgsgq.png)

在默认情况下，在Unity 7中使用常规Dash搜索时，它将首先联络Canonical的智能Scope服务器，该服务器会推荐适合搜索关键词的最好或最相关的S
cope。然后，下一步是在这些Scope中筛选查询到实际结果，然后呈现出来。

但是，这种方法意味着用户事先并不一定知道自己的搜索内容有向哪些Scope提出查询，而且搜索关键词会被发送到智能Scope的服务器。虽然发送至服务器的数据是匿
名的，我们了解到仍有一些用户担心数据隐私问题。正是出于这个原因，我们推出了隐私标记：一个阻止访问智能Scope服务器的Scope设置。

## Unity 8中的Scope搜索

![](/static/devportal_uploaded/e7048b72-48e8-4732-b2eb-3fbe0da9b8c7-625dcb44-c
67c-4c48-add2-fcbd9b58aab4-media/2015/06/26/vjqjzff.png)

Unity 8中的Scope体系结构截然不同：整个搜索过程不会涉及到智能Scope服务器。

相反，每次的搜索查询仅被发送到目前正在使用的Scope（即当前可见的Scope）中，因此用户始终知道他们的搜索数据的都会被发送到哪里。

如果是在使用一个聚合类Scope的情况下，
其中聚合了不同数据来源的子Scope，它的设置页面内会列出所有聚合了的子Scope。用户可以选择自行设置禁用每个单独子Scope的数据源。

## Unity 8废弃了过去遗留的隐私标记

由于在Unity 8中进行内容搜索查询时 ...

[Continue reading](/en/blog/2015/06/26/-scope-setting/)

[April Wang](/en/blog/authors/aprilswang/)

June 26, 2015

Filed under: [Scope设置](/en/blog/tags/Scope%E8%AE%BE%E7%BD%AE/)
[scope](/en/blog/tags/scope/) [unity 7](/en/blog/tags/unity%207/) [unity
8](/en/blog/tags/unity%208/)
[数据隐私](/en/blog/tags/%E6%95%B0%E6%8D%AE%E9%9A%90%E7%A7%81/)

#  [最新款Ubuntu手机现已开卖](/en/blog/2015/06/10/ubuntubqe5/)

[ ![最新款Ubuntu手机现已开卖](/static/devportal_uploaded/54d86b37-cea0-4179-b7f6-c6bc58
b5b885-uploads/zinnia/ubuntu-phone-scopes.jpeg)
](/en/blog/2015/06/10/ubuntubqe5/)

上周西班牙手机厂商BQ和Canonical再次联和发布又一新款Ubuntu手机 - BQ Aquaris E5 Ubuntu版本。
这也是BQ厂商发布的第二款Ubuntu手机， 这一次带来了更大的屏幕和更加强悍的摄像头硬件， 还有增强的电池容量，让这款手机待机更久。

2015年6月9日，英国时间， 这款最新Ubuntu手机正式开卖。 售价199.9欧元（约1399.31元人民币）， 比之前的BQ Aquarius
E4.5 Ubuntu版本手机贵了约30美金（约190元人民币）。 我们来看一下， 这款最新Ubuntu家族的成员到底新意何处。

Aquaris E5的硬件配置：

这款E5 Ubuntu手机只有一个颜色 - 黑色， 内存16GB

硬件配置来说， E5其实和前一款Ubuntu E4.5区别不大， 同样使用联发科技的四核处理器，搭配1GB的RAM。

最大的硬件提升是来自E5相机的。 E5机身前置和后置的相机都装配了BSI感应器和Largan镜片。
后置相机拍摄的照片像素可达1300万像素，而前置相机可达5百万像素。

另外E5还带有一个MSD卡片插槽， 可以将总内存增加到32GB。

目前这款BQ E5的Ubuntu手机仅限欧洲售卖，而且将会在6月22日开始发货。

此外Ubuntu酝酿很久的融汇Convergence口袋PC手机也在积极开发中。 让你的手机直接插上一个显示频， 键盘和鼠标就能当做PC来使用的话，
想想就很让人鸡冻\(≧▽≦)/！

[April Wang](/en/blog/authors/aprilswang/)

June 10, 2015

Filed under: [BQ E5](/en/blog/tags/BQ%20E5/)
[Convergence](/en/blog/tags/Convergence/) [Ubuntu](/en/blog/tags/Ubuntu/)
[口袋PC](/en/blog/tags/%E5%8F%A3%E8%A2%8BPC/)
[手机](/en/blog/tags/%E6%89%8B%E6%9C%BA/)
[融汇](/en/blog/tags/%E8%9E%8D%E6%B1%87/)

#  [“尖牙利齿”的Ubuntu 15.10 - Wily Werewolf](/en/blog/2015/05/05/jianyalichi-
ubuntu-1510-wily-werewolf/)

[ ![“尖牙利齿”的Ubuntu 15.10 - Wily Werewolf](/static/devportal_uploaded/e936dd25-f
715-4946-bd98-7841f46d2772-uploads/zinnia/Ubuntu_Wily_Werewolf.jpeg)
](/en/blog/2015/05/05/jianyalichi-ubuntu-1510-wily-werewolf/)

Mark Shuttleworth昨晚揭晓了Ubuntu 15.10 的版本代号 Wily Werewolf。Wily在英文中一般用于描述易于适应环境锐敏足
智的角色人物，而Werewolf则是传说中的一种神秘物种，小说中常常以人形出现但会在满月之日变成狼性的狼人

Ubuntu 15.10 将会在今年10月份发布，而它的代码名也是至今为止Ubuntu版本名中第二个被重复的字母
（另外一组曾被重复使用的字母为H，相关版本名分别为Hardy Heron和Hoary Hedgehog）

为了昨晚有错过直播的筒子们另外再献上 ， Mark现场的几段精彩keynote,致即将到来的Pocket PC！

“We [the Linux desktop] were always five, ten years behind. Always copying the
other guy. Here, for the first time, we have this vision at the same time,” he
said.

“It ...

[Continue reading](/en/blog/2015/05/05/jianyalichi-ubuntu-1510-wily-werewolf/)

[April Wang](/en/blog/authors/aprilswang/)

May 5, 2015

Filed under: [Wily Werewolf](/en/blog/tags/Wily%20Werewolf/) [ubuntu
15.10](/en/blog/tags/ubuntu%2015.10/)
[手机开发](/en/blog/tags/%E6%89%8B%E6%9C%BA%E5%BC%80%E5%8F%91/)








