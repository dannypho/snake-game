import pygame
import sys

class Snake:

    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings
        
        # Load the snake head
        self.image_head = pygame.image.load('images/snake_head.png')
        self.image_head = pygame.transform.scale(self.image_head, (self.settings.grid_size, self.settings.grid_size))
        self.rect = self.image_head.get_rect()

        # Load the snake body image
        self.image_body = pygame.image.load('images/snake_body.png')
        self.image_body = pygame.transform.scale(self.image_body, (self.settings.grid_size, self.settings.grid_size))

        # Start position of snake head
        self.rect.center = (250, 310)

        self.direction = None  # Added to track the current direction
        self.move_up = False
        self.move_down = False
        self.move_right = False
        self.move_left = False

        self.previous_direction = None

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.body_segments = []
        self.body_length = 3 

        for i in range(self.body_length):
            segment_rect = self.image_body.get_rect()
            segment_rect.center = (self.rect.centerx - (i + 1) * self.settings.grid_size, self.rect.centery)
            self.body_segments.append({'rect': segment_rect, 'pos': list(segment_rect.center)})

    def blitme(self):
        """Draw the snake head and body"""
        # Draw body segments first
        for segment in self.body_segments:
            self.screen.blit(self.image_body, segment['rect'])

        self.screen.blit(self.image_head, self.rect)

    def reset(self):
        self.rect.center = (250, 310)
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.direction = None  # Reset the direction
        self.move_up = False
        self.move_down = False
        self.move_right = False
        self.move_left = False

        self.previous_direction = None

        self.body_segments.clear()
        for i in range(self.body_length):
            segment_rect = self.image_body.get_rect()
            segment_rect.center = (self.rect.centerx - (i + 1) * self.settings.grid_size, self.rect.centery)
            self.body_segments.append({'rect': segment_rect, 'pos': list(segment_rect.center)})

    def update(self):
        """Controls movement of the snake head"""
        previous_head_pos = list(self.rect.center)

        if self.move_up:
            self.y -= self.settings.snake_speed
            self.direction = 'UP'
        
        elif self.move_down:
            self.y += self.settings.snake_speed
            self.direction = 'DOWN'

        elif self.move_right:
            self.x += self.settings.snake_speed
            self.direction = 'RIGHT'

        elif self.move_left:
            self.x -= self.settings.snake_speed
            self.direction = 'LEFT'

        self.rect.x = self.x
        self.rect.y = self.y

        if self.body_segments:
            # Store the previous position of each segment
            previous_positions = [previous_head_pos]
            for segment in self.body_segments[:-1]:
                previous_positions.append(list(segment['rect'].center))
        
            for i, segment in enumerate(self.body_segments):
                segment['rect'].center = previous_positions[i]
                segment['pos'] = list(previous_positions[i])

    def grow(self):
        # Call this method when the snake eats an apple
        segment_rect = self.image_body.get_rect()
        
        # Position the new segment at the end of the snake
        if self.body_segments:
            last_segment = self.body_segments[-1]
            segment_rect.center = last_segment['rect'].center
        else:
            segment_rect.center = (self.rect.centerx - self.settings.grid_size, self.rect.centery)
            
        self.body_segments.append({'rect': segment_rect, 'pos': list(segment_rect.center)})

    def check_self_collision(self):
        """Returns True if the snake has collided with itself"""
        for segment in self.body_segments:
            if self.rect.colliderect(segment['rect']):
                return True
        return False

    def set_direction(self, direction):
        if direction == 'UP':
            if self.direction != 'DOWN':  # Prevent reversing
                self.move_up = True
                self.move_down = False
                self.move_right = False
                self.move_left = False
        elif direction == 'DOWN':
            if self.direction != 'UP':  # Prevent reversing
                self.move_up = False
                self.move_down = True
                self.move_right = False
                self.move_left = False
        elif direction == 'RIGHT':
            if self.direction != 'LEFT':  # Prevent reversing
                self.move_up = False
                self.move_down = False
                self.move_right = True
                self.move_left = False
        elif direction == 'LEFT':
            if self.direction != 'RIGHT':  # Prevent reversing
                self.move_up = False
                self.move_down = False
                self.move_right = False
                self.move_left = True
