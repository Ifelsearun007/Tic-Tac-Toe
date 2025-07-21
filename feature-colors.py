def color(text, player):
    return f"\033[91m{text}\033[0m" if player == "X" else f"\033[94m{text}\033[0m"

def print_board(board):
    for row in board:
        print(" | ".join(color(cell, cell) if cell != " " else cell for cell in row))
