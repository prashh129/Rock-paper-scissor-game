# Rock Paper Scissors Game

A simple **Rock Paper Scissors** game implemented in Python. This game allows the player to play against the computer with options to choose between Rock, Paper, or Scissors using either numbers (1-3) or words.

## Features
✅ Accepts both **text input** (rock, paper, scissor) and **numeric input** (1, 2, 3).  
✅ Displays clear, human-readable outputs.  
✅ Keeps running in a loop until the user decides to quit.  
✅ Uses **random module** to let the computer make a choice.  
✅ Provides an easy-to-read result with **win, lose, or draw** conditions.  

## How to Play
1. Run the script in a Python environment.
2. Choose **Rock, Paper, or Scissor** by entering:
   - The **name** (e.g., `rock`, `paper`, `scissor`)
   - The **number** (`1` for Rock, `2` for Paper, `3` for Scissor)
3. The computer will randomly choose an option.
4. The winner is determined based on the following rules:
   - **Rock beats Scissor** (1 > 3)
   - **Paper beats Rock** (2 > 1)
   - **Scissor beats Paper** (3 > 2)
   - If both player and computer choose the same, it's a **draw**.
5. The game will ask if you want to play again (`y/n`).
6. If you enter `y`, the game restarts; if you enter `n`, the game ends.

## Example Gameplay
```
Rock Paper and Scissor Game
1. Rock
2. Paper
3. Scissor

Enter your choice: rock

Player: Rock
Computer: Paper
Player lose!

Do you want to play again (y/n)? y
```

## Requirements
- Python 3.x

## Running the Game
To run the game, simply execute the Python script:
```bash
python rock_paper_scissors.py
```

## Code Overview
The game logic is implemented as follows:
- **Dictionaries** store choices and allow easy lookup of input values.
- **Random selection** is used to determine the computer’s choice.
- **A loop** ensures continuous gameplay until the user chooses to exit.
- **Function `get_winner()`** evaluates the winner based on the predefined rules.

## Contributions
Feel free to fork the repository, make improvements, and submit a pull request!

## License
This project is open-source and available for personal or educational use.

---
Enjoy playing Rock Paper Scissors! ✌️🤖

