from game_functions import start_battleship


def display_game_menu():
    while True:
        print("=== Battleship Game === \n")
        print("1. Play Game")
        print("2. Game Rules")
        print("3. Exit \n")

        choice = input("Enter your choice: ")

        if choice == '1':
            start_battleship()
        elif choice == '2':
            display_game_rules()
        elif choice == '3':
            print("Exiting Battleship Game. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def display_game_rules():
    print("=== Battleship Game Rules === \n")
    print("In this very simple game you only have to strike down the ships.\n")
    print("1. You have x attempts to sink the ships.")
    print("2. You enter your guess by typing col + row (e.g. A3)")
    print("3. If you miss, the board will mark it with a '/'")
    print("4. If you hit, the board will mark the cell with an 'X'")
    print("5. If you run out of attempts, it's game over.")
    print("6. If you win, the game score will show.\n")
