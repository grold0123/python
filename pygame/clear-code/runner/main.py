import pygame,sys,os
from constants import *
from player import *
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_mode(RESOLUTION)
    def main(self):
        while True:
            self.run()
    def run(self):
        player = Player()
        while True:
            self.handle_events()
            self.update()
            self.draw()
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
        pygame.time.Clock().tick(FPS)

if __name__ == '__main__':
    os.system('cls')
    game = Game()
    game.main()
