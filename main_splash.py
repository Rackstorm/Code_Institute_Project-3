from game_functions import start_battleship, display_game_rules


def display_game_menu():
    """
    Displays the game menu and handles user choices.
    """
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
            print("\nExiting Battleship Game. Goodbye!\n")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    display_game_menu()
