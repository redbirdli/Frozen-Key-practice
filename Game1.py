import pygame
import random

# Initialize pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Tetris")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# Define the Tetris grid
grid_size = 30
grid_width = window_width // grid_size
grid_height = window_height // grid_size
grid = [[BLACK] * grid_width for _ in range(grid_height)]

# Define the Tetrimino shapes
shapes = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]]
]

# Define the Tetrimino colors
colors = [CYAN, YELLOW, RED, GREEN, BLUE, ORANGE, MAGENTA]

# Define the current Tetrimino
current_shape = random.choice(shapes)
current_color = random.choice(colors)
current_x = grid_width // 2 - len(current_shape[0]) // 2
current_y = 0

# Define the game clock
clock = pygame.time.Clock()

# Load the background music
pygame.mixer.music.load("background_music.mp3")
pygame.mixer.music.play(-1)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the current Tetrimino down
    current_y += 1

    # Check for collision
    if current_y + len(current_shape) > grid_height or any(
        grid[current_y + i][current_x + j] != BLACK
        for i, row in enumerate(current_shape)
        for j, cell in enumerate(row)
        if cell
    ):
        # Lock the current Tetrimino in place
        for i, row in enumerate(current_shape):
            for j, cell in enumerate(row):
                if cell:
                    grid[current_y + i - 1][current_x + j] = current_color

        # Check for completed rows
        for i, row in enumerate(grid):
            if all(cell != BLACK for cell in row):
                del grid[i]
                grid.insert(0, [BLACK] * grid_width)

        # Spawn a new Tetrimino
        current_shape = random.choice(shapes)
        current_color = random.choice(colors)
        current_x = grid_width // 2 - len(current_shape[0]) // 2
        current_y = 0

    # Clear the window
    window.fill(BLACK)

    # Draw the grid
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            pygame.draw.rect(window, cell, (j * grid_size, i * grid_size, grid_size, grid_size))

    # Draw the current Tetrimino
    for i, row in enumerate(current_shape):
        for j, cell in enumerate(row):
            if cell:
                pygame.draw.rect(window, current_color, ((current_x + j) * grid_size, (current_y + i) * grid_size, grid_size, grid_size))

    # Update the display
    pygame.display.update()

    # Limit the frame rate
    clock.tick(10)

# Quit the game
pygame.quit()