'''
945 Minimum Increment to Make Array Unique
Tags - Array, Hash Table
https://leetcode.com/problems/minimum-increment-to-make-array-unique/

Example:
Input: nums = [3,2,1,2,1,7]
Output: 6

Solution:
1. Create a counter of the elements in the array.
2. Sort the keys of the counter.
3. For each element in the sorted keys, check if the count is greater than 1.
4. If the count is greater than 1, calculate the distance between the current element and the next element.
5. If the distance is less than the count, then we can move the elements to the next element.
6. If the distance is greater than the count, then we can move the elements to the next element.
7. Calculate the number of moves required to move the elements to the next element.
8. Update the counter of the next element with the remaining elements.
9. Return the result.

Time complexity: O(nlogn)
Space complexity: O(n)
'''
from collections import Counter
from typing import List
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        counter = Counter(nums)
        sorted_nums = sorted(counter.keys())
        res = 0
        
        for i in range(len(sorted_nums) - 1):
            cur_num = sorted_nums[i]
            next_num = sorted_nums[i + 1]
            if counter[cur_num] > 1:
                distance = min(next_num - cur_num, counter[cur_num])
                remain = counter[cur_num] - distance
                
                a =(counter[cur_num] - 1) * counter[cur_num] / 2 
                b =(counter[cur_num] - distance - 1) * (counter[cur_num] - distance) / 2
                res += a - b
                counter[next_num] += remain
        if counter[sorted_nums[len(sorted_nums)- 1]] > 1:
            res += int(counter[sorted_nums[-1]] * (counter[sorted_nums[-1]] - 1) / 2)
        return res
    
    def minIncrementForUniqueOptimized(self, nums: List[int]) -> int:
        counter = Counter(nums)
        move = 0
        taken = 0
        
        for num in range(min(counter), max(counter) + len(counter)):
            if num in counter:
                if counter[num] > 1:
                    taken += counter[num] - 1
                    move -= num * (counter[num] - 1)
            elif taken > 0:
                taken -= 1
                move += num
        
        return move
Solution().minIncrementForUnique([3,2,1,2,1,7])
