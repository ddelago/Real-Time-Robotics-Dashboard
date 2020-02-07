import socket

class Rover:
    rover_socket = None

    def __init__(self):
        self.rover_socket = socket.socket()

    def connect(self, ip, port):
        self.rover_socket.connect(ip, port)

    def send_command(self, command):
        self.rover_socket.sendall(command.encode())

    
