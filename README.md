# IoT Platform

The Internet of Things (IoT) is becoming an active technology topic in recent years. The
IoT platforms manage IoT devices(sensors) and connect devices and data networks. In
this project, you will build a simple IoT platform.

**Topic: Device-application communication**

- Read through the documents about IoT platforms, e.g., [AWS IoT](https://aws.amazon.com/iot/), [Google IoT](https://cloud.google.com/solutions/iot#:~:text=Google%20Cloud%20IoT%20is%20a,for%20all%20your%20IoT%20needs), and [DeviceHive](https://www.hologram.io/). Understand the key features of the IoT platform.

- Implement a prototype of an IoT platform that can establish reliable and secure device-application communication. This prototype should include the following modules:

    - Reliable communication. The application controls the IoT devices remotely, and devices send sensory data to the application. (The platform should handle the situation that the device goes to IDLE mode)

    - Authentication.

    - Encryption and integrity checking.

- You can build the IoT platform on your own laptop/PC and use mobile phones to simulate the IoT devices. You may use python security libraries, e.g., [SSL](https://docs.python.org/2/library/ssl.html). Also, you can try with existing open-source platforms, e.g., [DeviceHive](https://www.hologram.io/).

- *Optional: optimize your platform for LTE/LTE-M/nb-IoT network and IoT traffic with small packets.

**How to run the server** 
 - Go to ./src/server
 - run "pip3 install -r requirements.txt"
 - run "gunicorn main:app"

 Note - The most upto date server is running on Heroku. 
