import platform
import subprocess
import random


def create_board(rows, cols):
    """
    creates a game board rows x cols.
    all empty cells are marked with an 'O'
    """
    board = []
    for _ in range(rows):
        row = ['O'] * cols
        board.append(row)
    return board


def clear_screen():
    """
    clearing screen for both windows/os users when called in other functions
    """
    if platform.system() == "Windows":
        if platform.release() in {"10", "11"}:
            subprocess.run("", shell=True)
            print("\033c", end="")
        else:
            subprocess.run(["cls"])
    else:
        print("\033c", end="")


def print_board(board, game_over=False):
    """
    prints the game board grid
    displays hits, misses, and revealed hidden ships
    """
    print(grid_reference(len(board[0])))

    for i, row in enumerate(board):
        display_row = [str(i + 1).rjust(2)]
        for cell in row:
            if cell == 'S' and not game_over:
                display_row.append('O')
            else:
                display_row.append(cell)
        print(" ".join(display_row))


def grid_reference(cols):
    """ displaying letters and numbers horizontally/vertically on game grid """
    letters = 'ABCDEFGHIJ'
    return "   " + " ".join(letters[:cols])


def place_ship(board, ship_size):
    """
    randomly places a ship on the board
    size can differ from 1 to 4
    ships can be placed horizontally or vertically
    """
    rows, cols = len(board), len(board[0])
    orientation = random.choice(['horizontal', 'vertical'])
    row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)

    for i in range(ship_size):
        if orientation == 'horizontal' and col + ship_size <= cols:
            board[row][col + i] = 'S'
        elif orientation == 'vertical' and row + ship_size <= rows:
            board[row + i][col] = 'S'
            break


def get_guess(rows, cols):
    """
    asks the player to input their guess (e.g., A5).
    converts the input into row and column indices on the board.
    """
    while True:
        try:
            guess = input("Enter your guess (e.g., A5):  \n").strip().upper()
            col, row = ord(guess[0]) - ord('A'), int(guess[1:]) - 1
            if 0 <= row < rows and 0 <= col < cols:
                return row, col
            else:
                print("Invalid guess. Try again. \n")
        except (ValueError, IndexError, TypeError):
            print("Invalid guess. Try again. \n")


def play_battleship(rows, cols, num_ships):
    """
    main function to play the game
    placing ships on board
    stating max attempts
    marking cells with O, X or /
    clearing screen after each try
    printing hidden ships if game over
    """
    board = create_board(rows, cols)
    ships_placed = 0

    while ships_placed < num_ships:
        place_ship(board, random.randint(1, 4))
        ships_placed += 1

    print("Welcome to Battleship! \n")
    print("You have 5 attempts to try and sink the battleships! \n")
    print_board(board)

    attempts, max_attempts = 0, 5

    while attempts < max_attempts:
        attempts += 1
        row, col = get_guess(rows, cols)
        clear_screen()

        if board[row][col] == 'S':
            print("Hit!")
            board[row][col] = 'X'
            num_ships -= 1
            print_board(board)

            if num_ships == 0:
                print("Good job! You sank all the battleships! \n")
                print_board(board, game_over=True)
                break
        else:
            print("Miss!")
            board[row][col] = '/'
            print_board(board)
    else:
        print("Game Over! Try again. \n")


def start_battleship():
    """
    choosing size and number of ships
    calling the main game function
    """
    rows, cols = 5, 5
    num_ships = 7
    play_battleship(rows, cols, num_ships)
    clear_screen()
