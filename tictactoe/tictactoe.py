"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_play_num = 0
    for row in board:
        for cell in row:
            if cell == "X":
                x_play_num += 1
    if x_play_num % 2 == 0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell is None:
                action = (i, j)
                actions.add(action)
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Validate action
    if action not in actions(board):
        raise Exception("Invalid action")

    # make a deep copy of board to avoid mutating original board
    origin_board = copy.deepcopy(board)

    # get current player
    current_player = player(board)
    origin_board[action[0]][action[1]] = current_player
    return origin_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    if len(actions(board)) == 0:
        return True
    if winner(board) is not None:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        win_player = winner(board)
        if win_player == X:
            return 1
        elif win_player == O:
            return -1
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_v(board):
        if terminal(board):
            return utility(board)
        value = -math.inf
        for action in actions(board):
            value = max(value, min_v(result(board, action)))
        return value

    def min_v(board):
        if terminal(board):
            return utility(board)
        value = math.inf
        for action in actions(board):
            value = min(value, max_v(result(board, action)))
        return value

    if terminal(board):
        return None
    
    current_player = player(board)
    if current_player == X:
        value = -math.inf
        best_action = None
        for action in actions(board):
            min_value = min_v(result(board, action))
            if min_value > value:
                value = min_value
                best_action = action
        return best_action
    else:
        value = math.inf
        best_action = None
        for action in actions(board):
            max_value = max_v(result(board, action))
            if max_value < value:
                value = max_value
                best_action = action
        return best_action

