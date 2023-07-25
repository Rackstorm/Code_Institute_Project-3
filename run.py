import random


def create_board(rows, cols):
    return [['O' for _ in range(cols)] for _ in range(rows)]


def print_board(board):
    for row in board:
        print(" ".join(row))


def place_ship(board, ship_size):
    rows = len(board)
    cols = len(board[0])
    orientation = random.choice(['horizontal', 'vertical'])

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
    while True:
        try:
            guess = input("Enter your guess (e.g., A5): \n").strip().upper()
            col, row = ord(guess[0]) - ord('A'), int(guess[1:]) - 1
            if 0 <= row < rows and 0 <= col < cols:
                return row, col
            else:
                print("Invalid guess. Try again.\n")


def play_battleship(rows, cols, num_ships):
    board = create_board(rows, cols)
    ships_placed = 0

    while ships_placed < num_ships:
        place_ship(board, random.randint(1, 4))
        ships_placed += 1

    print("Welcome to Battleship!\n")
    print("You have 5 attempts to try and sink the battleships!\n")
    print_board(board)

    attempts = 0
    max_attempts = 5

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
            print(
                f"Good job! You sank all the battleships!\n")
            break
    else:
        print(f"Game Over! Try again.")


if _name_ == "_main_":
    rows = 10
    cols = 10
    num_ships = min(
        int(input("Enter the number of ships: \n")), rows * cols // 5)
    play_battleship(rows, cols, num_ships)
