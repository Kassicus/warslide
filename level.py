import pygame

import lib
import grid

class Level():
    def __init__(self):
        self.grid = grid.Grid(16, 10)

        #TODO: Make this a thing // self.player = player.Player()

        self.entities = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

    def draw(self):
        self.grid.grid.draw(lib.display_surface)

    def update(self):
        self.grid.grid.update()