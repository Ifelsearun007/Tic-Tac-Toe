def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Rows, columns, and diagonals
    win_conditions = (
        [board[i] for i in range(3)] +                          # Rows
        [[board[i][j] for i in range(3)] for j in range(3)] +  # Columns
        [[board[i][i] for i in range(3)]] +                    # Diagonal \
        [[board[i][2 - i] for i in range(3)]]                  # Diagonal /
    )
    return any(all(cell == player for cell in condition) for condition in win_conditions)

def main():
    board = [[" "]*3 for _ in range(3)]
    current_player = "X"

    for turn in range(9):
        print_board(board)
        row = int(input(f"{current_player}'s turn. Enter row (0-2): "))
        col = int(input(f"{current_player}'s turn. Enter col (0-2): "))

        if board[row][col] == " ":
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"{current_player} wins!")
                return
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Cell taken. Try again.")
            turn -= 1

    print_board(board)
    print("It's a tie!")

if __name__ == "__main__":
    main()
