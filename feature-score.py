def play_game():
    scores = {"X": 0, "O": 0}
    while True:
        winner = run_single_game()
        if winner:
            scores[winner] += 1
        print(f"Scores: X = {scores['X']}, O = {scores['O']}")
        again = input("Play again? (y/n): ")
        if again.lower() != 'y':
            break
