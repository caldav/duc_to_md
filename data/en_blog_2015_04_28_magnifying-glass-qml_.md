





#  [A magnifying glass in QML](/en/blog/2015/04/28/magnifying-glass-qml/)

To create sharp visual components, we need to make sure our renderings look
good at the pixel level. This is a common task and the terms _precision_ and
_pixel-perfectness_ have become ubiquitous in discussions among programmers
and designers at Canonical. In the last years, the industry started to
increase the pixel density of screens, _again_ (remember the CRT era),
resulting in a higher number of pixels within a specified space (see Retina
Display for instance). A consequence is that jaggies are less visible than
before because we are reaching the point where the pixels are small enough
that the eye is not able to detect them. In an idealized world of high density
screens that would completely remove the need of anti-aliasing algorithms to
smooth edges, but the fact of the matter is that we are not there yet and we
will still have to thoroughly inspect the quality of anti-aliasing algorithms
for a while.

![Handheld magnifying glass](/static/devportal_uploaded/6cb63f34-3bae-400f-93e3-c56946e6172c-48a2ff5a-6022-4ab5-805e-84814f44dc72-media/2015/04/28/handheld_magnifying_glass.jpg)

At a previous job, a colleague of mine used to keep a handheld magnifying
glass on his desk. I was quite amused to see him glued to his screen
validating the visual quality of commits with this thing. As the graphics
engine programmer, I barely remember the reason for which I never proposed the
inclusion of a software magnifier, it could be because of the overloaded
backlog we had to deal with at the time but I guess it actually was just out
of sheer mischief. Most desktop environments include a software magnifier, but
depending on its quality (efficiency and ease of use), it often makes sense to
integrate a custom magnifier directly in the application being developed (it
makes less sense to ship it in release builds though...). This article
explains how to implement an efficient one with QML using offscreen
framebuffers and shaders.

Offscreen framebuffers (exposed as FBOs in OpenGL), vertex shaders and
fragment shaders are now widely available in mobile and mid-range GPUs
allowing the creation of interesting real-time post-processing effects for
most devices on the market. Magnification, or to be more precise _zooming &
panning_ (magnification solely being the process of rendering an image at a
higher scale), is one of it. In low-level graphics programming terms, all it
takes is to do a first pass that renders the scene in a FBO and a second pass
that renders a texture mapped quad to the default framebuffer reading the FBO
as a texture. Image zooming and panning is a basic 2D scale and translate
transformation that can be efficiently implemented by tweaking the texture
coordinates used to sample the FBO at the second pass. The vertex shader,
executed for the 4 vertices making our quad, will easily take care of it using
a single multiply-add op (transformed_coords = scale * coords + translation)
and the hardware accelerated rasterizer and texture units will make the actual
rendering very efficient. In order to clearly distinguish the magnified
pixels, it is important to use a simple nearest neighbour filter. These low-
level bits are nicely exposed to QML through the
[_ShaderEffectSource_](http://doc.qt.io/qt-5/qml-qtquick-shadereffectsource.html) and [_ShaderEffect_](http://doc.qt.io/qt-5/qml-qtquick-shadereffect.html) items. The former allows to render a given Item to
a FBO and the latter provides support for quads rendered using custom vertex
and fragment shaders.

Here is the QML code of the magnifier:

`**import** QtQuick 2.4`

`**Item** {

_// Public properties._

**property** **Item** scene: **null**  
**property** **MouseArea** area: **null**`

` **id**: root

**visible**: scene != **null**  
**property** **real** __scaling: 1.0  
**property** **variant** __translation: Qt.point(0.0, 0.0)`

` _// The FBO abstraction handling our first offscreen pass._

**ShaderEffectSource** {  
**id**: effectSource  
**anchors.fill**: **parent**  
**sourceItem**: scene  
**hideSource**: scene != **null**  
**visible**: **false**  
**smooth**: **false** _// Nearest neighbour texture filtering._  
}`

`_ // The shader abstraction handling our second pass with the

// translation and scaling in the vertex shader and the simple

// texturing from the FBO in the fragment shader._

**ShaderEffect** {  
**id**: effect  
**anchors.fill**: **parent**  
**property** **real** scaling: __scaling  
**property** **variant** translation: __translation  
**property** **variant** texture: effectSource`

` **vertexShader**: _"

uniform highp mat4 qt_Matrix;

uniform mediump float scaling;

uniform mediump vec2 translation;

attribute highp vec4 qt_Vertex;

attribute mediump vec2 qt_MultiTexCoord0;

varying vec2 texCoord;

void main() {

texCoord =_`

`_ qt_MultiTexCoord0 * vec2(scaling)_`

`_ + translation;

gl_Position = qt_Matrix * qt_Vertex;

}"_

**fragmentShader**: _"  
uniform sampler2D texture;

uniform lowp float qt_Opacity;

varying mediump vec2 texCoord;

void main() {

gl_FragColor =_`

`_ texture2D(texture, texCoord) * qt_Opacity;

}"_

}`

` _// Mouse handling._

**Connections** {  
**target**: scene != **null** ? area : **null**  
[...]

}

}`

And here is how to use it:

`**import** QtQuick 2.4`

`**Item** {

id: root`

` **Item** {

**id**: scene  
**anchors.fill**: **parent**  
}`

` **ZoomPan** {

**id**: zoomPan  
**anchors.fill**: **parent**  
**scene**: scene  
**area**: mouseArea  
}`

` **MouseArea** {

**id**: mouseArea  
**anchors.fill**: **parent**  
**enabled**: **true**  
**hoverEnabled**: **true**  
**acceptedButtons**: Qt.AllButtons  
}

}`

Mouse handling has been snipped off the code for conciseness but it can be
studied directly from [_the code repository_](http://bazaar.launchpad.net/~loic.molinari/+junk/magnifier/view/head:/ZoomPan.qml#L49). One important point to
notice is that for zooming to be a pleasant experience, it has to be
implemented using a logarithmic scale as opposed to a linear scale. Each scale
value at a zooming level is the previous one multiplied by the desired scale
factor, so a scale factor of 2 and a zooming level n give a scale value of 2n.
Another point is that to scale an image up, the range of its texture
coordinates must be scaled down, this explains why the actual scaling is
inverted. So a scale value of 2n would give an actual scaling of 2-n. A bit
counterintuitive at first…

We’re done with the theory. Let’s have a look at the final result:

[![](/static/devportal_uploaded/7a44385e-e28e-41e5-9621-5990e1c06050-342bc7fe-071c-4cf1-ae0d-a18cecd0e1a6-media/2015/04/29/magnifier_video.png)](https://you
tu.be/ycAqPeJ4SAM)

This technique helped me in the making of several visual elements, I would be
glad if other programmers find it useful too. Zooming and panning is a very
common feature in image viewers, the technique could be adapted for that use
case too (with potentially some tweaks to support tiling of big pictures).
Maybe that would be a good addition to the Ubuntu UI toolkit, don’t hesitate
to ask if you would like official support for it.

The source code is available on launchpad:

`$ bzr branch [_lp:~loic.molinari/+junk/magnifier_](https://code.launchpad.net/~loic.molinari/+junk/magnifier)`

[Loïc Molinari](/en/blog/authors/loic.molinari/)

April 28, 2015

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





