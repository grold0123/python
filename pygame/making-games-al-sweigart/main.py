from constants import *
from box import Box
from board import Board

class Game:
	def __ini__(self):
		self.board = None
	
	def get_randomized_board():
		self.board = Board()
		icons = []
		for color in ALLCOLORS:
			for shape in ALLSHAPES:
				icons.append((shape,color))

		random.shuffle
		