from flask import Flask, render_template
import socket
app = Flask(__name__)

data = ''

@app.route('/')
def hello_world():
    return render_template('index.html')                
  
def initializeSocket():
    # Socket initialization
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 12345                
    s.bind((host, port))         
    
    # put the socket into listening mode 
    s.listen()      

    # Establish connection with client. 
    c, addr = s.accept()      
    print('Got connection from', addr)
    
    while True: 
        data = c.recv(1024)

    # Close the connection with the client 
    c.close() 

if __name__ == '__main__':
    initializeSocket()
    app.run(host='0.0.0.0')