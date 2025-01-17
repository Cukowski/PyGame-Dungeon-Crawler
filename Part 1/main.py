import pygame
import constants
from character import Character

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("My Game")

# Create clock for FPS
clock = pygame.time.Clock()

# Define player movements
moving_left = False
moving_right = False
moving_up = False
moving_down = False

# Create character
character = Character(100, 100)

# Main game loop
running = True
while running:
    # Set FPS
    clock.tick(constants.FPS)

    # Clear screen
    screen.fill(constants.BACKGROUND_COLOR)

    # Calculate characters movement delta x and delta y
    deltaX = 0
    deltaY = 0
    if moving_left:
        deltaX -= constants.SPEED
    if moving_right:
        deltaX += constants.SPEED
    if moving_up:
        deltaY -= constants.SPEED
    if moving_down:
        deltaY += constants.SPEED

    # Update character position
    character.move(deltaX, deltaY)

    # Draw character on screen
    character.draw(screen)

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # keyboard inputs
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
            elif event.key == pygame.K_RIGHT:
                moving_right = True
            elif event.key == pygame.K_UP:
                moving_up = True
            elif event.key == pygame.K_DOWN:
                moving_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            elif event.key == pygame.K_RIGHT:
                moving_right = False
            elif event.key == pygame.K_UP:
                moving_up = False
            elif event.key == pygame.K_DOWN:
                moving_down = False

    # Update screen
    pygame.display.update()

pygame.quit()
exit()