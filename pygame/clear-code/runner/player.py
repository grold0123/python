 
import pygame

class Player:
    def __init__(self):
        walk1 = pygame.image.load('/graphics/Player/player_walk_1.png').convert_alpha()
        walk2 = pygame.image.load('/graphics/Player/player_walk_2.png').convert_alpha()
        self.player_walk = [walk1,walk2]
        self.player_index = 0
        self.player_jump = pygame.image.load('/graphics/Player/jump.png').convert_alpha()

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(80,300))
        self.jump_sound = pygame.mixer.Sound('/audio/jump.mp3')
        self.jump_sound.set_volume(0.5)
    def player_input(self):
        pass