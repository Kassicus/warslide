import pygame

import lib
import debug
import level

pygame.init()

class Game():
    def __init__(self):
        self.screen = lib.display_surface
        pygame.display.set_caption("WarSlide")

        self.running = True
        self.clock = pygame.time.Clock()

        self.debug_interface = debug.DebugInterface()

        self.test_level = level.Level()
        
    def run(self):
        while self.running:
            self.events()
            self.draw()
            self.update()

    def events(self):
        lib.events = pygame.event.get()

        for event in lib.events:
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

                if event.key == pygame.K_TAB:
                    self.debug_interface.toggle_active()

    def draw(self):
        self.screen.fill(lib.color.black)

        self.test_level.draw()

        if self.debug_interface.active:
            self.debug_interface.draw()
        
    def update(self):
        self.test_level.update()
        self.debug_interface.update(self.clock)
        pygame.display.update()
        lib.delta_time = self.clock.tick(lib.framerate) / 1000

if __name__ == '__main__':
    game = Game()
    game.run()
    pygame.quit()