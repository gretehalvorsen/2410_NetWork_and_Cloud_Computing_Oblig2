from socket import *
import _thread as thread
import time
import sys 

def now():
    #Returns the current time
    return time.ctime(time.time())

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