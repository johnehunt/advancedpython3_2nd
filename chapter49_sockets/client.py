import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Set a timeout value of 1 second
clientSocket.settimeout(1)

addr = ("127.0.0.1", 8085)
clientSocket.sendto('ping'.encode(), addr)

try:
    data, server = clientSocket.recvfrom(1024)
    print(data.decode())     
 
except Exception as exp:
    print(exp)

