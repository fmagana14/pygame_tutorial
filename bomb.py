from random import choice, randint
from gameobject import GameObject
from constants import lanes

class Bomb(GameObject):
    def __init__(self):
        super(Bomb, self).__init__(0, choice(lanes), './images/bomb.png')
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
        self.x = -64
        self.y = choice(lanes)
        self.direction = choice([0, 1])
        if self.direction == 0:
            self.x = -64
        else:
            self.x = 565
