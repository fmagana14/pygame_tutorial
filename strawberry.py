from random import choice, randint
from gameobject import GameObject
from constants import lanes

class Strawberry(GameObject):
    def __init__(self):
        super(Strawberry, self).__init__(0, choice(lanes), './images/strawberry.png')
        self.dx = (randint(0, 200) / 100) + 1
        self.dy = 0
        self.reset()
        self.direction = choice([0, 1])

    def move(self):
        if self.direction == 0:
            self.x += self.dx
            self.y += self.dy
            # Check the y position of the apple
            if self.x > 500:
                self.reset()
        else:
            self.x -= self.dx
            self.y -= self.dy
            # Check the y position of the apple
            if self.x < 0:
                self.reset()

    def reset(self):
        self.x = choice(lanes)
        self.direction = choice([0, 1])
        if self.direction == 0:
            self.y = -64
        else:
            self.y = 564
