#.\module\my_code\playing_sound_files.py

import pygame ,sys
pygame.init()

resolution = 300,50
window = pygame.display.set_mode(resolution)

sound_1_name = 'beep1.ogg'
sound1 = pygame.mixer.Sound('audio/beep1.ogg') 

sound_2_name = 'beep2.ogg'
sound2 = pygame.mixer.Sound('audio/beep2.ogg')

sound_3_name = 'beep3.ogg'
sound3 = pygame.mixer.Sound('audio/beep3.ogg')

sound_4_name = 'beep4.ogg'
sound4 = pygame.mixer.Sound('audio/beep4.ogg')

playing = ''
playing_name = ''
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_1:
				playing_name = sound_1_name
				print('playing....',playing_name )
				playing = sound1
			elif event.key == pygame.K_2:
				playing_name = sound_2_name
				print('playing....',playing_name )
				playing = sound2
			elif event.key == pygame.K_3:
				playing_name = sound_3_name
				print('playing....',playing_name )
				playing = sound3
			elif event.key == pygame.K_4:
				playing_name = sound_4_name
				playing = sound4
			elif event.key == pygame.K_0:
				print('stop playing.....',playing_name)
				if playing != '':
					playing.stop()
				playing = ''
			elif event.key == pygame.K_RETURN:
				pygame.quit()
				sys.exit()
			if playing != '':								playing.play()
		
	
	
