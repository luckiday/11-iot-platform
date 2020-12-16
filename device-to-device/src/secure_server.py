import socket
import ssl
import time
import sys


HOST = ''
sender_client_port = 65429        # Port to listen on (non-privileged ports are > 1023)
receiver_client_port= 65430       # Port to send data to

server_cert='/home/pi//Desktop/certs/server_cert.pem'
server_key='/home/pi/Desktop/certs/server_key.pem'
ca_certlocs='/Desktop/certs/device2laptop_cert.pem'
context=ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile=server_cert, keyfile=server_key)

s_sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_sender.bind((HOST, sender_client_port))
s_sender.listen(1)
#wrappedSocket=ssl.wrap_socket(s_sender, keyfile=server_key, certfile=server_cert, server_side=True,cert_reqs= CERT_REQUIRED, ssl_version=PROTOCOL_TLS, ca_certs=ca_certlocs)

s_receiver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_receiver.bind((HOST, receiver_client_port))
s_receiver.listen(1)
s_receiver.settimeout(10)

while True:
    print('Waiting for sender to connect')
    sender_conn, sender_addr = s_sender.accept()
    print('Connected by', sender_addr)
    sender_conn=context.wrap_socket(sender_conn,server_side=True)
    rx_data = sender_conn.recv(3)
    tx_data = rx_data
    print('Received data from the sender device. Trying to send it to the receiver device..')
    sender_conn.sendall(b'Message has been received by the server. The server is trying to send it to the receiver..')
    #print('Waiting for receiver to connect')
    #receiver_conn, receiver_addr = s_receiver.accept()
    #print('Connected by', receiver_addr)
    try:
	receiver_conn, receiver_addr = s_receiver.accept()
        print('Connected by', receiver_addr)
	receiver_conn = context.wrap_socket(receiver_conn, server_side=True)
	receiver_conn.sendall(tx_data)
	ack=receiver_conn.recv(1)
	print(ack)
	sender_conn.sendall(b'Message has been received by the receiver device.')
        print('One end-to-end transmission and reception successful.')
    except socket.timeout, e:
	err=e.args[0]
	if err == 'timed out':
            time.sleep(1)
            print('Waited for 10 seconds. Receiver offline. Retry later.')
	    sender_conn.sendall(b'Waited for 10 seconds. Receiver offline. Retry later')
