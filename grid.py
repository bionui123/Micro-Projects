import pygame
import sys
import random

class Grid:
    def __init__(self, width, height, cell_size, pattern):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.pattern = pattern

    def draw(self, screen):
        for i in range(5):
            for j in range(5):
                x = j * self.cell_size
                y = i * self.cell_size
                color = (map_value(self.pattern[i][j]), map_value(self.pattern[i][j]), map_value(self.pattern[i][j]))
                pygame.draw.rect(screen, color, (x, y, self.cell_size, self.cell_size))

def create_map():
    return [[random.uniform(0, 1) for j in range(5)] for i in range(5)]

def map_value(val):
    return int(val * 255)

def run_game():
    # initialize pygame
    pygame.init()

    # set window size and title
    width, height = 500, 500
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Grid Pattern")

    # set the cell size
    cell_size = 100

    # initialize pattern
    pattern = create_map()

    # initialize grid
    grid = Grid(width, height, cell_size, pattern)

    # main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        # clear the screen
        screen.fill((0, 0, 0))

        # draw the grid
        grid.draw(screen)

        # update the display
        pygame.display.update()

    # quit pygame
    pygame.quit()
    sys.exit()

run_game()

# let's create a Cell class that tracks its brightness value and update the Grid class to implement this
# add a universally called decay function that incrementally reduces the value of all cell's brightness until each cell is back to 0 (resting value) please note a cell's value can not go below 0

# You will be assisting in writing a draft for a pygame project. Please prioritize using classes and functions to make the dev process easier and more legible. Please write a pygame script that has a timer displayed that counts down from the timer variable. There should also be a Touple "range" variable that is instantiated at the beginning of the gameplay. There is a circle on the screen that's size is dependent on a size variable that increases "inflate_rate" amount when the space bar is held and decreases "inflate_decay" amount when it is not held. Whether or not the space bar is held should be checked per tick and the size should update accordingly. Please also include easily toggle-able labels (show_labels(bool))for all of these attributes to be displayed while we are debugging and make sure the display updated on every tick(tick_speed). 