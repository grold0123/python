'''
1.  Board - 10x20
2.  Box - for each grid coordinate in board
3.  Piece - made up of 4 boxes
4.  Shape - different combination of boxes , 
5.  Template - a list of shape data structures that represents all possible rotations of a shape.
6.  Landed - when a piece has reached the bottom of board or is touching a box
'''
import pygame,sys,os
from board import Board
from constants import *
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_mode(RESOLUTION)
        pygame.display.set_caption('')
    def main(self):
        while True:
            self.run()
    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            board = Board()
            board.draw()
            self.refresh()
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    def update(self):
        pass 
    def draw(self):
        pass
    def refresh(self):
        pygame.display.flip()
        pygame.time.Clock().tick()

if __name__ == '__main__':
    os.system('cls')
    game = Game()
    game.main()    

