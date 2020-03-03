import socket
import threading
import logging
from modules.gui_coms import app, socketio

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

""" 
TODO:
- Add swal
- Have a connected status icon in the corner of dash
"""

if __name__ == '__main__':
    # Start webhost server
    socketio.run(app, host="0.0.0.0", port="1337")
