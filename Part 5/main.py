import pygame
import constants
from character import Character
from weapon import Weapon

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("My Game")

# Create clock for FPS
clock = pygame.time.Clock()

# Define player movements
moving_left = False
moving_right = False
moving_up = False
moving_down = False

# Scale function
def scale_image(image, scale):
    return pygame.transform.scale(image, (image.get_width() * scale, image.get_height() * scale))

# Load weapon image
# arbalest_image = pygame.image.load("assets/weapons/arbalest.png")
arbalest_image = scale_image(pygame.image.load("assets/weapons/arbalest.png"), constants.WEAPON_SCALE)
bow_image = scale_image(pygame.image.load("assets/weapons/bow.png"), constants.WEAPON_SCALE)

# Load character images
chracter_animations = []
character_types = ["player", "buggy", "chunky", "ghosty", "kibby", "kitty", "muddy"]

animation_types = ["standing", "running"]

for character_type in character_types:
    animated_character_images = []
    for animation_type in animation_types:
        temp_list = []
        for i in range(4):
            player_image = pygame.image.load(f"assets/characters/{character_type}/{animation_type}/{i}.png")
            player_image = scale_image(player_image, constants.SCALE)
            temp_list.append(player_image)
        animated_character_images.append(temp_list)

    chracter_animations.append(animated_character_images)

# Create character
player = Character(100, 100, chracter_animations, 0) # Give index 0 for player

# Create weapon
arbalest = Weapon(arbalest_image)
# bow = Weapon(bow_image)

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

    # Update player position
    player.move(deltaX, deltaY)

    # Update player
    player.update()

    # Update weapon
    arbalest.update(player)

    # Draw player on screen
    player.draw(screen)

    # Draw weapon on screen
    arbalest.draw(screen)

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # keyboard inputs
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                moving_left = True
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                moving_right = True
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                moving_up = True
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                moving_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                moving_left = False
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                moving_right = False
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                moving_up = False
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                moving_down = False

    # Update screen
    pygame.display.update()

pygame.quit()
exit()