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
grid_width = 10
grid_height = 20
grid_size = 30
grid = [[BLACK for _ in range(grid_width)] for _ in range(grid_height)]

# Define the Tetriminos
tetriminos = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 1], [0, 0, 1]],  # J
    [[1, 1, 1], [1, 0, 0]]  # L
]

# Define the current Tetrimino
current_tetrimino = random.choice(tetriminos)
current_tetrimino_x = grid_width // 2 - len(current_tetrimino[0]) // 2
current_tetrimino_y = 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the current Tetrimino down
    current_tetrimino_y += 1

    # Check for collision
    if current_tetrimino_y + len(current_tetrimino) > grid_height:
        current_tetrimino_y -= 1
        # Add the current Tetrimino to the grid
        for i in range(len(current_tetrimino)):
            for j in range(len(current_tetrimino[i])):
                if current_tetrimino[i][j] == 1:
                    grid[current_tetrimino_y + i][current_tetrimino_x + j] = random.choice([RED, GREEN, BLUE, CYAN, MAGENTA, YELLOW, ORANGE])

        # Check for completed rows
        completed_rows = []
        for i in range(grid_height):
            if all(cell != BLACK for cell in grid[i]):
                completed_rows.append(i)

        # Remove completed rows and shift the rest down
        for row in completed_rows:
            del grid[row]
            grid.insert(0, [BLACK] * grid_width)

        # Generate a new current Tetrimino
        current_tetrimino = random.choice(tetriminos)
        current_tetrimino_x = grid_width // 2 - len(current_tetrimino[0]) // 2
        current_tetrimino_y = 0

    # Clear the window
    window.fill(WHITE)

    # Draw the grid
    for i in range(grid_height):
        for j in range(grid_width):
            pygame.draw.rect(window, grid[i][j], (j * grid_size, i * grid_size, grid_size, grid_size))

    # Draw the current Tetrimino
    for i in range(len(current_tetrimino)):
        for j in range(len(current_tetrimino[i])):
            if current_tetrimino[i][j] == 1:
                pygame.draw.rect(window, random.choice([RED, GREEN, BLUE, CYAN, MAGENTA, YELLOW, ORANGE]), ((current_tetrimino_x + j) * grid_size, (current_tetrimino_y + i) * grid_size, grid_size, grid_size))

    # Update the display
    pygame.display.update()

# Quit the game
pygame.quit()