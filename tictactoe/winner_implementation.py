from tictactoe import initial_state
from tictactoe import actions, player, terminal

X = "X"
O = "O"
EMPTY = None

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

instance_of_board = initial_state()
print(winner(instance_of_board))


