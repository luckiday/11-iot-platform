# Project Template
Template for project management

Build server docker on port 5000

- Build image `docker build -t restful-api .`
- Run container in detached mode and publish port 5000 `docker run -d -p 5000:5000 restful-api`
- API should be accessible on port 5000 `curl -i localhost:5000/api/messages`


Server API
- /api/messages - Get or Post current messages in server
- /api/messages/message_id - Get target message in server
- /api/devices - Get or Post devices connected to server
- /api/devices/device_id - Get selected device if it exists in server

Run Client on specified Port at local IP
 *Currently working on running on docker port, run local env with python app.py*
 *Run by python.app.py --deviceID <IP of target device to send message> --message <Message you want to send to IP>
Client API
- /api/messages - Get or create message in client
  
To Do
- Message failing and recovery
- Encryption and security
