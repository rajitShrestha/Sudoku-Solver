import pygame
import time
from simplesudokusolver import solve_puzzle,check_validity,find_empty
pygame.font.init()


element_color = (52,31,151)
black = (0,0,0)
white = (255,255,255)
myfont = pygame.font.SysFont("comicans",40)

board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

new_board = [[board[i][j] for j in range(len(board[0]))] for i in range(len(board[0]))]

class Grid:

	def __init__(self,win,row,column,width,height,new_board,selected):

		self.win = win
		self.row = row
		self.column = column
		self.width = width
		self.height = height
		self.new_board = new_board
		self.selected = selected
		self.new_board_grid = [[self.new_board[i][j] for i in range(self.row)] for j in range(self.column) ]


	def insert_values(self):

		for i in range(len(self.new_board[0])): 
			for j in range(len(self.new_board[0])):
				gap = self.width//9
				x = gap*i
				y = gap*j
				value = myfont.render(str(self.new_board[i][j]),0,black)
				invisible_value = myfont.render(str(self.new_board[i][j]),0,white)
				if self.new_board[i][j] != 0:
					self.win.blit(value,(x+(gap//2-value.get_width()//2),y+(gap//2-value.get_width()//2)))
				else:
					invisible_value = myfont.render(str(self.new_board[i][j]),0,white)




	def draw(self,clicked):

		gap_x= self.width//9
		gap_y = self.height//9

		for i in range(self.row+1):

			thickness = 1

			if i%3 == 0 and i!= 0:
				thickness = 3


			pygame.draw.line(self.win,black,(0,i*gap_x),(self.width,i*gap_x),thickness)
			pygame.draw.line(self.win,black,(i*gap_y,0),(i*gap_y,self.height),thickness)

			self.insert_values()

		if clicked != None:

			pygame.draw.rect(self.win,(255,0,0),(clicked[0]*gap_x,clicked[1]*gap_x,gap_x,gap_x),3)

class Solve_sudoku(Grid):

	def __init__(self,win,row,column,width,height,new_board,selected):
		super().__init__(win,row,column,width,height,new_board,selected)
		self.gap = self.width//9

	def click(self,position):

		if (position[0] and position[1]) < self.width:

			x_pos = position[0]//self.gap
			y_pos = position[1]//self.gap

			return (x_pos,y_pos)

	def check_value(self,clicked,key):

		cordinates = list(clicked)

		for i in range(len(self.new_board[0])):
			for j in range(len(self.new_board[0])):

				if self.new_board[cordinates[0]][cordinates[1]] == 0:
					checker = myfont.render(str(key),0,black)
					self.win.blit(checker,(self.gap*cordinates[0],self.gap*cordinates[1]))
					return cordinates


	def replace_value(self,cordinates,clicked,key):
		find = find_empty(new_board)
		replacer = myfont.render(str(key),0,black)
		if check_validity(new_board,key,clicked):
			print("true")
			self.new_board[cordinates[0]][cordinates[1]] = key

	def solve(self):
		solve_puzzle(self.new_board) 


def main():

	selected = False
	clicked = None
	white = (255,255,255)
	win = pygame.display.set_mode((540,600))
	win.fill(white)
	pygame.display.set_caption("Sudoku")
	game = Grid(win,9,9,540,540,new_board,selected)
	sudoku = Solve_sudoku(win,9,9,540,540,new_board,selected)
	run = True
	key = None
	mouse_test = False

	while run:


		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_1:
					key = 1
				if event.key == pygame.K_2:
				 	key = 2
				if event.key == pygame.K_3:
				 	key = 3
				if event.key == pygame.K_4:
					key = 4
				if event.key == pygame.K_5:
					key = 5
				if event.key == pygame.K_6:
					key = 6
				if event.key == pygame.K_7:
					key = 7
				if event.key == pygame.K_8:
					key = 8
				if event.key == pygame.K_9:
					key = 9
				if event.key == pygame.K_KP1:
					key = 1
				if event.key == pygame.K_KP2:
					key = 2
				if event.key == pygame.K_KP3:
					key = 3
				if event.key == pygame.K_KP4:
					key = 4
				if event.key == pygame.K_KP5:
					key = 5
				if event.key == pygame.K_KP6:
					key = 6
				if event.key == pygame.K_KP7:
					key = 7
				if event.key == pygame.K_KP8:
					key = 8
				if event.key == pygame.K_KP9:
					key = 9
				if event.key == pygame.K_SPACE:
					sudoku.solve()
				if key != None and mouse_test:
					cord = sudoku.check_value(clicked,key)

				if event.key == pygame.K_RETURN and mouse_test:
					win.fill(white)
					sudoku.replace_value(cord,clicked,key)

			if event.type == pygame.MOUSEBUTTONDOWN:

				mouse_test = True
				pos = pygame.mouse.get_pos()
				clicked = sudoku.click(pos)
				if clicked:
					win.fill(white)
					game.draw(clicked)
		game.draw(clicked)

		pygame.display.update()


main()
pygame.quit()
