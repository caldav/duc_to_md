





## How should I upload my webapp?

On Ubuntu devices, web applications are shipped as click packages.

Packaging a web application is quite easy, as explained in the following
steps.

### The manifest

We want our apps to be secure. To achieve this, all apps run under
confinement. When producing the apps, you get to decide which security
privileges your app needs. Please only pick security permissions your app is
actually going to use.

If you are unsure which security privileges to choose, read our article about
[Security policy for click packages](/en/phone/platform/guides/app-
confinement/).

Make sure your source directory contains a manifest.json file, which looks
like this:

    {
        "description": "Ubuntu app for example.com",
        "framework": "ubuntu-sdk-14.04",
        "hooks": {
            "example": {
            "apparmor": "app.json",
            "desktop": "app.desktop"
        }
    },
        "maintainer": "Joe Blobbs",
        "name": "com.ubuntu.developer.joe-blobbs.example",
        "title": "example.com webapp",
        "version": "0.1"
    }

### The .desktop file

You also need a .desktop file in the source directory too, call it app.desktop
for example. It should look like this:

    [Desktop Entry]
    Name=example.com
    Comment=webapp for example.com
    Type=Application
    Icon=app.png
    Exec=webapp-container http://m.example.com
    Terminal=false
    X-Ubuntu-Touch=true
    X-Ubuntu-StageHint=SideStage

webapp-container supports a few command line options to adjust to different
application scenarios.

The main option to add is --webappUrlPatterns This option restricts the access
to only URLs that are part of the web application. When a user navigates
outside of that domain, he will exit the webapp container and the default
browser will open that link. url_dispatcher is used to launch the main browser
when navigating to sites not matching the pattern. Patterns should typically
use ‘https?://’ to avoid needless redirects to the global browser. Also you
should typically specify globs at the end of the pattern, after ‘/’. Eg,
--webappUrlPatterns=https?://m.facebook.com/*

An example for a Twitter webapp might be:

    Exec=webapp-container --enable-back-forward \
         --webappUrlPatterns=https?://mobile.twitter.com/* \
    http://mobile.twitter.com

### The security policy groups

Now you need to specify the security permissions your app needs. Create a
app.json file, which looks like this:

    {
    "template": "ubuntu-webapp",
    "policy_groups": [
    "networking",
    "audio",
    "video",
    "webview",
    "content_exchange"
    ],
    "policy_version": 1.1
    }

If your app needs to decode and display audio or videos, add the “audio” and
“video” policy groups respectively. Again refer to [Security policy for click
packages](/en/phone/platform/guides/app-confinement/) for futher details.

### The icon

Now also add an icon. Call it app.png and make its size 256×256 pixels. The
icon should just be present at the root of the packaging directory. Find more
information about creating good icons [here](/en/publish/creating-a-good-
icon/).

### Building the package

This is the easiest step. Just run the following command in the source
directory and you are all set.

`click build .`

The resulting .click file is going to be in the parent directory of your
source.

Note: for updated versions of your package, just update the version in the
manifest and run the command again. Done.

### Technical requirements

In order for your webapp to be distributed in the Ubuntu Software Store beta
it must:

  * Be available to users at no cost (until after 13.10)

  * Be built as a click package

  * Comply to the [Terms of Service](https://myapps.developer.ubuntu.com/dev/tos/)

### Additional considerations

  * Webapps are isolated, cookies are not shared between them, nor with the web browser. Apparmor enforces that policy strictly. But phishing attacks via webapps are no different than click packages providing a webview. The app review and bug reporting process will take care of abuses.
  * For that same reason, a functionality like clicking “like on facebook” will be in the context of the webapp, not the main browser This limitation exists on other platforms as well.
  * A limitation in the current implementation is that a click on a twitter url in the facebook app, it will open in the main webbrowser instead of in the twitter webapp/click app. This should be handled by url dispatcher in a future release.

### Publishing your app

Once you have successfully created a click package, you are ready to upload it
and start the process of publishing it.

[Publish your app ›](https://myapps.developer.ubuntu.com/dev/click-
apps/new/?extract=1)





