import math
import pygame
import constants

class Character():
    def __init__(self, x, y, chracter_animations, character_type):
        self.character_type = character_type
        self.animated_player_images = chracter_animations[character_type]
        self.frame_index = 0
        self.action = 1 
        self.running = False
        self.update_time = pygame.time.get_ticks()
        self.image = self.animated_player_images[self.action][self.frame_index]
        self.flip = False
        self.rect = pygame.Rect(0, 0, 40, 40)
        self.rect.center = (x, y)

    def move(self, deltaX, deltaY):
        # Check if we're running
        self.running = deltaX != 0 or deltaY != 0

        if deltaX < 0:
            self.flip = True
        elif deltaX > 0:
            self.flip = False

        # Diagonal movement speed
        if deltaX != 0 and deltaY != 0: # Press buttons at the same time
            deltaX *= (math.sqrt(2) / 2)
            deltaY *= (math.sqrt(2) / 2)
            
        self.rect.x += deltaX
        self.rect.y += deltaY
    
    def update(self):
        if self.running:
            self.update_action(1) # run
        else:
            self.update_action(0)

        animation_cooldown = 100
        now = pygame.time.get_ticks()
        if now - self.update_time > animation_cooldown:
            self.update_time = now
            self.frame_index += 1
            if self.frame_index >= len(self.animated_player_images[self.action]):
                self.frame_index = 0
            self.image = self.animated_player_images[self.action][self.frame_index]

    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()


    def draw(self, screen):
        flipped_image = pygame.transform.flip(self.image, self.flip, False)
        if self.character_type == 0:
            screen.blit(flipped_image, (self.rect.x, self.rect.y - (constants.PLAYER_OFFSET * constants.SCALE)))
        else:
            screen.blit(flipped_image, self.rect)
        pygame.draw.rect(screen, constants.RED, self.rect, 1) 
