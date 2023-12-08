from random import choice, randint
from gameobject import GameObject
from constants import lanes


class Apple(GameObject):
    def __init__(self):
        super(Apple, self).__init__(choice([93, 218, 343]), 0, './images/apple.png')
        self.direction = choice([0, 1])
        self.dy = 1  # or set the desired initial value

    def move(self):
        super().move()
        if self.y > 500:
            self.reset()

    def reset(self):
        self.x = choice([93, 218, 343])
        self.direction = choice([0, 1])
        if self.direction == 0:
            self.y = -64
        else:
            self.y = 564