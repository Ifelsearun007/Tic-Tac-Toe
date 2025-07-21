def log_result(winner):
    with open("game_log.txt", "a") as f:
        f.write(f"Winner: {winner}\n")
