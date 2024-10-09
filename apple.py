import pygame

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
        self.rect.center = (430, 430)

    def blitme(self):
        """Draw the apple at starting position"""
        self.screen.blit(self.image, self.rect)