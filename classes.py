# This file is dedicated to classes
import pygame
import random

# Initialise Pygame
pygame.init()

# Variables
blue = (0, 0, 255)
red = (255, 0, 0)


# Create rectangles and render them
class rectangle:
    def __init__(self, color, rect):
        self.color = color
        self.rectX = rect[0]
        self.recty = rect[1]
        self.width = rect[2]
        self.height = rect[3]

    def render(self, screen):
        pygame.draw.rect(screen, self.color, (self.rectX, self.recty, self.width, self.height))
