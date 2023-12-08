from random import choice, randint
from gameobject import GameObject
from constants import lanes


class Apple(GameObject):
    def __init__(self):
        super(Apple, self).__init__(choice(lanes), 0, './images/apple.png')
        self.dx = 0
        self.dy = (randint(0, 200) / 100) + 1
        self.reset()
        self.direction = choice([0, 1])

    def move(self):
        if self.direction == 0:
            self.x += self.dx
            self.y += self.dy
            if self.y > 500:
                self.reset()
        else:
            self.x -= self.dx
            self.y -= self.dy
            if self.y < 0:
                self.reset()

 # add a new method
    def reset(self):
        self.x = choice(lanes)
        self.direction = choice([0, 1])
        if self.direction == 0:
            self.y = -64
        else:
            self.y = 564