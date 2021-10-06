import pygame
GRAVITY = 1


class PLayer:
    def __init__(self):
        self.x = 300
        self.y = 400
        self.image = pygame.image.load('Data/Pictures/Player.png')
        self.rect = pygame.Rect(self.x, self.y, 16, 32)
        self.vel_y = 0

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getImg(self):
        return self.image

    def getRect(self):
        return self.rect

    def move(self):
        dy = 0
        dx = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            dx -= 10

        if key[pygame.K_RIGHT]:
            dx = 10

        self.vel_y += GRAVITY
        dy += self.vel_y
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > 800:
            dx = 800 - self.rect.right
        if self.rect.bottom + dy > 600:
            self.vel_y = -20
        self.rect.x += dx
        self.rect.y += dy
