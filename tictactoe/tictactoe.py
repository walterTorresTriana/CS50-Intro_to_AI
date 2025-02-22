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
    possible_moves = set()

    for row_index, row in enumerate(board):
        for cell_index, cell in enumerate(row):
            if cell == EMPTY:
                possible_moves.add((row_index, cell_index))
    
    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # Verify action is valid
    if action not in actions(board):
        raise ValueError("Invalid action.")
    
    # Verify game is not over yet.
    if terminal(board):
        raise ValueError("Invalid action, the game is over.")
    
    # Create copy of the board
    import copy
    new_board = copy.deepcopy(board)

    # Make the move
    new_board[action[0]][action[1]] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if all(cell == row[0] for cell in row) and row[0] != EMPTY:
            return row[0]
        
    # Check columns
    for column in zip(*board):
        if all(cell == column[0] for cell in column) and column[0] != EMPTY:
            return column[0]        
    
    # Check diagonals
    diagonal = [board[i][i] for i in range(len(board))]
    antidiagonal = [board[i][len(board)-i-1] for i in range(len(board))]    

    if all(item == diagonal[0] for item in diagonal) and diagonal[0] != EMPTY:
        return diagonal[0]
    
    if all(item == antidiagonal[0] for item in antidiagonal) and antidiagonal[0] != EMPTY:
        return antidiagonal[0]

    # If no winner, return None"
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # Check if there is a winner
    if winner(board):
        return True
    
    # Check if there are empty spaces to make moves
    if not any(EMPTY in row for row in board):
        return True
    
    # Otherwise, the game is not over
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        elif winner(board) == None:
            return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return utility(board)
    
    if player(board) == X:
    
        best_value = float(-'inf')

        for action in actions(board):
            value = minimax(result(board, action))
            if value > best_value:
                best_value = value
                best_move = action

        return best_move
    
    else:

        best_value = float('inf')

        for action in actions(board):
            value = minimax(result(board, action))
            if value < best_value:
                best_value = value
                best_move = action
        return best_move

    


            


