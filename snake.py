import pygame
import random
import sys

pygame.init()
WINDOW_SIZE = (600, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Snake")
FPS = 10
clock = pygame.time.Clock()
GRID_SIZE = 20
x = WINDOW_SIZE[0] // 2
y = WINDOW_SIZE[1] // 2
dx = 0
dy = -GRID_SIZE
snake = [(x, y)]
food_x = random.randint(0, WINDOW_SIZE[0] // GRID_SIZE - 1) * GRID_SIZE
food_y = random.randint(0, WINDOW_SIZE[1] // GRID_SIZE - 1) * GRID_SIZE
food = (food_x, food_y)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dx = 0
                dy = -GRID_SIZE
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = GRID_SIZE
            elif event.key == pygame.K_LEFT:
                dx = -GRID_SIZE
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = GRID_SIZE
                dy = 0
    x += dx
    y += dy
    x %= WINDOW_SIZE[0]
    y %= WINDOW_SIZE[1]
    if (x, y) in snake:
        print("You lost!")
        break
    snake.insert(0, (x, y))
    if (x, y) != food:
        snake.pop()
    else:
        food_x = random.randint(0, WINDOW_SIZE[0] // GRID_SIZE - 1) * GRID_SIZE
        food_y = random.randint(0, WINDOW_SIZE[1] // GRID_SIZE - 1) * GRID_SIZE
        food = (food_x, food_y)
    screen.fill(BLACK)
    for square in snake:
        pygame.draw.rect(screen, WHITE, (square[0], square[1], GRID_SIZE, GRID_SIZE))
    pygame.draw.rect(screen, RED, (food[0], food[1], GRID_SIZE, GRID_SIZE))
    pygame.display.update()
    clock.tick(FPS)
