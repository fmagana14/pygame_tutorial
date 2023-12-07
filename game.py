# activate the virtual enviornment python -m venv venv
# importing pygame 
import pygame
pygame.init()
# creating the screen size
screen = pygame.display.set_mode([500,500])


class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(GameObject, self).__init__()
        self.surf = pygame.image.load(image)
        self.rect = self.surf.get_rect()
        self.rect.x = x
        self.rect.y = y

    def render(self, screen):
        screen.blit(self.surf, self.rect)

# Create an instance of GameObject
apple = GameObject(120, 300, 'apple.png')

# Making the game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the game objects
    apple.render(screen)

    # Update the window
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit the pygame
pygame.quit()



# class GameObject(pygame.sprite.Sprite):
#   def __init__(self, x, y, width, height):
#     super(GameObject, self).__init__()
#     self.surf = pygame.Surface((width, height))
#     self.surf.fill((255, 0, 255))
#     self.rect = self.surf.get_rect()
#     self.x = x
#     self.y = y

#   def render(self, screen):
#     screen.blit(self.surf, (self.x, self.y))

# box = GameObject(120, 300, 50, 50)

# # making the game loop
# running = True
# while running: 
#     # looks at event
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

# # Clear screen
# screen.fill((255, 255, 255))
# # Draw box
# box.render(screen)
# # Update the window
# pygame.display.flip()
# # WHEN TYPING THE FOLLOWING: 