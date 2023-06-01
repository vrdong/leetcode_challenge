"""
1091. Shortest Path in Binary Matrix
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix.
If there is no clear path, return -1.
A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.
"""

import collections
from typing import List

DIRECTION_X = [-1, -1, -1, 0, 0, 1, 1, 1]
DIRECTION_Y = [-1, 0, 1, -1, 1, -1, 0, 1]


class Solution:

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        '''
        Solution BFF
        
        '''
        def isValidCell(i, j, n):
            if i < 0 or j < 0 or i > n - 1 or j > n - 1:
                return False
            return True

        n = len(grid)
        queue = collections.deque()
        if grid[0][0] == 1:
            return -1
        queue.appendleft([0, 0, 1])
        grid[0][0] = -1
        while queue:
            x, y, distance = queue.pop()
            if x == n-1 and y == n-1:
                return distance

            for i in range(8):
                next_x = x + DIRECTION_X[i]
                next_y = y + DIRECTION_Y[i]
                if isValidCell(next_x, next_y, n) and abs(grid[next_x][next_y]) != 1:
                    queue.appendleft([next_x, next_y, distance + 1])
                    grid[next_x][next_y] = -1

        return -1


print(Solution().shortestPathBinaryMatrix(grid=[[1,0,0],[1,1,0],[1,1,0]]))
