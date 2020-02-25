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
    # Start webhost server
    socketio.run(app, host="0.0.0.0", port="1337")
