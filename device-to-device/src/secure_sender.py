#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 17:49:44 2020

@author: akshayjoshi
"""

import time
import socket
import ssl
import pprint
import sys

HOST = '172.20.10.4'  # The server's IP address
PORT = 65429        # The port used by the server

#client_key='/Users/akshayjoshi/Documents/UCLA/Fall20/CS211/IoT_Project/11-iot-platform/device-to-device/data/certs/device2laptop_key.pem'
#client_cert='/Users/akshayjoshi/Documents/UCLA/Fall20/CS211/IoT_Project/11-iot-platform/device-to-device/data/certs/device2laptop_cert.pem'

ca_certloc='/Users/akshayjoshi/Documents/UCLA/Fall20/CS211/IoT_Project/11-iot-platform/device-to-device/data/certs/server_cert.pem'

context = ssl.SSLContext(ssl.PROTOCOL_TLS)
context.verify_mode = ssl.CERT_REQUIRED
context.check_hostname = True
context.load_verify_locations(ca_certloc)

txdata='Lo and Behold'
print(sys.getsizeof(txdata))
try:
    t=time.time()
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #wrappedSocket=ssl.wrap_socket(s, keyfile=client_key, certfile=client_cert, server_side=False, cert_reqs=CERT_REQUIRED, ssl_version=PROTOCOL_TLS, ca_certs=ca_certloc)
    wrappedSocket=context.wrap_socket(s, server_hostname='AJ')
    wrappedSocket.connect((HOST, PORT))
    print('The time taken to authenticate the server is %f' %(time.time()-t))
    cert=wrappedSocket.getpeercert()
    pprint.pprint(cert)
    wrappedSocket.sendall(b'Lo and Behold!')
    data = wrappedSocket.recv(1) # 'Message received by the server. Trying to send it to the receiver.'
    print(data)
    data = wrappedSocket.recv(1) #
    print(data)

finally:
    wrappedSocket.close()
