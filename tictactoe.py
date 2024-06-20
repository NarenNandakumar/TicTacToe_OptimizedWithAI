"""
Tic Tac Toe Player
"""

import math

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
    xcount = 0
    ocount = 0
    for row in board:
        xcount += row.count(X)
        ocount += row.count(O)
    return X if xcount == ocount else O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] is not EMPTY:
        raise Exception("Invalid action")
    new_board = [row[:] for row in board]  # Create a deep copy of the board
    new_board[action[0]][action[1]] = player(board)
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winning_combinations = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    for combination in winning_combinations:
        if board[combination[0][0]][combination[0][1]] == board[combination[1][0]][combination[1][1]] == board[combination[2][0]][combination[2][1]] != EMPTY:
            return board[combination[0][0]][combination[0][1]]
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or all(cell is not EMPTY for row in board for cell in row)

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    current_player = player(board)
    if current_player == X:
        _, action = max_value(board)
    else:
        _, action = min_value(board)
    return action

def max_value(board):
    if terminal(board):
        return utility(board), None
    v = -math.inf
    best_action = None
    for action in actions(board):
        min_val, _ = min_value(result(board, action))
        if min_val > v:
            v = min_val
            best_action = action
    return v, best_action

def min_value(board):
    if terminal(board):
        return utility(board), None
    v = math.inf
    best_action = None
    for action in actions(board):
        max_val, _ = max_value(result(board, action))
        if max_val < v:
            v = max_val
            best_action = action
    return v, best_action
