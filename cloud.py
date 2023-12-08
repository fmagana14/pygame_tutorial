import pygame
from random import choice, randint
from gameobject import GameObject
from constants import lanes


class Cloud(GameObject):
    def __init__(self):
        super(Cloud, self).__init__(0, 0, './images/Cloud-b.png')
        self.dx = 1 

    def move(self):
        self.x += self.dx
        if self.x > 500:
            self.reset()

    def reset(self):
        self.x = -64
        self.y = randint(50,200)
        self.surf = pygame.image.load(choice(['./images/Cloud-b.png', './images/Cloud-c.png']))
