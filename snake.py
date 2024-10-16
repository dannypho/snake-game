import pygame
import sys

class Snake:

    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings
        
        # Load the snake head
        self.image = pygame.image.load('images/snake_head.png')
        self.image = pygame.transform.scale(self.image, (self.settings.grid_size, self.settings.grid_size))
        self.rect = self.image.get_rect()

        # Start position of snake head
        self.rect.center = (250, 310)

        self.move_up = False
        self.move_down = False
        self.move_right = False
        self.move_left = False

        self.previous_direction = None

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """Draw the snake head at starting position"""
        self.screen.blit(self.image, self.rect)

    def reset(self):
        self.rect.center = (250, 310)
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.move_up = False
        self.move_down = False
        self.move_right = False
        self.move_left = False

        self.previous_direction = None
        
    def update(self):
        """Controls movement of the snake head"""
        if self.move_up is True:
            if self.previous_direction == "Right" and self.rect.right % 20 != 0:
                self.x += 20 - (self.rect.right % 20)
            elif self.previous_direction == "Left" and self.rect.right % 20 != 0:
                self.x -= (self.rect.right % 20)
            self.y -= self.settings.snake_speed
            self.previous_direction = "Up"
        
        elif self.move_down is True:
            if self.previous_direction == "Right" and self.rect.right % 20 != 0:
                self.x += 20 - (self.rect.right % 20)
            elif self.previous_direction == "Left" and self.rect.right % 20 != 0:
                self.x -= (self.rect.right % 20)
            self.y += self.settings.snake_speed
            self.previous_direction = "Down"

        elif self.move_right is True:
            if self.previous_direction == "Up" and self.rect.top % 20 != 0:
                self.y -= (self.rect.top % 20)
            elif self.previous_direction == "Down" and self.rect.top % 20 != 0:
                self.y += (20 - self.rect.top % 20)
            self.x += self.settings.snake_speed
            self.previous_direction = "Right"

        elif self.move_left is True:
            if self.previous_direction == "Up" and self.rect.top % 20 != 0:
                self.y -= (self.rect.top % 20)
            elif self.previous_direction == "Down" and self.rect.top % 20 != 0:
                self.y += (20 - self.rect.top % 20)
            self.x -= self.settings.snake_speed
            self.previous_direction = "Left"

        self.rect.x = self.x
        self.rect.y = self.y
    