import socket
import threading
import time

class Rover:
    rover_socket = None
    connected = False
    incoming_payload = {}
    sending = False
    listen = False

    # TODO: Always listen for messages or only on request?

    def __init__(self, socketio, controller):
        self.rover_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected = True
        self.socketio = socketio
        self.controller = controller
        self.listen = True

    def connect(self, ip, port):
        print("Connecting to rover")
        self.rover_socket.connect((ip, int(port)))

        # self.send_command('0x00', '')
        print("Connected to Rover")
        self.socketio.emit('connection_status', dict(data='True'))

        listener_thread = threading.Thread(target=self.listen, daemon=True)
        listener_thread.start()

    def constructChecksum(self, command, data, size):
        checksum = 0xAA ^ size ^ command ^ data
        return checksum

    def send_command(self, command, data):
        self.rover_socket.sendall(f'0XAA{command}{data}'.encode())
    
    def send_led_command(self, command, data):
        payload = bytearray()
        payload.append(0xaa)
        payload.append(0x05)
        payload.append(0xca)

        checksum = self.constructChecksum(int(command, 16), data, 0x05)
        payload.append(data)
        payload.append(checksum)

        print(payload)
        self.sending = True
        while self.sending != False:
            self.rover_socket.send(payload)
            time.sleep(.500)

    # If controler is set to stream, stream
    def send_drive(self):
        payload = bytearray([0xaa, 0x06, 0xbb])
        
        while self.controller.is_streaming:
            fwd = self.controller.axis[2]
            steer = self.controller.axis[0]
            checksum = 0xaa ^ 0x06 ^ 0xbb ^ fwd ^ steer
            payload.append(fwd)
            payload.append(steer)
            payload.append(checksum)

            self.rover_socket.send(payload)
            time.sleep(.500)

    def send_arm(self, controller):
        self.send_command(
            '0xBE',
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
        # data = self.rover_socket.recv(1024).decode("utf-8")
        # self.socketio.emit('system_info', dict(data=data))

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
