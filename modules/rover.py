import socket
# TODO: Need to make a way to listen to messages from rover

class Rover:
    rover_socket = None
    incoming_payload = {}

    def __init__(self):
        self.rover_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        

    def connect(self, ip, port):
        print(ip, port)
        self.rover_socket.connect((ip, int(port)))

        self.rover_socket.sendall(b'0xAAHelloWorld')
        data = self.rover_socket.recv(1024)
        print(repr(data))

    def send_command(self, command):
        self.rover_socket.sendall(command.encode())
