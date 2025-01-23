import pygame
import math

class Weapon():
    def __init__(self, image):
        self.original_image = image
        self.angle = 0
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect() # Get the rect of the image

    # Weapon will be placed on the player
    def update(self, player):
        self.rect.center = player.rect.center

        # Get mouse position
        mouse_pos = pygame.mouse.get_pos()

        # Calculate angle
        x_distance = mouse_pos[0] - self.rect.centerx
        y_distance = -(mouse_pos[1] - self.rect.centery)
        self.angle = math.degrees(math.atan2(y_distance, x_distance)) - 45

    def draw(self, screen):
        # Draw positioned image
        self.image = pygame.transform.rotate(self.original_image, self.angle)

        # We'll add ofset for smooth motion and correct position
        screen.blit(self.image, ((self.rect.centerx - self.image.get_width() / 2), (self.rect.centery - self.image.get_height() / 2)))
