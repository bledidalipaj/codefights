
def nqueen_backtrack(row, n, board=[[False] * 8] * 8):
	def queen_safe(row, col):
		for i in range(n):
			if board[row][i] == True or board[i][col] == True:
				return False
		reset = min(row, col) - 1

		i = row - reset
		j = col - reset

		while i < n and j < n:
			if board[i][j] == True:
				return False
			i += 1
			j += 1

		i = row - reset
		j = col + reset

		while i < n and j > 0:
			if board[i][j] == True:
				return False
			i += 1
			j -= 1
		return True
		
	for i in range(n):
		if queen_safe(row, i):
			board[row][i] = True 		# place a queen
			if row == n:
				return board
			else:
				nqueen_backtrack(row + 1, n)

if __name__ == '__main__':
	nqueen_backtrack(1, 4)