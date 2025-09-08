
import pygame,sys,os,random
from pygame.locals import *
from constants import *


'''
class Buttons 
    |
    |
    +----attributes
    |       |
    |       |
    |       +----font,              fontstyle and size
    |       +----surface
    |       +----rect,              then reposition
    |        
    +----methods
            |
            |
            +----draw,              displaysurface.blit(buttonsurface,buttonrect)
            +----collision_check,   button.rect.collidepoint(arg_pos)

class Board
    |
    |
    +----attributes 
    |       |
    |       |
    |       +----tiles,             2d list 
    |       +----solved_board,      arranged 2d list 
    |       +----none_tile,         2d - list index of a value None 
    |       +----clock,             instance of clock object
    |
    |
    +----methods
            |
            |
            +----get_display,       get display surface of pygame window
            |
            +----create_board,      2d list using BOARDHEIGHT as lenght of list, 
            |                       and BOARDHEIGHT as length of inner list, 
            |                       append an incrementing number starting from 1
            |
            +----draw_tiles,        loop through element of the 2d list,
            |                       draw a rect and value of element
            |
            +----randomize_board,   move the blank tile a number of times, 
            |                       draw board each movement 
            |
            +----print_grid, 
            +----str overload, 
            +----move_blank_tile,   get position of blank_tile, 
            |                       get tile using position given
            |                       set value of tile to position of blank_tile, 
            |                       set value of tile in position given to None 
            |
            +----get_blank_tile,    loop through the 2d list, return if None
            +----get_tile,          return element of 2d list at index row, tile

class Game:
    |
    |
    +---attributes 
            |
            |
            +---clock,
            +---board,
            +---reset button 
            +---quit button
            +---action, represents string value 
            +---action button 
            
    +---methods            
            |
            |
            +---
            

'''


class Buttons:
    def __init__(self,text,pos):
        self.font = pygame.font.Font(FONTSTYLE,FONTSIZE)
        self.surface = self.font.render(text,True,TEXTCOLOR)
        self.rect = self.surface.get_rect()
        self.rect.left = pos[0]
        self.rect.bottom = pos[1]
    def draw(self):
        pygame.display.get_surface().blit(self.surface,self.rect)
    def collision_check(self,pos):
        if self.rect.collidepoint(pos):
            return True 
        return False
class Board:
    def __init__(self,clock):
        self.tiles = []
        self.solved_board = []
        self.none_tile = 0,0
        self.clock = clock
        self.create_board()
    def get_display(self):
        return pygame.display.get_surface()
    def create_board(self):
        number = 1
        for row in range(BOARDHEIGHT):
            rows = []
            for tile in range(BOARDWIDTH):
                rows.append(number)
                number += 1
            self.solved_board.append(rows)
            self.tiles.append(rows)
        self.solved_board[-1][-1] = None
        self.tiles[-1][-1] = None
    def draw_tiles(self,exclude=None):
        for row in range(BOARDHEIGHT):
            for tile in range(BOARDWIDTH):
                if exclude != None:
                    continue
                x,y = tile*TILESIZE+XMARGIN,row*TILESIZE+YMARGIN
                tile = self.tiles[row][tile]
                color = TILECOLOR
                if tile == None:
                    color = BLACK
                    tile = ''
                tile_rect = pygame.Rect(x,y,TILESIZE-1,TILESIZE-1)
                font = pygame.font.Font(FONTSTYLE,FONTSIZE)
                font_surface = font.render(str(tile),True,TEXTCOLOR)
                font_rect = font_surface.get_rect(center = tile_rect.center)
                pygame.draw.rect(self.get_display(),color,tile_rect)
                self.get_display().blit(font_surface,font_rect)
    def randomize_board(self,game):
        self.create_board()
        moves = 20
        possible_moves = [self.move_up,self.move_down,self.move_left,self.move_right]
        for move in range(moves):
            game.reset()
            game.draw_game()
            random.choice(possible_moves)()
            game.refresh()
    def print_grid(self):
        print(self)
    def __str__(self):
        board = ''
        for row in range(BOARDHEIGHT):
            for tile in range(BOARDWIDTH):
                boardtile = self.tiles[row][tile]
                if len(str(boardtile)) < 2:
                    board += '0' + str(boardtile) + '    '
                else:
                    board += str(boardtile) + '    '
            board += '\n\n\n\n'
        return f'{board}'
    def move_blank_tile(self,row,tile):
        blankrow,blanktile = self.get_blank_tile()
        dest_row,dest_tile = row , tile
        self.tiles[blankrow][blanktile] = self.tiles[dest_row][dest_tile]
        self.tiles[dest_row][dest_tile] = None
    def get_not_blank_tile(self,row,tile):
        if row in range(BOARDHEIGHT) and tile in range(BOARDWIDTH):
            return self.tiles[row][tile]
        return None
    def get_blank_tile(self):
        for row in range(BOARDHEIGHT):
            for tile in range(BOARDWIDTH):
                boardtile = self.tiles[row][tile]
                if boardtile == None:
                    return row,tile

    def move_up(self):
        row,tile = self.get_blank_tile()
        mrow , mtile = row - 1 , tile
        if self.get_not_blank_tile(mrow,mtile) != None:
            self.move_blank_tile(mrow,mtile)
    def move_down(self):
        row,tile = self.get_blank_tile()
        mrow , mtile = row + 1 , tile
        if self.get_not_blank_tile(mrow,mtile) != None:
            self.move_blank_tile(mrow,mtile)
    def move_right(self):
        row,tile = self.get_blank_tile()
        mrow , mtile = row  , tile + 1
        if self.get_not_blank_tile(mrow,mtile) != None:
            self.move_blank_tile(mrow,mtile)
    def move_left(self):
        row,tile = self.get_blank_tile()
        mrow , mtile = row, tile -1 
        if self.get_not_blank_tile(mrow,mtile) != None:
            self.move_blank_tile(mrow,mtile)    
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_mode(RESOLUTION)
        self.clock = pygame.time.Clock()
        self.board = Board(self.clock)
        print(self.board)
        self.reset_button = Buttons('RESTART',RESTARTPOSITION)
        self.quit_button = Buttons('QUIT',QUITPOSITION)
        self.action = 'RANDOMIZING BOARD'
        self.action_button = self.get_action()
        self.board.randomize_board(self)
        self.action = 'WAITING FOR ACTION'
        self.action_button = self.get_action()
    def get_action(self):
        return Buttons(self.action,ACTIONPOSITION)
    def reset(self):
        self.get_display().fill(BGCOLOR)
    def get_display(self):
        return pygame.display.get_surface()
    def refresh(self):
        pygame.display.flip()
        self.clock.tick(FPS)
    def handle_events(self):
        def buttons(event):
            if event.type == MOUSEBUTTONUP:
                if self.reset_button.collision_check(event.pos):
                    self.action = 'RANDOMIZING BOARD'
                    self.action_button = self.get_action()
                    self.board.randomize_board(self)
                elif self.quit_button.collision_check(event.pos):
                    self.action = 'CLOSING GAME....'
                    self.action_button = self.get_action()
                    self.reset()
                    self.draw_game()
                    self.refresh()
                    pygame.time.delay(300)
                    
                    pygame.quit()
                    sys.exit()
        def move_blanktile(event):
            if event.type == KEYDOWN:
                if event.key == K_w:
                    self.board.move_up()
                    self.action = 'MOVE UP'
                    self.action_button = self.get_action()
                elif event.key == K_d:
                    self.board.move_right()
                    self.action = 'MOVE RIGHT'
                    self.action_button = self.get_action()
                elif event.key == K_a:
                    self.board.move_left()
                    self.action = 'MOVE LEFT'
                    self.action_button = self.get_action()
                elif event.key == K_s:
                    self.board.move_down()
                    self.action = 'MOVE DOWN'
                    self.action_button = self.get_action()
                os.system('cls')
                print(self.board)
        def close_window(event):
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_RETURN:
                self.action = 'CLOSING GAME....'
                self.action_button = self.get_action()
                self.reset()
                self.draw_game()
                self.refresh()
                pygame.time.delay(300)
                pygame.quit()
                sys.exit()
        def print_board(event):
            if event.type == KEYDOWN and event.key == K_p:
                self.board.print_grid()
        def main():
            for event in pygame.event.get():
                close_window(event)
                buttons(event)
                print_board(event)
                move_blanktile(event)
        main()
    def draw_game(self):
        self.reset_button.draw()
        self.quit_button.draw()
        self.action_button.draw()
        self.board.draw_tiles()
    def run(self):
        while True:
            self.reset()
            self.handle_events()
            self.draw_game()
            self.refresh()
if __name__ == '__main__':
    os.system('cls')
    game = Game()
    game.run()