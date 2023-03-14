import pygame

import lib

class Grid():
    def __init__(self, width: int, height: int):
        self.grid = pygame.sprite.Group()

        self.width = width
        self.height = height

        self.create_grid(self.width, self.height)

    def create_grid(self, width: int, height: int):
        for w in range(width):
            for h in range(height):
                g = GridSquare(w, h)
                self.grid.add(g)

    def get_all_uuid(self):
        for g in self.grid:
            print(g.get_uuid())

    def get_adjacent(self, grid_id: int) -> list [int, int, int, int]:
        adjacent = []
        
        for g in self.grid:
            if g.uuid == grid_id:
                reference_grid = g

        for a in self.grid:
            if a.uuid == reference_grid.uuid - 1:
                adjacent.append(a.uuid)
            if a.uuid == reference_grid.uuid + 1:
                adjacent.append(a.uuid)
            if a.uuid == reference_grid.uuid - self.height:
                adjacent.append(a.uuid)
            if a.uuid == reference_grid.uuid + self.height:
                adjacent.append(a.uuid)

        return adjacent
    
    def highlight_adjacent(self, target_grid: int):
        adjacent = self.get_adjacent(target_grid)
        
        for g in self.grid:
            if g.uuid == target_grid:
                g.active = True

            if g.uuid in adjacent:
                g.adjacent = True
            

class GridSquare(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()

        self.scale = 64

        self.uuid_string = str(str(x) + str(y))
        self.uuid = int(self.uuid_string)

        self.pos = pygame.math.Vector2(x * self.scale, y * self.scale)

        self.active = False
        self.adjacent = False

        self.base_color = lib.color.white
        self.active_color = lib.color.blue
        self.adjacent_color = lib.color.green

        self.image = pygame.Surface([self.scale, self.scale])
        self.image.fill(lib.color.white)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def get_uuid(self) -> int:
        return self.uuid

    def update(self):
        if self.active:
            self.image.fill(self.active_color)
        elif self.adjacent:
            self.image.fill(self.adjacent_color)
        else:
            self.image.fill(self.base_color)