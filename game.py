# activate the virtual enviornment python -m venv venv
# importing pygame 
import pygame
from random import randint
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
class Apple(GameObject):
    def __init__(self):
        super(Apple,self).__init__(0, 0, 'apple.png')
        self.dx = 0 
        self.dy = (randint(0, 200) / 100) + 1
        self.reset()

    def move(self):
        self.x += self.dx
        self.y += self.dy
   # Check the y position of the apple
        if self.y > 500: 
            self.reset()

 # add a new method
    def reset(self):
       self.x = randint(50, 400)
       self.y = -64

class Player(GameObject):
  def __init__(self):
    super(Player, self).__init__(0, 0, 'player.png')
    self.dx = 0
    self.dy = 0
    self.reset()

  def left(self):
    self.dx -= 100

  def right(self):
    self.dx += 100

  def up(self):
    self.dy -= 100

  def down(self):
    self.dy += 100

  def move(self):
    self.rect.x -= (self.rect.x - self.dx) * 0.25
    self.rect.y -= (self.rect.y - self.dy) * 0.25
    
  def reset(self):
    self.x = 250 - 32
    self.y = 250 - 32


apple = Apple()

player = Player()

# Making the game loop
running = True
clock = pygame.time.Clock()

while running:
    # Inside the event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.left()
            elif event.key == pygame.K_RIGHT:
                player.right()
            elif event.key == pygame.K_UP:
                player.up()
            elif event.key == pygame.K_DOWN:
                player.down()

    #  Update the position of the object of each frame
    apple.rect.x += 1
    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the game objects
    apple.move()
    apple.render(screen)

    #player
    player.move()
    player.render(screen)

    # Update the window
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit the pygame
pygame.quit()


