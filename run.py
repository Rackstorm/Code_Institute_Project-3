""" Battleship Game """
""" The player has 5 attempts to sink the ships on the board. """
""" The player inserts commands such as "A6" or "B4" to make guessess """

import random

def creating_board(rows, cols)
""" creating the board consisting of a grid 10x10 """
return [['O' for _ in range(cols)] for _ in range(rows)]

def print_board(board)
""" printing out the grid """
    for row in board:
        print(" ".join(row))

def placing_ships(board, ship_size)
""" the users chooses how many ships to put on the board """
    rows = len(board)
    cols = len(board[0])
    orientation = random.choice(['horizontal', 'vertical'])

""" randomly put out the ships on the board and add an S to the board """
    if orientation == 'horizontal':
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - ship_size)
        for i in range(ship_size):
            board[row][col + i] = 'S'
    else:
        row = random.randint(0, rows - ship_size)
        col = random.randint(0, cols - 1)
        for i in range(ship_size):
            board[row + i][col] = 'S'

def get_guess(rows, cols):
    """ the user types in their guesses """

def play_game(rows, cols, num_ships):
    """ puts the ships randomly on the board, keeps track of hits/misses"""

if __name__ == "__main__":
    rows = 10 
    cols = 10  
    num_ships = min(int(input("Enter the number of ships: ")), rows * cols // 5)
    play_game(rows, cols, num_ships)