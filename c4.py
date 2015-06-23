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

    firstToPlay = randomlySelectFirstPlayer()

    playRandomlyANumberOfTurns(30, firstToPlay)

    drawBoard()
    
    evaluateBoardForWinner()

def evaluateBoardForWinner():
    """ This method examines the board for a winner either vertically, diagonally or horizontally """

    print("Horizontal ", checkHorizontals())
    print("Vertical ", checkVerticals())
    print(checkDiagonals())


def checkHorizontals():
    """This method checks for any horizontal victories! """
    
    result = "No Winner"

    for rowIndex in range(BOARDHEIGHT):
        # initialise at the start of the current row
        colour = RED
        count = 0
        for columnIndex in range(BOARDWIDTH):
            thisColour = BOARD[columnIndex][rowIndex]

            if thisColour == colour:
                count = count + 1
            elif thisColour == EMPTY:
                count = 0
            else:
                colour = thisColour
                count = 1

            if count == 4:
                result = "win for {0}, in row {1:d}".format(colour, rowIndex + 1)
                break
   
    return result

def checkVerticals():
    """This method checks for any vertical victories! """

    result = "No Winner"
 
    for columnIndex in range(BOARDWIDTH):
        # initialise at the start of the current column
        colour = RED
        count = 0
        for rowIndex in range(BOARDHEIGHT):
            thisColour = BOARD[columnIndex][rowIndex]

            if thisColour == colour:
                count = count + 1
            elif thisColour == EMPTY:
                count = 0
            else:
                colour = thisColour
                count = 1

            if count == 4:
                result = "win for {0}, in column {1:1d}".format(colour, columnIndex + 1)
                break

    return result

def checkDiagonals():
	"""This method checks for any diagonal victories! """
	#need to implement checks in both diagonal directions
	
def randomlySelectFirstPlayer():
    """ This method randomly chooses the first player colour and returns """
    
    first = randint(0, 1)
    
    firstToPlay = RED
    
    if first == 0:
        firstToPlay = YELLOW

    return firstToPlay

def playRandomlyANumberOfTurns(totalTurns, firstToPlay):
    """ This method randomly plays a number of turns specified starting with the colour passed in """

    # initialise the turn variable
    currentTurn = firstToPlay

    for turn in range(totalTurns):
        
        playATurnAtRandom(currentTurn)

        # set turn variable to the other colour ready for next turn
        if currentTurn == RED:
            currentTurn = YELLOW
        else:
            currentTurn = RED    

def playATurnAtRandom(colour):  
    """ This method tries to play a move at random for the colour passed in - it does nothing if this is not possible """  
    
    invalidMove = True;

    validMoveExists = checkValidMoveExists()

    while invalidMove and validMoveExists:
        columnIndex = randint(0, BOARDWIDTH - 1)
        heightIndex = findLowestValidHeightPosition(columnIndex)
        if(heightIndex >= 0):
            invalidMove = False
            BOARD[columnIndex][heightIndex] = colour   

def checkValidMoveExists():
    """ This method to check there actually is a valid place to play """
    
    validMoveExists = False
    
    # look for an empty space on the top row meaning there is a valid move
    for x in range(BOARDWIDTH):
        if EMPTY == BOARD[x][BOARDHEIGHT - 1]:
            validMoveExists = True
            break
            
    return validMoveExists


def findLowestValidHeightPosition(columnIndex):
    # this needs to check if the column is a valid move and if so return the lowest index. 
    # If move is invalid as the column is full return -1
    
    for y in range(BOARDHEIGHT):
        if EMPTY == BOARD[columnIndex][y]:
            return y
    
    return -1    

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
    # start with a structural row outside the loop
    drawStructuralRow()

    # when drawing we need to do rowIndex axis backwards i.e bottom to top!
    for rowIndex in range(BOARDHEIGHT-1, -1, -1):
        drawRow(rowIndex)  
        drawStructuralRow()  

    # draw numbers along the bottom
    print('  ', end='')
    for x in range(BOARDWIDTH):
        print('  {0} '.format(x + 1), end='')   
    print('')

def drawStructuralRow():
    print('  +---+' + ('---+' * (BOARDWIDTH - 1)))

def drawRow(rowNum):
    print("{0:1d} ".format(rowNum + 1), end='')

    for columnIndex in range(BOARDWIDTH):
        print('| {0} '.format(BOARD[columnIndex][rowNum]), end='')
    
    print('| ')


# call the main function once everything defined
main()