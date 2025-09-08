import sys,os,pygame,random
from constants import * 
from pygame.locals import *

class Box:
    def __init__(self,pos,color,shape):
        self.grid_pos = pos 
        x,y = pos
        x = x * (BOXSIZE+GAPSIZE)+XMARGIN
        y = y * (BOXSIZE+GAPSIZE)+YMARGIN
        self.rect = pygame.Rect(x,y,BOXSIZE,BOXSIZE)
        self.color = color 
        self.shape = shape 
        self.display = pygame.display.get_surface()
        self.is_selected = False
        self.is_revealed = False
    def draw_icon(self):
        quarter = int(BOXSIZE * 0.25) # syntactic sugar            
        half =    int(BOXSIZE * 0.5)  # syntactic sugar
        left, top = self.rect.x,self.rect.y
        color,shape = self.color,self.shape
        DISPLAYSURF = self.display
        # Draw the shapes
        if shape == DONUT:
            pygame.draw.circle(DISPLAYSURF, color, (left + half, top + half), half - 5)
            pygame.draw.circle(DISPLAYSURF, BGCOLOR, (left + half, top + half), quarter - 5)
        elif shape == SQUARE:
            pygame.draw.rect(DISPLAYSURF, color, (left + quarter, top + quarter, BOXSIZE - half, BOXSIZE - half))
        elif shape == DIAMOND:
            pygame.draw.polygon(DISPLAYSURF, color, ((left + half, top), (left + BOXSIZE - 1, top + half), (left + half, top + BOXSIZE - 1), (left, top + half)))
        elif shape == LINES:
            for i in range(0, BOXSIZE, 4):
                pygame.draw.line(DISPLAYSURF, color, (left, top + i), (left + i, top))
                pygame.draw.line(DISPLAYSURF, color, (left + i, top + BOXSIZE - 1), (left + BOXSIZE - 1, top + i))
        elif shape == OVAL:
            pygame.draw.ellipse(DISPLAYSURF, color, (left, top + quarter, BOXSIZE, half))
    def draw_cover(self):
        pygame.draw.rect(self.display,BOXCOLOR,self.rect)
    def collision_check(self,pos):
        if self.rect.collidepoint(pos):
            return True 
        return False
    def reset(self):
        self.is_selected = False
    def select(self):        
        self.is_selected = True
    def reveal(self):
        self.is_revealed = True
class Board:
    def __init__(self):
        self.boxes = None
        self.random_boxes()
    def random_boxes(self):
        self.boxes = []
        icons = []
        for color in ALLCOLORS:
            for shape in ALLSHAPES:
                icons.append((color,shape))
        random.shuffle(icons)
        ic_count = int(ROWS*COLUMNS/2)
        icons = icons[:ic_count]*2
        random.shuffle(icons)
        for column in range(COLUMNS):
            rows = []
            for row in range(ROWS):
                pos = row,column
                color,shape = icons.pop(0)
                rows.append(Box(pos,color,shape))
            self.boxes.append(rows)
    def draw_board(self):
        for row in self.boxes:
            for box in row:
                if not box.is_selected and not box.is_revealed:
                    box.draw_cover()
    def draw_icons(self):
        for row in self.boxes:
            for box in row:
                if box.is_selected or box.is_revealed:
                    box.draw_icon()
    def get_board(self):
        board = []
        for row in self.boxes:
            for box in row:
                board.append(box)
        return board
class Mouse:
    def __init__(self):
        self.pos = 0,0
        self.is_clicked = False
    def reset(self):
        self.is_clicked = False
    def click(self):
        self.is_clicked = True 
    def move(self,pos):
        self.pos = pos
class Puzzle:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock = pygame.time.Clock()
        self.mouse = Mouse()
        self.board =Board()
        self.selected = []
        self.reveal_count = 0
    def new_game_animation(self,group,boxes):
        def draw_covers(group):
            self.display_surface.fill((0,0,0))
            for box in boxes:
                if box not in group:
                    box.draw_cover()
        def draw_cover_frame(group,coverage):
            for box in group:
                box.draw_icon()
                x,y = box.rect.x,box.rect.y
                rect = pygame.Rect(x,y,coverage,BOXSIZE)
                pygame.draw.rect(self.display_surface,BOXCOLOR,rect)
        def draw_reveal_frame(group,coverage):
            for box in group:
                box.draw_icon()
                x,y = box.rect.x,box.rect.y
                rect = pygame.Rect(x,y,coverage,BOXSIZE)
                pygame.draw.rect(self.display_surface,BOXCOLOR,rect)
        def reveal_animation(group):
            for coverage in range(BOXSIZE,-REVEALSPEED,-REVEALSPEED):
                draw_covers(group)
                draw_cover_frame(group,coverage)
                pygame.display.flip()
                self.clock.tick(FPS)
        def cover_animation(group):
            for coverage in range(0,BOXSIZE+REVEALSPEED,REVEALSPEED):
                draw_covers(group)
                draw_reveal_frame(group,coverage)
                pygame.display.flip()
                self.clock.tick(FPS)
        reveal_animation(group)
        cover_animation(group)
    def newgame(self):
        self.board.random_boxes()
        boxes = self.board.get_board()
        group_count = 7
        groups = [boxes[i:i+group_count]for i in range(0,len(boxes),group_count)]
        random.shuffle(groups)
        for group in groups:
            self.new_game_animation(group,boxes)
            pygame.display.flip()
            pygame.time.wait(300)
    def draw(self):
        self.board.draw_board()
        self.board.draw_icons()
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_RETURN):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                self.mouse.move(event.pos)
            elif event.type == MOUSEBUTTONUP:
                self.mouse.move(event.pos)
                self.mouse.click()
            elif event.type == KEYDOWN:
                if event.key == K_0:
                    print(self.reveal_count)
                elif event.key == K_9:
                    self.newgame()
    def update_game(self):
        def select_box():
            if self.mouse.is_clicked:
                for box in self.board.get_board():
                    if box.collision_check(self.mouse.pos):
                        if not box in self.selected:
                            box.select()
                            self.selected.append(box)
        select_box()
    def compare(self):
        box1 = self.selected[0].color,self.selected[0].shape
        box2 = self.selected[1].color,self.selected[1].shape
        if box1 == box2:
            return True 
        return False
    def reset(self):
        def reset_selected():
            if len(self.selected) == 2:
                if self.compare():
                    for box in self.selected:
                        box.reveal()
                    self.reveal_count += 1
                else:
                    for box in self.selected:
                        box.reset()
                self.selected = []
                pygame.time.wait(250)
        self.display_surface.fill((0,0,0))
        reset_selected()
        self.mouse.reset()
    def refresh_screen(self):
        pygame.display.flip()
        self.clock.tick(FPS)
    def run(self):
        self.newgame()
        while True:
            self.reset()
            self.handle_events()
            self.update_game()
            self.draw()
            self.refresh_screen()
if __name__ == '__main__':
    game = Puzzle()
    game.run()
    
    
    '''
    29
    1,3
    4,14
    2,6
    5,7
    8,9
    10,11
    12,13
    15,16
    18,19
    22,24
    25,26
    
    1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,22,24,25,26,29
    
    '''