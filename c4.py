from __future__ import print_function
from random import randint
# import random
# import copy
# import sys

BOARDWIDTH = 7
BOARDHEIGHT = 6
RED = 'R'
YELLOW = 'Y'
EMPTY = ' '

# co-ordinates are always given in the for x, y i.e. across then up
#
#
#     +---+---+---+---+---+---+---+
#   5 | O | X | O | X | O | X | O |
#     +---+---+---+---+---+---+---+
#   4 | X | O | X | O | X | O | X |
#     +---+---+---+---+---+---+---+
#   3 | O | X | O | X | O | X | O |
#     +---+---+---+---+---+---+---+
#   2 | X | O | X | O | X | O | X |
#     +---+---+---+---+---+---+---+
#   1 | O | X | O | X | O | X | O |
#     +---+---+---+---+---+---+---+
#   0 | X | O | X | O | X | O | X |
#     +---+---+---+---+---+---+---+
#       0   1   2   3   4   5   6 ---> x

BOARD = [[EMPTY for y in range(BOARDHEIGHT)] for x in range(BOARDWIDTH)] 

def main():
    #fillATestBoard()

    # randomly choose first player
    first = randint(0, 1)
    firstToPlay = RED
    if first == 0:
        firstToPlay = YELLOW

    playRandomlyANumberOfTurns(10, firstToPlay)
    drawBoard()

def playRandomlyANumberOfTurns(totalTurns, firstToPlay):
    # randomly select a column
    # check if that column can be played i.e. it is a valid move
    currentTurn = firstToPlay

    for turn in range(totalTurns):
    	playATurnAtRandom(currentTurn)
    	if currentTurn == RED:
    		currentTurn = YELLOW
    	else:
    	    currentTurn = RED	

def playATurnAtRandom(colour):    
    invalidMove = True;

    validMoveExists = checkValidMoveExists()

    while invalidMove and validMoveExists:
    	columnIndex = randint(0, BOARDWIDTH - 1)
    	heightIndex = findLowestValidHeightPosition(columnIndex)
    	if(heightIndex => 0):
    		invalidMove = False

def checkValidMoveExists():
	# need to check there actually is a valid place to play
	validMoveExists = False
    for x in range(BOARDWIDTH):
        if EMPTY == BOARD[x][BOARDHEIGHT - 1]:
        	validMoveExists = True
        	break
        	
    return validMoveExists


def findLowestValidHeightPosition(columnIndex):
    # this needs to check if the column is a valid move and if so return the lowest index. 
    # If move is invalid as the column is full return -1


def fillATestBoard():
    print('fill')
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            if ((x + y) % 2) == 1:
                print("BOARD[{0:1d}][{1:1d}] is X".format(x, y))
                BOARD[x][y] = RED
            else:
                print("BOARD[{0:1d}][{1:1d}] is O".format(x, y))
                BOARD[x][y] = YELLOW 

# functions to draw the connect 4 board
def drawBoard():
    print('drawBoard')
    
    # draw numbers along the top
    for x in range(BOARDWIDTH):
        print('  {0} '.format(x + 1), end='')
    print('')

    # start with a structural row outside the loop
    drawStructuralRow()

	# when drawing we need to do y axis backwards i.e bottom to top!
    for y in range(BOARDHEIGHT, -1, -1):
        drawRow(y)    
        drawStructuralRow()  

def drawStructuralRow():
    print('+---+' + ('---+' * (BOARDWIDTH - 1)))

def drawRow(rowNum):
    #print('drawRow(' + str(rowNum) + ')')
    for x in range(BOARDWIDTH):
        print('| {0} '.format(BOARD[x][rowNum]), end='')
    print('|')


# call the main function once everything defined
main()