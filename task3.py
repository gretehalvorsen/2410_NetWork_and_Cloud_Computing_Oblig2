from socket import *
import _thread as thread
import time
import sys 

#Function that use the time library to return the current time
def now():
    return time.ctime(time.time())

'''
The handleClient() function will process a single client request on a given socket connection.
It takes one argument, the connectionSocket which represents the socket connection between 
the server and client. The function uses this connection to receive a file request from the 
client, send a response back to the client, and ultimately close the connection.

The function has a try/except block to handle IOError exceptions.

The function does not return any value, because its purpose is to carry out a series of operationsing
not to compute a result.
'''
def handleClient(connectionSocket):
    try:
        #Get the client request
        message = connectionSocket.recv(1024).decode()
        #Get file name
        filename = message.split()[1]
        #if filename is root, redirect to index.html
        if filename == '/':
            filename = '/index.html'
        #Open and read file    
        f = open(filename[1:])
        #Send one HTTP header line to socket
        outputdata = f.read()
        encoding = 'ascii'
        connectionSocket.send(bytes('HTTP/1.0 200 OK\r\n', encoding))
        connectionSocket.send(bytes('Content-Type: text/html\r\n\r\n', encoding))

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
    except IOError:
        #Send response message if file does not exist
        outputdata = b'HTTP/1.0 404 NOT FOUND\n\nFile Not Found'
        try:
            connectionSocket.send(outputdata)
        except:
            pass
    finally:
        #Close client socket
        connectionSocket.close()

'''
The main() function sets up a server that listens for incoming connections on port 8000.
When a connection is established, it creates a new thread to handle the client's request, 
allowing for concurrent processing of multiple client requests.

The function includes a try/except block to handle exceptions.
If an exception occurs it prints an error message and exits the program.

The function does not return a value. Its purpose is to set up the server and manage 
incoming client connections'''
def main():
    #Creates a server socket, listens for new connections and
    #spawns a new thread whenever a new connection join
    serverPort = 8000
    serverSocket = socket(AF_INET,SOCK_STREAM)
    try:
        serverSocket.bind(('',serverPort))
        print('Ready to serve...')
    except: 
        print("Bind failed. Error : ")
        sys.exit()
    serverSocket.listen(1)
    
    while True:
        connectionSocket, addr = serverSocket.accept() 
        print('Server connected by ', addr, 'at', now())
        thread.start_new_thread(handleClient, (connectionSocket,))
       
    serverSocket.close()

if __name__ == '__main__':
    main()