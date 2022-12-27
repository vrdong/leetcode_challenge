
'''
886. Possible Bipartition
https://leetcode.com/problems/possible-bipartition/description/
We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.
Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.

Example 1:
Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4] and group2 [2,3].

Example 2:
Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:
Input: n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false
 

Constraints:
1 <= n <= 2000
0 <= dislikes.length <= 104
dislikes[i].length == 2
1 <= dislikes[i][j] <= n
ai < bi
All the pairs of dislikes are unique.
'''

from typing import List
from collections import deque

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        '''
        Dung
        '''
        def bfs(source):
            q = deque([source])
            color[source] = RED
            while q:
                node = q.popleft()
                for neighbor in adj[node]:
                    if color[neighbor] == color[node]:
                        return False
                    if color[neighbor] == UNSPECIFIC:
                        color[neighbor] = 1 - color[node]
                        q.append(neighbor)
            return True
        
        # define constant
        UNSPECIFIC = -1
        RED = 0
        BLUE = 1
        
        adj = [[] for i in range(n + 1)]
        for dislike in dislikes:
            adj[dislike[0]].append(dislike[1])
            adj[dislike[1]].append(dislike[0])
            
        color = [UNSPECIFIC] * (n + 1)
        
        for i in range(n + 1):
            if color[i] == UNSPECIFIC:
                if not bfs(i):
                    return False       
        return True

print(Solution().possibleBipartition(5, [[1,2],[2,3],[3,4],[4,5],[1,5]]))