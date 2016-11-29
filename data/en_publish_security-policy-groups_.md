





On Ubuntu, applications published in the store run under confinement. In
practice, it means that applications only have write and read access to a set
of specific directories and need to declare security policy groups to be
granted access to most device functionalities and content. This allows a
speedy review process and is a security measure to protect user data and
system integrity.

### Introduction to Security Policy groups

To access most features of the operating system, your app needs to request the
relevant security policy groups. This article focuses on setting this up for
your app.

#### **Security Policy groups are channels between your app and the rest of
the system**

Whether your app needs to record audio, access the network or do anything
outside its confined context, you need to know which security policy group it
needs to declare to be granted access. Doing so opens controlled channels
between your app and the rest of the system.

#### Practical example

Let’s imagine a comics creator app, which would allow the user to snap a few
pictures, place text on it, merge them in a single image and share it with
other people. Here are the groups you would need to use :

  * Take one or several pictures with the camera: **camera**
  * Make it available to other applications: **content_exchange_source**
  * Share it with other people: **networking**

If you forget to declare a group, it will prevent your app to work normally,
as we will see in a moment.

### Meet Permy

To have an overview of what is generally allowed to do with an Ubuntu app, you
can search for **Permy** in the store and install it on your device. It shows
security policy groups used by installed applications. For example, here is
what Permy can tell us about Reminders (an Evernote sync app).

![](/static/devportal_uploaded/1a90a9d1-034f-4fa9-8484-7ad8bdf913cf-
cms_page_media/163/permy_reminders.png) ![](/static/devportal_uploaded/77a807e
b-6e23-4ad3-86c7-4d95a833688e-cms_page_media/163/permy_reminders_pgroups.png)

Reminders is granted access to playing audio, accessing the network,
displaying pages in a webview, accessing other apps content via the content-
hub and accessing the online accounts framework. With these policy groups
declared, it can retrieve the user’s Evernote credentials and handle the
various types of content that can be stored in notes.

### Declaring policy groups with the SDK

In the “Publish” view of the SDK, you can declare policy groups your app
needs. You can manage them and see the full list of available groups with
their description. Doing this directly edits your click packaging files.

![](/static/devportal_uploaded/ae80b68d-a60e-4376-bfe2-3cc8fd1d1121-cms_page_m
edia/163/permissions_click.png)

The first lines on the right pane of the groups list gives you a short
description of what the policy group will grant you access to. Each policy
group will allow you access to certain file paths and system calls. The full
list can be viewed below the description.

![](/static/devportal_uploaded/7ad36ceb-d66a-4bb0-9bf0-65bfdb264ba8-cms_page_m
edia/163/policy_groups_list-700x416.png)

### Invalid and reserved policy groups

If you happen to manually edit policy groups in your click packaging files,
some may be invalid. In that case, your package won’t be validated by the SDK
and show a warning. Note that the store always rejects invalid packages. A
handful of policy groups, such as **calendar** or **debug**, are reserved to
certain types of apps, as you can see in red in their descriptions. If you
declare one, your app will be rejected by the store and will have to be fixed
to comply.

### Debugging and logs

Application confinement is ensured by AppArmor, a framework designed to
restrict applications to a limited set of resources. Each time your app is
trying to use a device functionality or reading and writing data, the action
is authorized or denied by AppArmor.

#### What happens when my application tries to use a functionality I’ve not
declared or I’m not allowed to?

It depends on what it is trying to do : it may crash, it may misbehave, it
might just not use the functionality or even appear to work fine. It
essentially comes down to what you are trying to use and how the app is
written to handle these denials. In any case, if AppArmor denied it, there
will be a message in a log file.

#### Where are logs?

Authorization denials are stored with other system messages in
/var/log/syslog. You can filter them with:

    grep DENIED /var/log/syslog

To ensure proper logging of all AppArmor messages when developing your
application, you might need to disable logging rate limiting:

    sudo sysctl -w kernel.printk_ratelimit=0

### Going further with app confinement

  * [Content Hub guide: get access to content on the device](/en/phone/platform/guides/content-hub-guide/)
  * [Security policy for click packages: build your app with confinement in mind](/en/phone/platform/guides/app-confinement/)





