from flask import Flask, render_template
import socket
import threading
app = Flask(__name__)

@app.route('/')
def entry():
    return render_template('index.html')                
  
# Handle Socket Connections from Clients
def handle_client_connection(client_socket, address):
    print('Accepted connection from {}:{}'.format(address[0], address[1]))
    while True:
        # Receiving from client
        data = client_socket.recv(1024)
        print('{}:{} sent: {}'.format(address[0], address[1], data))

        # If no data, connection was lost
        if not data:
            print('Connection to {}:{} lost.'.format(address[0], address[1]))
            break
    
    # Close connection to client
    client_socket.close()

def initializeSocket():
    # Socket initialization
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 5001                
    server.bind((host, port))         
    
    # Listen for connection to the server 
    server.listen()      

    # Create sockets to clients
    while True:
        # Accept connection from the client
        client_sock, address = server.accept()

        # Each client gets their own thread
        client_handler = threading.Thread(
            target=handle_client_connection,
            args=(client_sock,address,)
        )

        # Begin the client thread
        client_handler.start()

if __name__ == '__main__':
    # Creating thread for socket io
    t1 = threading.Thread(target=initializeSocket, daemon=True) 
    t1.start() 
    
    # Start webhost server
    app.run(host='127.0.0.1')