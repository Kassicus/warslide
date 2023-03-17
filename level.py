import pygame

import lib
import grid
import player

class Level():
    def __init__(self):
        self.grid = grid.Grid(16, 10)

        self.player = player.Player(self.grid)

        self.entities = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.player_camera = pygame.sprite.Group()

        self.player_camera.add(self.player)

    def draw(self):
        self.grid.grid.draw(lib.display_surface)

        self.player_camera.draw(lib.display_surface)

    def update(self):
        self.grid.grid.update()

        self.player_camera.update()