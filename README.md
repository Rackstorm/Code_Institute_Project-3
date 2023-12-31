# Battleships Game

![Mockup](docs/readme_images/mockup.png)

This is a classic Battleships game with 1 player only against the computer. I had fun making this game, however, due to the issues with Codeanywhere I partly had to work on this code offline in VS Code.

* The project repository can be found here https://github.com/Rackstorm/Code_Institute_Project-3
* The project is deployed, live and playable at https://code-project-3-e97f40034e15.herokuapp.com/

## How to Play
1. The game board is set up with a grid of 5x5.
2. 7 enemy ships is placed randomly on the board.
3. The player inputs their guess by writing rows + column (e.g. "A6" or "C3")
4. The player has 20 attempts/bullets to strike down the battleships.
5. If the player runs out of attempts the game will close and show "Game over! Try again!" and show hidden ships.
6. If the player wins the game will show "Good job! You won!" and ask user to play again.

## Design of the Game
![LucidChart](docs/readme_images/lucid.png)

## Features

### The Game
1. Heading at the top displaying the game name.
2. User gets to choose to either play game, read game rules or exit the app.
![Game](docs/readme_images/game.png)


### Game Rules
1. Displaying a list of rules on how to play the game.
2. The user can then choose another option in the menu.
![GameRules](docs/readme_images/game_rules.png)



### Exit
If the user chooses "Exit" the entire game shuts down.
![Exit](docs/readme_images/exit.png)


### Play Game - Enter guess
User input their guess in the Terminal by printing 'B6' for example.
![EnterGuess](docs/readme_images/enter_guess.png)


### Play Game - Hit
If user strikes a battleship, an X will be visible on the board.
![Hit](docs/readme_images/hit.png)


### Play Game - Miss
If user strikes a battleship, an X will be visible on the board.
![Miss](docs/readme_images/miss.png)


### Play Game - Invalid Guess
If user types in number before letter, typing other symbols, letters or numbers, or trying to go off grid an 'Invalid Guess' statement will appear, asking the user to provide a new input.
![InvalidGuess](docs/readme_images/invalid_guess.png)


### Play Game - Keep Track
Throughout the game, the score will remain until user wins or it's game over.
![KeepTrack](docs/readme_images/keep_track.png)


### Play Game - Game Over
If the user looses, a print statement with "Game Over" will appear along with the board showing the remaining hidden ships. The user will then be asked to try again or choose another option from the menu.
![GameOver](docs/readme_images/game_over.png)


### Play Game - Winner!
If the user wins, a print statement with "Good job, you won!" will appear along with the board showing the score. The user will then be asked to play again or choose another option from the menu.
![Winner](docs/readme_images/winner.png)

## Future features

1. Creating a multiplayer version
2. Making the game more interactive by letting the player put their own ships on the board

# Technologies

* The game is completely written in Python.
* The IDE used has been Codeanywhere with Code Institutes template.
* The IDE used when Codeanywhere has been buggy is VSCode.
* Heroku has been used to deploy the project.
* Git has been used to regularly adding, committing and pushing code to GitHub.
* All code and assets have been stored at GitHub.
* The project has also been deployed to Git Pages.

# Testing

Throughout this project I have been testing the game by running it in the Terminal. 
![Testing](docs/readme_images/testing.png)

## Solved Bugs

**1. Grid reference** - The grid was not displaying letters horizontally and numbers vertically. Solved it by adding the grid_reference() function to display letters horizontally and numbers vertically.

**2. Grid reference shift** - All letters were shifted one space to the right. Turns out I had one line of unneccessary code displaying an extra column with 'O' outside the regular grid.

**3. Indentation errors** - Received repeated indentation errors but mainly in the print_board() and play_battleship() functions. Fixed the indentation by ensuring all code lines in the functions were correctly aligned.

**4. Parsing fail** - Numerous parsing failures. Solved by fixing indentation errors and correct arguments.

**5. Board** - The game board was not displaying all of the O's and some letters were missing. Solved this by clearing out some unneccessary code and simplify it.

**6. Clearing screen** - Added a clear_screen() and it was not clearing the screen after each round. Solved it by putting the clear_screen() at appropriate places in the play_battleship() function to clear the screen after each input guess and when the game is over.

**7. Hidden ships** - The board was not updating correctly when the game was over showing all hidden ships not being sunk. Solved this by modifying the play_battleship() function to print the board after the game was over, either due to winning or losing.

**8. Maximum attempts** - The board was clearing after the maximum attempts instead of printing "Game Over." Solved this by modifying the play_battleship() function to print "Game Over" when the maximum attempts were reached, and then we displayed the board with hidden ships.

**9. Ships not displaying on the board** - The loop for placing ships was not correct, leading to not all ships being placed on the board. Adjusted the loop by modifying the place_ship function to properly check for valid ship placements and ensuring that each ship is placed without overlapping any other ship.

## Unresolved Bugs

1. No unresolved bugs.


## Validator Testing
Code has been run through the Code Institutes Linter with no errors.
![RunPy](docs/readme_images/run_linter.png)
![MainSplash](docs/readme_images/main_splash_linter.png)
![GameFunctions](docs/readme_images/game_functions_linter.png)

# Deployment

## Adding, committing and pushing code

- All code has been pushed to the repository https://github.com/Rackstorm/Code_Institute_Project-3
- All code has been regurlary added, committed and pushed throughout the project.
- The commands being used are `git add <file>`,
  `git commit -m “commit message”` and
  `git push`
- Due to being completely brand new into this tech world, the `git commit -m “commit message”` have gradually improved throughout this project since it was difficult for me to understand the importance of good logging in the beginning.

## Deploying to Heroku
I deployed my project directly to Heroku by doing the following:

1. Created an account at Heroku.com.
2. Since I haven't received a Student Activation Code for GitHub I added billing information myself on Heroku.
3. Clicked on "Create new app" and named it Code-Institute-3.
4. Clicked on Settings and added Backpacks - Python and Node.js.
5. Made sure the backpacks were in the right order.
6. Connected my GitHub profile and found the right Repository.
7. Manually deployed the page and clicked "Eanble automatic deploys" at the same time.

# Credits 
1. Inspired by [Saran Sundars Battleship for Beginners](https://github.com/SaranSundar/PythonCurriculum/blob/main/Battleships/battleships_complete.py).
2. Simplistic code and functionality has been inspired from [Saran Sundars Battleship for beginners](https://www.youtube.com/watch?v=MgJBgnsDcF0).
3. Borrowing code and modified it from [Code Academy](https://www.youtube.com/watch?v=7Ki_2gr0rsE)
4. Using ideas, nesting functions and other types from this s[Dr Codie](https://www.youtube.com/watch?v=Ej7I8BPw7Gk&list=PLpeS0xTwoWAsn3SwQbSsOZ26pqZ-0CG6i) YouTube series.
5. As usual, a massive amount of searching for answers on [Stack Overflow](https://stackoverflow.com) when troubleshooting.

# Acknowledgement
1. Big thanks to my mentor Luke, being awesome as usual.
2. To my Python enthusiastic friend Nicklas who has tried my game and served me a plate full of errors to solve.