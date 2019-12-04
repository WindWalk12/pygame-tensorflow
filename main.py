from classes import *
import pygame
import random

pygame.init()

# Creates the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game with Tensorflow")

# Variables
blue = (0, 0, 255)
red = (255, 0, 0)

# Controllable rectangle
center = (375, 275)
rectX = 375
rectY = 275

# Movements of the controllable rectangle
rectX_change = 0
rectY_change = 0
speed_left = -0.2
speed_right = 0.2
speed_up = -0.2
speed_down = 0.2

# uncontrollable rectangle
urectX = random.randint(100, 700)
urectY = random.randint(25, 575)


# Function to draw the controllable rectangle
def rect(color, x, y):
    pygame.draw.rect(screen, color, (x, y, 50, 50))


def urect(color, x, y):
    pygame.draw.rect(screen, color, (x, y, 100, 25))


# Infinite loops the game until closed
running = True
while running:
    # Set screen color - RGB
    screen.fill((70, 70, 70))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Control rectangle
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # Left key
                rectX_change = speed_left
            if event.key == pygame.K_RIGHT:
                # Right key
                rectX_change = speed_right
            if event.key == pygame.K_UP:
                # Up key
                rectY_change = speed_up
            if event.key == pygame.K_DOWN:
                # Down key
                rectY_change = speed_down
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                rectX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                rectY_change = 0

    # Movements of controllable rectangle
    rectX += rectX_change
    rectY += rectY_change

    # Make sure the controllable rectangle stays in the screen
    if rectX <= 0:
        rectX_change = 0
    elif rectX >= 750:
        rectX_change = 0
    elif rectY <= 0:
        rectY_change = 0
    elif rectY >= 550:
        rectY_change = 0

    # Creates the controllable rectangle
    rect(blue, rectX, rectY)

    # Creates the uncontrollable rectangle
    urect(red, urectX, urectY)

    # Updates the screen
    pygame.display.update()
