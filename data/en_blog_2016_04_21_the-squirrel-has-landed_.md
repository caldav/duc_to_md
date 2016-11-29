





#  [The squirrel has landed!](/en/blog/2016/04/21/the-squirrel-has-landed/)

Today, we are proud to bring you our 6th Long Term Support release: **Ubuntu
16.04 LTS**. It is the sum of the work of thousands of people collaborating
all over the world, working tirelessly for the last six months and we'd like
to share a few highlights.

![Ubuntu 16.04 LTS is here!](http://i.imgur.com/R47hOnz.png)

## Software distribution

You have probably already heard about this: we are bringing a new package
format for you to start distributing your apps. It's called snap and it allows
you to deliver software to users without going through the traditional Ubuntu
archive inclusion process. Whether you are making a game, an utility or [_the
next Firefox_](https://blog.mozilla.org/futurereleases/2016/04/21/firefox-
default-browser-for-linux-users-ubuntu-new-snap-format-coming-soon), it will
enable you to continuously bring the latest version to users. And it’s easy!
–it will mostly involve adding [_a single declarative file to your source
tree_](https://developer.ubuntu.com/en/desktop/).

## Ubuntu Core and Snapcraft

Snappy Ubuntu Core is the future of Ubuntu, it is built around the snap
packaging format and is a brand new world if you are used to classic Ubuntu.
Transactional updates, confined apps, smaller and very modular, it’s the
Ubuntu for all devices and form factors: your ARM board, your router, your
drone, your laptop… your imagination is the limit.

Version 2.0 has just been released, and we’ve collected the highlights from
the development team to get you started:

  * [_Snappy Ubuntu Core 2.0 is OUT_](http://blog.labix.org/2016/04/16/snappy-ubuntu-core-2-0-is-out)

  * [_Snappy changes_](http://blog.labix.org/2016/04/20/snappy-changes)

  * [_Snappy, snapcraft and interfaces_](http://www.zygoon.pl/2016/04/snappy-snapcraft-and-interfaces.html)

  * [_Snappy interfaces, plugs, slots and connections_](http://www.zygoon.pl/2016/04/snappy-interfaces-plugs-slots-connections.html)

This is important for app developers in a multitude of ways. Snappy Ubuntu
Core incorporates a lot of the feedback of third party app developers, ISVs
and upstream projects we have been getting over the years. What all of them
wanted in a nutshell was: a solid Ubuntu base, a lot of flexibility in
handling their app and the relevant stack, being mostly independent from
distro freezes, dead-simple packaging, bullet-proof upgrades and rollbacks,
and an app store model established with the rise of the smartphones. Snappy
Ubuntu Core is exactly that and more. What it also brings to Ubuntu is a clear
isolation between apps and a universal trust model.

We have been working with the Engineering teams extensively and assisted them
in testing the software, making sure that things worked, writing
documentation, putting together examples and bootstrapping an initial
community.

What we have today is just the start. There are still a number of details to
be figured out, which will all land in Ubuntu through SRUs and Ubuntu Core
updates.

## Phone and Tablet

We have [_a tablet that converges into a
desktop_](http://www.ubuntu.com/tablet) when a bluetooth mouse is detected! It
ships some desktop apps by default such as Firefox and LibreOffice and of
course, Ubuntu SDK apps. This is an exciting moment for everyone involved as
it’s a milestone on the road to full devices convergence: many form factors
and architectures, one codebase.

We have released the latest and greatest phone over-the-air update: OTA 10 a
few days ago, which - as usual - brings new features and bug fixes, such as:

  * Re-designed Out Of the Box Experience

  * VPN support

  * Easy switching to desktop mode

  * New colour palette

  * New default apps: uNav, Dekko, Calendar

For more, see the [_release
notes_](https://wiki.ubuntu.com/Touch/ReleaseNotes/OTA-10).

Here is what to look forward to [_in OTA 11_](https://launchpad.net/canonical-
devices-system-image/+milestone/11) and of course, the Ubuntu SDK roadmap for
the next 6 months: [_speed and more
convergence_](https://developer.ubuntu.com/en/blog/2016/03/16/planning-the-
sdk-16-10/).

### Community phone ports

Our porting community of volunteers, lead by the indefatigable Marius
Gripsgard has been extending the range of devices where Ubuntu can be
installed.

Along with the OnePlus One port, a Fairphone 2 port, with great help and
support from the Fairphone Engineering team, is on the way. The
[_ubports_](https://ubports.com/) site and the [_Porting
Guide_](http://developer.ubuntu.com/en/start/ubuntu-for-devices/porting-new-
device/) have all the information on status, how to get started and contribute
to new or existing ports.

## Developer portal

The [_Developer Portal_](https://developer.ubuntu.com/) is _the_ place to get
started with developing apps for Ubuntu, no matter if your primary interest is
the phone, IoT devices or Ubuntu in general. Thus we have been supporting the
various Engineering and product teams to bring together all app development
resources and present them in a coherent and digestible way.

One important update was reflecting the changes in products and priorities. We
wanted to make it clearer that the primary choice on the site is the one
concerning products. An overview of the related changes (both implemented and
planned) can be seen [_here_](https://coggle.it/diagram/Vv0bMp2DmQlVtZWL).

A lot of work was put into importing already existing documentation. Both in
terms of guides written by Engineering teams, but API docs as well. As usual
in a diverse organisation as Ubuntu they come in various forms and we had to
adapt to bring them onto the site without confusing our users. From now on it
will be easier to import more API docs from more packages from various
frameworks at the same time.

One of the great features of the developer site is that it will allow us to
get the imported guides translated as well. This is useful for the docs
imported from our Markdown importer, e.g.
[_snappy_](https://github.com/ubuntu-core/snappy/tree/master/docs) and
[_snapcraft_](https://github.com/ubuntu-core/snapcraft/tree/master/docs). Here
we almost exclusively rely on the great work of the Engineering teams and work
in conjunction with them. The Marketing team has been contributing some more
docs recently, which will land on the site very soon. On the snappy side of
things, we also automatically import [_available gadget
snaps_](https://developer.ubuntu.com/snappy/start/gadget-snaps) from the
store.

With the amount of information growing and growing, we are looking for ways to
provide more clarity next cycle. We would like to make the versioning of
documentation more obvious and improve the navigation. Luckily we are not
alone in this quest, but are working on this together with the [_Design and
Web teams_](http://design.canonical.com/2016/04/redesigning-ubuntu-coms-
navigation/). And lastly we are looking to landing a new blog engine soon,
which is [_being tested_](https://code.launchpad.net/~dholbach/ubucon-
site/newsblog/+merge/290402) on the [_Ubucon Site_](http://ubucon.org/en/)
right now.

## Community and planning

The next edition of the [_Ubuntu Online Summit _](http://summit.ubuntu.com/)is
also coming in 2 weeks –3rd to 5th May. It is an excellent opportunity to meet
other community members, plan together the next cycle and learn and provide
feedback on the roadmaps of the Engineering teams. We hope to see you there.

We’d like to thank everyone who has helped put together yet again our best
release so far: from documenters, to translators, to forum and Ask Ubuntu
moderators, IRC operators, advocates, bug triagers, testers, app developers,
packagers, artists and more…. here’s to you: [happy Ubuntu
16.04!](http://ubuntu.com)

[Community Team](/en/blog/authors/Community-Team/)

April 21, 2016

Filed under: [Ubuntu OS](/en/blog/tags/Ubuntu%20OS/) [planet-
ubuntu](/en/blog/tags/planet-ubuntu/)





## Comments

No comments yet.

## Add your comment

Name:

Email address:

URL:

Comment:

If you enter anything in this field your comment will be treated as spam:





