from __future__ import print_function
from random import randint
# import random
# import copy
# import sys

BOARDWIDTH = 7
# The number of squares wide the gameboard is
BOARDHEIGHT = 6
# The number of squares high the gameboard is
RED = 'R'
# designation for the red game token 
YELLOW = 'Y'
# designation for the yellow game token
EMPTY = ' '
# designation for empty game space
GAME_RESULT = [];
# holds the result of the game

BOARD = [[EMPTY for y in range(BOARDHEIGHT)] for x in range(BOARDWIDTH)] 
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


def main():
    #fillATestBoard()

    firstToPlay = randomlySelectFirstPlayer()

    playRandomlyANumberOfTurns(35, firstToPlay)

    drawBoard()
    evaluateBoardForWinner()
    drawBoard()
    

def evaluateBoardForWinner():
    """ This method examines the board for a winner either vertically, diagonally or horizontally """

    checkHorizontals()
    checkVerticals()
    checkDiagonals()
    
    print("\nAnd the winner is: \n")
    
    if len(GAME_RESULT) > 0:
        for res in GAME_RESULT : 
            print(res)
    else :
        print("No Winner")


def checkHorizontals():
    """This method checks for any horizontal victories! """

    for y in range(BOARDHEIGHT):
        # initialise at the start of the current row
        colour = RED
        count = 0
        for x in range(BOARDWIDTH):
            thisColour = BOARD[x][y]
 
            if thisColour == colour:
                count = count + 1
            elif thisColour == EMPTY:
                count = 0
            else:
                colour = thisColour
                count = 1

            if count == 4:
                GAME_RESULT.append("Horizontal win for {0}, in row {1:d}".format(colour, y + 1))
                break
   
    

def checkVerticals():
    """This method checks for any vertical victories! """
 
    for x in range(BOARDWIDTH):
        # initialise at the start of the current column
        colour = RED
        count = 0
        for y in range(BOARDHEIGHT):
            thisColour = BOARD[x][y]

            if thisColour == colour:
                count = count + 1
            elif thisColour == EMPTY:
                count = 0
            else:
                colour = thisColour
                count = 1

            if count == 4:
                GAME_RESULT.append("Vertical win for {0}, in row {1:d}".format(colour, y + 1))
                break


def checkDiagonals():
    """This method checks for any diagonal victories! 
        The following example 7 * 6 board shows the positions we need to start checking for diagonal win at:

          +---+---+---+---+---+---+---+
        5 |   |   |   |   |   |   |   | 
          +---+---+---+---+---+---+---+
        4 |   |   |   |   |   |   |   | 
          +---+---+---+---+---+---+---+
        3 |   |   |   |   |   |   |   | 
          +---+---+---+---+---+---+---+
        2 | f |   |   |   |   |   | b | 
          +---+---+---+---+---+---+---+
        1 | f |   |   |   |   |   | b | 
          +---+---+---+---+---+---+---+
        0 | f | f | f | x | b | b | b | 
          +---+---+---+---+---+---+---+
            0   1   2   3   4   5   6 
        
        where f is checking forwards (increment of 1 and b is backwards (increment of -1) x is both)
    """

    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT - 3):
            if((x == 0 or y == 0) and x < BOARDWIDTH - 3):
                res = checkDiagonal(x, y, 1)

            if((x == (BOARDWIDTH - 1) or y == 0) and x >= BOARDWIDTH - 4):
                checkDiagonal(x, y, -1)

def checkDiagonal(startX, startY, increment):
    """This method looks from the provided start co-ordinate for a diagonal victory
       The increment should be set to 1 for the check to look forward or -1 for backwards"""
    print('>>>>> check diagonal [{0:1d}, {1:1d}] using increment {2:1d}'.format(startX, startY, increment))
    
    x = startX
    y = startY
    colour = RED
    count = 0
    
    while ((x < BOARDWIDTH and x >= 0) and (y < BOARDHEIGHT and y >= 0)):
        thisColour = BOARD[x][y]
        print('>>>>>>>>>>>>>>>>>>>>> check [{0:1d}, {1:1d}] =  {2}'.format(x, y, thisColour))
        if thisColour == colour:
            count = count + 1
        elif thisColour == EMPTY:
            count = 0
        else:
            colour = thisColour
            count = 1

        print('>>>>>>>>>>>>>>>>>>>>> count = {0:1d}, Colour  =  {1}'.format(count, colour))

        if count == 4:
            GAME_RESULT.append("Diagonal win for {0}, between [{3:d}, {4:d}] and [{1:d}, {2:d}]".format(colour, x+1, y+1, x - (increment * 3) + 1, y-2))
            break

        x = x + increment
        y = y + 1
    
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
        x = randint(0, BOARDWIDTH - 1)
        heightIndex = findLowestValidHeightPosition(x)
        if(heightIndex >= 0):
            invalidMove = False
            BOARD[x][heightIndex] = colour   

def checkValidMoveExists():
    """ This method to check there actually is a valid place to play """
    
    validMoveExists = False
    
    # look for an empty space on the top row meaning there is a valid move
    for x in range(BOARDWIDTH):
        if EMPTY == BOARD[x][BOARDHEIGHT - 1]:
            validMoveExists = True
            break
            
    return validMoveExists


def findLowestValidHeightPosition(x):
    # this needs to check if the column is a valid move and if so return the lowest index. 
    # If move is invalid as the column is full return -1
    
    for y in range(BOARDHEIGHT):
        if EMPTY == BOARD[x][y]:
            return y
    
    return -1    

# functions to draw the connect 4 board
def drawBoard():
    # start with a structural row outside the loop
    drawStructuralRow()

    # when drawing we need to do y axis backwards i.e bottom to top!
    for y in range(BOARDHEIGHT-1, -1, -1):
        drawRow(y)  
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

    for x in range(BOARDWIDTH):
        print('| {0} '.format(BOARD[x][rowNum]), end='')
    
    print('| ')


# call the main function once everything defined
main()