# <!--@nested-tags:topic,here/is/a/nested/example-->

from typing import List
from collections import defaultdict
'''
Description:
https://leetcode.com/problems/two-sum/
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 
'''


class Solution:
    def twoSum_1(self, nums: List[int], target: int) -> List[int]:
        dd = defaultdict(list)

        for idx in range(len(nums)):
            dd[nums[idx]].append(idx)

        for cur_num in list(dd.keys()):
            if target - cur_num != cur_num:
                if len(dd[target-cur_num]) > 0:
                    return [dd[cur_num][0], dd[target - cur_num][0]]
            else:
                if len(dd[cur_num]) > 1:
                    return [dd[cur_num][0], dd[cur_num][1]]

        return []

    # Optimal solution just 1 traversal
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Time complexity O(N)
        Space complexity O(N)
        '''
        dd = {}
        for i in range(len(nums)):
            j = dd.get(target - nums[i], None)
            if j is not None:
                return [i, j]
            dd[nums[i]] = i