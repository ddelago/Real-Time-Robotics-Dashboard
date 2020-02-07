from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import threading
import time
from modules.controller import Controller 

# TODO: Handle error for when controller is not connected
# TODO: Handle case where client asks to connect controller but controller already connected
# TODO: Add more checks (is_controller_connected, etc)

app = Flask(__name__, template_folder='../templates', static_folder='../static')
socketio = SocketIO(app)
controller = Controller()

@app.route('/')
def entry():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    print('received message: ', message)

@socketio.on('connect')
def on_connect():
    print("socketio has connected")
    payload = dict(data='Connected')
    emit('data', payload)

@socketio.on('page_change')
def on_page_change(message):
    page = message['page']
    current_page = page

@socketio.on('connect_controller')
def on_connect_controller():
    # Start controller
    controller.init_joystick()
    controller_thread = threading.Thread(target=controller.start, daemon=True )
    controller_thread.start()

    # Begin stream
    if(not controller.is_streaming):
        controller.is_streaming = True
        controller_stream = threading.Thread(target=emit_controller_state, daemon=True )
        controller_stream.start()

    # reply to client
    payload = dict(data='Controller connected')
    emit('data', payload)

@socketio.on('get_controller_state')
def on_get_controller_state():
    controller.start_stream()

@socketio.on('pause_controller_state')
def on_pause_controller_state():
    controller.stop_stream()

@socketio.on('stop_controller')
def on_stop_controller():
    controller.stop()

def emit_controller_state():
    while(controller.is_streaming):
        payload = dict(data=controller.get_values())
        socketio.emit('data', payload)
        time.sleep(.100)