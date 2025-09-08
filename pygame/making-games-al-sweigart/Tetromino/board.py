import pygame 
from constants import *
class Board:
    def __init__(self):
        self.width = BOARDWIDTH
        self.height = BOARDHEIGHT
    def draw(self):
        for y in range(self.height):
            for x in range(self.width):
                base_rect = pygame.Rect(X_OFFSET+(x*BOXSIZE),Y_OFFSET+(y*BOXSIZE),BOXSIZE,BOXSIZE)
                pygame.draw.rect(pygame.display.get_surface(),pygame.Color('white'),base_rect,1)

