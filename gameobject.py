import pygame



class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image, dx=0, dy=0):
        super(GameObject, self).__init__()
        self.surf = pygame.image.load(image)
        self.x = x
        self.y = y
        self.rect = self.surf.get_rect()
        self.dx = dx
        self.dy = dy

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def render(self, screen):
        self.rect.x = self.x  # add
        self.rect.y = self.y  # add
        screen.blit(self.surf, self.rect.topleft)
