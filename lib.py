import pygame
import random

screen_width = 1200
screen_height = 900

class Color():
    def __init__(self):
        self.black = pygame.Color(0, 0, 0, 255)
        self.white = pygame.Color(255, 255, 255, 255)
        self.red = pygame.Color(255, 0, 0, 255)
        self.green = pygame.Color(0, 255, 0, 255)
        self.blue = pygame.Color(0, 0, 255, 255)
    
    def random(self) -> pygame.Color:
        c = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        return c
    
color = Color()

display_surface = pygame.display.set_mode([screen_width, screen_height])
events = pygame.event.get()

delta_time = 0
framerate = 120