import socket
import threading

class Rover:
    rover_socket = None
    connected = False
    incoming_payload = {}

    # TODO: Always listen for messages or only on request?

    def __init__(self, socketio):
        self.rover_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected = True
        self.socketio = socketio

    def connect(self, ip, port):
        print("Connecting to rover")
        self.rover_socket.connect((ip, int(port)))

        self.send_command('0x00', '')
        print("Connected to Rover")
        # data = self.rover_socket.recv(1024)
        # print('Receieved reply: ', data)
        self.socketio.emit('connection_status', dict(data='True'))

        listener_thread = threading.Thread(target=self.listen, daemon=True)
        listener_thread.start()


    def send_command(self, command, data):
        """ Send a command to the rover
        params:
            command: The byte code defined in global_defs.h
            data: Values supplied for the command (eg: drive values)
        """
        self.rover_socket.sendall(f'{command}{data}'.encode())

    def send_drive(self, controller):
        self.send_command(
            'OxAA',
            f'{controller.axis[0]}' +
            f'{controller.axis[1]}' +
            f'{controller.axis[2]}' +
            f'{controller.axis[3]}' +
            f'{controller.axis[4]}'
        )

    def send_arm(self, controller):
        self.send_command(
            'OxBE',
            f'{controller.axis[0]}' +
            f'{controller.axis[1]}' +
            f'{controller.axis[2]}' +
            f'{controller.axis[3]}' +
            f'{controller.axis[4]}'
        )

    def send_reset(self):
        self.send_command('0x00', '')

    def ping(self):
        self.send_command('0xFA', '')

    def get_sys_info(self):
        self.send_command('0xAB','')
        data = self.rover_socket.recv(1024).decode("utf-8")
        print('Received system info: ', data)
        self.socketio.emit('system_info', dict(data=data))

    def listen(self):
        while True:
            # Receiving from rover
            data = self.rover_socket.recv(1024)
            print(data)

            # If no data, connection was lost
            if not data:
                print('Connection to rover lost.')
                self.socketio.emit('connection_status', dict(data='False'))
                self.connected = False
                break

        # Close connection to client
        self.rover_socket.close()
