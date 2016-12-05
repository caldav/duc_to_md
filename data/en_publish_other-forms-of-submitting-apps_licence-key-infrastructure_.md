





## Licence keys

You can upload apps that need a licence key in a file on the purchaser’s
computer to work. This can help you determine if the user purchased this copy
of the app, or if they just downloaded it elsewhere.

Once you’ve enabled licence keys, the Ubuntu Software Centre will fetch a
licence key when it completes a purchase, and copy that into the right file
for your app to check. It is up to you, the developer, to provide keys that
are hard to guess, check if the key is there when your application starts and
behave accordingly.

You will receive a notification by email when the number of available licence
keys goes below a certain configurable threshold, and you will see notices
when you visit the website telling you about this also. If we run out of
license keys we will necessarily stop selling copies of your app.

To enable licence keys for your app you need to provide two things:

  * **A set of licence keys**. These will be provisioned to users, one per subscription together with the downloaded package.
  * **A path to the file where your app will expect to find the licence key**. This should be entered as a path relative to the installed binary, or alternatively a path within the user's home folder, beginning with '~'. For example, 'data/license.txt' will place the key under /opt/ /data/license.txt and '~/myapp_license.txt' will place the license in the user's home folder

**Note:**

This article refers to publishing third-party desktop applications packaged
with the traditional .deb format.

Ubuntu is migrating to the new .snap format to easily and securely distribute
apps.

If you are looking for information on how to publish an app for mobile or IoT
devices, [check out the current documentation instead›](https://developer.ubuntu.com/en/publish)





