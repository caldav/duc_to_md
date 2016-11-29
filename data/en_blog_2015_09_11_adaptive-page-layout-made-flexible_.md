





#  [Adaptive page layout made flexible](/en/blog/2015/09/11/adaptive-page-
layout-made-flexible/)

A few weeks ago Tim posted a nice article about [_Adaptive page layouts made
easy_](https://developer.ubuntu.com/en/blog/2015/08/10/adaptive-page-
layouts/). It is my turn now to continue the series, with the hope that you
will all agree on the title.

Ladies and Gentlemen, we have good news and (slightly) bad news to announce
about the AdaptivePageLayout. If the blogging would be interactive, I’d ask
you which one to start with, and most probably you would say with the bad
ones, as it is always good to get the cold shower first and then have a
sunbath. Sorry folks, this time I’ll start with the good news.

# The good news

We’ve added a column configurability API to the AdaptivePageLayout! From now
on you can configure more than two columns in your layout, and for each column
you can configure the minimum, maximum and preferred sizes as well as whether
to fill the remaining width of the layout or not. And even more, if the
minimum and maximum values of the column configuration differs, the column can
be resized with mouse or touch. See the following
[video](https://youtu.be/KYZu7LcfWxM) demonstrating the feature.

## **<commercials>

And all this is possible right now, right here, only with Ubuntu UI Toolkit!

</commercials>**

You can configure any number of column configurations, with conditions when
those should be applied. The one column mode doesn’t need to be configured,
that is automatically applied when none of the specified column configuration
conditions apply. However, if you wish, you can still configure the single
column mode, in case you want to apply minimum width value for the column.
Note however that the minimum width configuration will not (yet) be applied on
the application’s minimum resizable width, as you can observe on the video
above.

The video above was made based on the sample code from [_Tim’s
post_](https://developer.ubuntu.com/en/blog/2015/08/10/adaptive-page-
layouts/), with the following additions:

    
    AdaptivePageLayout {
        id: layout
        \\ [...]
        layouts: [
            // configure two columns
            PageColumnsLayout {
                when: layout.width > units.gu(80)
                PageColumn {
                    minimumWidth: units.gu(20)
                    maximumWidth: units.gu(60)
                    preferredWidth: units.gu(40)
                }
                PageColumn {
                    fillWidth: true
                }
            },
            // configure minimum size for single column
            PageColumnsLayout {
                when: true
                PageColumn {
                    minimumWidth: units.gu(20)
                    fillWidth: true
                }
            }
        ]
    }

The full source code is on lp:~zsombi/+junk/AdaptivePageLayoutMadeFlexible.

# The bad news

Oh, yes, this is the time you guys start to get mad. But let’s see how bad it
is going to be this time.

We started to apply the AdaptivePageLayout in a few core applications, when we
realized that the UI is getting blocked when Pages with heavy content are
added to the columns. As pages were created synchronously, we would have had
to redo each app’s Page content management to be able to load at least
partially asynchronously using Loaders. And that seemed to be a really bad
omen for the component. So we decided to bring in an API break for the
AdaptivePageLayout **addPageTo{Current|Next}Column()** functions, so if the
second argument is a file URL or a Component, the functions now return an
incubator object which can be used to track the loading completion. In the
case of an existing Page instance, as you already have it, the functions will
return null. More on how to use incubators in QML can be read from
[_http://doc.qt.io/qt-5/qml-qtqml-component.html#incubateObject-
method_](http://doc.qt.io/qt-5/qml-qtqml-component.html#incubateObject-
method).

A code snippet to catch page completion would then look like

    
    var incubator = layout.addPageToNextColumn(thisPage, Qt.resolvedUrl(pageDocument));
    if (incubator && incubator.status == Component.Loading) {
        incubator.onStatusChanged = function(status) {
            if (status == Component.Ready) {
                // incubator.object contains the loaded Page instance
                // do whatever you wish with the Page
                incubator.object.title = "Dynamic Page";
            }
        }
    }

Of course, if you want to set up the Page properties with some parameters, you
can do it in the good old way, by specifying the parameters in the function,
i.e.

`addPageToNextColumn(thisPage, Qt.resolvedUrl(pageDocument), {title: “Dynamic
Page”})`.

The incubator approach you would need if you want to do some bindings on the
properties of the page, which cannot be done with the creation parameters.

So, the bad news is not so bad after all, isn’t it? That’s why I started with
the good news ;)

# More “bad” news to come

Oh, yes, we have not finished yet with the bad news. So from now on pages
added to the columns are asynchronous by default, except the very first page.
That is still going to be loaded synchronously. The good news: it is not for
long ;) We are planning to enable asynchronous loading of the primary page as
well, and most probably you will get a signal triggered when the page is
loaded. In this way you would be able to show something else while the first
page is loading, an animation, another splash screen, or the Flying Dutchman,
whatever :)

Stay tuned! We’ll be back!

[Zsombor Egri](/en/blog/authors/zsombi/)

Sept. 11, 2015

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





