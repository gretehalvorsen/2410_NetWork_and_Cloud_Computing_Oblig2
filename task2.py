import argparse
from socket import *

def main(server_ip, server_port, filename):
	
    # Create a TCP client socket
    client_sd = socket(AF_INET,SOCK_STREAM) 
    # Connect to the server 
    client_sd.connect((server_ip, server_port)) 

    # Create GET request
    request = 'GET {} HTTP/1.0\r\n\r\n'.format(filename)
    #Sends the request to the server
    client_sd.send(request.encode())

    # Read data from the socket
    received_line = client_sd.recv(1024).decode()
    print(received_line)
	
    # Close the connection
    client_sd.close()

#Setup command line arguments
parser = argparse.ArgumentParser()	
parser.add_argument('-i', '--server_ip', type=str, required=True, help='Sever IP address')
parser.add_argument('-p', '--server_port', type=int, required=True, help='Server port number')
parser.add_argument('-f', '--filename', type=str, required=True, help='Name of file')

args = parser.parse_args()


if __name__=='__main__':
    main(args.server_ip, args.server_port, args.filename)