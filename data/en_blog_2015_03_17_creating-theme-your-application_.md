





#  [Creating a theme for your application](/en/blog/2015/03/17/creating-theme-your-application/)

![Creating a theme for your application](/static/devportal_uploaded/4966443d-82b5-48e9-839e-fc268197bfa0-uploads/zinnia/appTheming.png)

The theming engine is one of the least documented features of Ubuntu UI
Toolkit. While we are preparing to create the third generation theming engine,
which will support sub-theming and runtime palette color customizations, there
are more and more app developers asking about how to create their own theme
for the application itself. There were also questions on how to create a
shared theme so other applications can use these themes. But let’s get first
the application theming.

The application themes are application specific, and should be located in the
application’s installation folder. They can derive from a pre-defined system
theme (Ambiance or SuruDark) as well as be standalone themes, not reusing any
system defined themes. However this latest one is not recommended, as in this
case you must implement the style of every component, which in one way
requires lot of work, and secondly it uses few APIs which are not
stable/documented.

Assuming the theme is located in a separate folder called MyTheme, the second
step would be to create a file called “parent_theme” where you put the URI of
the theme your application theme derives from. Your parent_theme would look
like

    
    // parent_theme
    Ubuntu.Components.Themes.SuruDark

Now, let’s change some palette values. The way to do that is to create a
Palette.qml file, and override some values you want.

    
    // Palette.qml
    
    import QtQuick 2.4
    import Ubuntu.Components 1.2
    import Ubuntu.Components.Themes.SuruDark 1.1 as SuruDark
    
    SuruDark.Palette {
        normal.background: “#A21E1C”
        selected.backgroundText: “lightblue”

If you want to change some component styles, you have to look into the parent
theme and check the style component you want to change. It can be that the
parent theme doesn’t have the style component defined, in which case you must
follow its parent theme, and search for the component there. This is the case
if you want to change the Button’s style, SuruDark theme doesn’t have the
style component defined, therefore you must take the one from its parent,
Ambiance. So the redefined ButtonStyle would look like:

    
    // ButtonStyle.qml
    
    import QtQuick 2.4
    import Ubuntu.Components 1.2
    
    // Note: you must import the Ambiance theme!
    import Ubuntu.Components.Themes.Ambiance 1.1 as Base
    
    Base.ButtonStyle {
        // Let’s override the default color
        defaultColor: UbuntuColors.green
    }

For now only a few style component is exported from the two supported system
themes, in case you see one you’d like to override just file a bug. Then there
are only a handful of style APIs made stable, therefore overriding the non-
documented styles may be dangerous, as their API may change. The stable style
APIs are listed in Ubuntu.Components.Styles module and their implementation
and unstable APIs are in Ambiance and SuruDark themes.

And finally you can load the theme in the application as follows:

    
    // main.qml
    
    import QtQuick 2.4
    import Ubuntu.Components 1.2
    
    MainView {
        // Your code comes here
    
        // Set your theme
        Component.onCompleted: Theme.name = “MyTheme”
    
    }

That’s it. Enjoy your colors!

P.S. A sample code is available
[here](https://code.launchpad.net/~zsombi/+junk/AppTheming).

[Zsombor Egri](/en/blog/authors/zsombi/)

March 17, 2015

Filed under: [planet-ubuntu](/en/blog/tags/planet-ubuntu/)
[sdk](/en/blog/tags/sdk/)





## Comments

No comments yet.

## Add your comment

Name:

Email address:

URL:

Comment:

If you enter anything in this field your comment will be treated as spam:





