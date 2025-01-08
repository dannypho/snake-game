# Snake Game with Pygame

A modern take on the classic Snake game built using Python and Pygame. This project features dynamic snake growth, grid-based movement, and collision detection.

## Features

- **Dynamic Snake Growth**: The snake increases in length with each apple it consumes.
- **Grid-Based Movement**: Movement within a grid structure provides a smooth and predictable gameplay experience.
- **Collision Detection**: The game ends when the snake collides with the wall or itself.
- **Customizable Settings**: Easily adjust screen size, grid size, and colors.

## File Descriptions

- `main.py`: Handles the game logic, including the `Game` class and main loop.
- `settings.py`: Defines the `Settings` class with customizable game settings.
- `snake.py`: Implements the `Snake` class to manage movement, growth, and collisions.
- `apple.py`: Contains the `Apple` class for spawning and relocating apples.
- `game_stats.py`: Manages game state with the `GameStats` class.


## How to Run

1. Install Python 3.x and Pygame.
2. Clone or download the repository.
3. Navigate to the project directory and run:

```bash
   python main.py
```

## Controls

* Arrow keys: Move the snake up, down, left, or right
* The snake cannot reverse direction directly.

## Future Improvements

* Implement a scoring system
* Add pause and restart functionality
* Introduce difficulty levels and additional game modes


