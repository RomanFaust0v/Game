import pygame
from world import world

WHITE = (255, 255, 255)
TILE_SIZE = 32

tile_image = pygame.image.load('Data/Pictures/Dirt1.png')
tile_map = {}
for i in range(10):
    tile_map[str(i + 4) + ';14'] = [i + 4, 14]
tile_map['15;10'] = [15, 10]
tile_map['16;10'] = [16, 10]



class game:
    def __init__(self, screensize):
        pygame.init()
        self.screenWidth = screensize[0]
        self.screenHeight = screensize[1]
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        self.world = world(tile_map)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.draw()

            pygame.display.flip()
        pygame.quit()

    def draw(self):
        for tile in tile_map:
            pygame.draw.rect(self.screen, WHITE, pygame.Rect(tile_map[tile][0] * TILE_SIZE, tile_map[tile][1] * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)
            self.screen.blit(tile_image, (tile_map[tile][0] * TILE_SIZE, tile_map[tile][1] * TILE_SIZE))
