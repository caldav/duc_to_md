





#  [UI Toolkit for OTA9](/en/blog/2016/02/01/ui-toolkit-ota9/)

Hello folks, it’s been a while since the last update came from our busy
toolkit ants. As OTA9 came out recently, it is the time for a refreshment from
our side to show you the latest and greatest cocktail of features our barmen
have prepared. Beside the bugfixes we’ve provided, here is a list of the big
changes we’ve introduced in OTA9. Enjoy!

# PageHeader

![](/static/devportal_uploaded/c5e7c8a2-b7e9-45a1-a15b-a48468872c9a-53856781-4
40a-47de-bf54-b997dc4c8244-media/2016/02/01/screenshot-2016-02-01-113108.png)

One of the most awaited components is the PageHeader. This now makes it
possible to have a detached header component which then can be used in a Page,
a Rectangle, an Item, wherever you wish. It is composed of a base, plain
Header component, which does not have any layout, but handles the default
behavior like showing, hiding the header and dealing with the auto-hiding when
an attached Flickable is moved. Some part of that API has been introduced in
OTA8, but because it wasn’t yet polished enough, we decided not to announce it
there and provide more distilled functionality now.

The PageHeader then adds the navigation and the trailing actions through the -
hopefully - well known ActionBar component.

# Toolbar

![](/static/devportal_uploaded/d93e2df9-ad08-44dc-
ae6b-8ced8a963789-795579e5-1ec4-4edd-94a4-6058a03673bd-
media/2016/02/01/screenshot-2016-02-01-113813.png)

Yes, it’s back. Voldemort is back! But this time it is back as a detached
component :) The API is pretty similar to PageHeader (it contains a leading
and trailing ActionBar), and you can place it wherever you wish. The only
restriction so far is that its layout only supports horizontal orientation.

# Facelifted Scrollbar

Yes, finally we got a loan headcount to help us out in creating some nice
facelift for the Scrollbar. The design follows the same principles we have for
the upcoming 16.04 desktop, with the scroll handler residing inside the bar,
and having two pointers to drive page up/down scrolling.

![](/static/devportal_uploaded/956935c5-96b6-4dfe-88cd-196a730057c9-eaa6de15-1
877-40e7-8755-7fa6ab12b480-media/2016/02/01/screenshot-2016-02-01-134059.png)

This guy also convinced us that we need a Scrollview, like in QtQuick Controls
v1, so we can handle the “buddy” scrollbars, the situation when horizontal and
vertical scrollbars are needed at the same time and their overlapping should
be dealt with. So, we have that one too :) And let's name the barman: [Andrea
Bernabei](https://plus.google.com/117368048981708663503) aka faenil is the
one!

# The unified BottomEdge experience

Finally we got a complete design pattern ready for the bottom edge behavior,
so it was about the time to get a component around the pattern. It can be
placed within any component, and its content can be staged, meaning it can be
changed while the content is dragged. The content is always loaded
asynchronously for now, we will add support to force synchronous loading in
the upcoming releases.

![](/static/devportal_uploaded/aa253973-be37-4c2c-b45c-4349670cff38-204797d0-9
231-45f3-8944-6f8af9ace08b-media/2016/02/01/screenshot-2016-02-01-114422.png)

# Focus handling in CheckBox, Switch, Button ActionBar

![](/static/devportal_uploaded/6d6f3e30-a1ee-4162-b87a-9ba30971c2da-1b4cd5f3-7
69b-4ab1-8165-6c30ae57b824-media/2016/02/01/screenshot-2016-02-01-114719.png)!
[](/static/devportal_uploaded/7d11418b-2933-4bf2-8e68-415734717a59-64b09ce8-ed
a2-4de4-824d-310f1351e2bc-media/2016/02/01/screenshot-2016-02-01-114819.png)![
](/static/devportal_uploaded/e74994ac-db9b-4d03-8a36-ec5cc3501cfc-6b203d89-cf7
c-4637-a7a8-6ff36c65a4b2-media/2016/02/01/screenshot-2016-02-01-114859.png)

![](/static/devportal_uploaded/d19217cc-54c3-43aa-b479-05bee04591f0-3b3aa5a3-b
7dd-448b-980d-55994e2e1526-media/2016/02/01/screenshot-2016-02-01-114934.png)

Starting now, pressing Tab and Shift+Tab on a keyboard will show a focus ring
on components that support it. CheckBox, Switch, Button and ActionBar have
this right now, others will follow soon.

# Action mnemonics

As we are heading towards the implementation of contextual menus, we are
preparing a few features as prerequisite work for the menus. For one adding
mnemonic handling to Action.

So far there was only one way to define shortcuts for an Action, through the
shortcut property. This now can be achieved by specifying the mnemonic in the
text property of the Action using the ‘&’ character. This character will then
be converted into a shortcut and, if there is a hardware keyboard attached, it
will underline the mnemonic.

[Zsombor Egri](/en/blog/authors/zsombi/)

Feb. 1, 2016

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





