from random import choice, randint
from gameobject import GameObject
from constants import lanes


class Strawberry(GameObject):
    def __init__(self):
        super(Strawberry, self).__init__(0, choice([93, 218, 343]), './images/strawberry.png')
        self.direction = choice([0, 1])
        self.dx = 1
        self.dy = 0  

    def move(self):
        super().move()
        if self.x > 500:
            self.reset()

    def reset(self):
        self.x = -64
        self.y = choice([93, 218, 343])
        self.direction = choice([0, 1])
        if self.direction == 0:
            self.x = -64
        else:
            self.x = 564

    