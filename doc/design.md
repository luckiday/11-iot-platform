## Design Draft of Project xxx

### Problem Statement

- Making a simple IoT device with sensors that can communicate with an application on
a different machine via the internet. There are three main components to this project.
1) The IoT device which has some sensor and internet capabilities.
2) The server communicates with the IoT device and acts like a web-server that can
cater to the user’s commands over the web.
3) The web client is a command-line interface that will allow the user to send control of the IoT device. 

### Challenge

- The following chalenges are experienced in building this system:
1) Light weigght client which cannot handle a lot of client side processsing. 
2) Ability to connect to the server whenever the device is online.
3) Abiliy to send small bt efficient data packets. 
4) The server should be able to notify the user if a device is not working. 
5) The server should be able to store the information revieced from the device. 
6) The data should be encrypted to prevent data leaks. 

### System Model and Solution

- The first choice taken was between the IoT framework to use. Over studying the
documentation of the Google IoT, AWS IoT, and Device hive, It was decide to use a simple custom flask rest api framework in place of a predefined IoT framework. The custom system is light and independednt of any cloud resources. 

The second choice was taken over the language for development. Python was selected to keep all the development in the same language. The raspberry device was selected as the IoT device due to its modularity which would allow us to use multiple and diverse sensors. 

The system implmented is a simple flask rest api server which uses jwt tokens to pass messages between the server and the client. each code base have a predefined secret as a enviromental variable whch is used to enncrypt the jwt token containing the message using the SHA-256 algorithm. The server is running on a free heroku instance found at https://cs211-server.herokuapp.com/. We have two rest routes a GET ad a POST message route. The client is a lightweight codebase which send thhe message to the server and gets the lastest message periodically. 

### Performance Analysis and Evaluations

- 

### Related Work

- 

