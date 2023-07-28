import random


def create_board(rows, cols):
    """
    creates a game board 10x10 rows/columns.
    all empty cells are marked with an 'O'
    """
    board = []
    for _ in range(rows):
        row = ['O'] * cols
        board.append(row)
    return board


def print_board(board):
    """
    prints the game board as well 
    displays hits, misses and revealed hidden ships 
    """

    for row in board:
        display_row = []
        for cell in row:
            if cell == 'S' and not game_over:
                display_row.append('O') 
            else:
                display_row.append(cell)  
        print(" ".join(display_row))


def place_ship(board, ship_size):
    """
    randomly places a ship on the board.
    size can differ from 1 to 4.
    ships can be placed horizontally or vertically.
    """
    rows, cols = len(board), len(board[0])
    orientation = random.choice(['horizontal', 'vertical'])

    row, col = random.randint(
        0, rows - ship_size), random.randint(0, cols - ship_size)

    for i in range(ship_size):
        if orientation == 'horizontal':
            board[row][col + i] = 'S'
        else:
            board[row + i][col] = 'S'


def get_guess(rows, cols):
    """
    asks the player to input their guess (e.g., A5).
    converts the input into row and column indices on the board.
    """
    while True:
        try:
            guess = input("Enter your guess (e.g., A5): ").strip().upper()
            col, row = ord(guess[0]) - ord('A'), int(guess[1:]) - 1
            if 0 <= row < rows and 0 <= col < cols:
                return row, col
            else:
                print("Invalid guess. Try again.")
        except (ValueError, IndexError, TypeError):
            print("Invalid guess. Try again.")


def play_battleship(rows, cols, num_ships):
    board = create_board(rows, cols)
    ships_placed = 0

    while ships_placed < num_ships:
        place_ship(board, random.randint(1, 4))
        ships_placed += 1

    print("Welcome to Battleship!")
    print("You have 5 attempts to try and sink the battleships!")
    print_board(board)

    attempts, max_attempts = 0, 5 

    while attempts < max_attempts:
""" 
if player wins, print first statement 
if player looses, show hidden ships and print second statement 
"""
        if num_ships == 0:
            print("Good job! You sank all the battleships!")
            print_board(board, game_over=True)
            break  
        else:
            print("Game Over! Try again.")


def main():
    rows, cols = 10, 10
    num_ships = 3
    play_battleship(rows, cols, num_ships)


if __name__ == "__main__":
    main()
