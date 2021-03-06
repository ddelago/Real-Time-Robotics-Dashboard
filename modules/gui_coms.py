import time
import threading
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from modules.controller import Controller
from modules.rover_coms import Rover

"""
TODO: 
- Add swal when connected to rover/etc
- Have a connected status icon in the corner of dash
"""

app = Flask(__name__, template_folder='../templates', static_folder='../static')
socketio = SocketIO(app)
controller = Controller()
rover = Rover(socketio, controller)

@app.route('/')
def entry():
    """
    Default page to render
    """
    return render_template('index.html')

@socketio.on('message')
def handle_message(payload):
    """
    Log to terminal the message received from the dashboard
    """
    print('received message: ', payload)

@socketio.on('connect')
def on_connect():
    """
    Reply to the client it has connected to the server.
    """
    print("socketio has connected")
    payload = dict(data='Connected')
    emit('data', payload)

@socketio.on('connect_to_rover')
def on_connect_to_rover(payload):
    """
    Connect to the rover server using the given ip and port.
    """
    rover.connect(payload['ip'], payload['port'])

@socketio.on('disconnect_from_rover')
def on_disconnect_from_rover():
    """
    Disconnect from the rover server and tear down connections.
    """
    rover.listening = False
    rover = None
    controller.stop_stream()
    controller.exit()

@socketio.on('send_command')
def on_send_command(payload):
    """
    Send a commend to the rover server.
    """
    if rover.connected:
        rover.send_command(payload['command'], payload['data'])
    else:
        emit('error', {'message': 'Rover not connected!'})

@socketio.on('connect_controller')
def on_connect_controller():
    """
    Connect controller and begin streaming its values.
    """
    if not controller.is_available():
        print('No controller connected')
        emit('error', {'message': 'No controller connected!'})
        return

    # Start controller
    controller.init_joystick()
    controller_thread = threading.Thread(target=controller.start, daemon=True )
    controller_thread.start()

    # Begin streaming controller
    if not controller.is_streaming:
        controller.start_stream()

        # Stream to GUI
        gui_stream = threading.Thread(target=stream_controller_to_gui, daemon=True)
        gui_stream.start()

        # Stream to rover
        rover_stream = threading.Thread(target=stream_drive_to_rover, daemon=True)
        rover_stream.start()

    # reply to GUI client
    emit('controller_status', {'status': True})

def stream_controller_to_gui():
    """
    Stream the controller state the the GUI.
    """
    while controller.is_streaming:
        payload = dict(drive=controller.axis[2], steer=controller.axis[0])
        socketio.emit('controller_data', payload)
        time.sleep(.100)

def stream_drive_to_rover():
    """
    Stream the controller state the the rover server.
    """
    while controller.is_streaming:
        # If not connected to rover yet, wait 3 seconds then try again.
        if not rover.connected:
            time.sleep(3)
            continue

        # sending fwd, steer
        rover.send_command('drive', [controller.axis[2], controller.axis[0]])
        time.sleep(.250)
