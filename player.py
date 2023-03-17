import pygame

import lib

class Player(pygame.sprite.Sprite):
    def __init__(self, grid_ref: object):
        super().__init__()

        self.grid_pos = 12
        self.grid_ref = grid_ref

        self.pos = self.get_relative_pos(self.grid_pos)

        self.image = pygame.Surface([64, 64])
        self.image.fill(lib.color.blue)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def update(self):
        self.rect.topleft = self.pos

        self.event_handler()

    def event_handler(self):
        for event in lib.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.pos = self.get_relative_pos(self.move("left"))
                if event.key == pygame.K_d:
                    self.pos = self.get_relative_pos(self.move("right"))

    def get_relative_pos(self, grid_pos) -> pygame.math.Vector2():
        grid_string = str(grid_pos)
        print(grid_string)

        if len(grid_string) < 3:
            grid_x = int(grid_string[0])
            grid_y = int(grid_string[1])

            return pygame.math.Vector2(int(grid_x * 64), int(grid_y * 64))

    def move(self, direction: str) -> int:
        match direction:
            case "up":
                rval = self.grid_pos - 1
            case "down":
                rval = self.grid_pos + 1
            case "left":
                rval = self.grid_pos - self.grid_ref.height
            case "right":
                rval = self.grid_pos + self.grid_ref.height

        self.grid_pos = rval

        return rval