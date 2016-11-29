





## How should I upload my app?

In order for your application to be delivered via the Ubuntu Software Centre,
it must be packaged in a standard format that makes it possible to distribute
it to users. The technology Ubuntu uses for that purpose is called **Debian
packaging**.

### Commercial and proprietary software

In order to package your software properly, it must meet all of the points in
the Technical requirements section below.

You need to provide us with the a **Debian source package **(.dsc, diff.gz,
orig.tar.gz files), bundled in an archive file (.tar.gz, .zip, etc).

### Open source software at zero cost

We recommend open source applications to be distributed via a **Personal
Package Archive (PPA)**.

[Learn more about packaging and PPAs ›](/en/publish/other-forms-of-submitting-
apps/ppa/)

### Technical requirements

In order for your application to be distributed in the Software Centre it
must:

  * Be in one, self-contained directory when installed
  * Be able to be installed into the /opt/<package-name> directory (*)
  * Be executable by all users from the /opt/<package-name> directory (**)
  * Write all configuration settings to ~/.config/<package-name> (This can be one file or a directory containing multiple configuration files)

(*) We recommend open source, zero-cost apps to be installable at
/opt/extras.ubuntu.com/<package-name>

(**) Users have only read (and not write) privileges to this directory

**Note:**

This article refers to the publishing third-party desktop applications
packaged with the .deb format.

Ubuntu is migrating to the new .snap format to easily and securely distribute
apps. If you are looking for information on how to publish an app for mobile
or IoT devices, [check out the current documentation instead
›](https://developer.ubuntu.com/en/publish)





