# activate the virtual enviornment python -m venv venv
# importing pygame
import pygame
from random import choice
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, lanes
from gameobject import GameObject
from apple import Apple
from strawberry import Strawberry
from player import Player
from bomb import Bomb
from cloud import Cloud
from scoreboard import Scoreboard

pygame.init()


# class GameObject(pygame.sprite.Sprite):
    # def __init__(self, x, y, image):
    #     super(GameObject, self).__init__()
    #     self.surf = pygame.image.load(image)
    #     self.x = x
    #     self.y = y
    #     self.rect = self.surf.get_rect()

    # def render(self, screen):
    #     self.rect.x = self.x  # add
    #     self.rect.y = self.y  # add
    #     screen.blit(self.surf, self.rect.topleft)


# Create an instance of GameObject


# class Apple(GameObject):
#     def __init__(self):
#         super(Apple, self).__init__(choice(lanes), 0, './images/apple.png')
#         self.dx = 0
#         self.dy = (randint(0, 200) / 100) + 1
#         self.reset()
#         self.direction = choice([0, 1])

#     def move(self):
#         if self.direction == 0:
#             self.x += self.dx
#             self.y += self.dy
#             if self.y > 500:
#                 self.reset()
#         else:
#             self.x -= self.dx
#             self.y -= self.dy
#             if self.y < 0:
#                 self.reset()

#  # add a new method
#     def reset(self):
#         self.x = choice(lanes)
#         self.direction = choice([0, 1])
#         if self.direction == 0:
#             self.y = -64
#         else:
#             self.y = 564


# class Strawberry(GameObject):
    # def __init__(self):
    #     super(Strawberry, self).__init__(0, choice(lanes), './images/strawberry.png')
    #     self.dx = (randint(0, 200) / 100) + 1
    #     self.dy = 0
    #     self.reset()
    #     self.direction = choice([0, 1])

    # def move(self):
    #     if self.direction == 0:
    #         self.x += self.dx
    #         self.y += self.dy
    #         # Check the y position of the apple
    #         if self.x > 500:
    #             self.reset()
    #     else:
    #         self.x -= self.dx
    #         self.y -= self.dy
    #         # Check the y position of the apple
    #         if self.x < 0:
    #             self.reset()

    # def reset(self):
    #     self.x = -64
    #     self.y = choice(lanes)
    #     self.direction = choice([0, 1])
    #     if self.direction == 0:
    #         self.x = -64
    #     else:
    #         self.x = 565


# class Player(GameObject):
#     def __init__(self):
#         super(Player, self).__init__(0, 0, './images/player.png')
#         self.dx = 93
#         self.dy = 93
#         self.pos_x = 1
#         self.pos_y = 1
#         self.reset()

#     def left(self):
#         if self.pos_x > 0:
#             self.pos_x -= 1
#             self.update_dx_dy()

#     def right(self):
#         if self.pos_x < len(lanes) - 1:
#             self.pos_x += 1
#             self.update_dx_dy()

#     def up(self):
#         if self.pos_y > 0:
#             self.pos_y -= 1
#             self.update_dx_dy()

#     def down(self):
#         if self.pos_y < len(lanes) - 1:
#             self.pos_y += 1
#             self.update_dx_dy()

#     def move(self):
#         self.x -= (self.x - self.dx) * 0.25
#         self.y -= (self.y - self.dy) * 0.25

#     def reset(self):
#         self.rect.x = lanes[self.pos_x]
#         self.rect.y = lanes[self.pos_x]
#         self.dx = self.rect.x
#         self.dy = self.rect.y

#     def update_dx_dy(self):
#         self.dx = lanes[self.pos_x]
#         self.dy = lanes[self.pos_y]


class Fruit(GameObject):
    def __init__(self, image):
        super(Fruit, self).__init__(0, 0, image)

    def reset(self):
        self.rect.x = choice(lanes)
        self.rect.y = -64


# class Bomb(GameObject): 
    # def __init__(self):
    #     super(Bomb, self).__init__(0, choice(lanes), './images/bomb.png')
    #     self.dx = (randint(0, 200) / 100) + 1
    #     self.dy = 0
    #     self.reset()
    #     self.direction = choice([0, 1])

    # def move(self):
    #     if self.direction == 0:
    #         self.x += self.dx
    #         self.y += self.dy
    #     # Check the y position of the apple
    #         if self.x > 500:
    #             self.reset()
    #     else:
    #         self.x -= self.dx
    #         self.y -= self.dy
    #     # Check the y position of the apple
    #         if self.x < 0:
    #             self.reset()

    # def reset(self):
    #     self.x = -64
    #     self.y = choice(lanes)
    #     self.direction = choice([0, 1])
    #     if self.direction == 0:
    #         self.x = -64
    #     else:
    #         self.x = 565

# class Cloud(GameObject):
#     def __init__(self):
#         super(Cloud, self).__init__(0, 0, './images/Cloud-b.png')
#         self.dx = 1 

#     def move(self):
#         self.x += self.dx
#         if self.x > 500:
#             self.reset()

#     def reset(self):
#         self.x = -64
#         self.y = randint(50,200)
#         self.surf = pygame.image.load(choice(['./images/Cloud-b.png', './images/Cloud-c.png']))


# instances
apple = Apple()
strawberry = Strawberry()
player = Player()
bomb = Bomb()
cloud = Cloud()
score = Scoreboard(30, 30, 0)
# made a fruit group
fruit_sprites = pygame.sprite.Group()
# make a sprites group
all_sprites = pygame.sprite.Group()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

all_sprites.add(apple)
all_sprites.add(strawberry)
all_sprites.add(player)
all_sprites.add(bomb)
all_sprites.add(cloud)
all_sprites.add(score)


fruit_sprites.add(apple)
fruit_sprites.add(strawberry)


# Making the game loop
running = True
clock = pygame.time.Clock()

while running:
    # Looks at events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                player.left()
            elif event.key == pygame.K_RIGHT:
                player.right()
            elif event.key == pygame.K_UP:
                player.up()
            elif event.key == pygame.K_DOWN:
                player.down()

    # reset screen
    screen.fill((255, 255, 255))

    for entity in all_sprites:
        entity.move()
        entity.render(screen)
   
    # Check Colisions
    fruit = pygame.sprite.spritecollideany(player, fruit_sprites)
    if fruit:
        score.update(100)
        fruit.reset()
    if pygame.sprite.collide_rect(player, bomb):
        running = False
    
    score.move
    score.render(screen)
    # Update the window
    pygame.display.flip()
    clock.tick(60)

# Quit the pygame
pygame.quit()
