class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        def is_valid(row, col, char):
            for i in range(9):
                if board[row][i] == char:
                    return False
                if board[i][col] == char:
                    return False
                if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == char:
                    return False
            return True
            
        def solve():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for c in "123456789":
                            if is_valid(i, j, c):
                                board[i][j] = c
                                if solve():
                                    return True
                                board[i][j] = "."
                        return False
            return True
            
        solve()
