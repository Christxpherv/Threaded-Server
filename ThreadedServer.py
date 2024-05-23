#import socket module
from socket import *
# to terminate the program
import sys 
# support for threading
import threading

def handle(connectionSocket):
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        
        #Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\n\n".encode())

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
            
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:

        #Send response message for file not found
        connectionSocket.send("\nHTTP/1.1 404 Not Found\n\n".encode())

        #Close client socket
        connectionSocket.close()

#Prepare a sever socket
serverSocket = socket(AF_INET, SOCK_STREAM)
port = 6789
serverSocket.bind(('', port))
serverSocket.listen(5)

while True:
    print('ready to serve...')
    connectionSocket, addr = serverSocket.accept()

    #create a new thread to handle the request
    t = threading.Thread(target=handle, args=(connectionSocket,))
    t.start()

serverSocket.close()
sys.exit()