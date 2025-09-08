import pygame,random,sys,os,time
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 640 ; WINDOWHEIGHT = 480
RESOLUTION = 640,480 
FLASHSPEED = 500 
FLASHDELAY = 200 
BUTTONSIZE = 200 
BUTTONGAPSIZE = 20
TIMEOUT = 4

WHITE = 255,255,255
BLACK = 0,0,0
BRIGHTRED = 255,0,0
RED = 155,0,0
BRIGHTGREEN = 0,255,0
GREEN = 0,155,0
BRIGHTBLUE = 0,0,255
BLUE = 0,0,155
BRIGHTYELLOW = 255,255,0
YELLOW = 155,155,0
TEXTCOLOR = 155,155,0


XMARGIN = int((WINDOWWIDTH-(2*BUTTONSIZE)-BUTTONGAPSIZE)/2)
YMARGIN = int((WINDOWHEIGHT-(2*BUTTONSIZE)-BUTTONGAPSIZE)/2)

YELLOWRECT = pygame.Rect(XMARGIN,YMARGIN,BUTTONSIZE,BUTTONSIZE)
BLUERECT = pygame.Rect(XMARGIN+BUTTONGAPSIZE+BUTTONSIZE,YMARGIN,BUTTONSIZE,BUTTONSIZE)
REDRECT = pygame.Rect(XMARGIN,YMARGIN+BUTTONSIZE+BUTTONGAPSIZE,BUTTONSIZE,BUTTONSIZE)
GREENRECT = pygame.Rect(XMARGIN+BUTTONSIZE+BUTTONGAPSIZE,YMARGIN+BUTTONSIZE+BUTTONGAPSIZE,BUTTONSIZE,BUTTONSIZE)

INFOTEXT = 'Match the pattern by clicking on the button or using the Q,W,A,S keys'
INFOTOPLEFT = 10,WINDOWHEIGHT-25

class Buttons:
    def __init__(self):
        pass
class Text:
    def __init__(self,txt_str,color,topleft):
        self.font = pygame.font.Font(r'..\font\freesansbold.ttf',16)
        self.surface = self.font.render(txt_str,1,color)
        self.rect = self.surface.get_rect(topleft=topleft)
    def draw(self):
        pygame.display.get_surface().blit(self.surface,self.rect)
class Sound:
    def __init__(self,file_name):
        self.sound = pygame.mixer.Sound(file_name)
    def play(self):
        self.sound.play()
class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode(RESOLUTION)        
        self.information = Text(INFOTEXT,WHITE,INFOTOPLEFT)
        self.beep = {
                        1:Sound(r'..\audio\beep1.ogg'),
                        2:Sound(r'..\audio\beep2.ogg'),
                        3:Sound(r'..\audio\beep3.ogg'),
                        4:Sound(r'..\audio\beep4.ogg')
                    }
        self.pattern = []
        self.current_step = 0
        self.last_click_time = 0
        self.score_count = 0
        self.score = Text('Score: '+str(self.score_count),WHITE,(WINDOWWIDTH-100,10))
        self.waiting_for_input = False 
        self.clicked_button = None
        self.bgcolor = 0,0,0
    def reset(self):
        self.clicked_button = None
        self.display.fill(self.bgcolor)
        self.score.draw()
        self.information.draw()
    def handle_events(self):
        def quit_event(event):
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_RETURN):
                print('Closing game...')
                #pygame.time.delay(200)
                pygame.quit()
                sys.exit()
        def get_clicked(event):
            if event.type == KEYDOWN:
                if event.key == K_q:
                    self.clicked_button = YELLOW
                elif event.key == K_w:
                    self.clicked_button = BLUE
                elif event.key == K_a:
                    self.clicked_button = RED
                elif event.key == K_s:
                    self.clicked_button = GREEN
        def main():
            for event in pygame.event.get():
                quit_event(event)
                get_clicked(event)
        main()
    def update_game(self):
        def flash_button_animation(button,animation_speed=50):
            if button == YELLOW:
                sound = self.beep[1]
                flash_color = BRIGHTYELLOW
                rectangle = YELLOWRECT
            elif button == BLUE:
                sound = self.beep[2]
                flash_color = BRIGHTBLUE
                rectangle = BLUERECT
            elif button == RED:
                sound = self.beep[3]
                flash_color = BRIGHTRED
                rectangle = REDRECT
            elif button == GREEN:
                sound = self.beep[4]
                flash_color = BRIGHTGREEN
                rectangle = GREENRECT
            original_surface = self.display.copy()
            flash_surface = pygame.Surface((BUTTONSIZE,BUTTONSIZE))
            flash_surface = flash_surface.convert_alpha()
            r,g,b = flash_color
            sound.play()
            for start,end,step in ((0,255,1),(255,0,-1)):
                for alpha in range(start,end,animation_speed*step):
                    self.handle_events()
                    self.display.blit(original_surface,(0,0))
                    flash_surface.fill((r,g,b,alpha))
                    self.display.blit(flash_surface,rectangle.topleft)
                    self.refresh()
            self.display.blit(original_surface,(0,0))
        def draw_buttons():
            pygame.draw.rect(self.display,YELLOW,YELLOWRECT)
            pygame.draw.rect(self.display,BLUE,BLUERECT)
            pygame.draw.rect(self.display,RED,REDRECT)
            pygame.draw.rect(self.display,GREEN,GREENRECT)
        def game_over_animation(button=WHITE,animation_speed=50):
            original_surface = self.display.copy()
            flash_surface = pygame.Surface(self.display.get_size())
            flash_surface = flash_surface.convert_alpha()
            for beep,sound in self.beep.items():
                sound.play()
            r,g,b = button
            for i in range(3):
                for start,end,step in ((0,255,1),(255,0,-1)):
                    for alpha in range(start,end,animation_speed*step):
                        self.handle_events()
                        flash_surface.fill((r,g,b,alpha))
                        self.display.blit(original_surface,(0,0))
                        self.display.blit(flash_surface,(0,0))
                        draw_buttons()
                        self.refresh()
        def change_background_animation(animation_speed=40):
            new_bg_color = (random.randint(0,255)),(random.randint(0,255)),(random.randint(0,255))
            new_bg_surface = pygame.Surface((RESOLUTION))
            new_bg_surface = new_bg_surface.convert_alpha()
            
            r,g,b = new_bg_color
            
            for alpha in range(0,255,animation_speed):
                self.handle_events()
                self.reset()
                new_bg_surface.fill((r,g,b,alpha))
                self.display.blit(new_bg_surface,(0,0))
                draw_buttons()
                self.refresh()
            self.bgcolor = new_bg_color
        def main():
            if not self.waiting_for_input:
                pygame.display.update()
                pygame.time.wait(1000)
                self.pattern.append(random.choice([YELLOW,BLUE,RED,GREEN]))
                for button in self.pattern:
                    flash_button_animation(button)
                    pygame.time.wait(FLASHDELAY)
                self.waiting_for_input = True
            else:
                if self.clicked_button and (self.clicked_button == self.pattern[self.current_step]):
                    flash_button_animation(self.clicked_button)
                    self.current_step += 1
                    self.last_click_time = time.time()
                    if self.current_step == len(self.pattern):
                        change_background_animation()
                        self.score_count += 1
                        self.waiting_for_input = False 
                        self.current_step = 0
                elif (self.clicked_button and self.clicked_button != self.pattern[self.current_step]) or (self.current_step != 0 and time.time() - TIMEOUT > self.last_click_time):
                    game_over_animation()
                    self.pattern = []
                    self.current_step = 0
                    self.waiting_for_input = False
                    self.score_count = 0
                    pygame.time.wait(1000)
                    change_background_animation()
        draw_buttons()
        main()
        self.refresh()
    def refresh(self):
        pygame.display.flip()
        self.clock.tick(FPS)
    def run(self):
        while True:
            self.reset()
            self.handle_events()
            self.update_game()
            self.refresh()
if __name__ == '__main__':
    os.system('cls')
    game = Game()
    game.run()
    
