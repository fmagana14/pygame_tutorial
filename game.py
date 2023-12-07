# activate the virtual enviornment python -m venv venv
# importing pygame 
import pygame
pygame.init()
# creating the screen size
screen = pygame.display.set_mode([500,500])

# rest of your code...


# making the game loop
running = True
while running: 
    # looks at event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # # Clear the Screen

   # Configure the screen

    # Create a new instance of surface
    surf = pygame.Surface([50,50])
    surf.fill((255, 111, 33))

    # clear screen
    screen.fill((255, 255, 255))

    # Draw the surface 
    screen.blit(surf, (100, 120))
    
    pygame.display.flip()

# WHEN TYPING THE FOLLOWING: 