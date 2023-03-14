import pygame

import lib

class DebugInterface():
    def __init__(self):
        self.active = False

        self.font = pygame.font.SysFont("Courier", 12)
        self.margin = 10

        # The text element of each debug menu item
        self.t_fps = None
        self.t_mouse = None

        # The offset position of each debug menu item
        self.o_fps = 0
        self.o_mouse = 0

        self.display_surface = pygame.display.get_surface()

    def get_fps(self, clock: pygame.time.Clock) -> list [pygame.Surface, int]:
        string = "FPS: " + str(int(clock.get_fps()))
        text = self.font.render(string, True, lib.color.white)

        offset = int(lib.screen_width - text.get_width() - self.margin)

        return text, offset
    
    def get_mouse(self) -> list [pygame.Surface, int]:
        x, y = pygame.mouse.get_pos()

        string = "Mouse: " + str(x) + "," + str(y)
        text = self.font.render(string, True, lib.color.white)

        offset = int(lib.screen_width - text.get_width() - self.margin)

        return text, offset
    
    def show_adjacent_tiles(self) -> int:
        x, y = pygame.mouse.get_pos()

        grid_x = round(x / 64)
        grid_y = round(y / 64)

        return int(str(str(grid_x) + str(grid_y)))
    
    def toggle_active(self):
        if self.active:
            self.active = False
        else:
            self.active = True

    def draw(self):
        self.display_surface.blit(self.t_fps, (self.o_fps, 10))
        self.display_surface.blit(self.t_mouse, (self.o_mouse, 30))

    def update(self, clock: pygame.time.Clock):
        self.t_fps, self.o_fps = self.get_fps(clock)
        self.t_mouse, self.o_mouse = self.get_mouse()