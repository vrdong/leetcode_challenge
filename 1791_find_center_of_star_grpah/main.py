'''
1791. Find Center of Star Graph
Medium
Tags - Array, Hash Table
https://leetcode.com/problems/find-center-of-star-graph/

Example:
Input: edges = [[1,2],[2,3],[4,2]]
Output: 2
'''
from collections import defaultdict
from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        '''
        Solution:
        1. Create a defaultdict to store the count of the nodes.
        2. For each edge, increment the count of the nodes.
        3. Get the total number of nodes.
        4. For each node, check if the count is equal to total number of nodes - 1.
        5. If the count is equal to total number of nodes - 1, return the node.
        6. Return the result.
        Time complexity: O(n)
        Space complexity: O(n)
        '''
        dd = defaultdict(int)
        
        for edge in edges:
            dd[edge[0]] += 1
            dd[edge[1] ] += 1
        
        total_note = len(dd.keys())

        for key, value in dd.items():
            if value == total_note - 1:
                return key
    
    def findCenterOptimized(self, edges: List[List[int]]) -> int:
        '''
        Solution:
        1. Return the intersection of the first and second element of the first and second element of the edges.
        Time complexity: O(1)
        Space complexity: O(1)
        '''
        # return set(edges[0]).intersection(set(edges[1])).pop()
        # Check if the first node of the first edge is the center
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        # Otherwise, the second node of the first edge is the center
        return edges[0][1]