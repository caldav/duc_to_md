





#  [Cleaning up scopes settings](/en/blog/2015/06/11/cleaning-scopes-
settings/)

The scopes architecture on Unity 7, which provides the Ubuntu shell and
default UX experience on current desktops, and Unity 8, which powers the phone
and soon the convergent desktop, differ to a large degree when it comes to
visibility of data sources. Future Unity 8 builds will be obsoleting the
legacy privacy flag in favour of a clearer way for users to decide where the
data is being sent to.

## Scope searches and preserving privacy in Unity 7

![](http://i.imgur.com/guhGSGq.png)

By default, using a regular Dash search in Unity 7 will first contact
Canonical's smart scopes server, which recommends the best or most promising
scopes for the search term. Then, as a second step, those scopes are queried
for actual results, which will finally be presented.

However, this approach means that the user doesn't necessarily know in advance
which scopes are queried and that the search term will be hitting the smart
scopes server. Although the data sent to server is anonymized, we understood
that some users might still be concerned about data privacy. It was for that
reason that privacy flag was introduced: a setting for scopes that prevents
access to the smart scopes server.

## Scope searches in Unity 8

![](http://i.imgur.com/VJQJZFF.png)

The scopes architecture in Unity 8 is quite different: there is no smart scope
server involved in the search lifecycle.

Instead, each query is only sent to the currently active scope (that is, the
one that is currently visible), so that the user always knows where their
search data ends up.

For the case where the current scope being is aggregating multiple other
scopes, its settings page will list all aggregated scopes, offering the
possibility to individually disable each one if desired.

## Obsoleting the privacy flag in Unity 8

With this clear visibility of what's being queried, and the possibility to
easily disable sources/scopes, the privacy flag becomes redundant in Unity 8.
As such, we have decided to remove this legacy setting in one of our
phone/Unity 8 next snapshots.

If you have been using this flag under Unity 8, either unfavorite or disable
the respective scopes from the aggregator settings to reach the same result.
You can also uninstall the individual scopes.

## Creating privacy in Unity 8

In the shell you can see two kind of scopes: normal scopes and aggregator
scopes. Normal scopes can access either local or remote data but never both at
the same time. So, if there is a scope called “My Music” then this scope will
only query your phone, while a “BBC News” scope will only query bbc.co.uk. If
you don’t want to use “BBC News” scope then do not invoke (via manage dash) or
favor the scope (similar to not to invoke (web)apps).

Aggregator scopes in contrast can aggregate all kind of scopes whether they
access local or remote data. If you’re concerned about a specific scope you
can disable it via the scopes’ settings page that lists all scopes being
aggregated. However, given that most scopes deal with remote data, it will be
faster to just unfavorite the respective aggregator via “Manage Dash” and
favorite the interesting scopes dealing with local data like “My Music” or “My
Videos”. This has also the benefit of not having (almost) empty dash pages.

[Pawel Stolowski](/en/blog/authors/stolowski/)

June 11, 2015

Filed under: [planet-ubuntu](/en/blog/tags/planet-ubuntu/)
[privacy](/en/blog/tags/privacy/) [scopes](/en/blog/tags/scopes/)





## Comments

No comments yet.

## Add your comment

Name:

Email address:

URL:

Comment:

If you enter anything in this field your comment will be treated as spam:





