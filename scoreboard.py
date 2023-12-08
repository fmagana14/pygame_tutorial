import pygame

class Scoreboard(pygame.sprite.Sprite):
    def __init__(self, x, y, score = 0):
        super(Scoreboard, self).__init__()
        self.score = score
        self.font = pygame.font.SysFont('Comic Sans MS', 36)
        self.surf = self.font.render(f"{self.score}", False, (0, 0, 0))
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0

    def update(self, points):
        self.score += points
        
    def move(self):
        self.x += self.dx
        self.y += self.dy

    def render(self, screen):
        self.surf = self.font.render(f"{self.score}", False, (0, 0, 0))
        screen.blit(self.surf, (self.x, self.y))

    def reset(self):
        self.score = 0 