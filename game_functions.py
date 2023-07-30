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
    """
    displaying letters and numbers horizontally/vertically on game grid
    """
    letters = 'ABCDEFGHIJ'
    return "   " + " ".join(letters[:cols])


def place_ship(board, ship_size):
    """
    randomly places a ship on the board
    size can differ from 1 to 4
    ships can be placed horizontally or vertically
    ensuring the ships cannot be placed on top of eachother
    checking ship placement possible in for loop
    """
    rows, cols = len(board), len(board[0])
    placed_positions = []
    ships_placed = 0

    while ships_placed < 7:
        orientation = random.choice(['horizontal', 'vertical'])
        row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)

        valid_placement = False
        pos_check = []

        for i in range(ship_size):
            if orientation == 'horizontal' and col + ship_size <= cols:
                if board[row][col + i] != 'S':
                    valid_placement = True
                    pos_check.append((row, col + i))
                else:
                    valid_placement = False
                    break
            elif orientation == 'vertical' and row + ship_size <= rows:
                if board[row + i][col] != 'S':
                    valid_placement = True
                    pos_check.append((row + i, col))
                else:
                    valid_placement = False
                    break
            else:
                valid_placement = False
                break

        position_not_placed = all(
            pos not in placed_positions for pos in pos_check
        )
        if valid_placement and position_not_placed:
            if orientation == 'horizontal':
                for i in range(ship_size):
                    board[row][col + i] = 'S'
            else:
                for i in range(ship_size):
                    board[row + i][col] = 'S'
            placed_positions.extend(pos_check)
            ships_placed += 1
        else:
            ships_placed += 1


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
    marking cells with O, X, or /
    clearing screen after each try
    printing hidden ships if game over
    """
    board = create_board(rows, cols)
    ships_placed = 0

    place_ship(board, 1)
    place_ship(board, 2)
    place_ship(board, 3)
    place_ship(board, 4)

    while ships_placed < num_ships:
        place_ship(board, random.randint(1, 4))
        ships_placed += 1

    print("Welcome to Battleship! \n")
    print("You have 20 attempts to try and sink the battleships! \n")
    print_board(board)

    attempts, max_attempts = 0, 20

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
                print("\n Want another go? \n")
                break
        else:
            print("Miss!")
            board[row][col] = '/'
            print_board(board)
    else:
        print("")
        print("Game Over! \n")
        print("Here are the hidden ships: \n")
        print_board(board, game_over=True)
        print("\n Want another go? \n")


def display_game_rules():
    """
    Displaying the rules of the game.
    """
    print("=== Battleship Game Rules === \n")
    print("In this very simple game you only have to strike down the ships.\n")
    print("1. You have 20 attempts/bullets to sink the ships.")
    print("2. You enter your guess by typing col + row (e.g. A3)")
    print("3. If you miss, the board will mark the cell with a '/'")
    print("4. If you hit, the board will mark the cell with an 'X'")
    print("5. If you run out of attempts/bullets, it's game over.")
    print("6. Good luck!\n")


def start_battleship():
    """
    Choosing size and number of ships.
    Calling the main game function.
    """
    rows, cols = 5, 5
    num_ships = 7
    play_battleship(rows, cols, num_ships)
