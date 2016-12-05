





# Tag archives: 数据隐私





#  [博文转发之-清理Scope Settings](/en/blog/2015/06/26/-scope-setting/)

Pawel Stolowski于2015年6月11日发布一篇名为“Cleaning up scopes
settings”的博文，我们在这里简单翻译转发和大家分享一下。

Unity 7（在当前桌面上提供Ubuntu shell和默认UX体验）和Unity
8（支持手机且很快将支持融合桌面）在数据源可见性方面存在很大程度的差异。未来Unity
8版本将废弃过去遗产的隐私标记，会更偏向于一种更加清晰的方式，让用户自己决定将数据发送到哪里。

## Unity 7中的Scope搜索并保存隐私

![](/static/devportal_uploaded/d33b6bd2-826e-48ea-a0c0-88b796a97a7c-7aab8d61-16fe-4976-9b3a-bffbf3938d24-media/2015/06/26/guhgsgq.png)

在默认情况下，在Unity 7中使用常规Dash搜索时，它将首先联络Canonical的智能Scope服务器，该服务器会推荐适合搜索关键词的最好或最相关的S
cope。然后，下一步是在这些Scope中筛选查询到实际结果，然后呈现出来。

但是，这种方法意味着用户事先并不一定知道自己的搜索内容有向哪些Scope提出查询，而且搜索关键词会被发送到智能Scope的服务器。虽然发送至服务器的数据是匿
名的，我们了解到仍有一些用户担心数据隐私问题。正是出于这个原因，我们推出了隐私标记：一个阻止访问智能Scope服务器的Scope设置。

## Unity 8中的Scope搜索

![](/static/devportal_uploaded/e7048b72-48e8-4732-b2eb-3fbe0da9b8c7-625dcb44-c67c-4c48-add2-fcbd9b58aab4-media/2015/06/26/vjqjzff.png)

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
[scope](/en/blog/tags/scope/) [unity 7](/en/blog/tags/unity%207/) [unity8](/en/blog/tags/unity%208/)
[数据隐私](/en/blog/tags/%E6%95%B0%E6%8D%AE%E9%9A%90%E7%A7%81/)





