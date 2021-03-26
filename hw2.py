#import socket module
from socket import *
import sys #in order to terminate program

serverSocket = socket(AF_INET, SOCK_STREAM)
#prepare a serverSocket
#to do



while True:
    #establish connection
    print('Ready to server...')
    connectionSocket, addr =
    try:
        message =
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata =

        #send one HTTP header line into serverSocket
        ## TODO:

        #send the content of requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())

        connectionSocket.close()

    except IOError:
        #send response message for file not found
        ## TODO:


        #close client serverSocket
        ## TODO:

    serverSocket.close()
    #terminate the program after sending coreesponding data
    sys.exit()
        
