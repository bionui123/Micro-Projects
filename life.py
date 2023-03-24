import pygame
import enum
import time

# Enum for player states
class PlayerState(enum.Enum):
    NEUTRAL = 1
    HUNGRY = 2
    TIRED = 3

# Player class
class Player:
    def __init__(self, screen_width, screen_height):
        self.x = screen_width // 2
        self.y = screen_height // 2
        self.hunger = 100
        self.energy = 100
        self.hunger_decay = 1
        self.energy_decay = 1
        self.radius = 20
        self.state = PlayerState.NEUTRAL
        self.target = None

    def move(self):
        # Move towards the target if set
        if self.target:
            x_diff = self.target.x - self.x
            y_diff = self.target.y - self.y
            distance = (x_diff**2 + y_diff**2)**0.5

            if distance > self.radius:
                self.x += x_diff / distance
                self.y += y_diff / distance

    def update(self):
        # Decrease hunger and energy
        self.hunger -= self.hunger_decay
        self.energy -= self.energy_decay

        # Check player state
        if self.hunger <= 0:
            self.state = PlayerState.HUNGRY
            self.target = None
            for zone in zones:
                if zone.type == "food":
                    self.target = zone
        elif self.energy <= 0:
            self.state = PlayerState.TIRED
            self.target = None
            for zone in zones:
                if zone.type == "sleep":
                    self.target = zone
        elif self.hunger >= 100 and self.energy >= 100:
            self.state = PlayerState.NEUTRAL
            self.target = None
            for zone in zones:
                if zone.type == "home":
                    self.target = zone

# Zone class
class Zone:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
        self.radius = 50

    def update(self, player):
        # Check if player is inside radius
        x_diff = self.x - player.x
        y_diff = self.y - player.y
        distance = (x_diff**2 + y_diff**2)**0.5

        if distance <= self.radius:
            if self.type == "food":
                player.hunger = min(100, player.hunger + 2)
            elif self.type == "sleep":
                player.energy = min(100, player.energy + 2)

# Initialize pygame
pygame.init()

# Set screen size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Create player and zones
player = Player(screen_width, screen_height)
zones = [
    Zone(100, 100, "food"),
    Zone(700, 500, "sleep"),
    Zone(400, 300, "home")
]

# Colors for player states
state_colors = {
    PlayerState.NEUTRAL: (0, 255, 0),
    PlayerState.HUNGRY: (255, 0, 0),
    PlayerState.TIRED: (0, 0, 255)
}

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Clear the screen
    screen.fill((255, 255, 255))

    # Update player and zones
    player.update()
    player.move()
    for zone in zones:
        zone.update(player)

    # Draw player and zones
    pygame.draw.circle(screen, state_colors[player.state], (int(player.x), int(player.y)), player.radius)
    for zone in zones:
        pygame.draw.circle(screen, (255, 0, 0) if zone.type == "food" else (0, 0, 255), (zone.x, zone.y), zone.radius)

    # Update the screen
    pygame.display.update()

# Quit pygame
pygame.quit()