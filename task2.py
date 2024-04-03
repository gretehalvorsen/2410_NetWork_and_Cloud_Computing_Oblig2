import argparse
from socket import *
'''
The main function is used to create an HTTP GET request, send it to a server, 
receive the server's response, and print that response. The main function takes server_ip, 
server_port and filename as arguments. The function doesn't return anything. 
But it prints the response received from the server to the console.'''

def main(server_ip, server_port, filename):
    # Create a TCP client socket
    client_sd = socket(AF_INET,SOCK_STREAM) 
    # The socket connects to the server specified by server_ip and server_port 
    client_sd.connect((server_ip, server_port)) 

    # Create a GET request. The request asks for the file specified by filename
    request = 'GET {} HTTP/1.0\r\n\r\n'.format(filename)
    #Sends the request to the server
    client_sd.send(request.encode())

    # Read data from the socket
    received_line = client_sd.recv(1024).decode()
    # The received data is printed to the console
    print(received_line)
	
    # Close the connection
    client_sd.close()

# Setup command line arguments. argparse is used to handle the command line arguments.
parser = argparse.ArgumentParser()	
parser.add_argument('-i', '--server_ip', type=str, required=True, help='Sever IP address')
parser.add_argument('-p', '--server_port', type=int, required=True, help='Server port number')
parser.add_argument('-f', '--filename', type=str, required=True, help='Name of file')

# The command line arguments are parsed
args = parser.parse_args()


if __name__=='__main__':
    # The server IP address, port number and filename are passed from the command line arguments to the main function
    main(args.server_ip, args.server_port, args.filename)