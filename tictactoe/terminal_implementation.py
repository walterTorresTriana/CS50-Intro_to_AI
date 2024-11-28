from tictactoe import initial_state
from tictactoe import actions, player, terminal, winner

X = "X"
O = "O"
EMPTY = None

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
    
isinstance_of_board = initial_state()
print(terminal(isinstance_of_board))