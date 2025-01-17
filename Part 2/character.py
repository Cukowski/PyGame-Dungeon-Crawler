import math
import pygame
import constants

class Character():
    def __init__(self, x, y, animated_player_images):
        self.animated_player_images = animated_player_images
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.image = animated_player_images[self.frame_index]
        self.flip = False
        self.rect = pygame.Rect(0, 0, 40, 40)
        self.rect.center = (x, y)

    def move(self, deltaX, deltaY):
        if deltaX < 0:
            self.flip = True
        elif deltaX > 0:
            self.flip = False

        # diagonal movement speed
        if deltaX != 0 and deltaY != 0: # press buttons at the same time
            deltaX *= (math.sqrt(2) / 2)
            deltaY *= (math.sqrt(2) / 2)
            
        self.rect.x += deltaX
        self.rect.y += deltaY
    
    def update(self):
        animation_cooldown = 100
        now = pygame.time.get_ticks()
        if now - self.update_time > animation_cooldown:
            self.update_time = now
            self.frame_index += 1
            if self.frame_index >= len(self.animated_player_images):
                self.frame_index = 0
            self.image = self.animated_player_images[self.frame_index]

    def draw(self, screen):
        flipped_image = pygame.transform.flip(self.image, self.flip, False)
        screen.blit(flipped_image, self.rect)
        pygame.draw.rect(screen, constants.RED, self.rect, 1) 
