'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
'''
from typing import List
import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        Time complexity: O(n)
        Space complexity: O(1)
        '''
        i = j = 0
        cur_idx = 0
        m, n = len(nums1), len(nums2)
        mid_idx = (m + n - 1) // 2
        ans = 0
        while cur_idx <= mid_idx:
            num1_val = nums1[i] if i < m else math.inf
            num2_val = nums2[j] if j < n else math.inf
            
            if num1_val < num2_val:
                i+=1
            else:
                j+=1
            
            if cur_idx == mid_idx:
                ans = min(num1_val, num2_val)
            cur_idx += 1

        if (m + n) % 2 == 0:
            num1_val = nums1[i] if i < m else math.inf
            num2_val = nums2[j] if j < n else math.inf
            
            ans += min(num1_val, num2_val) 
            return ans / 2
        else:
            return ans
        
        
    # Optimal solution Olog(m+n)
    # TODO

print(Solution().findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))