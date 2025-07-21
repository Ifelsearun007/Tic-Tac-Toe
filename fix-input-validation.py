try:
    row = int(input("Enter row: "))
    col = int(input("Enter col: "))
    if not (0 <= row <= 2 and 0 <= col <= 2):
        raise ValueError("Out of bounds")
except ValueError as e:
    print(f"Invalid input: {e}")
    continue
