"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state(): # S0
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
    # Check if board is not over
    if terminal(board):
        return False
    
    # Count number of occurrences for different possible values
    x_counts = o_counts = empty_counts = 0  
    for row in board:
        for cell in row:
            if cell == X:
                x_counts += 1
            elif cell == O:
                o_counts +=1
            elif cell == EMPTY:
                empty_counts += 1
    
    # Return next turn based on counted elements logic
    if empty_counts == 0:
        return False
    elif x_counts == o_counts:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Initialize empty set
    possible_moves = set()

    # Iterate through the board to get empty spaces
    for row_index, row in enumerate(board):
        for cell_index, cell in enumerate(row):
            if cell == EMPTY:
                possible_moves.add((row_index, cell_index))
    
    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
