# KELİME OYUNU
# Game Readme

This is a Python game where users answer questions and accumulate scores based on their answers. 

## How to Play

1. The program will ask for the user's name.
2. Press Enter to start the game.
3. The first question will be displayed with underscores representing the missing letters.
4. The user will be presented with two options: "C" to provide an answer or "H" to request a letter.
5. If the user chooses to provide an answer, they can enter their response. If the answer is correct, the score will increase; otherwise, the score will decrease. The score and remaining time will be displayed after each question.
6. If the user chooses to request a letter, the first missing letter will be revealed. Subsequent requests will reveal the next missing letters.
7. This pattern continues until the last question is reached or the time limit is exceeded.
8. At the end of the game, the final score and remaining time (if applicable) will be displayed. The top scores will be saved in a leaderboard file.
9. The user will have the option to play again, exit the game, or view the leaderboard.

## Code Explanation

The code consists of several functions:

- `read_questions(filename)`: Reads the questions and answers from a file and returns a dictionary of question-answer pairs.
- `random_letter(dict)`: Generates a list of lists representing the progressive reveal of missing letters for each answer.
- `main(dict, list, remaining_time)`: Executes the main game logic, including displaying questions, handling user input, updating the score, and tracking the remaining time.
- `user_and_skor(username, skor, time)`: Creates a dictionary to store the user's information (username, score, remaining time).
- `database(filename, dict)`: Writes the user's information to a CSV file.
- `top_10(filename)`: Reads the user data from a CSV file, sorts it based on score and remaining time, and writes the top 10 scores to a new CSV file.
- `play_again(filename)`: Offers options to play again, exit the game, or view the leaderboard.

The main program prompts the user for their name, reads the questions from a file, initializes the time limit, and starts the game. It calls the necessary functions to play the game, store user information, update the leaderboard, and offer options to the user.

## File Structure

The game requires a text file containing the questions and answers. The file format should follow the guidelines specified in the code.

Additionally, the program uses two CSV files:
- `database.csv`: Stores user information (username, score, remaining time).
- `top_users.csv`: Contains the leaderboard with the top 10 scores.

## Dependencies

The code does not have any external dependencies beyond the standard Python libraries.

Please ensure that you have Python installed on your machine to run the game.

## How to Run

1. Save the code in a Python file (e.g., `game.py`).
2. Place the question and answer file (e.g., `soru.txt`) in the same directory as the Python file.
3. Open a terminal or command prompt and navigate to the directory containing the Python file.
4. Run the command `python game.py`.
5. Follow the prompts in the terminal to play the game.

Enjoy the game and have fun!
