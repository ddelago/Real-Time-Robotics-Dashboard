import logging
from modules.gui_coms import app, socketio

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

"""
TODO: Add a Python executable
"""
if __name__ == '__main__':
    # Start webhost server
    socketio.run(app, host="0.0.0.0", port="1337")
