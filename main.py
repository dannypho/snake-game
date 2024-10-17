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
        self.clock = pygame.time.Clock()

    def run_game(self):
        while True:
            self._check_events()
            if self.game_stats.game_active:
                self.snake.update()
                self._check_snake_boundary_collision()
                self._check_apple_collision()
            self._update_screen()
            # Control the frame rate
            self.clock.tick(15)  # Control the frame rate

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
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

        for x in range(0, width, grid_size):
            for y in range(0, height, grid_size):
                pygame.draw.line(self.screen, line_color, (x, 0), (x, height))
                pygame.draw.line(self.screen, line_color, (0, y), (width, y))

    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP and self.snake.direction != 'DOWN':
            self.snake.set_direction('UP')
        elif event.key == pygame.K_DOWN and self.snake.direction != 'UP':
            self.snake.set_direction('DOWN')
        elif event.key == pygame.K_RIGHT and self.snake.direction != 'LEFT':
            self.snake.set_direction('RIGHT')
        elif event.key == pygame.K_LEFT and self.snake.direction != 'RIGHT':
            self.snake.set_direction('LEFT')

    def _check_snake_boundary_collision(self):
        if (self.snake.rect.left < 0 or self.snake.rect.top < 0 or 
            self.snake.rect.right > self.settings.screen_width or 
            self.snake.rect.bottom > self.settings.screen_height or
            self.snake.check_self_collision()):
            self._reset_game()
            self.game_stats.game_active = False

    def _check_apple_collision(self):
        if self.snake.rect.colliderect(self.apple.rect):
            self.apple.relocate()
            self.snake.grow()

    def _reset_game(self):
        self.snake.reset()
        self.apple.reset()

if __name__ == '__main__':
    game = Game()
    game.run_game()
