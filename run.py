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
    prints the game board
    """
    for row in board:
        print(" ".join(row))

def place_ship(board, ship_size):
    """
    randomly places a ship on the board.
    size can differ from 1 to 4.
    ships can be placed horizontally or vertically.
    """
    rows, cols = len(board), len(board[0])
    orientation = random.choice(['horizontal', 'vertical'])

    row, col = random.randint(0, rows - ship_size), random.randint(0, cols - ship_size)

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
            guess = input("Enter your guess (e.g., A5): " n\).strip().upper()
            col, row = ord(guess[0]) - ord('A'), int(guess[1:]) - 1
            if 0 <= row < rows and 0 <= col < cols:
                return row, col
            else:
                print("Invalid guess. Try again." n\)
        except (ValueError, IndexError, TypeError):
            print("Invalid guess. Try again." n\)

def play_battleship(rows, cols, num_ships):
    """
    main function to play the game.
    """
    board = create_board(rows, cols)
    ships_placed = 0

    while ships_placed < num_ships:
        place_ship(board, random.randint(1, 4))
        ships_placed += 1

    print("Welcome to Battleship!" n\)
    print("You have 5 attempts to try and sink the battleships!"n\)
    print_board(board)

    attempts, max_attempts = 0, 5

    while attempts < max_attempts:
        attempts += 1
        row, col = get_guess(rows, cols)

        if board[row][col] == 'S':
            print("Hit!")
            board[row][col] = 'X'
            print_board(board)
            num_ships -= 1

        else:
            print("Miss!")
            print_board(board)

        if num_ships == 0:
            print("Good job! You sank all the battleships!")
            break
    else:
        print("Game Over! Try again.")

def main():
    rows, cols = 10, 10
    num_ships = 4
    play_battleship(rows, cols, num_ships)

if __name__ == "__main__":
    """is called when program is run from terminal or PyCharms"""
    main()