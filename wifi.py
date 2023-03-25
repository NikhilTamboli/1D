import socket
import struct


HOST = '0.0.0.0'
PORT = 8888       # Port to listen on
 
# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# Bind the socket to a specific address and port
server_socket.bind((HOST, PORT))
 
# Listen for incoming connections
server_socket.listen(1)
print('Listening on {}:{}'.format(HOST, PORT))
 
while True:
    # Accept incoming connections
    client_socket, address = server_socket.accept()
    # print('Connection from {}'.format(address))
 
    # Receive float data from client
    data = client_socket.recv(1024)
    # float_data=float(data.decode())
    float_data = struct.unpack('f', data)[0]
    # print('Received: {}'.format(float_data))
    print(f"{float_data:.3f}")
 
    # Close the connection
    client_socket.close()