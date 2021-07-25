import pygame

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

#def print_board(bo):
#
#	for i in range(len(bo)):
#
#		if i % 3 == 0 and i != 0:
#			print("- - - - - - - - - - ") 
#
#		for j in range(len(bo[0])): 
#
#			if j  % 3 == 0 and j != 0:
#				print("|",end="") 
#
#			if j == 8:
#				print(bo[i][j])
# 
#			else : 
#				print(str(bo[i][j])+" ",end="") 
 
def solve_puzzle(bo):

	find = find_empty(bo) 

	if not find:  
		return True 

	else:
		row, column = find 

	for i in range(1,10):

		if check_validity(bo,i,(row, column)):
			bo[row][column] = i
			#pygame.time.delay(100)
			#pygame.display.update()
			#print_board(board)

			if solve_puzzle(bo): 
				return True   

			bo[row][column] = 0 

	return False 
 
def check_validity(bo,num,pos):   

	for i in range(len(bo[0])):

		if bo[pos[0]][i] == num and pos[1] != i:
			return False

	for j in range(len(bo[0])):

		if bo[j][pos[1]] == num and pos[0] != i: 
			return False 

	box_x = pos[1] // 3
	box_y = pos[0] // 3 

	for i in range (box_y*3, box_y*3+3): 

		for j in range(box_x*3,box_x*3+3):

			if bo[i][j] == num and (i,j) != pos:
				return False

	return True
 
def find_empty(bo):

	for i in range(len(bo)): 

		for j in range(len(bo[0])):

			if bo[i][j] == 0:  
				return (i,j)

	return None


   
#print_board(board)
solve_puzzle(board) 
#print("____________________")
#print_board(board)