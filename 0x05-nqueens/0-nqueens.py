#!/usr/bin/python3
"""
The N Queens puzzle is the challenge of placing N non-attacking
queens on an N×N chessboard. This program solves the N queens problem.
"""

import sys


def print_board(board):
    """Print the board in the required format."""
    result = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                result.append([i, j])
    print(result)


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col):
    """Utilize backtracking to solve the N Queens problem."""
    if col == len(board):
        print_board(board)
        return True

    res = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_nqueens_util(board, col + 1) or res
            board[i][col] = 0  # Backtrack

    return res


def solve_nqueens(n):
    """Solve the N Queens problem for a given n."""
    board = [[0] * n for _ in range(n)]
    solve_nqueens_util(board, 0)


def validate_input():
    """Validate the input to ensure it meets the problem's constraints."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    return n


if __name__ == "__main__":
    n = validate_input()
    solve_nqueens(n)
