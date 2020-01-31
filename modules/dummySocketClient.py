# Import socket module
import socket
import time
import random

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 5001

# connect to the server on local computer
s.connect(('127.0.0.1', port))

count = 0
# Send message to server and recieve response
while True:
    count += 1
    message = str(count)
    s.sendall(message.encode())

    if count == 100:
        count = 0
    time.sleep(.100)

# close the connection
s.close()
