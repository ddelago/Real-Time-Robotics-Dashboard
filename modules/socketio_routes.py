from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from modules.controller import Controller
from modules.rover import Rover 
import threading
import time

app = Flask(__name__, template_folder='../templates', static_folder='../static')
socketio = SocketIO(app)
controller = Controller()
rover = Rover()

@app.route('/')
def entry():
    return render_template('index.html')

@socketio.on('message')
def handle_message(payload):
    print('received message: ', payload)

@socketio.on('connect')
def on_connect():
    print("socketio has connected")
    payload = dict(data='Connected')
    emit('data', payload)

@socketio.on('connect_to_rover')
def on_connect_to_rover(payload):
    rover.connect(payload['ip'], payload['port'])

@socketio.on('connect_controller')
def on_connect_controller():

    if(not controller.is_available()):
        payload = dict(data='Error: No controller available')
        emit('data', payload)
        return

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