import socket
import threading
import time

# TODO: Add parsing function

class Rover:
    incoming_payload = {}
    commands = {
        'drive': (0xBB, 0x06),
        'arm': (0xBE, 0),
        'sr': (0xBD, 0),
        'ping': (0xFA, 0),
        'led': (0xCA, 0x05),
        'sys': (0xAB, 0),
        'reset': (0x00, 0)
    }
    rover_socket = None
    connected = False
    sending = False
    listen = False

    def __init__(self, socketio, controller):
        self.rover_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected = True
        self.socketio = socketio
        self.controller = controller
        self.listen = True

    def connect(self, ip, port):
        print("Connecting to rover")
        self.rover_socket.connect((ip, int(port)))

        print("Connected to Rover")
        self.socketio.emit('connection_status', dict(data='True'))

        # Start listener loop
        listener_thread = threading.Thread(target=self.listen, daemon=True)
        listener_thread.start()

    def send_command(self, command, data):
        # Get byte values for command
        command = self.commands[command][0]
        size = self.commands[command][1]
        payload = bytearray([0xAA, size, command])

        # Calc checksum
        checksum = 0xAA ^ size ^ command 
        for val in data:
            payload.append(val)
            checksum = checksum ^ val
        
        payload.append(checksum)
        # print(payload)
        self.rover_socket.send(payload)

    def send_drive(self):
        while self.controller.is_streaming:
            # sending fwd, steer
            self.send_command('drive', [self.controller.axis[2], self.controller.axis[0]])
            time.sleep(.500)

    def listen(self):
        while self.listen == True:
            try:
                # Receiving from rover
                data = self.rover_socket.recv(4096)
                if data == b'':
                    continue
                # print(data)
                self.sending = False
            except e:
                err = e.args[0]
                if err == errno.EAGAIN or err == errno.EWOULDBLOCK:
                    print('No data available')
                    continue
                else:
                    # a "real" error occurred
                    print('Connection to rover lost.', e)
                    self.socketio.emit('connection_status', dict(data='False'))
                    self.connected = False
                    break

        # Close connection to client
        self.rover_socket.close()
