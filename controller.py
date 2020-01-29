import pygame
import time

class Controller:
    axis = []
    buttons = []
    hat = ()

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

    def init_joystick(self):
        pygame.joystick.init()
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()

    def stop(self):
        pygame.quit()

    def start(self):
        while True:        
            pygame.event.get()
            self.axis = [
                round(self.joystick.get_axis( 0 ), 3),     
                round(self.joystick.get_axis( 1 ), 3),               
                round(self.joystick.get_axis( 2 ), 3),       
                round(self.joystick.get_axis( 3 ), 3),           
                round(self.joystick.get_axis( 4 ), 3)
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
        
    def get_values(self):
        return(self.axis, self.buttons, self.hat)