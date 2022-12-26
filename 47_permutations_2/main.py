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
from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        '''
        We using a counter to determine number of choice for a current position
        Given the input of [1, 1, 2], at the first stage, we have 2 choices to pick a number as the first number in the final permutation, i.e. 1 and 2.
        Suppose that we pick the number 1, now the remaining numbers would become [1, 2]. 
        Note: The reason that we have only 2 choices instead of 3, is that there is a duplicate in the given input. 
        Picking any of the duplicate numbers as the first number of the permutation would lead us to the same permutation at the end. 
        Should the numbers in the array be all unique, we would then have the same number of choices as the length of the array.

At the second stage, we now then have again 2 choices, i.e. [1, 2]. Let us pick again the number 1, which leaves us the only remaining number 2.

Now at the third stage, we have only one candidate number left, i.e. [2]. We then pick the last remaining number, which leads to a final permutation sequence of [1, 1, 2].

Moreover, we need to revisit each of the above stages, and make a different choice in order to try out all possibilities. The reversion of the choices is what we call backtracking.
        '''
        counter = Counter(nums)
        result = [] 
        comb = []
                
        def backtrack(comb, counter):
            if len(comb) == len(nums):
                result.append(list(comb))
            
            for num in counter:
                if counter[num] > 0:
                    comb.append(num)
                    counter[num] -= 1
                    backtrack(comb, counter)
                    comb.pop()
                    counter[num] += 1
        
        backtrack(comb, counter)
        return result

print(Solution().permuteUnique([1,2,3]))                        
            