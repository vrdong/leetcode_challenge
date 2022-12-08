'''
46. Permutations
https://leetcode.com/problems/permutations/

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
'''

from typing import List
class Solution:
    '''
    Solution:
    O(N! * N)
    '''
    def findPermute(self, nums: List[int], currentResult: List[int]):
        if len(currentResult) == len(nums):
            self.result.append(currentResult[:])
            return
    
        for i in range(len(nums)):
            if self.visited[i] == False:
                self.visited[i] = True
                currentResult.append(nums[i])
                self.findPermute(nums, currentResult)
                currentResult.pop(len(currentResult) - 1)
                self.visited[i] = False
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.visited = [False] * len(nums)
        self.findPermute(nums, [])
        return self.result
        

        
        
        
        
print(Solution().permute(nums=[1,2,3]))