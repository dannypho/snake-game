import pygame
import random

class Apple:
        
    def __init__(self, game):

        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings
            
        # Load the apple
        self.image = pygame.image.load('images/apple.png')
        self.image = pygame.transform.scale(self.image, (self.settings.grid_size, self.settings.grid_size))
        self.rect = self.image.get_rect()

        # Start position of apple
        self.rect.center = (470, 310)

    def blitme(self):
        """Draw the apple at starting position"""
        self.screen.blit(self.image, self.rect)
    
    def reset(self):
        self.rect.center = (470, 310)

    def relocate(self):
        """Move the apple to randomly generatedf coordinates"""
        self.rect.center = self._generate_coordinates()

    def _generate_coordinates(self):
        """Generate random x and y coordinates for the apple"""

        while True:
            x_coordinate = random.randint(1, self.settings.screen_width)
            y_coordinate = random.randint(1, self.settings.screen_height)
            
            if (x_coordinate % 10 == 0 and x_coordinate % 20 != 0) and (y_coordinate % 10 == 0 and y_coordinate % 20 != 0):
                return (x_coordinate, y_coordinate)