mode = input("Select mode: 1 = PvP, 2 = PvE: ")

def get_ai_move(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return i, j
