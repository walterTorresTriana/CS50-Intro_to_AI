from tictactoe import initial_state
from tictactoe import actions, player, terminal

X = "X"
O = "O"
EMPTY = None

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

# Temporary used while coding results function
instance_of_board = initial_state()
print(actions(instance_of_board))
print(result(board=instance_of_board, action=next(iter(actions(instance_of_board)))))


