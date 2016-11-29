





#  [Using Eclipse IOT 101 : MQTT will get you started on your IoT
journey](/en/blog/2015/11/12/using-eclipse-iot-101-mqtt-will-get-you-started-
your-iot-journey/)

![](/static/devportal_uploaded/5f64a2b7-6fa9-4cab-a315-837cdc8bf611-3e22b70a-d
372-464d-b279-ee92a2e5ce53-media/2015/11/12/paho_logo_400.png)The [Eclipse
Foundation](http://eclipse.org) has become a new home for a number of IoT
projects. For the newcomers in the IoT world it’s always hard to see the
forest for the trees in the number of IoT related Eclipse projects. So here is
a first blog to get you started with IoT development using Eclipse technology.

The place to start with IoT development is [MQTT](http://mqtt.org/) (Messaging
Queuing Telemetry Transport). MQTT is a messaging protocol used to send
information between your Things and the Cloud. It’s a bit like the REST API of
the IoT world, it’s standardised and supported by most clients, servers and
IOT Backend As A Service (BaaS) vendors ([AWS
IOT](https://aws.amazon.com/iot/), [IBM Bluemix](https://www.ibm.com/cloud-
computing/bluemix/solutions/iot/), [Relayr](https://developer.relayr.io/),
[Evrything](https://evrythng.com/) to name a few).

If you’re not familiar with MQTT here is a quick rundown of how it works:

  * MQTT was created for efficient and lightweight message exchanges between Things (embedded devices / sensors).

  * An MQTT client is typically running on the embedded device and sends messages to an MQTT broker located on a server.

  * MQTT messages are made of 2 fields a topic and a message.

  * MQTT clients can send (publish in MQTT linguo) messages on a specific topic. Typically a light in my kitchen would send a message of this type to indicate it’s on: `topic =”Thibaut/Light/Kitchen/Above_sink/pub” message=”on”`.

  * MQTT clients can listen (subscribe in MQTT linguo) to messages on a specific topic. Typically a light in my kitchen would subscribe to messages to await for instruction to be turned off by subscribing to the `topic =”Thibaut/Light/Kitchen/Above_sink/sub” `and waiting for a `message: message=”turn_off”`.

  * MQTT brokers listen to incoming messages and retransmit the messages to clients subscribed to a specific topic. In this way it resembles a multicast network.

  * Most MQTT brokers are running in the cloud but increasingly MQTT brokers can be found on IoT gateways in order to do message filtering and create local rules for emergency or privacy reasons. For example a typical local rule in my house would be if a presence sensor in the kitchen sends a message saying that no one is in the kitchen a simple rule would send a message to the light to switch it. Our rules engine would look like: if receive message: `topic=”Thibaut/presence_sensor/Kitchen/pub” message =”No presence”` then send message on `topic =”Thibaut/Light/Kitchen/Above_sink/sub” with message=”turn_off”`

  * BaaS vendors would typically offer a simple rules engine sitting on top of the MQTT broker, even though most developers would probably build their rules within their code. Your choice!

  * To get started Eclipse provides multiple MQTT client under the [Paho project](https://eclipse.org/paho/)

  * To get started with your own broker Eclipse provides an MQTT broker under the [Mosquitto project](http://www.eclipse.org/mosquitto/)

  * Communication between MQTT client and broker supports different level of authentication from none to using public /private keys through username / password

  * When using a public MQTT broker (like the Eclipse sandbox) your messages will be visible to all people who subscribe to your topics so if you’re going to do anything confidential make sure you have your own MQTT broker (either through a BaaS or build your own on a server).

That’s all there is to know about MQTT! As you can see it’s both simple and
powerful which is why it’s been so successful and why so many vendors have
implemented it to get everyone started with IoT.

And now is your time to get started!! To help out here’s a quick example on
[Github](https://github.com/campbieil/mqtt-for-ubuntu-core) that shows you how
you can get the Paho Python MQTT running on Ubuntu Core and talking to the
Eclipse Foundation MQTT sandbox server. Have a play with it and tell us what
you’ve created with it!

[Thibaut Rouffineau](/en/blog/authors/thibautr/)

Nov. 12, 2015

Filed under: [mqtt](/en/blog/tags/mqtt/) [planet-ubuntu](/en/blog/tags/planet-
ubuntu/) [ubuntu-core](/en/blog/tags/ubuntu-core/)





## Comments

No comments yet.

## Add your comment

Name:

Email address:

URL:

Comment:

If you enter anything in this field your comment will be treated as spam:





