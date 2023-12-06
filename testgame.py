# Example 2

# Import and initialize pygame
import pygame as testgame
testgame.init()
# Configure the screen
screen = testgame.display.set_mode([500, 500])

# Create a new instance of surface
surf = testgame.Surface((50, 50))
surf.fill((255, 111, 33))
# draw the surface
screen.blit(surf, (100, 120))

running = True
while running:
    # Looks at events
    for event in testgame.event.get():
        if event.type == testgame.QUIT:
            running = False

    # Draw a circle
    screen.fill((255, 255, 255))
    # Update the window
    testgame.display.flip()
