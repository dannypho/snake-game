import sys
import pygame
from settings import Settings
from snake import Snake
from apple import Apple
from game_stats import GameStats

class Game:

    def __init__(self):

        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Snake")

        self.snake = Snake(self)
        self.apple = Apple(self)
        self.game_stats = GameStats(self)       

    def run_game(self):

        while True:
            self._check_events()
        
            if self.game_stats.game_active:
                self.snake.update()
                self._check_snake_boundary_collision()
                self._check_apple_collision()

            self._update_screen()
    
    def _check_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if not self.game_stats.game_active:
                        self.game_stats.game_active = True
                    self._check_keydown_events(event)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.snake.blitme()
        self.apple.blitme()
        self._draw_grid()
        pygame.display.flip()

    def _draw_grid(self):
            grid_size = self.settings.grid_size
            width = self.settings.screen_width
            height = self.settings.screen_height
            line_color = self.settings.line_color

            for x in range(0, width // grid_size + 1):
                for y in range(0, height // grid_size + 1):
                    pygame.draw.line(self.screen, (line_color), (grid_size * x, 0), (grid_size * x, 600))
                    pygame.draw.line(self.screen, (line_color), (0, grid_size * y), (800, grid_size * y))
        
    def _check_keydown_events(self, event):
        # Prevent movement in opposite direction
        if event.key == pygame.K_UP and self.snake.move_down != True:
            self.snake.move_down = False
            self.snake.move_right = False
            self.snake.move_left = False
            self.snake.move_up = True
        elif event.key == pygame.K_DOWN and self.snake.move_up != True:
            self.snake.move_up = False
            self.snake.move_right = False
            self.snake.move_left = False
            self.snake.move_down = True
        elif event.key == pygame.K_RIGHT and self.snake.move_left != True:
            self.snake.move_up = False
            self.snake.move_down = False
            self.snake.move_left = False
            self.snake.move_right = True
        elif event.key == pygame.K_LEFT and self.snake.move_right != True:
            self.snake.move_up = False
            self.snake.move_down = False
            self.snake.move_right = False
            self.snake.move_left = True

    def _check_snake_boundary_collision(self):
        if self._check_boundary_collision():
            self.game_stats.game_active = False
            self._reset_game()

    def _check_boundary_collision(self):
        """"Returns true if snake head collides with boundary of the screen"""
        if self.snake.rect.left < 0:
            return True
        if self.snake.rect.top < 0:
            return True
        if self.snake.rect.right > self.settings.screen_width:
            return True
        if self.snake.rect.bottom > self.settings.screen_height:
            return True
        return False

    def _check_apple_collision(self):
        """Relocates apple if snake collides with apple"""
        if self.snake.rect.colliderect(self.apple.rect):
            self.apple.relocate()

    def _reset_game(self):
        self.snake.reset()
        self.apple.reset()

if __name__ == '__main__':
    game = Game()
    game.run_game()