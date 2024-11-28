from tictactoe import initial_state
from tictactoe import actions, player, terminal, winner

X = "X"
O = "O"
EMPTY = None

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0