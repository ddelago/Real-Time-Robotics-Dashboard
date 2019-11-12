from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import socket
import threading
app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def entry():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    print('received message: ', message)

@socketio.on('connect')
def on_connect():
    payload = dict(data='Connected')
    emit('data', payload)

# Handle Socket Connections from Clients
def client_handler(client_socket, address):
    print('Accepted connection from {}:{}'.format(address[0], address[1]))
    while True:
        # Receiving from client
        data = client_socket.recv(1024)
        # print('{}:{} sent: {}'.format(address[0], address[1], data))

        # Emit to websocket client
        payload = dict(data=data.decode("utf-8"))
        socketio.emit('data', payload)

        # If no data, connection was lost
        if not data:
            print('Connection to {}:{} lost.'.format(address[0], address[1]))
            break

    # Close connection to client
    client_socket.close()

def socket_handler(server):
    # Listen for connection to the server
    server.listen()

    # Create sockets to clients
    while True:
        # Accept connection from the client
        client_sock, address = server.accept()

        # Each client gets their own thread
        client_thread = threading.Thread(
            target=client_handler,
            args=(client_sock,address,)
        )

        # Begin the client thread
        client_thread.start()

if __name__ == '__main__':
    # Socket initialization
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 5001
    server.bind((host, port))

    # Create thread for socket server
    t1 = threading.Thread(target=socket_handler, args=(server,), daemon=True)
    t1.start()

    # Start webhost server
    # app.run(host='127.0.0.1')
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    socketio.run(app)
