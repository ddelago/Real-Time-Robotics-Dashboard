import socket
import threading
import logging
from modules.socketio_routes import app, socketio

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

""" 
TODO:
- Add swal
- Have a connected status icon in the corner of dash
- Look at arduino packet structure
- Look at other dashboards
"""

if __name__ == '__main__':
    # Socket initialization
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 5001
    server.bind((host, port))

    # Create thread for socket server
    t1 = threading.Thread(target=socket_listen, args=(server,), daemon=True)
    t1.start()

    # Start webhost server
    socketio.run(app)
