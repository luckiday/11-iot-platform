# Project Template
Template for project management

Run Server
- Go to server folder /src/Server
- Run server with python3 app.py

Server will be running on http://localhost:8000/

Server API
- /api/messages - Get or Post current messages in server
- /api/messages/message_id - Get target message in server
- /api/devices - Get or Post devices connected to server
- /api/devices/device_id - Get selected device if it exists in server

Run Client
- Run Client at /src/Server
- python3 app.py

Can interact with client at http://localhost:5000/

Marks current Device ID
List of messages received by device
Dropdown of all devices currently in server. Can connect multiple devices, using the same client app.py.
  
To Do
- Message failing and recovery
