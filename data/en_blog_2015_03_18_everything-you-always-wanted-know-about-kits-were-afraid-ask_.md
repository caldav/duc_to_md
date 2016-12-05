





#  [Everything You Always Wanted to Know About Kits But Were Afraid toAsk](/en/blog/2015/03/18/everything-you-always-wanted-know-about-kits-were-afraid-ask/)

So if you are new to QtCreator the first thing that freaks you out will be the
concept of Kits. Yes it does look complicated, big and you might want to ask
why do I need this.

## ![](/static/devportal_uploaded/e4fcc5b7-5485-4a92-b914-a5cbcd0f6575-2013f70b-3096-4f88-b684-cb883dd1267e-media/2015/03/18/options.jpg)

## Right, let’s take few steps back and look at the bigger picture.

Most programmers start their hobby or carrier with basic (not that one) pc
programming. You have the compiler and libraries on your machine, you start
hacking around with your code and once you think it will pass at least the
syntax check you go to the terminal, compile the code and be happy when you
see the binary executable. If it runs without segfaults then you start to gain
confidence and you are the happiest kid on Earth once the program does what
you coded it for.

That is a fairly simple and common scenario, still it has all the components
what actually make an SDK. And i guess you know that in the SDK, the K stands
for Kit.

Let’s continue with this thinking. You want to show the program to your
friends. That is nothing strange, even coders are social beings. If your
program is using dynamically linked libraries from the system then your
friends need a bit of luck to have the very same system libraries on their
machine as you have on yours. Not to mention that you compiled your program
for one specific processor architecture and nothing guarantees that your
friends have the same architecture as you had.

So, we are safe and good as long our program stays on our computer but trouble
with libraries, binary compatibility and processor architecture will pop up
when we want to move our program around without recompiling it again. And
imagine, we are still talking about PC to PC porting. Let’s raise the bar.

How does it go when you want to write an application for a mobile device? Most
likely your computer is an x86 based PC and these days most mobile devices
have some sort of ARM processor. So, here we go, our native local compiler
what made us so happy just few paragraphs back is now obsolete and we will
need a compiler what can produce an ARM binary for the specific device. It
could be armv6, armv7 or whatever exotic ARM processor your target device is
built with. Good, we now have a compiler but our code is still using a bunch
of libraries. In the Ubuntu world and specially with the ultimate convergence
on our roadmap this part of the story is a bit easier and will get even better
soon. But still if your PC is running the LTS Ubuntu release (14.04 right now)
you do not necessarily expect the same libraries and header files being
present on your machine as on a target device what is on 15.04 or even newer.

I guess at this point many would say with a disappointed tone that after you
learned that your good old compiler is obsolete now all your locally installed
development libraries and header files are useless too. Think of Borat saying
“nice”.

Okay, so we are left without compiler, libraries and header files. But they
should come from somewhere, right?

And that is where the Kits come into the picture. The official definition of
the QtCreator Kits sure sounds a bit academic and dry, so let’s skip it. In
short, Kits are the set of values that define one environment, such as a
device, compiler, Qt version, debugger command, and some metadata.

I love bicycling so I use cycling analogies whenever it is possible. Imagine
that you are in the mood to have a ride downhill in the forest. You will take
your mountain bike, knee and elbow pad, lots of water, some snacks and your
clothes what take dirt better, a massive helmet and your camera. If you just
cycle to your office you take your city bike, lighter helmet and you put on
regular street wear. Different target, different set of equipment. How cool it
would be just to snap your finger and say out loud “ride to the city” and all
the equipment would just appear in front of you.

![](/static/devportal_uploaded/00213277-f20d-407b-9f29-f195ab6be5a8-b0a15034-154f-487c-a48d-ad922e27dc99-media/2015/03/18/scope-with-targets.jpg)That is
exactly what happens when you have Kits set up in your QtCreator and you are
building your application for and running them on different targets.

QtCreator is an IDE and developers who choose to work with IDEs do expect a
certain level of comfort. For example we do not want to resolder and rewire
our environment just because we want to build our project for a different
target. We want to flip a switch and expect that the new binaries are made
with a different compiler against a different set of libraries and headers.
That is what QtCreator’s target selector is for. You simply change from the
LTS Desktop Kit to the 15.04 based armhf target and you have a whole different
compiler toolchain and API set at your service.

At this point Kits looks pretty and easy. You might ask what is the catch
then. Why IDEs and SDKs do not come with such cool and well integrated Kits?
Well there is a price for every cool feature. At this moment each Kit in ready
for action state is about 1.7GB. So kits are big and the SDK does not know
what Kits you want to use. What means is that if we want to install all kits
you might use the SDK would be 8-10GB easily.

## Why kits are so big and can they be made smaller?

![](/static/devportal_uploaded/c9b456ea-a8f8-492d-a664-2cbc7559b814-927ea5a9-21c3-4478-8ab3-eb717cbe8e9f-media/2015/03/18/ubuntu-options.jpg)That is a fair
question I got very often. First of all, the kits are fully functional chroots
in the case of the Ubuntu SDK. It means that other than the compiler toolchain
we have all the bells and whistles one needs when entering a chroot. Just
enter the click chroot and issue the dpkg -l command to see that yes, we do
have a full blown Ubuntu under the hood. In our SDK model the toolchain and
the native developer tools live in the click chroots and these chroots are
bootstrapped just as any other chroot. It means that each library, development
package and API is installed as if it were installed on a desktop Ubuntu. And
that means pulling in a good bunch of dependencies you might not need ever.
Yes, we are working on making the Kits smaller and we are considering to
support static kits next to the present dynamic bootstrapped kits.

Alright, so far we have covered what Kits are, what they contain. The most
important question is do you need to care about all of these? Do you need to
to configure and set up these kits yourself. Luckily the answer to these
questions is no.

In the Ubuntu SDK these Kits are created on the first start of the SDK and set
up automatically when a new emulator is deployed or a new device is plugged
in. Of course you can visit the builder chroots under the Ubuntu and Build &
Run sections in the dialog what opens with the Tools->Options… menu. But most
of the application developers can be productive without knowing anything about
these. Of course understanding what they are is good and if you are into
development tools and SDKs then it is fun to look behind the curtains a bit.

[Zoltán Balogh](/en/blog/authors/bzoltan/)

March 18, 2015

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





