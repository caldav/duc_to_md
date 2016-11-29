





## How should I upload my app?

To Ubuntu users, additional apps are shipped as click packages. To generate
click packages, the first step is to open your project in the Ubuntu SDK,
click on the Edit tab on the left hand side and fill out the manifest.json
file form.

![](/static/devportal_uploaded/44dc6f8f-dc88-4274-a85a-2a14396a936b-cms_page_m
edia/214/publish-manifest.png)

The Name field should contain your appname, a dot, then the package namespace
you chose when you signed up on MyApps. In the example above the namespace of
the user would be lexmur and the package name of the app would be angry-
giraffes.

Most of this information is automatically filled during [the project
creation](/en/phone/apps/sdk/tutorials/creating-an-sdk-app-project/), but this
is a good opportunity to check for any mistakes you could have made.

### Security policy groups

We want our apps to be secure. To achieve this, all apps run under
confinement. When producing the apps, you get to decide which security
privileges your app needs. Please only pick security permissions your app is
actually going to use. networking is the only one the Ubuntu SDK suggests by
default. If you are unsure which security privileges to choose, read our
article about [Security policy for click packages](/en/publish/security-
policy-groups/).

To manage your security policy groups, select the <appname>.apparmor file in
the project files tree.

![](/static/devportal_uploaded/84cf49ef-4a64-4e13-b6a4-dcb4a3d5e8f3-cms_page_m
edia/214/publish-policygroups.png)

### Package validation

Then, go to the Publish tab, click on "Create and validate Click Package" and
wait for the package to be built and tests to pass. Now, the parent directory
of your project should contain the click package which is ready for upload.

![](/static/devportal_uploaded/48c1fdac-e82c-4d57-8ff1-f49d76f06549-cms_page_m
edia/214/publish-validateclick.png)

### Technical requirements

In order for your application to be distributed in the Software Centre it
must:

  * Be less than 3GB in size
  * Be available to users at no cost (until after 13.10)
  * Be built as a click package
  * Comply to the [Terms of Service](https://myapps.developer.ubuntu.com/dev/tos/)

### Publishing your app

Once you have successfully created a click package, you are ready to upload it
and start the process of publishing it. If you should have any problems
publishing your app, please do reach out to our [app developer community]().

[Publish your app](https://myapps.developer.ubuntu.com/dev/click-
apps/new/?extract=1)





