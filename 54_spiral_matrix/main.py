from typing import List

MOVE_RIGHT = 0
MOVE_DOWN = 1
MOVE_LEFT = 2
MOVE_UP = 3


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i, j = 0, -1
        m = len(matrix)
        n = len(matrix[0])
        left, right = 0, n - 1
        top, bottom = 1, m - 1

        mode = MOVE_RIGHT
        res = []

        while len(res) < m * n:
            print(res)
            if mode == MOVE_RIGHT:
                while j < right:
                    j += 1
                    res.append(matrix[i][j])
                mode += 1
                right -= 1
            elif mode == MOVE_LEFT:
                while j > left:
                    j -= 1
                    res.append(matrix[i][j])
                mode += 1
                left += 1
            elif mode == MOVE_UP:
                while i > top:
                    i -= 1
                    res.append(matrix[i][j])
                mode += 1
                top += 1
            elif mode == MOVE_DOWN:
                while i < bottom:
                    i += 1
                    res.append(matrix[i][j])
                mode += 1
                bottom -= 1
            mode %= 4
        return res

    def spiralOrderV2(self, matrix: List[List[int]]) -> List[int]:
        '''
        Another solutions
        '''
        row, col = len(matrix), len(matrix[0])
        top = 0
        bottom = row - 1
        left = 0
        right = col - 1

        res = []

        while top <= bottom and left <= right:
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top += 1
            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right -= 1

            if top > bottom or left > right:
                break

            for i in range(right, left-1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1

            for i in range(bottom, top-1, -1):
                res.append(matrix[i][left])
            left += 1

        return res


print(Solution().spiralOrder(
    matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
