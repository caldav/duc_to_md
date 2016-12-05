





#  [Snapcraft 2.10: zip files, devmode andmacaroons](/en/blog/2016/06/13/Snapcraft-210-zip-files-devmode-and-macaroons/)

A new version of Snapcraft, the tool to create snaps to distribute your
software, was recently released: Snapcraft 2.10 is packed with new features
and improvements, including:

  * The ‘`snapcraft init`’ command now produces a template to bootstrap developers to create their snaps and uses [‘devmode’ ](http://askubuntu.com/q/783945/9781)as the default confinement mode
  * Added support for zip files, which can now be used as a source to be snapped for most Snapcraft plugins.
  * Renamed the ‘`strip`’ step to ‘`prime`’. Use of ‘`strip`’, the former snap lifecycle step, will print deprecation warnings
  * Initial backend support to work on the parts ecosystem
  * Migration to macaroons for authentication. The decentralized, cloud-aware authentication system will enable the addition of more features to talk to the Ubuntu Store APIs and a better developer experience. After this change, developers will need to do a one-off relogin to do uploads
  * A new `‘assumes’` field, which will be used by snapd to assert certain features are supported by the system for a particular snap to work properly
  * General polish around command output and error messages
  * Improvements to the Go and nodejs plugins

Check out the full details on all [bug fixes and new features in Snapcraft2.10](https://launchpad.net/snapcraft/%2Bmilestone/2.10).

## Install Snapcraft

### On Ubuntu

Simply open up a terminal with Ctrl+Alt+t and run these commands to install
Snapcraft from the Ubuntu archives on Ubuntu 16.04 LTS

    
    sudo apt update
    sudo apt install snapcraft

### On other platforms

[Get the Snapcraft source code › ](https://github.com/ubuntu-core/snapcraft/releases/tag/2.10)

## Craft your snaps!

There is a thriving community of developers who can give you a hand getting
started or unblocking you when creating your snap. You can participate and get
help in multiple ways:

  * Mailing list: a great place to collaborate and discuss features, bugs and ideas on   
snapcraft is the [Snapcraft mailing list](https://lists.ubuntu.com/mailman/listinfo/snapcraft&sa=D&ust=1465822249728000&usg=AFQjCNEvI-YJWngLaYmFiha8YRctjgpY4A)

  * Talk live to other snappy developers on the [#snappy IRC channel on Freenode](https://webchat.freenode.net/?channels%3Dsnappy)
  * If something is not working for you or you’ve spotted a missing feature, feel free to [file a bug report](https://bugs.launchpad.net/snapcraft/%2Bfilebug)
  * Ask a question or check out the growing Snapcraft FAQs at [Ask Ubuntu](http://askubuntu.com/questions/tagged/snapcraft)

Last but not least the Snapcraft team would like to thank all the
contributions from our community, keep them coming!

## What’s next?

Next release, 2.11, will include improved documentation and getting started
utilities. Subsequent releases will focus on the parts ecosystem, plugins,
pull sources, and better integration with the Ubuntu Store for registration,
uploads and snap releases.

[David Callé](/en/blog/authors/davidc3/)

June 13, 2016

Filed under: [planet-ubuntu](/en/blog/tags/planet-ubuntu/)
[snap](/en/blog/tags/snap/) [snapcraft](/en/blog/tags/snapcraft/)





## Comments

No comments yet.

## Add your comment

Name:

Email address:

URL:

Comment:

If you enter anything in this field your comment will be treated as spam:





