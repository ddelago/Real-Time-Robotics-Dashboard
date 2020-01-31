from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import threading
from modules.controller import Controller 
import time

# TODO: Handle error for when controller is not connected
# TODO: Handle case where client asks to connect controller but controller already connected

app = Flask(__name__)
socketio = SocketIO(app)
controller = Controller()
current_page = 'Dashboard'

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

    # reply to client
    payload = dict(data='Controller connected')
    emit('data', payload)

@socketio.on('get_controller_state')
def on_get_controller_state():
    while current_page == 'Dashboard':
        payload = dict(data=controller.get_values())
        emit('data', payload)
        time.sleep(.100)

@socketio.on('stop_controller')
def on_stop_controller():
    controller.stop()