import socket
import threading

"""
TODO: Add parsing function for incoming data (parse_message)
"""

class Rover:
    """
    Handles communication to and from the rover server.
    """
    # (command byte, command size)
    commands = {
        'drive': (0xBB, 0x06),
        'arm': (0xBE, 0),
        'sr': (0xBD, 0),
        'ping': (0xFA, 0),
        'led': (0xCA, 0x05),
        'sys': (0xAB, 0),
        'reset': (0x00, 0)
    }
    incoming_payload = {}
    connected = False
    listening = False

    def __init__(self, socketio, controller):
        self.rover_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected = True
        self.socketio = socketio
        self.controller = controller
        self.listening = True

    def connect(self, ip, port):
        """
        Create a socket connection to the rover server.
        """
        print("Connecting to rover server")
        try:
            self.rover_socket.connect((ip, int(port)))
        except:
            print("Unable to connect to Rover")
            self.socketio.emit('error', {'message': 'Unable to connet to rover.'})
            return

        # Successfully able to connect
        self.connected = True
        print("Connected to Rover")
        self.socketio.emit('connection_status', {'staus': True})

        # Start listener loop
        listener_thread = threading.Thread(target=self.listen, daemon=True)
        listener_thread.start()

    def send_command(self, command, data):
        """ Parses the command and constucts the byte array to be sent to the rover.
        arguments:
            command: the command to send as specified in the commands table above.
            data: A list of data to be sent according to the command.
        """
        # Get byte values for command
        command_byte = self.commands[command][0]
        size = self.commands[command][1]
        payload = bytearray([0xAA, size, command_byte])

        # Calc checksum and add data to payload
        checksum = 0xAA ^ size ^ command_byte
        for val in data:
            payload.append(val)
            checksum = checksum ^ val
        payload.append(checksum)

        # Send data
        self.rover_socket.send(payload)

    def listen(self):
        """
        Listen for incoming data from the rover.
        """
        while self.listening:
            try:
                # Receiving from rover
                data = self.rover_socket.recv(4096)

                # Skip empty messages
                if data == b'':
                    continue
                else:
                    self.parse_message(data)
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

    def parse_message(self, data):
        """
        Parse the incoming data from the rover.
        This will then be sent to the GUI.
        """
        self.incoming_payload = data
