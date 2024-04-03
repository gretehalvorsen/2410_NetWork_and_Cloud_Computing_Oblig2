#import socket module
from socket import *
import sys # In order to terminate the program

'''
This script sets up a basic HTTP server that can accept connections from clients, 
send responses back. It uses try/except to handle errors. The server can handle one request at a time. 
After serving a file or handling an error, it goes back to waiting for another connection. 
The server keeps running until manually stopped.
'''
#Prepare a server socket
serverSocket = socket(AF_INET, SOCK_STREAM)
port = 8000
server_ip=  '127.0.0.1'
serverSocket.bind((server_ip, port))
serverSocket.listen()

while True:
    #Establish the connection 
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    
    
    try:
        #Get the client request
        message = connectionSocket.recv(1024).decode()
        #Get the file name
        filename = message.split()[1]
        # If the filename is root, redirect to index.html
        #if filename == '/':
        #    filename = '/index.html'
        #Open and read the file
        f = open(filename[1:])
        #Send one HTTP header line into socket
        outputdata = f.read()
        encoding = 'ascii'
        connectionSocket.send(bytes('HTTP/1.0 200 OK\r\n', encoding))
        connectionSocket.send(bytes('Content-Type: text/html\r\n\r\n', encoding))

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
        
    except IOError:
        #Send response message for file not found
        outputdata = b'HTTP/1.0 404 NOT FOUND\n\nFile Not Found'
        connectionSocket.send(outputdata)
        #Close client socket
        connectionSocket.close()

#Close server socket
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data