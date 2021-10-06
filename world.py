import pygame
from surface import surface
TILE_SIZE = 32
WHITE = (255, 255, 255)


class world:
    def __init__(self, tile_map, screen):
        self.tile_map = tile_map
        self.tiles = []
        self.tileInit()
        self.screen = screen

    def tileInit(self):
        for tile in self.tile_map:
            self.tiles.append(surface(self.tile_map[tile][0] * TILE_SIZE, self.tile_map[tile][1] * TILE_SIZE))

    def draw(self):
        for tile in self.tiles:
            pygame.draw.rect(self.screen, WHITE, tile.getRect(), 1)
            self.screen.blit(tile.getImg(), (tile.getX(), tile.getY()))
