#import socket module
from socket import *
import sys #in order to terminate program

#welcoming socket
serverSocket = socket(AF_INET, SOCK_STREAM)
#prepare a serverSocket
serverPort = 80  #80 port for http servers
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("using port number:", serverPort)

while True:
    #establish connection
    print('Ready to server...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()  #read bytes from socket
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()                           #read page

        #send one HTTP header line into serverSocket
        ## TODO:
        #on success
        connectionSocket.send('\nHTTP/1.1 200 OK\n\n'.encode())
        connectionSocket.send(outputdata.encode())
        print("data from the page: ", outputdata)

        #send the content of requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())

        connectionSocket.close()

    except IOError:
        #send response message for file not found
        ## TODO:
        connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n'.encode())
        #close client serverSocket
        ## TODO:
        connectionSocket.close()

    serverSocket.close()
    #terminate the program after sending coreesponding data
    sys.exit()
