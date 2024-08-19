
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = 9

        row_check = [[True] * n for _ in range(n)]
        col_check = [[True] * n for _ in range(n)]
        block_check = [[True] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if board[i][j] != ".":
                    row_check[i][int(board[i][j]) - 1] = False
                    col_check[j][int(board[i][j]) - 1] = False
                    block_check[self.get_block(i, j)][int(
                        board[i][j]) - 1] = False

        self.solve(board, 0, row_check, col_check, block_check)
        print(board)

    def solve(self, board, idx, row_check, col_check, block_check):
        if idx == 81:
            return True

        x, y = self.get_pos(idx)
        # Nếu ô đã có số
        if board[x][y] != ".":
            return self.solve(board, idx + 1, row_check, col_check, block_check)

        # Ô chưa có số
        for num in range(1, 10):
            if row_check[x][num-1] and col_check[y][num-1] and block_check[self.get_block(x, y)][num-1]:
                row_check[x][num-1] = False
                col_check[y][num-1] = False
                block_check[self.get_block(x, y)][num-1] = False
                board[x][y] = str(num)
                # print(board)
                is_solve = self.solve(
                    board, idx + 1, row_check, col_check, block_check)
                if is_solve:
                    return True
                row_check[x][num-1] = True
                col_check[y][num-1] = True
                block_check[self.get_block(x, y)][num-1] = True
                board[x][y] = "."

        return False

    def get_block(self, x, y):
        return (x // 3) * 3 + y // 3

    def get_pos(self, idx):
        return idx // 9, idx % 9


Solution().solveSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], [
    "4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]])