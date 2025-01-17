import math
import pygame
import constants

class Character():
    def __init__(self, x, y):
        self.rect = pygame.Rect(0, 0, 40, 40)
        self.rect.center = (x, y)

    def move(self, deltaX, deltaY):
        # diagonal movement speed
        if deltaX != 0 and deltaY != 0: # press buttons at the same time
            deltaX *= (math.sqrt(2) / 2)
            deltaY *= (math.sqrt(2) / 2)
            
        self.rect.x += deltaX
        self.rect.y += deltaY

    def draw(self, screen):
        pygame.draw.rect(screen, constants.RED, self.rect)
