from tictactoe import initial_state,terminal

X = "X"
O = "O"
EMPTY = None

terminal_status = False

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Check if board is not over
    if terminal(board):
        return False
    
    # Count number of occurrences for different possible values
    x_count = o_count = empty_count = 0  
    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count +=1
            elif cell == EMPTY:
                empty_count += 1
    
    if empty_count == 0:
        return False
    elif x_count == o_count:
        return X
    else:
        return O
        
instance_of_board = initial_state()
print(player(board=instance_of_board))