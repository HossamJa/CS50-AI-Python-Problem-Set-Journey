# Tic-Tac-Toe

## Overview
The **Tic-Tac-Toe** problem is part of Project 0 in **CS50’s Introduction to Artificial Intelligence with Python**. It implements an AI that plays Tic-Tac-Toe optimally using the Minimax algorithm, ensuring the AI never loses. The game is playable via a graphical interface using Pygame, allowing users to compete against the AI.

## What I Learned and Practiced
- **Minimax Algorithm**: Implemented the Minimax algorithm to enable the AI to choose optimal moves by evaluating all possible game outcomes.
- **Game Theory**: Learned to model Tic-Tac-Toe as a two-player game with states (board configurations), actions (moves), and utilities (win/loss/tie).
- **Python Programming**: Used Python 3.12 to handle nested lists for the game board, exception handling for invalid moves, and deep copying to preserve board states.
- **Data Structures**: Worked with lists to represent the 3x3 board and sets to track possible actions.
- **Pygame Integration**: Interacted with the provided `runner.py` to visualize the game, learning how to integrate AI logic with a graphical interface.

## Purpose
The purpose of the Tic-Tac-Toe problem is to apply the Minimax algorithm to create an unbeatable AI opponent for a classic game. It introduces adversarial search, where the AI evaluates future game states to maximize its chance of winning while assuming the opponent plays optimally. This simulates strategic decision-making in a competitive setting.

## Explanation
The program, implemented in `[tictactoe.py](/tictactoe.py)`, consists of several functions I completed to enable the AI to play Tic-Tac-Toe:

- **player(board)**: Determines whose turn it is (X or O) by counting moves. X moves first, and players alternate. Returns `None` for terminal boards.
- **actions(board)**: Returns a set of possible moves as `(i, j)` tuples for empty cells on the board.
- **result(board, action)**: Creates a new board by applying the given action (move) for the current player, using a deep copy to avoid modifying the original board. Raises an exception for invalid actions.
- **winner(board)**: Checks for a winner by examining rows, columns, and diagonals, returning X, O, or `None`.
- **terminal(board)**: Returns `True` if the game is over (win or full board) and `False` otherwise.
- **utility(board)**: Assigns a utility value for terminal boards: 1 for X’s win, -1 for O’s win, 0 for a tie.
- **minimax(board)**: Implements the Minimax algorithm to find the optimal move. For the current player:
  - If X, maximizes the score by selecting the move with the highest utility.
  - If O, minimizes the score by selecting the move with the lowest utility.
  - Recursively evaluates all possible moves, returning the optimal `(i, j)` action or `None` for terminal boards.

The provided `runner.py` handles the graphical interface, displaying the 3x3 board and allowing human vs. AI play. The AI’s optimal play ensures a tie or win, making it impossible to beat when both players play perfectly.

## Demo
The demo is best experienced by running `[runner.py](/runner.py)` to play the game interactively. Below is a sample game scenario (text-based for reference, as the actual output is graphical):

```
Initial Board:
  - | - | -
 ---+---+---
  - | - | -
 ---+---+---
  - | - | -

Human (X) moves to (0, 0):
  X | - | -
 ---+---+---
  - | - | -
 ---+---+---
  - | - | -

AI (O) moves to (1, 1):
  X | - | -
 ---+---+---
  - | O | -
 ---+---+---
  - | - | -

[Game continues until a tie or AI win]
```

To see the graphical version, run the program and interact with the Pygame window, where you click to place X’s, and the AI responds with O’s.

### Demo Video of AI in Action 
[![Watch the Demo Video](https://img.youtube.com/vi/VPs1B-Y-K98/maxresdefault.jpg)](https://youtu.be/VPs1B-Y-K98)
## How to Run
1. Ensure Python 3.12 and Pygame are installed:
   ```bash:disable-run
   pip install -r requirements.txt
   ```
2. Navigate to the folder:
   ```bash
   cd tic-tac-toe
   ```
3. Run the graphical interface:
   ```bash
   python runner.py
   ```
4. Click on the 3x3 grid to make moves as X; the AI plays as O.

## Files
- **[tictactoe.py](/tictactoe.py)**: Contains the AI logic, including `player`, `actions`, `result`, `winner`, `terminal`, `utility`, and `minimax` functions.
- **[runner.py](/runner.py)**: Provided script for the Pygame graphical interface.
- **[requirements.txt](/requirements.txt)**: Lists `pygame` as the required dependency.

## Reflections
Implementing Tic-Tac-Toe was a fascinating dive into adversarial search. The Minimax algorithm was challenging to grasp at first, but coding it helped me understand how to evaluate game trees and make optimal decisions. Ensuring the board state remained unmodified taught me the importance of deep copying. Playing against my own AI was rewarding, as its unbeatable nature confirmed the algorithm’s correctness. This problem solidified my understanding of recursive algorithms and game theory, setting a strong foundation for more complex AI challenges.

