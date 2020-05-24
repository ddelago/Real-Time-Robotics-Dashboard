import pygame

class Controller:
    """
    Connect and stream the values of a controller.
    """
    axis = []
    buttons = []
    hat = ()
    is_streaming = False

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

    def is_available(self):
        """
        Check if a controller is connected.
        """
        if pygame.joystick.get_count() > 0:
            return True
        return False

    def init_joystick(self):
        """
        Initialize the controller.
        """
        pygame.joystick.init()
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()
        self.controller_connected = True

    def start(self):
        """
        Stream and update the controller values.
        """
        while self.is_streaming:
            pygame.event.get()
            self.axis = [
                int(self.joystick.get_axis(0) * 127 + 127),
                round(self.joystick.get_axis(1), 3),
                int(self.joystick.get_axis(2) * -127 + 127),
                round(self.joystick.get_axis(3), 3),
                round(self.joystick.get_axis(4), 3)
            ]

            self.buttons = [
                self.joystick.get_button(0),
                self.joystick.get_button(1),
                self.joystick.get_button(2),
                self.joystick.get_button(3),
                self.joystick.get_button(4),
                self.joystick.get_button(5),
                self.joystick.get_button(6),
                self.joystick.get_button(7),
                self.joystick.get_button(8),
                self.joystick.get_button(9)
            ]

            # D-pad, returns a tuple (x,y)
            self.hat = self.joystick.get_hat(0)
            self.clock.tick(20)

            # Add a deadzone
            if self.axis[0] > 110 and self.axis[0] < 150:
                self.axis[0] = 127
            if self.axis[2] > 124 and self.axis[2] < 130:
                self.axis[2] = 127

    def start_stream(self):
        """
        Begin streaming the controller.
        """
        self.is_streaming = True

    def stop_stream(self):
        """
        Stop streaming the controller values
        """
        self.is_streaming = False

    def get_values(self):
        """
        Return the current values of the controller
        """
        return(self.axis, self.buttons, self.hat)

    def exit(self):
        pygame.quit()
