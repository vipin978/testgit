def n_queens(col):
	if col>n-1:
		return True
	row = 0
	while row<=n-1:
		queens.append((row,col))
		if issafe(row,col) and n_queens(col+1):
			return True
		queens.pop()		
		row = row+1
	return False

def issafe(r,c):
	for i in range(len(queens)-1):
		if(queens[i][0]==r):
			return False
		if(abs(queens[i][0]-r)==abs(queens[i][1]-c)):
			return False
	return True			


n = 4
queens = []
n_queens(0)
print(queens)
