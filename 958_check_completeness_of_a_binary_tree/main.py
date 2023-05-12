'''
958. Check Completeness of a Binary Tree
Given the root of a binary tree, determine if it is a complete binary tree.
In a complete binary tree, every level, except possibly the last, 
is completely filled, and all nodes in the last level are as far left as possible.
It can have between 1 and 2h nodes inclusive at the last level h.

Example 1:
Input: root = [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.

Example 2:
Input: root = [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.
 
Constraints:
The number of nodes in the tree is in the range [1, 100].
1 <= Node.val <= 1000
'''
# Definition for a binary tree node.
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        '''
        BFS Solution
        n is the number of node in the binary tree
        Space complexity O(n): Using an additional queue to store node in the Tree
        Time complexity O(n): We add all node in the tree to queue then pop to process and process time is O(1) => O(n)
        We using BFS adding all note to queue. If we found an None node before a valid None 
        => Uncomplete binary tree 
        Example: 
        Case 1:
        queue = [1,2,3,4,5,6,null] => True

        Case 2:
        queue = [1,2,3,4,5,null,7] => False
        '''

        if root is None:
            return False

        queue = deque()
        queue.append(root.val)
        hasNone = False

        while queue:
            cur = queue.popleft()
            if cur is None:
                hasNone = True
                continue
            if hasNone:
                return False
            queue.append(cur.left)
            queue.append(cur.right)

        return True

    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        '''
        DFS Solution
        Time complexity O(n)
        Space complexity O(n)
        '''

        def countNumNodes(root):
            if root is None:
                return 0
            return 1 + countNumNodes(root.left) + countNumNodes(root.right)

        numNodes = countNumNodes(root)

        def checkCompleteTree(root, idx, numNodes):
            if root is None:
                return True

            if idx > numNodes:
                return False

            return checkCompleteTree(root.left, idx * 2, numNodes) and checkCompleteTree(root.right, idx * 2 + 1, numNodes)
        
        return checkCompleteTree(root, 1, numNodes)
