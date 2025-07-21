move_stack = []

# On valid move
move_stack.append((row, col))
board[row][col] = current_player

# Undo option
if input("Undo? (y/n): ") == 'y' and move_stack:
    r, c = move_stack.pop()
    board[r][c] = " "
