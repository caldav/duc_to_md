





#  [程序猿Ubuntu北京黑客松回忆录分享篇](/en/blog/2015/07/10/ubuntu/)

![程序猿Ubuntu北京黑客松回忆录分享篇](/static/devportal_uploaded/84036537-a507-4250-8e1c-8ce
961b8dda9-uploads/zinnia/Ubuntu设计-ol-01.jpg)

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
Scope，官方给出了一个框架并提供了各类API，可以快速的做出一个不错的
Scope，具体可以参见[这里](https://developer.ubuntu.com/en/scopes/) (友情提示:
网页底部有切换简体中文的链接)

二是 QML App，这也是真正意义上的 Native App 吧。使用 QML 语言进行开发，当然可以结合Qt使用C++对其做支持。

三是 HTML5 App，HTML5 应用，当下比较流行吧。因为今年的 HTML5
标准正式发布，和之前各种宣传，HTML5技术也多用于移动设备开发，最大的好处就是 write once, run everywhere 。

四是 Webapp，这个其实就没什么了，可以把现有的网站 url 打包成一个简单的入口 webapp。其实就是一个网站的快捷方式。

对于 Qt/QML，虽然很早也知道了解过，但从来没写过东西。那Qt是用的C++，好久没碰了。其实 QML 里面可以直接写 Javascript
也不用担心太多，真是万能的 Javascript 啊。那后来发现一些比较复杂不方便在QML里面做的事情，还有一些敏感的内容不能直接暴露在 QML
里面，那么就只能用 C++ 了，写了一段时间发现真的是生疏了。后来 Google 之发现有人说可以用 Golang，瞬间欣喜起来，自己学习过 Golang
也做过一些项目，而且也在期待 Google 将其用在 Android 开发上。然后就得知了 [go-qml](https://github.com/go-
qml/qml) 这个项目后，就开始深入使用 QML 结合 Golang 来做 GUI 应用。其实 go-qml 的作者也说了，这个库属于 alpha
阶段，而且确实从 v0 到 v1 的时候有些写法和API也确实变了，读了部分源码后发现源码里面一些 Comment 也标记了一些 TODO 和
疑问。所以就当实验性开发吧，不过现在用过来并没有发现很多问题，唯一比较麻烦的就是 Golang Type 到 QML Type 的转换上面有限制。

对于 Scope，第一感觉就像是 Android 里面的 Widget。后来慢慢啃文档也就慢慢理解了，Scope
主要的作用也就是作为一种对信息的聚合、展示、搜索等功能。Scope 可以聚合子 Scope 的信息，也可以对子 Scope 进行搜索。不过目前的 Scope
在功能性方面还是不是特别多，并且 Scope 里的 previewwidget 的功能目前也比较弱，使得很多想象力被限制了。所以 Joey Chan 和
校长 也都和我说 Scope 也就那样了，做 App 吧。So... Learn by doing...

### 疯狂一下吧

![](http://www.ubuntukylin.com/upload/images/hackathon.jpg)

7月4～5日，自从 Rex 那里知道有 Hackathon 以后这个日子已经期待很久了，终于来了～由于最近比较忙，4日凌晨1点才睡觉的，也没怎么准备早上7点
40起来，随便把电脑、各种线往书包里面塞，另外还带了我做了特殊处理出国网络比较快的 Raspberry Pi2～

9点多到了 Microsoft 大厦，后来回想起来倒是怪怪的，抱着装着 Ubuntu 的 MacbookPro 去了 Microsoft 大厦参加
Ubuntu Hackathon～呵呵～

一进会场～哇，有美女接待，一紧张忘记拍照了，后悔啊～～～然后默默地找自己的名字，然后弱弱地说我没有团队一个人来的 :) 。找到一个比较靠前的 8
号桌坐下来了。整理好东西，坐下等待安排了。瞬间发现0点钟方向坐着刘老师、11点钟方向坐着 Rex 和 Penk
。刘老师之前见过，Rex第一次见面，不过看见他一直拿着笔记本蹲跪在地上忙，就没过去打扰了。后来上前和刘老师打了声招呼然后聊了会儿之前我和他说用 Golang
的事情。

Rex 和 Penk 上台做简要介绍，Rex 介绍说已经有国内开发者在开发 Ubuntu Touch 平台的 App 了，出现了 Joey Chan 的
AesyWeibo，然后PPT上突然出现我之前做的 Youku Scope，嘿嘿～欣喜一下。然后 Rex 说 Youku Scope
是在场的一位开发者做的，问他在哪。我开始懵了一下然后站起来，只见 Penk 在那喊了一声，“原来就是你啊”。然后继续，今天的主题就是没有主题。Let's
start...

现场很多人是没有 Nexus4 或者其他可以运行 Ubuntu Touch
的手机，于是官方向每一桌提供开发机。哇，是刚才签到的妹纸来发～～只见快到我这桌了，好紧张，然后就看到她默默地走过去了，略过我这桌了，为什么？我很费解，此时
Penk 突然在我面前坐下了。好吧，妹纸走了，Penk大神来了～哈哈，都不用相互介绍我们就聊起来了，问我要做什么，我说还没想好，可能做个音乐相关的吧。Pen
k说要不要把Youku Scope 完善一下，也行...然后 coding...

为 Scope 添加 Account
功能之前还没看，这下顺便开一下，还请教了几次刘老师，遇到了挺多困难的。后来休息一下，想想，还是尝试做新的东西吧，这样在限时里完成才有挑战，那好，开启 QML
模式～ 之前就想在 Ubuntu Touch 做类似豆瓣FM的app，那好就定这个了～

![](http://ww1.sinaimg.cn/large/9ea22347gw1etr08aiogdj20u01hcjwh.jpg)

哈哈，晚饭居然可以自助选择盖饭和麻辣烫～ 吃饱喝足继续 Hack~ 不过每次红牛都被抢光了，都是结束的时候 Rex 分了我一灌，感谢～

Coding...

Coding...

Coding...

我算是坚持的比较晚的吧～4日晚上基本没睡，电脑里面一直循环着一些 Death Metal。邻座的一组貌似还是外地来参加的学生，他们也比较努力也都好多没睡，听
他们在讨论，发现年轻真好，比我在大学的时候强多了！PS：刘老师混进了同学们中，开始还在聊技术，后来还聊到大学生活，刘老师真能聊，哈哈～～

5日凌晨的时候还遇到了一个好玩的事情～调试了一个微博的接口，用到了上传图片，由于权限的问题，我只能上传整张图片，而不能给定url。这个接口调了我好久，就是为
了能有一个分享音乐的功能，后来去请教 Penk，Penk 也是一夜没有睡了佩服！向 Penk
说了一下后，他理解了我的思路也确定没问题，但怎么就不行了呢～调用微博的接口总报错不给通过，好吧，吐槽一下微博的文档好多细节没写好。见 Penk
也是一夜没睡，很累的样子，感谢听我瞎扯~ 后来自己想办法吧！快速用 Python
在本地做了个服务，直接发请求到本地，看看是不是自己的问题，瞬间条理就清晰了～哈哈～ Penk 给我当了一次小黄鸭～后来在厕所碰到 Penk，兴奋的和
Penk 说了我怎么解决的～ 回来后瞬间感觉又有能量了，直到坚持到7点后吃了 Joe 提供的早餐，我就小睡了一会儿～～～

Debug 到早上8点，基本要完成的都完成了。嘿嘿～豆瓣FM for Ubuntu Touch ! 还有一个离线播放的功能还没做完，因为目前没法精确判断
WiFi 和 移动数据 的状态，不过已经有人在 Launchpad 上提交 Bug 了。PS: 其实 Ubuntu Touch
现在就像一个小孩子，我也是慢慢看着它一点点的变化，要不是平时很忙，我恨不得仔细读读所有的源码，把一些我发现的 Bug 直接 fix
掉再提交。呵呵，我早晚会仔细研究其源码的。不过我还是贡献了挺多翻译的～

### 闪电秀

  * 尺子
  * Couple like
  * 优图
  * 斗地主
  * 日记本
  * 记忆词典
  * 路痴助手
  * uChat
  * rocket 拼图
  * LoLi team(mb)
  * 撞脸
  * 小飞机
  * 需求交互
  * 豆瓣FM for Ubuntu touch

上面的就是小伙伴们30个小时的奋战成果！值得一提的是其中有些朋友是刚开始学习开发，尺子的作者他就提到他也是学习 C++/Qt
不久，但我觉得尺子这个作品很实用的。

Couple Like 是一对搭档完成的，嘿嘿，这个创意不错，是一款通过图像人脸识别辨别其年龄以及两个人的匹配程度的应用。最强的是演示时候用的 Demo
图片。

斗地主、日记本等那些，原来大家都是qt高手啊，都在 Ubuntu 平台上实现了很好玩的应用。希望早日在 Ubuntu Touch 见到。

值得一提的是 LoLi team 他们在用 Js 在 Ubuntu Touch 上实现了 LoLi 的解析器，LoLi 是他们自己发明的一个 Lisp
的方言，纯技术层面来说，这个很牛啊～佩服佩服～而且让我感觉到年轻真好～～要哭了

uChat 一款基于 LBS 的社交应用，是一组在校的同学做的，他们做的演示和理念都不错，我以前也想过一个类似的应用～

轮到我的 豆瓣FM for Ubuntu Touch
登场了～哈哈～可能一晚上没睡，感觉自己演讲的不好吧～随便整理了一个[slide](https://slides.com/dawndiy/douban-
fm), 这个 [slide](https://slides.com/dawndiy/douban-fm)
也是开源的哦，大家可以folk，里面有一些有用的资料。借用 Rex 的电脑简单的把 slide
讲了一遍，还是那句话，因为我喜欢音乐，所以我做了相关的应用，这样真的很开心。然后就是演示了，点击应用播放的刚好是 自然卷 的单曲《坐在巷口的那对男女》，大家
都挺熟悉的，当我把话筒对着手机的扬声器时，大家听见音乐都鼓起掌了。谢谢大家喜欢，然后介绍了一些必要的功能(后来发现其实我好多忘记演示了)，然后...然后就没
有然后了... No～还有 One More Thing... 大家听到还有"One more thing"的时候有惊奇起来。为了纪念这次活动，我在
豆瓣FM for Ubuntu Touch 中制作了一个彩蛋，嘿嘿，只有特殊的方式才能进去的哦～大家看到后都哈哈大笑起来。待我把它完善好后，大家自己去发现吧
:)

### 后话

![](http://ww3.sinaimg.cn/large/4c3236c5gw1ettdoqn4tlj21kw11ogqu.jpg)第一次参加
Hackathon，感觉很充实，也认识了很多朋友。最好的感受就是和一群兴趣相投的朋友做自己爱做的事情真好～最后就是回家睡个天昏地暗～

小站最近改版，好久没写博文了，突然发现码了好多字啊～不行，我得睡觉了～88

[April Wang](/en/blog/authors/aprilswang/)

July 10, 2015

Filed under: [Hackathon](/en/blog/tags/Hackathon/) [Ubuntu phone
hackathon](/en/blog/tags/Ubuntu%20phone%20hackathon/)
[黑客松](/en/blog/tags/%E9%BB%91%E5%AE%A2%E6%9D%BE/)





## Comments

No comments yet.

## Add your comment

Name:

Email address:

URL:

Comment:

If you enter anything in this field your comment will be treated as spam:





