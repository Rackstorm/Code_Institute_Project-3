# Battleships Game

![Mockup]

This is a classic Battleships game with 1 player only against the computer. I had fun making this game, however, due to the issues with Codeanywhere I partly had to work on this code offline in VS Code.

## How to Play
1. The game board is set up with a grid of 10x10.
2. 4 ships is placed on the board.
3. The player inputs their guess by writing rows + column (e.g. "A6" or "C3")
4. The player has 50 attempts/bullets to strike down the battleships.
5. If the player runs out of attempts the game will close and show "Game over!".
6. If the player wins the game will show "Good job! You won!"


## Features

1. 
2. 
3. 

## Future features

1. Creating a multiplayer version
2. Making the game more interactive by letting the player put their own ships on the board

# Technologies
For this project I have been working with:
1. IDE - VSCode and Codeanywhere.
2. Python - Creating the game.
3. Checking the game throughout the process in the Terminal.
4. Tried to deploy to Heroku.

# Testing

![Testing]

Throughout this project I have been testing the game by running it in the Terminal. 

## Solved Bugs

**1. Grid reference** - The grid was not displaying letters horizontally and numbers vertically. Solved it by adding the grid_reference() function to display letters horizontally and numbers vertically.

**2. Grid reference shift** - All letters were shifted one space to the right. Turns out I had one line of unneccessary code displaying an extra column with 'O' outside the regular grid.

**3. Indentation errors** - Received repeated indentation errors but mainly in the print_board() and play_battleship() functions. Fixed the indentation by ensuring all code lines in the functions were correctly aligned.

**4. Parsing fail** - Numerous parsing failures. Solved by fixing indentation errors and correct arguments.

**5. Board** - The game board was not displaying all of the O's and some letters were missing. Solved this by clearing out some unneccessary code and simplify it.

**6. Clearing screen** - Added a clear_screen() and it was not clearing the screen after each round. Solved it by putting the clear_screen() at appropriate places in the play_battleship() function to clear the screen after each input guess and when the game is over.

**7. Hidden ships** - The board was not updating correctly when the game was over showing all hidden ships not being sunk. Solved this by modifying the play_battleship() function to print the board after the game was over, either due to winning or losing.

**8. Maximum attempts** - The board was clearing after the maximum attempts instead of printing "Game Over." Solved this by modifying the play_battleship() function to print "Game Over" when the maximum attempts were reached, and then we displayed the board with hidden ships.

## Unresolved Bugs

1. No unresolved bugs.


## Validator Testing

![Validator]

# Deployment

# Credits 
1. Some code have been used and modified from [Saran Sundars Battleship for Beginners](https://github.com/SaranSundar/PythonCurriculum/blob/main/Battleships/battleships_complete.py).
2. Simplistic code and functionality has been inspired from [Saran Sundars Battleship for beginners](https://www.youtube.com/watch?v=MgJBgnsDcF0).
3. Borrowing code and modified it from [Code Academy](https://www.youtube.com/watch?v=7Ki_2gr0rsE)
4. Using ideas, nesting functions and other types from this s[Dr Codie](https://www.youtube.com/watch?v=Ej7I8BPw7Gk&list=PLpeS0xTwoWAsn3SwQbSsOZ26pqZ-0CG6i) YouTube series.
5. As usual, a massive amount of searching for answers on [Stack Overflow](https://stackoverflow.com) when troubleshooting.

# Acknowledgement
1. Big thanks to my mentor Luke, being awesome as usual.
2. To my Python enthusiastic friend Nicklas who has tried my game and served me a plate full of errors to solve.