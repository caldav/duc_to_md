





#  [The versioning of the Ubuntu UI Toolkit](/en/blog/2016/05/24/about-
versioning-ubuntu-ui-toolkit/)

## **Let’s start with the background story.**

The UITK releases, before we opened the 1.3 branch for development, was mainly
targeting touch devices and their main objective was to offer more or less a
complete API set for mobile application development. The versions prior to 1.3
were working on the desktop too, but they were clearly suboptimal for those
use cases because for example they were missing mouse and keyboard
capabilities

With the 1.3 development branch we set on a single goal. With this release the
UITK will offer a feature complete API set for devices of all form factors
with all kinds of capabilities. It means that applications built for the 1.3
UITK will work on a touchscreen device with a small display just as on a large
screen with mouse and keyboard. It was a very ambitious plan, but absolutely
realistic.

We have decided that we follow the "release early and release often" principle
so developers will have time to adapt their applications to the new APIs. At
the same time we promised that whatever API we release will be supported for
at least one minor revision and we will follow a strict and developer friendly
deprecation process if needed.

## **It means that even if the source code of the 1.3 UITK is not frozen, all
APIs released in it are stable and safe to use.**

So far we did keep our promise. There was not a single application in the
store or in the archive that suffered functional regression due to an
intentional API break in the UITK. True, UITK has bugs. True, one can argue
about if changing the color palette classifies to be an API change or not. Not
to mention the awkward situation when an application takes advantage of a bug
in the UITK and loses that advantage when the bug gets fixed. Also we have
seen broken applications because they were using private APIs and properties.

It is absolutely true that using a frozen API set is the safest for
application developers. No doubt about it and I do hear the opinions that some
developers wish to see a fully frozen 1.3 UITK. We do wish the same.

Now, let us visit this idea and check a bit around. I do promise that folding
out the big picture will help everyoneunderstand why the UITK is developed in
the way it is.

So, let us say we freeze the 1.3 UITK today. In that case we need to open the
1.4 branch plus we would certainly open a Labs space. Before going any further
let me list what kind of changes we do in the UITK codebase:

  1. Critical bug fixes. Right, I am sure that nobody argues the fact that once we found or reported a critical bug we have to push a fix to the supported releases as soon as possible. At this very moment we have a good number of open bug reports. About 80% of the merged branches and patches to the UITK code are bug fixes. With every OTA release we push out 10-20 critical bug fixes. It means that each bugfix needs to target both the frozen and the development branch, plus the labs space. From the point of bug fixes it is important that the supported branches of the UITK do not diverge too much. One may say 1.3 should be frozen, so no bug fixes should go there, eventually some showstoppers. However we have way too many of those fixes which we must land in 1.3 as well. Fragmenting the UITK and so the platform at this early stage might fire back later.

  2. Feature gaps for convergence. As we have stated many times, the convergence features are not yet completely implemented in the UITK. We do wish they were, but sadly they are not. It means that almost every day we push something to the UITK codebase that makes that feature gap smaller. In case we freeze the 1.3 UITK we can push these convergence features only to the 1.4 and the labs space. That would mean that all core applications would need to migrate to the 1.4 UITK because they are the primary consumers of the convergence feature.

  3. UITK uses dynamic styling of components. The styles are loaded from a specified theme matching the version of the UITK module the component is imported from. This is necessary because themes implement UX including behavior and looks, so just like functions in the API developers may rely on theming when designing their apps, or even adding custom components. We are using the property cache to detect the version of the module. As we are not planning any API additions to StyledItem, moving to 1.4 would require us to declare a dummy property just to be able to detect that the component is imported from the 1.4 version. Introducing a property just to be able to differentiate doesn’t sound really professional. Yes, the version could be set in the component itself, but that would immediately break the symlink idea (second time) and beside that, noone guarantees that the version will be set prior to the style document name, so a dual-style loading can be eliminated. We had this API in the first version of the sub-theming, but was removed, and perhaps it was the only API break we did in 1.3 so far.

  4. Unit tests are also affected. They need to be duplicated at the least when components in 1.4 diverge in behavior and features - but even bugs in superclass A altered in 1.4 may affect component B which is not altered and still fail test cases. On the other hand Autopilot is not so flexible. While the CPOs (Custom Proxy Objects, the classes that represent QML components in Python test cases) basically do not care about the import versions, they do have problems with the API differences, and it is not so easy doing differentiation for the same component to detect which API can be used in what context. We’ve been discussing to try to move as many tests as we can to QTest (unit tests), however there are still tons of apps using Autopilot, and we have to provide and maintain CPOs for those.

  5. The upcoming Labs space will hold the components and APIs that we do not promise to be stable and are subject to change even in one minor version. We need this space to experiment with features and ideas that would not be possible in a stable branch.

If we look at this picture we will see immediately that the further we go with
closing the feature gaps the more we diverge from the codebase of the frozen
1.3. Note that code change does not mean API change! We are committed to
stable APIs not to stable code. Freezing code is a luxurious privilege of very
mature products. Implementing new features and fixing critical bugs in two
different branches would mean that we need to fork the UITK. And that itself
would bring issues which have not been seen by many. A good example for this
is the recently discovered incompatibility issue between the old style header
and the refactored (to be implemented in C++) AdaptivePageLayout. To gain the
performance improvements in 1.3 it’s necessary to change the component
completely. Furthermore if only 1.4 started off with a rewritten
AdaptivePageLayout fixing bugs would consume considerable time in two entirely
different codebases at that point.

It is important to note that the UITK comes in a single package in a single
library. Forking the UITK package is clearly not an option. The applications
do not have control over their dependencies. Also creating multiple libraries
for different versions is not an option either. Providing the UITK in a single
plugin has some consequences. Many of the developers asked why there are no
more frequent minor version bumps. The answer is simple. As long as all the
versions come in a single plugin, each and every minor release will increase
the memory consumption of the UITK. Bumping the UITK version 3-4 times a year
would end up in a 10-12 times bigger memory footprint in just two years. We do
not want that. And most probably when we “release” 1.4, we will need features
from Qt 5.6, which means we need to bump imports in all our QML documents to
2.6. So it is a nice theory but it is not a working one.

To summarize the whole story, we are where we are for good reason. The way the
UITK is versioned, packaged and provided to the application developers is not
accidental. At the same time we do admit that after measuring the costs and
benefits of different paths, we had to make compromises. The present so called
rolling 1.3 release is safe to use, the APIs provided by the UITK are all
stable and supported. But as it is still evolving and improving it is a good
idea to follow the news and announcements of the SDK developer team. We are
available pretty much 24/7 on the #ubuntu-app-devel Freenode channel, on
[ubuntu-phone@lists.launchpad.net](mailto:ubuntu-phone@lists.launchpad.net)
mailing list, on Telegram and on all commonly used public platforms. We are
happy to listen to you and answer your questions.

[Zoltán Balogh](/en/blog/authors/bzoltan/)

May 24, 2016

Filed under: [planet-ubuntu](/en/blog/tags/planet-ubuntu/)
[sdk](/en/blog/tags/sdk/) [ubuntu-sdk](/en/blog/tags/ubuntu-sdk/)





## Comments

No comments yet.

## Add your comment

Name:

Email address:

URL:

Comment:

If you enter anything in this field your comment will be treated as spam:





