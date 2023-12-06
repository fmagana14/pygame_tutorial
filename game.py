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

    # color: blue
    screen.fill((255, 255, 255))
    color = (0,191,255)
    position = (400,400)
    pygame.draw.circle(screen, color, position, 75)

    # color: Red
    color = (255, 0, 0)
    position = (80, 80)
    pygame.draw.circle(screen, color, position, 75)

    # color: Yellow
    color = (255, 255, 0)
    position = (250, 250)
    pygame.draw.circle(screen, color, position, 75)
   
    # color: Green
    color = (0,255,0)
    position = (80,400)
    pygame.draw.circle(screen, color, position, 75)

    # color: Orange
    color = (255,128,0)
    position = (400,80)
    pygame.draw.circle(screen, color, position, 75)  
    
    pygame.display.flip()

# WHEN TYPING THE FOLLOWING: 