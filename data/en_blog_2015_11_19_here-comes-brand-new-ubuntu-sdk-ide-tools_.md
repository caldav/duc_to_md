





#  [Here comes the brand new Ubuntu SDK IDE tools](/en/blog/2015/11/19/here-comes-brand-new-ubuntu-sdk-ide-tools/)

In the last couple of weeks, we had to completely rework the packaging for the
SDK tools and jump through hoops to bring the same experience to everyone
regardless if they are on LTS or the development version of Ubuntu. It was not
easy but we finally are ready to hand this beauty to the developer’s hands.

The two new packages are called “ubuntu-sdk-ide” and “ubuntu-sdk-dev”
(applause now please).

The official way to get the Ubuntu SDK installed is from now on by using the
Ubuntu SDK Team release PPA:

    https://launchpad.net/~ubuntu-sdk-team/+archive/ubuntu/ppa

Releasing from the archive with this new way of packaging is sadly not
possible yet, in Debian and Ubuntu Qt libraries are installed into a standard
location that does not allow installing multiple minor versions next to each
other. But since both, the new QtCreator and Ubuntu UI Toolkit, require a more
recent version of Qt than the one the last LTS has to offer we had to
improvise and ship our own Qt versions. Unfortunately that also blocks us from
using the archive as a release path.

If you have the old SDK installed, the default QtCreator from the archive will
be replaced with a more recent version. However apt refuses to automatically
remove the packages from the archive, so that is something that needs to be
done manually, best before the upgrade:

    
    sudo apt-get remove qtcreator qtcreator-plugin*

Next step is to add the ppa and get the package installed.

    
    sudo add-apt-repository ppa:ubuntu-sdk-team/ppa \
        && sudo apt update \
        && sudo apt dist-upgrade \
        && sudo apt install ubuntu-sdk

That was easy, wasn’t it :).

Starting the SDK IDE is just as before, either by running `qtcreator` or
`ubuntu-sdk` directly and also by running it from the dash. We tried to not
break old habits and just reused the old commands.

However, there is something completely new. An automatically registered Kit
called the “Ubuntu SDK Desktop Kit”. That kit consists of the most recent UITK
and Qt used on the phone images. Which means it offers a way to develop and
run apps easily even on an LTS Ubuntu release. Awesome, isn’t it Stuart?

The old qtcreator-plugin-ubuntu package is going to be deprecated and will
most likely be removed in one of the next Ubuntu versions. Please make sure to
migrate to the new release path to always get the most recent versions.

[Benjamin Zeller](/en/blog/authors/zeller-benjamin/)

Nov. 19, 2015

Filed under: [planet-ubuntu](/en/blog/tags/planet-ubuntu/)
[qtcreator](/en/blog/tags/qtcreator/) [sdk](/en/blog/tags/sdk/)
[tools](/en/blog/tags/tools/)





## Comments

No comments yet.

## Add your comment

Name:

Email address:

URL:

Comment:

If you enter anything in this field your comment will be treated as spam:





