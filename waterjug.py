def r_to_l(x,y,c_x,c_y,n_left,n_right):
	if(x==n_left):
		return
	while True:
		x = x+1
		y = y-1
		if(x==c_x or y==0):
			break	
	print(f"LEFT JUG: {x} AND RIGHT JUG: {y}\n")		
	if(x==c_x):
		pour_left(x,y,c_x,c_y,n_left,n_right)
	else:
		fill_right(x,y,c_x,c_y,n_left,n_right)
	return		

def l_to_r(x,y,c_x,c_y,n_left,n_right):
	if(x==n_left):
		return	
	while True:
		if(x==0 or y==c_y):
			break		
		x = x-1
		y = y+1
	print(f"LEFT JUG: {x} AND RIGHT JUG: {y}\n")	
	if(x==0):	
		fill_left(x,y,c_x,c_y,n_left,n_right)
	else:	
		pour_right(x,y,c_x,c_y,n_left,n_right)
	return


def fill_right(x,y,c_x,c_y,n_left,n_right):
	if(x==n_left):
		return
	y = c_y
	print(f"LEFT JUG: {x} AND RIGHT JUG: {y}\n")
	r_to_l(x,y,c_x,c_y,n_left,n_right)
	return

def fill_left(x,y,c_x,c_y,n_left,n_right):	
	if(x==n_left):
		return
	x=c_x
	print(f"LEFT JUG: {x} AND RIGHT JUG: {y}\n")
	l_to_r(x,y,c_x,c_y,n_left,n_right)	
	return


def pour_right(x,y,c_x,c_y,n_left,n_right):	
	if(x==n_left):
		return
	y=0
	print(f"LEFT JUG: {x} AND RIGHT JUG: {y}\n")	
	l_to_r(x,y,c_x,c_y,n_left,n_right)
	return


def pour_left(x,y,c_x,c_y,n_left,n_right):	
	if(x==n_left):
		return
	x=0
	print(f"LEFT JUG: {x} AND RIGHT JUG: {y}\n")	
	r_to_l(x,y,c_x,c_y,n_left,n_right)
	return

x = 4#int(input())
y = 0#int(input())
c_x = 4
c_y = 3
n_left = 2 #int(input("NEEDED IN LEFT:\n"))
n_right = 0#int(input("NEEDED IN RIGHT:\n"))
print(f"LEFT JUG: {x} AND RIGHT JUG: {y}\n")

if(x==0):
	r_to_l(x,y,c_x,c_y,n_left,n_right)
else:
	l_to_r(x,y,c_x,c_y,n_left,n_right)
	
