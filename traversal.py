# code for making the bot move in the grid

# ALL BLOCK COMMENTS ANSWER THE QUESTION "WHAT DO I HAVE AT THIS POINT?"

# take input of the matrix of the image
# store this x,y in a different variable

# take input of the start and the end point

from bot_movement import *
#from click_picture import click_picture

"""
I get a matrix which has some 0's and 1's
I get a start point and an end point
"""

"""
I have a way to move in different directions
I still have to configure these functions
I am working on it lets see what happens.
so now it just becomes a problem of changing my control
from one location to the other in a matrix
"""
"""
/* values represent:
0=free path
1=blocked path
3=valid path
4=invalid path
5=goal
"""
"""
This program gives the best path to move from source to destination.
"""

mapp=[[]]

def look(x, y):
	global mapp
        rows = len(mapp)
        columns = len(mapp[0])
	if (not((x < rows and x >= 0) and (y < columns and y >= 0))):
		return False
	if (mapp[x][y]==5):
		return True
	if (mapp[x][y]!=0):
		return False
	mapp[x][y] = 3
	if (look(x-1,y) == True):
		return True
	if (look(x,y+1) == True):
		return True
	if (look(x+1,y) == True):
		return True
	if (look(x,y-1) == True):
		return True
	#mapp[x][y] = 4
	return False

"""
Now I can create a matrix which has a path path of 3's
which i can follow to get my bot to the final location
"""

def find_path(x, y):
	global mapp
	print mapp
	rows = len(mapp)
        columns = len(mapp[0])
	mapp[x][y] = 0
	while (mapp[x][y] != 5):
		if x-1 >= 0:
			if (mapp[x-1][y] == 3 or mapp[x-1][y] == 5):					# LEFT
				up()
				x -= 1
				if mapp[x][y] == 5:
                                    mapp[x][y] = 0
                                    break
                                else:
                                    mapp[x][y] = 0
                                    print "left"
                                    continue
		if x+1 < rows:
			if (mapp[x+1][y] == 3 or mapp[x+1][y] == 5):
				down()
				x += 1
				if mapp[x][y] == 5:
                                    mapp[x][y] = 0
                                    break
                                else:
                                    mapp[x][y] = 0
                                    print "right"
                                    continue
		if y+1 < columns:
			if (mapp[x][y+1] == 3 or mapp[x][y+1] == 5):					# DOWN
				right()
				y += 1
				if mapp[x][y] == 5:
                                    mapp[x][y] = 0
                                    break
                                else:
                                    mapp[x][y] = 0
                                    print "down"
                                    continue
		if y-1 >=0:
			if (mapp[x][y-1] == 3 or mapp[x][y-1] == 5):					# UP
				left()
				y -= 1
				if mapp[x][y] == 5:
                                    mapp[x][y] = 0
                                    break
                                else:
                                    mapp[x][y] = 0
                                    print "up"
                                    continue
	else:
		return "you have reached your destination" # put a different kind of result

"""
I have reached my final destination
using the matrix with 3's 
I found where there was 3 and accordingly
I moved the bot to the location needed
"""

"""
Now i need to create a function that can make
each location i have to go to 5 in turn so that
i can go and take pictures of each obstacle
"""

# x and y being the current position of the bot
def mapping(x, y, maps):
	global mapp
	mapp = maps
	rows = len(mapp)
        columns = len(mapp[0])
        #look(x,y)
	#find_path(x,y)
	for i in range(rows):
		for j in range(columns):
			if (mapp[i][j] == 1):
				if (i-1 >= 0 and mapp[i-1][j] == 0):
                                        global mapp
					mapp[i-1][j] = 5;
					look(x,y)
					find_path(x,y)
					look_down()
					x = i-1
					y = j
					#click_picture(i,j)
					mapp[i-1][j] = 0
				elif (j+1 < columns and mapp[i][j+1] == 0):
                                        global mapp
					mapp[i][j+1] = 5;
					look(x,y)
					find_path(x,y)
					look_left()
					x = i
					y = j+1
					#click_picture(i,j)
					mapp[i][j+1] = 0
				elif (i+1 < rows and mapp[i+1][j] == 0):
                                        global mapp
					mapp[i+1][j] = 5;
					look(x,y)
					find_path(x,y)
					look_up()
					x = i+1
					y = j
					#click_picture(i,j)
					mapp[i+1][j] = 0
				elif (j-1 >= 0 and mapp[i][j-1] == 0):
                                        global mapp
					mapp[i][j-1] = 5;
					look(x,y)
					find_path(x,y)
					look_right()
					x = i
					y = j-1
					#click_picture(i,j)
					mapp[i][j-1] = 0
				else:
					print "there is some error in mapping function in file traversal.py"
