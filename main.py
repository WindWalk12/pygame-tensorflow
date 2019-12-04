from classes import *

pygame.init()

# Creates the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game with Tensorflow")

# Controllable rectangle
center = (375, 275)
rectX = 375
rectY = 275
rectWidth = 50
rectHeight = 50

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
urectWidth = 100
urectHeight = 25

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
    rect = rectangle(blue, (rectX, rectY, rectWidth, rectHeight))
    rect.render(screen)

    # Creates the uncontrollable rectangle
    urect = rectangle(red, (urectX, urectY, urectWidth, urectHeight))
    urect.render(screen)

    # Updates the screen
    pygame.display.update()
