from tictactoe import initial_state
from tictactoe import actions, player, terminal, winner

X = "X"
O = "O"
EMPTY = None

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

instance_of_board = initial_state()
print(utility(instance_of_board))