def print_solution(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))
    print()

def is_safe(board, row, col, n):
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col, n):
    if col >= n:
        return True

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1

            if solve_n_queens_util(board, col + 1, n):
                return True

            board[i][col] = 0  # Backtrack

    return False

def solve_n_queens(n, first_queen_row):
    board = [[0 for _ in range(n)] for _ in range(n)]
    board[first_queen_row][0] = 1  # Place the first queen

    if not solve_n_queens_util(board, 1, n):  # Start from the second column
        print("Solution does not exist")
        return None

    print_solution(board)
    return board

# Example usage
n = 8  # Size of the chessboard
first_queen_row = 0  # Row where the first queen is placed
solve_n_queens(n, first_queen_row)