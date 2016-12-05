





#  [Snappy Playpen Kickoff Highlights](/en/blog/2016/06/08/snappy-playpen-kickoff-highlights/)

We [announced the SnappyPlaypen](https://developer.ubuntu.com/en/blog/2016/06/03/announcing-snappy-playpen/) a few days ago and yesterday was the Kickoff event where we
basically invited everyone who was interested, brought in a lot of snapd and
snapcraft experts and started snapping software together.

It was simply beautiful to see the level of excitement, the collaboration, how
people got to know each other and how much stuff got done. Big hugs to
everyone involved - great work!

![People](https://daniel.holba.ch/blog/wp-content/plugins/2016/06/people.png)

Along with the usual #snappy IRC channel on Freenode, we used
[gitter.im](https://gitter.im/ubuntu/snappy-playpen) as an experiment and it
worked out well. We had at least 40 people participating there (many more on
IRC and the mailing list), 850 messages in gitter alone and even after 24
hours we're still working our way through some software to go into the Playpen
repository.

**Without further ado, here's what already landed in the Snappy Playpen since yesterday:**

Landed in the playpen:

  * [Add leafpad](https://github.com/ubuntu/snappy-playpen/pull/33) by Daniel Holbach
  * [Fix VLC](https://github.com/ubuntu/snappy-playpen/pull/34) by David Callé
  * [SMPlayer](https://github.com/ubuntu/snappy-playpen/pull/36) by David Callé
  * [Galculator](https://github.com/ubuntu/snappy-playpen/pull/37) by Martin Wimpress

Another beautiful thing which landed is Vincent Jobard's French [videotutorial about Snapcraft](https://www.youtube.com/watch?v=xR5avbskSdQ) just in
time to celebrate the kickoff.

We have many great things which are still work in progress:

  * [Heroku CLI](https://github.com/ubuntu/snappy-playpen/pull/40) by Leo Arias
  * [Gimp from git](https://github.com/ubuntu/snappy-playpen/pull/39) by Andy Keech ([discussion on the list](https://lists.ubuntu.com/archives/snapcraft/2016-June/000113.html))
  * [Ubuntu Kylin Icon theme](https://github.com/ubuntu/snappy-playpen/pull/38) by Fabio Colella
  * [etherpad-lite](https://github.com/ubuntu/snappy-playpen/pull/32) by Vincent Jobard ([discussion on the list](https://lists.ubuntu.com/archives/snapcraft/2016-June/000118.html))
  * [plank](https://github.com/ubuntu/snappy-playpen/pull/31) by Michael Hall
  * [kdenlive](https://github.com/ubuntu/snappy-playpen/tree/kdenlive) by Alan Pope
  * [FlightGear](https://github.com/ubuntu/snappy-playpen/tree/flightgear) by Alan Pope
  * [ejabberd](https://github.com/jamestait/snappy-playpen/tree/master/ejabberd) by James Tait

Not targeting the Snappy Playpen, but still nice snaps we worked on together
as a team:

  * [ownCloud](https://github.com/kyrofa/owncloud-snap) by Kyle Fazzari
  * [Mycroft](https://github.com/MycroftAI/snapcraft-mycroft-core) by aatchison
  * [qt5-launcher](https://github.com/dplanella/qt5conf) improvements, by Leo Arias

We also used this time to improve our crowdsourced docs on AskUbuntu:

  * [What is --devmode](http://askubuntu.com/questions/783945/what-is-devmode-for-snaps/) by David Planella
  * [How to debug snaps](http://askubuntu.com/questions/783979/how-to-debug-snaps) by David Planella & Jamie Strandboge

The Snapcraft mailing-list has been buzzing with questions, answers and
discussions:

  * [Lots of general questions](https://lists.ubuntu.com/archives/snapcraft/2016-June/000122.html) by Alekseenko Vasilii
  * [Installing snaps in LXD containers](https://lists.ubuntu.com/archives/snapcraft/2016-June/000128.html) by Sujeevan Vijayakumaran
  * [Debugging `confinement: strict` issues](https://lists.ubuntu.com/archives/snapcraft/2016-June/000134.html) by Reinhard Pointner
  * [Errant codes sent to stdout](https://lists.ubuntu.com/archives/snapcraft/2016-June/000145.html) by Bill Janssen

And of course, kudos to the experts who managed to be very active and helpful,
while preparing new releases of snapd and snapcraft.

  * [snapd 2.0.8 release](https://github.com/snapcore/snapd/commit/14ff9e23e48de107b34938a398a319bbb38730be&sa=D&ust=1465395364314000&usg=AFQjCNGh_-hHiti50td2brtA5_DbMTjvnA)
  * [snapcraft 2.10 release](https://github.com/ubuntu-core/snapcraft/commit/3bfb571e7f965848dc5b5b9e6dea9c930aa0b253&sa=D&ust=1465395364315000&usg=AFQjCNG7LLAFdV9uBnodCHO0lBNJ9FuFFQ)
  * 10 bugs filed on [snapcraft](https://bugs.launchpad.net/snapcraft/%2Bbugs?orderby%3D-id%26start%3D0&sa=D&ust=1465395364315000&usg=AFQjCNGrLjKQgYyxqQF7Z0D1tcvTQRxmlw) (most of them triaged and in progress already)
  * 4 bugs filed on [snapd](https://bugs.launchpad.net/snappy/?orderby%3D-id%26start%3D0&sa=D&ust=1465395364316000&usg=AFQjCNFnEJXs7ePxq5UDRXKMxrk89sx1lg)

Until the next Playpen event, which will be more focused on a specific
software/framework/technology, we encourage you to have a look at all the
snaps and snapcraft recipes available [in therepo](https://github.com/ubuntu/snappy-playpen). Git clone it, cd into a
project and run snapcraft to see how all the pieces are coming together to
create a snap.

If you are the upstream of one of the above apps, help yourself with these
branches and get in touch with us on IRC (freenode/#snappy),
[Gitter](https://gitter.im/ubuntu/snappy-playpen) or on the [mailing-list](https://lists.ubuntu.com/mailman/listinfo/snapcraft) so we can provide
support if needed.

[David Callé](/en/blog/authors/davidc3/)

June 8, 2016

Filed under: [snap](/en/blog/tags/snap/) [snapcraft](/en/blog/tags/snapcraft/)
[ubuntu-planet](/en/blog/tags/ubuntu-planet/)





## Comments

No comments yet.

## Add your comment

Name:

Email address:

URL:

Comment:

If you enter anything in this field your comment will be treated as spam:





