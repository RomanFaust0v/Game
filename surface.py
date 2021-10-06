import pygame
TILE_SIZE = 32



class surface:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, TILE_SIZE, TILE_SIZE)

        self.tile_image = pygame.image.load('Data/Pictures/Dirt1.png')

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getRect(self):
        return self.rect

    def getImg(self):
        return self.tile_image
