import pygame
import random

# Initialize pygame
pygame.init()

# Set game dimensions and title
WIDTH = 500
HEIGHT = 500
TITLE = "Floor is Lava"

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

# Set colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Set grid dimensions
GRID_SIZE = 10
SQUARE_SIZE = 50

# Initialize highscore
highscore = 0

# Initialize game variables
grid = [[0 for x in range(GRID_SIZE)] for y in range(GRID_SIZE)]
player_x = 0
player_y = 0
score = 0

# Function to generate new map
def generate_map():
    global grid, player_x, player_y
    # Reset grid and player position
    grid = [[0 for x in range(GRID_SIZE)] for y in range(GRID_SIZE)]
    player_x = 0
    player_y = 0
    # Generate white squares
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            if random.random() < 0.8 or (x == 0 and y == 0):
                grid[x][y] = 1
    # Generate yellow square
    while True:
        x = random.randint(0, GRID_SIZE - 1)
        y = random.randint(0, GRID_SIZE - 1)
        if grid[x][y] == 1:
            grid[x][y] = 2
            player_x = x
            player_y = y
            break

# Run game loop
running = True
generate_map()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Handle arrow key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and player_x > 0:
                player_x -= 1
            elif event.key == pygame.K_RIGHT and player_x < GRID_SIZE - 1:
                player_x += 1
            elif event.key == pygame.K_UP and player_y > 0:
                player_y -= 1
            elif event.key == pygame.K_DOWN and player_y < GRID_SIZE - 1:
                player_y += 1
            # Check if player moved off of white square
            if grid[player_x][player_y] == 1:
                grid[player_x][player_y] = 0
                score += 1
            # Check if player moved back to yellow square
            if grid[player_x][player_y] == 2:
                generate_map()
                if score > highscore:
                    highscore = score
                score = 0
    # Draw grid
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            if grid[x][y] == 1:
                        pygame.draw.rect(screen, WHITE, (x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            elif grid[x][y] == 2:
                pygame.draw.rect(screen, YELLOW, (x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    # Draw player
    pygame.draw.rect(screen, RED, (player_x * SQUARE_SIZE, player_y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    # Draw score and highscore
    score_text = pygame.font.Font(None, 30).render("Score: " + str(score), True, (0, 0, 0))
    highscore_text = pygame.font.Font(None, 20).render("Highscore: " + str(highscore), True, (0, 0, 0))
    screen.blit(score_text, (WIDTH/2 - score_text.get_width()/2, 20))
    screen.blit(highscore_text, (WIDTH - highscore_text.get_width() - 20, 20))
    # Update display
    pygame.display.update()
    #Quit pygame
    pygame.quit()
