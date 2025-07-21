import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def print_board(board):
    clear_screen()
    print("\n   0   1   2")
    for i, row in enumerate(board):
        print(f"{i}  " + " | ".join(row))
        if i < 2:
            print("  " + "-" * 9)
