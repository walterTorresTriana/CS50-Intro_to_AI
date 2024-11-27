from tictactoe import initial_state
from tictactoe import actions

# Temporary used while coding results function


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    import copy

    new_board = copy.deepcopy(board)

    l = []
    for i in actions(instance_of_board):
        if isinstance(i, tuple):
            l.append("yes")
    return l

instance_of_board = initial_state()
print(actions(instance_of_board))
print(result(board=instance_of_board, action=actions(instance_of_board)))


