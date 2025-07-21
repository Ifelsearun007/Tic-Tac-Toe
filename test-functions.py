# test_tic_tac_toe.py
from tic_tac_toe import check_winner

def test_check_winner_row():
    board = [["X", "X", "X"], [" ", " ", " "], [" ", " ", " "]]
    assert check_winner(board, "X") == True
