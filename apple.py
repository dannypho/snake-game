import pygame
import random

class Apple:

    def __init__(self, game):
        self.screen = game.screen
        self.settings = game.settings
        self.image = pygame.image.load('images/apple.png')
        self.image = pygame.transform.scale(self.image, (self.settings.grid_size, self.settings.grid_size))
        self.rect = self.image.get_rect()
        self.relocate()

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def reset(self):
        self.relocate()

    def relocate(self):
        self.rect.x = random.randrange(0, self.settings.screen_width, self.settings.grid_size)
        self.rect.y = random.randrange(0, self.settings.screen_height, self.settings.grid_size)
