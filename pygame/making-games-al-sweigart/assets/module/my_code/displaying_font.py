#.\module\my_code\displaying_font.py 
import pygame, sys
pygame.init()

resolution = 400,300
game_title = 'Hello World'
window = pygame.display.set_mode(resolution)
pygame.display.set_caption(game_title)

white = (255,255,255)
green = (0,255,0)
blue = (0,0,128)

font_style = pygame.font.Font('font/freesansbold.ttf',32)
text = 'Hello World!'
display_text = font_style.render(text,True,green,blue)
display_text_rect = display_text.get_rect(center=(200,150))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT or ( 
					event.type == pygame.KEYDOWN and 					event.key == pygame.K_RETURN):
			pygame.quit()
			sys.exit()
	window.fill(white)
	window.blit(display_text,display_text_rect)
	pygame.display.update()
	
