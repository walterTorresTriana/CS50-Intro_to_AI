from tictactoe import initial_state

X = "X"
O = "O"
EMPTY = None

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

instance_of_board = initial_state()
print(actions(board=instance_of_board))
