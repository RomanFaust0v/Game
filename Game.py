import pygame
from player import PLayer
from world import world

clock = pygame.time.Clock()
FPS = 60
WHITE = (255, 255, 255)
TILE_SIZE = 32


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
        self.background = pygame.image.load('Data/Pictures/background.png')
        self.world = world(tile_map, self.screen)
        self.player = PLayer(self.world.tiles)

    def run(self):
        running = True
        while running:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.player.move()
            self.draw()

            pygame.display.flip()
        pygame.quit()

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.world.draw()
        self.screen.blit(self.player.getImg(), (self.player.rect.x, self.player.rect.y))
        #pygame.draw.rect(self.screen, WHITE, self.player.rect)
