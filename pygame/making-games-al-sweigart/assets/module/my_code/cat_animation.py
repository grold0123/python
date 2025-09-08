import pygame,sys
pygame.init()


class Cat:
	def __init__(self):
		self.image = pygame.image.load('graphics/cat.png')
		self.rect = self.image.get_rect()
		self.direction = 'right'



class Game:
	def __init__(self):
		
		#frames per second
		self.fps = 30
		self.clock = pygame.time.Clock()
		
		#window
		resolution = 400,300
		flags = 0
		bits = 32
		game_title = 'Animation'
		self.display_window = pygame.display.set_mode(
						resolution,
						flags,
						bits
					)
		pygame.display.set_caption(game_title)
		
		self.white = (255,255,255)
		
		self.cat = Cat()
		

	def game_loop(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT or (
							event.type == pygame.KEYDOWN
							and event.key == pygame.K_RETURN
							):
					pygame.quit()
					sys.exit()

			self.display_window.fill(self.white)
			if self.cat.direction == 'right':
				self.cat.rect.x += 5
				if self.cat.rect.x == 280:
					self.cat.direction = 'down'
			elif self.cat.direction == 'down':
				self.cat.rect.y += 5
				if self.cat.rect.y == 220:
					self.cat.direction = 'left'
			elif self.cat.direction == 'left':
				self.cat.rect.x -= 5
				if self.cat.rect.x == 10:
					self.cat.direction = 'up'
			elif self.cat.direction == 'up':
				self.cat.rect.y -= 5
				if self.cat.rect.y == 10:
					self.cat.direction = 'right' 
			self.display_window.blit(
				self.cat.image,self.cat.rect
				)

			pygame.display.update()
			self.clock.tick(self.fps)

if __name__ == '__main__':
	game = Game()
	game.game_loop()