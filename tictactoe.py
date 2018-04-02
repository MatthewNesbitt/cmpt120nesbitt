# CMPT 120 Intro to Programming
# Lab #6 – Lists and Error Handling
# Author: Matt Nesbitt
# Created: 2018-30-03

symbol = [ " ", "x", "o" ]

# JA: This works, but you had to use a list of lists
board = [' ',' ',' ',
         ' ',' ',' ',
         ' ',' ',' ']

def printBoard(board):
    print('+-----------+')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('+-----------+')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('+-----------+')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('+-----------+')

def hasBlanks(board):
    for cell in board:
        if cell == ' ':
            return True
    return False

def markBoard(board):
    player = 1
    while hasBlanks(board):
        choice = input('Player %d, choose a box (0-8): ' % player)
        choice = int(choice)
        if choice < 0 or choice > 8:
            print ("Please make sure your entry is between 0 and 8")
        elif board[choice] != ' ':
            print ("This spot has already been filled. Please choose a different spot.")
        else:
            board[choice] = symbol[player]
            printBoard(board)
            if player == 1:
                player = 2
            else:
                player = 1

def main():
    printBoard(board)
    markBoard(board)

main()
