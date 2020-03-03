from flask import Flask, render_template, Response
from flask_socketio import SocketIO, emit
from modules.controller import Controller
from modules.rover_coms import Rover
import threading
import time

""" 
TODO: 
- Catch controller/server is/not connected errors
- Add swal
- Have a connected status icon in the corner of dash
"""

app = Flask(__name__, template_folder='../templates', static_folder='../static')
socketio = SocketIO(app)
controller = Controller()
rover = Rover(socketio, controller)

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

@socketio.on('activate_led')
def on_activate_led(payload):
    rover.send_command('led', [payload['data']])

@socketio.on('connect_controller')
def on_connect_controller():
    if(not controller.is_available()):
        emit('controller_status', dict(data='False'))
        return

    # Start controller
    controller.init_joystick()
    controller_thread = threading.Thread(target=controller.start, daemon=True )
    controller_thread.start()

    # Begin streaming controller
    if(not controller.is_streaming):
        controller.is_streaming = True
        # Stream to GUI
        controller_stream = threading.Thread(target=emit_controller_state, daemon=True )
        controller_stream.start()
        
        # Stream to rover
        drive_stream = threading.Thread(target=rover.send_drive, daemon=True )
        drive_stream.start()

    # reply to GUI client
    emit('controller_status', dict(data='True'))

@socketio.on('disconnect_from_rover')
def on_disconnect_from_rover():
    rover.listen = False
    rover = None
    controller.stop_stream()
    controller.stop()
    controller.exit()

@socketio.on('send_controller_state')
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
        payload = dict(drive=controller.axis[2], steer=controller.axis[0])
        socketio.emit('controller_data', payload)
        time.sleep(.100)
