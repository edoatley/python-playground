import random
import copy
import sys

BOARDWIDTH = 7
BOARDHEIGHT = 6

BOARD = [[0 for x in range(BOARDWIDTH)] for y in range(BOARDHEIGHT)] 

def main():
	print('main')
	fillATestBoard()
	#drawBoard()

def fillATestBoard():
	print('fill')
	for x in range(BOARDWIDTH + 1):
		print('x = {0:1d}'.format(x))
		for y in range(BOARDHEIGHT):	
			print('y = {0:1d}'.format(y))
			if ((x + y) % 2) == 1:
				print("BOARD[{0:1d}][{1:1d}] is X".format(x, y))
				BOARD[x][y] = 'X'
			else:
				print("BOARD[{0:1d}][{1:1d}] is O".format(x, y))
				BOARD[x][y] = 'O' 


def drawBoard():
    print('draw')
    for x in range(1, BOARDWIDTH + 1):
        print(' %s  ' % x)
    print()

    print('+---+' + ('---+' * (BOARDWIDTH - 1)))

    for y in range(BOARDHEIGHT):
        print('|   |' + ('   |' * (BOARDWIDTH - 1)))

        print('|')
        for x in range(BOARDWIDTH):
            print(' %s |' % BOARD[x][y])
        print()

        print('|   |' + ('   |' * (BOARDWIDTH - 1)))

        print('+---+' + ('---+' * (BOARDWIDTH - 1)))

main()