import sys
import pygame
from settings import Settings
from snake import Snake

class Game:

    def __init__(self):

        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Snake")

        self.snake = Snake(self)        

    def run_game(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event) 
                                    
            
            self.snake.update()
            self.screen.fill(self.settings.bg_color)
            self.snake.blitme()
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

if __name__ == '__main__':
    game = Game()
    game.run_game()