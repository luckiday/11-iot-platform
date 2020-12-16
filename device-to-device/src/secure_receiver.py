import socket
import ssl
import pprint

HOST='172.20.10.4' # Server's IP address
PORT=65430 # Port used by the server

ca_certloc='/home/pi/Desktop/certificates/server_cert.pem'

context = ssl.SSLContext(ssl.PROTOCOL_TLS)
context.verify_mode = ssl.CERT_REQUIRED
context.check_hostname = True
context.load_verify_locations(ca_certloc)

try:
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #wrappedSocket=ssl.wrap_socket(s, keyfile=client_key, certfile=client_cert, server_side=False, cert_reqs=CERT_REQUIRED, ssl_version=PROTOCOL_TLS, ca_certs=ca_certloc)
    wrappedSocket=context.wrap_socket(s, server_hostname='AJ')
    wrappedSocket.connect((HOST, PORT))
    cert=wrappedSocket.getpeercert()
    pprint.pprint(cert)
    data = wrappedSocket.recv(3) # 'Hello, world!'
    print('Received data:', repr(data))
    wrappedSocket.sendall(b'Message received')

finally:
    wrappedSocket.close()
