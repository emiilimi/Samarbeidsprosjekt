import pygame
from pygame.locals import *

from player import Player

WIDTH, HEIGHT = 400, 400
FPS = 24

class App:
    def __init__(self):
        self.awake()
        self.start()


    def awake(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("pygame mal")
        self.running = True
        self.all_sprites = pygame.sprite.Group()

    def start(self):
        self.all_sprites.add(Player("skib.png", pygame.Vector2(10,180)))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill("black")
        self.all_sprites.draw(self.screen)
        pygame.display.update()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()


if __name__ == "__main__":
    app = App()
    app.run()
