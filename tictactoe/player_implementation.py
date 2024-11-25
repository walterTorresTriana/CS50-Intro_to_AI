from tictactoe import initial_state,terminal

X = "X"
O = "O"
EMPTY = None

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
        
instance_of_board = initial_state()
print(player(board=instance_of_board))