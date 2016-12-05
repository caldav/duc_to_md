





#  [Keeping track of evolving QML components](/en/blog/2015/05/26/keeping-track-evolving-qml-components/)

We all love QML because it allows for fast prototyping, and not only that,
it's a very efficient tool for production applications. The complexity of C
and C++ is hidden behind neat and simple API. Many if not most app developers
these days take advantage of that without even having to know the
implementation details. Most of the _Ubuntu UI Toolkit_ is pure QML except for
performance-critical elements like the new ListItem or the theming engine.

There's a notable flaw however to QML as a language when it comes to
versioning. Any QML component is made known to the engine in one of two ways.
Using [qmldir](http://doc.qt.io/qt-5/qtqml-modules-qmldir.html), which
essentially is a text file listing with version numbers and filenames -
unfortunately there's no error handling whatsoever so _qmldir_ files in
productive use are all but flawless and mistakes including missing files won't
be noticed easily, made worse by the fact that QML automagically recognizes
files as class names regardless of being registered anywhere. The other way is
[qmlRegisterType](http://doc.qt.io/qt-5/qqmlengine.html#qmlRegisterType) in
one of its various incarnations - seemingly with inbuilt support for minor
revisions which in fact are completely unrelated to QML.

Looking further at how classes behave it's not looking much better either.
There's no support for versions in functions, properties or signals. All
members will show up in all versions the same QML file is registered to.
Additions as well as changes affect all versions - unless you fork the
implementation, which is what we do for the _Ubuntu UI Toolkit_ these days to
ensure new versions don't break existing code, with the exception of bug
fixes. To make matters worse, if the implementation imports another, newer
version, the public API will follow suit. Regardless of the policy of a
particular project, there's no easy way of ensuring the public API is what you
want it to be, it's just too failible.

Fortunately the _Ubuntu UI Toolkit_ has employed a solution that's now become
available for everyone:

    
    Usage: apicheck [-v[v]] [-qml] [-json] IMPORT_URI [...IMPORT_URI]
    
    Generate an API description file of one or multiple components.
    Example: apicheck Ubuntu.Components
        apicheck --json Ubuntu.DownloadManager
    
    The following rules apply for inclusion of public API:
    
     - Types not declared as internal in qmldir
     - C++ types exported from a plugin
     - Properties and functions not prefixed with __ (two underscores)
     - Members of internal base classes become part of public components

It's designed to serialize the public QML API in a way that is human readable
as well as easy to process in a pogrammatic fashion. Let's try it out, shall
we?

`/usr/lib/x86_64-linux-gnu/ubuntu-ui-toolkit/apicheck Ubuntu.Components >
components.api.new`

This will give you something like the following in the file
_components.api.new_:

`

    Ubuntu.Components.PageHeadConfiguration 1.1: Object
        readonly property Action actions  
    
        property Action backAction  
    
        property Item contents  
    
        property color foregroundColor  
    
        property string preset  
    
        readonly property PageHeadSections sections  
    
    Ubuntu.Components.PageHeadConfiguration 1.3: Object  
    
        readonly property Action actions  
    
        property Action backAction  
    
        property Item contents  
    
        property color foregroundColor  
    
        property bool locked  
    
        property string preset  
    
        readonly property PageHeadSections sections  
    
        property bool visible  
    
    Ubuntu.Components.UbuntuShape.HAlignment: Enum  
    
        AlignHCenter  
    
        AlignLeft  
    
        AlignRight  
    
    Ubuntu.Components.ViewItems 1.2: QtObject  
    
        property bool dragMode  
    
        signal dragUpdated(ListItemDrag event)  
    
        property bool selectMode  
    
        property QList<int> selectedIndices  
    
    Ubuntu.Components.i18n 1.0 0.1: QtObject  
    
        property string domain  
    
        property string language  
    
        function bindtextdomain(string domain_name, string dir_name)  
    
        function string tr(string text)  
    
        function string tr(string singular, string plural, int n)  
    
        function string dtr(string domain, string text)  
    
        function string dtr(string domain, string singular, string plural, int n)  
    
        function string ctr(string context, string text)  
    
        function string dctr(string domain, string context, string text)  
    
        function string tag(string text)  
    
        function string tag(string context, string text)

`

There are, in order, a QML component, an enum, an attached property and a
singleton, all read from the typesystem in the way they will be available to
QML applications.

Now in addition to reviewing this file with the naked eye you also use _diff_:

`diff -F '[.0-9]' -u components.api{,.new}`

Now let's imagine we're making some changes to some of the classes and running
it again will yield this result:

`

    @@ -415,11 +415,11 @@ Ubuntu.Components.PageHeadConfiguration  
    
     Ubuntu.Components.PageHeadConfiguration 1.3: Object  
    
         readonly property Action actions  
    
         property Action backAction  
    
    -    property Item contents  
    
    +    property var contents  
    
         property color foregroundColor  
    
         property bool locked  
    
         property string preset  
    
    -    readonly property PageHeadSections sections  
    
    +    property PageHeadSections sections  
    
         property bool visible  
    
     Ubuntu.Components.PageHeadSections 1.1: QtObject  
    
         property bool enabled  
    
    @@ -1001,7 +1001,7 @@ Ubuntu.Components.UbuntuShape.FillMode:  
    
     Ubuntu.Components.UbuntuShape.HAlignment: Enum  
    
         AlignHCenter  
    
         AlignLeft  
    
    -    AlignRight  
    
    +    AlignTop  
    
     Ubuntu.Components.UbuntuShape.VAlignment: Enum  
    
         AlignBottom  
    
         AlignTop  
    
    @@ -1017,7 +1017,6 @@ Ubuntu.Components.UriHandler 1.0 0.1: Qt  
    
     Ubuntu.Components.ViewItems 1.2: QtObject  
    
         property bool dragMode  
    
         signal dragUpdated(ListItemDrag event)  
    
    -    property bool selectMode  
    
         property QList<int> selectedIndices  
    
     Ubuntu.Components.i18n 1.0 0.1: QtObject  
    
         property string domain  
    
    @@ -1027,7 +1026,7 @@ Ubuntu.Components.i18n 1.0 0.1: QtObject  
    
         function string tr(string singular, string plural, int n)  
    
         function string dtr(string domain, string text)  
    
         function string dtr(string domain, string singular, string plural, int n)  
    
    -    function string ctr(string context, string text)  
    
    +    function string ctr(string context, string text, bool newArgument)  
    
         function string dctr(string domain, string context, string text)  
    
         function string tag(string text)  
    
         function string tag(string context, string text)

`

See what happened there? Several changes show up in the _diff_ output,
including changed arguments, removed and added members and even the removal of
the readonly keyword.

In the case of the _Ubuntu UI Toolkit_ a _components.api_ file lives in the
repository. A _qmake target_ generates _components.api.new_ from the local
branch and prints a _diff_ of the two files. This is run as part of _make
check_, meaning any changes to the API become visible at the time you run unit
tests, as well as CI builds for merge requests made on Launchpad. Any changes
will cause _make check_ to fail so the branch has to include an updated
_componets.api_ which shows up in Launchpad reviews and _bzr_ command line
tools.

If any of this got you excited, maybe you wanna add it to your own components
and improve QA?

[Christian Dywan](/en/blog/authors/kalikiana/)

May 26, 2015

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





