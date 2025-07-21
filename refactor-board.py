class Board:
    def __init__(self):
        self.grid = [[" "] * 3 for _ in range(3)]

    def display(self):
        for row in self.grid:
            print(" | ".join(row))

    def mark(self, row, col, player):
        if self.grid[row][col] == " ":
            self.grid[row][col] = player
            return True
        return False
