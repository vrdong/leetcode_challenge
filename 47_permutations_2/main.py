'''
47. Permutations II
https://leetcode.com/problems/permutations-ii/
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],[1,2,1],[2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 
Constraints:
1 <= nums.length <= 8
-10 <= nums[i] <= 10
'''

from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = [] 
        current = []
        visited = [False] * len(nums)
        
        def backtrack(nums: List[int]):
            if len(current) == len(nums):
                result.append(current)
            
            for i in range(nums):
                if visited[i] == False:
                    if len(current) != 0:
                        if current[len(current) - 1] == nums[i]:
                            continue
                    