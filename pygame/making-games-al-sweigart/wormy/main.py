import pygame,sys,os,random
from pygame.locals import *

GAMETITLE = 'Wormy'
CELLSIZE = 20
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
RESOLUTION = WINDOWWIDTH,WINDOWHEIGHT
CELLWIDTH = int(WINDOWWIDTH/CELLSIZE)       # number of cells lenght-wise
CELLHEIGHT = int(WINDOWHEIGHT/CELLSIZE)     # number of cells height-wise
FONTSTYLE = 'freesansbold.ttf'

WHITE   = 255,255,255
BLACK   = 0,0,0
RED     = 255,0,0
GREEN   = 0,255,0
DARKGREEN = 0,155,0
DARKGRAY = 40,40,40
BGCOLOR = BLACK

FPS = 15

RIGHT = 'right'
LEFT = 'left'
UP = 'up'
DOWN = 'down'


DIFFICULTY = 1

class Apple:
    def __init__(self):
        self.pos = random.randint(0,CELLWIDTH-1),random.randint(0,CELLHEIGHT-1)
    def get_rect(self):
        x,y = self.pos
        return pygame.Rect(x*CELLSIZE,y*CELLSIZE,CELLSIZE,CELLSIZE)
    def spawn(self):
        self.pos = random.randint(0,CELLWIDTH-1),random.randint(0,CELLHEIGHT-1)
    def draw(self):
        pygame.draw.rect(pygame.display.get_surface(),RED,self.get_rect())
class Worm:
    def __init__(self):
        x,y = random.randint(0,CELLWIDTH-5),random.randint(0,CELLHEIGHT-5)
        self.body = [(x,y),(x-1,y),(x-2,y)]
        self.direction = RIGHT
    def get_head(self):
        return self.body[0]
    def get_rect(self,pos):
        x,y = pos 
        return pygame.Rect(x*CELLSIZE,y*CELLSIZE,CELLSIZE,CELLSIZE)
    def draw(self):
        display = pygame.display.get_surface()
        for part in self.body:
            x,y = part[0]*CELLSIZE,part[1]*CELLSIZE
            pygame.draw.rect(display,DARKGREEN,(x,y,CELLSIZE,CELLSIZE))
            pygame.draw.rect(display,GREEN,(x+4,y+4,CELLSIZE-8,CELLSIZE-8))
    def move(self):
        x,y = self.get_head()
        direction = self.direction
        if direction == RIGHT:
            pos = x+1,y 
            self.body.insert(0,pos)
        elif direction == LEFT:
            pos = x-1,y 
            self.body.insert(0,pos)
        elif direction == UP:
            pos = x,y-1 
            self.body.insert(0,pos)
        elif direction == DOWN:
            pos = x,y+1 
            self.body.insert(0,pos)
    def remove_tail(self):
        self.body.pop()
class Level:
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.basic_font = pygame.font.Font(FONTSTYLE,18)
        self.title_font = pygame.font.Font(FONTSTYLE,100)
        self.game_over_font = pygame.font.Font(FONTSTYLE,150)
    def draw_grid(self):
        for x in range(CELLWIDTH):
            x = x * CELLSIZE
            start_pos = x,0
            end_pos = x,CELLWIDTH * CELLSIZE
            pygame.draw.line(self.display,DARKGRAY,start_pos,end_pos)
        for y in range(CELLHEIGHT):
            y = y * CELLSIZE
            start_pos = 0,y
            end_pos = CELLWIDTH * CELLSIZE ,y
            pygame.draw.line(self.display,DARKGRAY,start_pos,end_pos)
    def draw_score(self,score):
        pass
        surface = self.basic_font.render(f'Score: {score}',True,WHITE)
        rect = surface.get_rect()
        rect.topleft = WINDOWWIDTH-120,10
        self.display.blit(surface,rect)
    def draw_press_key(self):
        surface = self.basic_font.render('Press a key to play',True,WHITE,2)
        rect = surface.get_rect()
        rect.topleft = (WINDOWWIDTH-200,WINDOWHEIGHT-30)
        self.display.blit(surface,rect)
    def draw_game_over(self):
        g_surface = self.game_over_font.render('Game',True,WHITE)
        o_surface = self.game_over_font.render('Over',True,WHITE)
        g_rect = g_surface.get_rect()
        o_rect = o_surface.get_rect()
        g_rect.midtop = WINDOWWIDTH/2,10
        o_rect.midtop = WINDOWWIDTH/2,g_rect.height+10+25
        self.display.blit(g_surface,g_rect)
        self.display.blit(o_surface,o_rect)
    def draw(self,score):
        self.draw_grid()
        self.draw_score(score)
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_mode(RESOLUTION)
        pygame.display.set_caption(GAMETITLE)
    def main(self):
        self.in_game = True
        self.running = False
        self.level = Level()
        self.standby()
        while self.in_game:
            self.run()
            self.game_over_screen()
        self.close_game()
    def close_game(self):
        pygame.quit()
        sys.exit()
    def game_over_screen(self):
        while not self.running:
            self.level.draw_game_over()
            self.level.draw_press_key()
            self.refresh_screen()
            pygame.time.wait(500)
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    self.running = True
    def standby(self):
        def background_fill():
            pygame.display.get_surface().fill(BGCOLOR)
        def draw(surface,rect):
            pygame.display.get_surface().blit(surface,rect)
        font = self.level.title_font
        surface1 = font.render('Wormy!',True,WHITE,DARKGREEN)
        surface2 = font.render('Wormy!',True,GREEN)
        degrees1,degrees2 = 0,0
        while not self.running:
            background_fill()
            rsurface1 = pygame.transform.rotate(surface1,degrees1)
            rrect1 = rsurface1.get_rect()
            rrect1.center = WINDOWWIDTH/2,WINDOWHEIGHT/2
            rsurface2 = pygame.transform.rotate(surface2,degrees2)
            rrect2 = rsurface2.get_rect()
            rrect2.center = WINDOWWIDTH/2,WINDOWHEIGHT/2
            draw(rsurface1,rrect1)
            draw(rsurface2,rrect2)
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    self.running = True
            self.level.draw_press_key()
            self.refresh_screen()
            degrees1,degrees2 = degrees1+3,degrees2+7
    def run(self):
        self.worm = Worm()
        self.apple = Apple()
        self.score = 0
        self.running = True
        while self.running :
            self.handle_events()
            self.update()
            self.draw()
            self.refresh_screen()
    def handle_events(self):
        def worm_control(event):
            if event.type == KEYDOWN:
                if event.key == K_w and self.worm.direction != DOWN:
                    self.worm.direction = UP
                elif event.key == K_s and self.worm.direction != UP:
                    self.worm.direction = DOWN
                elif event.key == K_d and self.worm.direction != LEFT:
                    self.worm.direction = RIGHT
                elif event.key == K_a and self.worm.direction != RIGHT:
                    self.worm.direction = LEFT
        def close_game(event):
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                self.close_game()
        def main():
            for event in pygame.event.get():
                close_game(event)
                worm_control(event)
        main()
    def update(self):
        def eat():
            head_rect = self.worm.get_rect(self.worm.get_head())
            apple_rect = self.apple.get_rect()
            if apple_rect.colliderect(head_rect):
                self.score += 1
                self.apple.spawn()
            else:
                self.worm.remove_tail()
        def bite_self():
            head_rect = self.worm.get_rect(self.worm.get_head())
            for part in self.worm.body[1:]:
                part_rect = self.worm.get_rect(part)
                if part_rect.colliderect(head_rect):
                    self.running = False
        def out_of_bounds():
            x,y = self.worm.get_head()
            if 0>x or x>=CELLWIDTH or 0>y or y>=CELLHEIGHT:
                self.running = False            
        self.worm.move()
        eat()
        out_of_bounds()
        bite_self()
    def draw(self):
        def background_fill():
            pygame.display.get_surface().fill(BGCOLOR)
        def apple():
            self.apple.draw()
        def worm():
            self.worm.draw()
        def level():
            self.level.draw(self.score)
        background_fill()
        level()
        apple()
        worm()
    def refresh_screen(self):
        pygame.display.flip()
        pygame.time.Clock().tick(FPS)
        

if __name__ == '__main__':
    os.system('cls')
    game = Game()
    game.main()