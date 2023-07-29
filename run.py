import platform
import subprocess
import random

# TO DO
# - cleaning up cell refernces
# - welcome/game rules
# - show hidden ships (Game over)
# - number of ships
# - maximum attempts
# - different files
# - Deployment


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
    displays hits, misses and revealed hidden ships
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
    letters = 'ABCDEFGHIJ'
    return "   " + " ".join(letters[:cols])


def place_ship(board, ship_size):
    """
    randomly places a ship on the board.
    size can differ from 1 to 4.
    ships can be placed horizontally or vertically.
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
    """
    board = create_board(rows, cols)
    ships_placed = 0

    while ships_placed < num_ships:
        place_ship(board, random.randint(1, 4))
        ships_placed += 1

    print("Welcome to Battleship! \n")
    print("You have 5 attempts to try and sink the battleships! \n")
    print_board(board)

    attempts, max_attempts = 0, 80

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
                print("Good job! \n")
                print("You sank all the battleships! \n")
                print("You made it in {attempts} attempts. \n")
                print_board(board, game_over=True)
                break
        else:
            print("Miss!")
            board[row][col] = '/'
            print_board(board)
    else:
        print("Game Over! Try again. \n")


def start_battleship():
    rows, cols = 10, 10
    num_ships = 80
    play_battleship(rows, cols, num_ships)
    clear_screen()


def display_game_rules():
    print("=== Battleship Game Rules === \n")
    print("In this very simple game you only have to strike down the ships.\n")
    print("1. You have x attempts to sink the ships.")
    print("2. You enter your guess by typing col + row (e.g. A3)")
    print("3. If you miss, the board will mark it with a '/'")
    print("4. If you hit, the board will mark the cell with an 'X'")
    print("5. If you run out of attempts, it's game over.")
    print("6. If you win, the game score will show.\n")


def main():

    while True:
        print("=== Battleship Game === \n")
        print("1. Play Game")
        print("2. Game Rules")
        print("3. Exit \n")

        choice = input("Enter your choice: ")
        clear_screen()

        if choice == '1':
            start_battleship()
        elif choice == '2':
            display_game_rules()
        elif choice == '3':
            print("Exiting Battleship Game. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
