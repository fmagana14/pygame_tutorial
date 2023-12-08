from random import choice, randint
from gameobject import GameObject
from constants import lanes

class Bomb(GameObject):
    def __init__(self):
        super(Bomb, self).__init__(choice([93, 218, 343]), 0, './images/bomb.png')
        self.dx =1
        self.dy =1


    def move(self):
        super().move()
        if self.x > 500:
            self.x = -64
        elif self.x < -64:
            self.x = 565
        if self.y > 500:
            self.reset()


    def reset(self):
        self.x = -64
        self.y = choice([93, 218, 343])
        self.direction = choice([0, 1])
        if self.direction == 0:
            self.x = -64
        else:
            self.x = 565
