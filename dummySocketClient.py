# Import socket module 
import socket                
import time
  
# Create a socket object 
s = socket.socket()          
  
# Define the port on which you want to connect 
port = 5001
  
# connect to the server on local computer 
s.connect(('127.0.0.1', port)) 
  
# Send message to server and recieve response
while True:
    s.sendall(b'Hello, world')
    time.sleep(1)

# close the connection 
s.close()        