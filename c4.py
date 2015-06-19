from __future__ import print_function
# import random
# import copy
# import sys

BOARDWIDTH = 7
BOARDHEIGHT = 6

# co-ordinates are always given in the for x, y i.e. across then up

BOARD = [[0 for y in range(BOARDHEIGHT)] for x in range(BOARDWIDTH)] 

def main():
    print('main')
    fillATestBoard()
    #BOARD[3][2] = 'X'
    drawBoard()

def fillATestBoard():
    print('fill')
    for x in range(BOARDWIDTH):
        #print('x = {0:1d}'.format(x))
        for y in range(BOARDHEIGHT):    
            #print('y = {0:1d}'.format(y))
            if ((x + y) % 2) == 1:
                print("BOARD[{0:1d}][{1:1d}] is X".format(x, y))
                BOARD[x][y] = 'X'
            else:
                print("BOARD[{0:1d}][{1:1d}] is O".format(x, y))
                BOARD[x][y] = 'O' 

def drawStructuralRow():
    print('+---+' + ('---+' * (BOARDWIDTH - 1)))

def drawRow(rowNum):
    #print('drawRow(' + str(rowNum) + ')')
    for x in range(BOARDWIDTH):
        print('| {0} '.format(BOARD[x][rowNum]), end='')
    print('|')

def drawBoard():
    print('drawBoard')
    
    for x in range(BOARDWIDTH):
        print('  {0} '.format(x + 1), end='')
    print('')
    drawStructuralRow()

    for y in range(BOARDHEIGHT):
        #print('|   |' + ('   |' * (BOARDWIDTH - 1)))

        drawRow(y)    
        #print()

        #print('|   |' + ('   |' * (BOARDWIDTH - 1)))
        drawStructuralRow()

        

main()