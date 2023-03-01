from typing import List
from collections import deque
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[0 for _ in range(n)] for _ in range(n)]
        q = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    visited[i][j] = 1
                    q.append([i,j])
        
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        max_move = 0

        while q:
            coordinate = q.popleft()
            x, y = coordinate[0], coordinate[1]
            if visited[x][y] > max_move:
                max_move = visited[x][y]
            
            for direction in directions:
                new_x = x + direction[0]
                new_y = y + direction[1]
                if 0 <= new_x < n and 0 <= new_y < n:
                    if visited[new_x][new_y] == 0:
                        q.append([new_x, new_y])
                        visited[new_x][new_y] = visited[x][y] + 1
        
        distance = max_move - 1
        if distance == 0:
            return -1
        return distance


print(Solution().maxDistance([[1,0,1],[0,0,0],[1,0,1]]))