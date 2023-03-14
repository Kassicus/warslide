import pygame

import lib

class Grid():
    def __init__(self, width: int, height: int):
        self.grid = pygame.sprite.Group()

        self.create_grid(width, height)

    def create_grid(self, width: int, height: int):
        for w in range(width):
            for h in range(height):
                g = GridSquare(w, h)
                self.grid.add(g)

    def get_all_uuid(self):
        for g in self.grid:
            print(g.get_uuid())

class GridSquare(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()

        self.scale = 64

        self.uuid = str(str(x) + str(y))

        self.pos = pygame.math.Vector2(x * self.scale, y * self.scale)

        self.image = pygame.Surface([self.scale, self.scale])
        self.image.fill(lib.color.random())
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def get_uuid(self) -> tuple:
        return self.uuid

    def update(self):
        pass