





### What are PPAs?

Using a Personal Package Archive (PPA), you can distribute software and
updates directly to Ubuntu users. Create your source package, upload it and
Launchpad will build binaries (.deb files) and then host them in your own apt
repository.

That means Ubuntu users can install your packages in just the same way they
install standard Ubuntu packages and they'll automatically receive updates as
and when you make them. PPAs are part of Launchpad, and thus follow the
Launchpad terms of use:

  * Software must be free according to [Launchpad's licensing guidelines](https://help.launchpad.net/Legal/ProjectLicensing).
  * Each PPA gets 2 GiB of disk space. If you need more space for a particular PPA, this can be arranged through Launchpad admins.
  * You need to sign the Ubuntu Code of Conduct. (Instructions below.)

As Launchpad has a limited amount of package build machines, the build queue
can at times be clogged, so it might take longer until your packages are
built, but normally you can expect built packages within an hour.

### Creating your PPA

Ubuntu uses Launchpad as the central development platform. Bug reports,
translations, code, packages, everything happens in Launchpad. You need to
sign up, which is very easy to do and just takes a few minutes. To create an
account simply head to
[https://launchpad.net/+login](https://launchpad.net/+login)

To use PPAs you will need to sign the Code of Conduct. This is the foundation
document of the Ubuntu community. To us it's important that community members
who offer software accept the same principles and share the same ethos and
feeling for responsibility. To do this you will first have to set up a GPG
key.

In standard Ubuntu, start the 'seahorse' program by hitting the Super key and
searching for _"Passwords and Encryption Keys". _

  * **Step 1:** Open _Passwords and Encryption Keys_.
  * **Step 2:** Select _File > New_, select _PGP Key_ and then follow the on-screen instructions. Now you'll see your new key listed in the _Passwords and Encryption Keys_ tool.  
![Passwords and Encryption keys](/static/devportal_uploaded/e58df597-01c2-4a9e
-80c5-96c92c813054-cms_page_media/263/Screenshot-Passwords-and-Encryption-
Keys.png)

  * **Step 3**: Select the _My Personal Keys_ tab, select your key.
  * **Step 4**: Select _Remote > Sync and Publish Keys_ from the menu. Choose the Sync button. (You may need to add hkp://keyserver.ubuntu.com to your key servers if you are not using Ubuntu.)
  * **Step 5**: Select the _My Personal Keys_ tab, select your key and open the property window by pressing Space Bar or double clicking with your pointer. Select the _Details_ tab of the property window.
  * **Step 6**: Select the _Fingerprint_ text (the ten blocks of numbers and letter). Copy the text by pressing the control+c keys together.
  * **Step 7**: Visit [your OpenPGP keys page](https://launchpad.net/~/+editpgpkeys).
  * **Step 8**: Paste the fingerprint that you copied in step 3 into the Fingerprint text-box, then click the Import Key button. Launchpad will use the fingerprint to check the Ubuntu key server for your key and, if successful, send you an encrypted email asking you to confirm the key import.
  * **Step 9**: Check the email account that Launchpad has sent the confirmation email to. If your email client supports OpenPGP encryption, it will prompt you for the password you chose for the key when GPG generated it. Enter the password, then click the link to confirm that the key is yours. (Launchpad encrypts the email, using your public key, so that it can be sure that the key is yours. If your email software doesn't support OpenPGP encryption (for Thunderbird, try the Enigmail extension), copy the encrypted email's contents, type gpg in your terminal, then paste the email contents into your terminal window, followed by ctrl-D (an EOF character). )
  * **Step 10**: Back on the Launchpad website, use the Confirm button and Launchpad will complete the import of your OpenPGP key.

Then follow the on-screen instructions to sign the [Code of
Conduct](https://launchpad.net/codeofconduct).

### Setting up your PPA

You have multiple options when setting up the PPA. First of all you can set up
multiple PPAs. This makes sense if you have separate projects you maintain. As
an app developer it makes sense to have a separate PPA for each app, so users
can easily identify it. Secondly you can create a PPA for a user, but also for
a team. This means that if you maintain an app as a team, you would likely
want to set it up for the development team instead, so everybody on the team
can access it. To create the PPA, simply head to either of the two:

  * Personal PPA: [https://launchpad.net/~/+activate-ppa](https://launchpad.net/~/+activate-ppa)
  * Team PPA: [https://launchpad.net/~TEAMNAME/+activate-ppa](https://launchpad.net/~TEAMNAME/+activate-ppa) (be sure to replace TEAMNAME with the Launchpad ID of your team, or click on the "Create a new PPA" link on the team page). Note: You need to be owner (or admin) of the team.

### Uploading packages to your PPA

To generate packages, you will need to install a few tools on your machine and
configure a few things. This should just take a few minutes and is only
required once. First install the necessary tools by running:

    sudo apt-get install packaging-dev

Next edit your ~/.bashrc file and add something like the following in there:

    export DEBFULLNAME="Bob Dobbs" export DEBEMAIL="subgenius@example.com" 

Then save the file and afterwards simply restart your terminal or run:

    source ~/.bashrc

**Releasing your app** Once you're happy with your code and want to do a release, you document the changes in debian/changelog and give the release a version number. It is very important to document your change sufficiently so developers who look at the code in the future won’t have to guess what your reasoning was and what your assumptions were. Every Debian and Ubuntu package source includes debian/changelog, where changes of each uploaded package are tracked. The easiest way to update this is to run:
    dch -i

This will add a boilerplate changelog entry for you and launch an editor where
you can fill in the blanks. An example of this could be:

    superapp (1.4) precise; urgency=low
    * New release: + add Frobicator support. + document frobnication properly.
    -- Emma Adams <emma.adams@isp.com> Sat, 17 Jul 2010 02:53:39 +0200

dch should fill out the first and last line of such a changelog entry for you
already. Line 1 consists of the source package name, the version number, which
Ubuntu release it is uploaded to, the urgency (which almost always is ‘low’).
The last line always contains the name, email address and timestamp of the
change. Every new release should have a new changelog entry and the version
number should be higher than the one before. "dch -i" will automatically take
care of you for this, but if you want a different version number, you can edit
it manually as well.

In the bzr source branch run:

    bzr bd -- -S -sa
    dput ppa:<Launchpad ID>/<PPA name>

### Test building locally

In some cases it makes sense to test a build locally before uploading it to
Launchpad. Especially if it's the first build you can easily verify if
everything works according to plan. Luckily it's very easy to set up a build
environment with pbuilder. pbuilder allows you to build packages locally on
your machine. It serves a couple of purposes:

  * The build will be done in a minimal and clean environment. This helps you make sure your builds succeed in a reproducible way, but without modifying your local system
  * There is no need to install all necessary _build dependencies_ locally
  * You can set up multiple instances for various Ubuntu and Debian releases

Setting pbuilder up is very easy, run:

    pbuilder-dist <release> create

where <release> is for example precise, quantal or raring or in the case of
Debian maybe sid. This will take a while as it will download all the necessary
packages for a “minimal installation”. These will be cached though. To build a
test package with your changes, run these commands:

    bzr bd -- -S -sa
    pbuilder-dist <release> build ../<package>_<version>.dsc

This will create a source package from the branch contents and pbuilder-dist
will build the package from source for whatever release you choose. Once the
build succeeds, install the package from ~/pbuilder/<release>_result/ (using
sudo dpkg -i<package>_<version>.deb). Then test to see if the bug is fixed.

### Distributing the apps from your PPA

To get your app out to users, you can give them very easy instructions to
install your app by adding the PPA. If your Launchpad ID is "bobdobbs" and
your PPA name is "superedit", you could tell your users to simply:

    sudo add-apt-repository ppa:bobdobbs/superedit && sudo apt-get update
    sudo apt-get install <package name of your app>

Done. That's it.

### Getting help

The Ubuntu community provides you with a strong support network that can help
you solve your development challenges. [Join in and share your knowledge]().

For the majority of apps, what we describe in this article should make things
work for you and get your app out there. There are obviously more options
around and if your project starts growing, you might want to have a look into
alternatives or extensions. If you generally want to know more about
packaging, we highly recommend the [Ubuntu Development
Guide](http://packaging.ubuntu.com/).

**Note:**

This article refers to publishing third-party desktop applications packaged
with the traditional .deb format.

Ubuntu is migrating to the new .snap format to easily and securely distribute
apps.

If you are looking for information on how to publish an app for mobile or IoT
devices, [check out the current documentation instead
›](https://developer.ubuntu.com/en/publish)





