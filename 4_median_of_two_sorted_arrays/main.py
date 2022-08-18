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
    def findMedianSortedArraysMySelf(self, nums1: List[int], nums2: List[int]) -> float:
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
                i += 1
            else:
                j += 1

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

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        l = m+n

        if l % 2 == 1:
            return self.kthSmallest(nums1, 0, m - 1, nums2, 0, n - 1, l // 2 + 1)
        else:
            mid_val_1 = self.kthSmallest(
                nums1, 0, m-1, nums2, 0, n - 1, l // 2 + 1)
            mid_val_2 = self.kthSmallest(
                nums1, 0, m-1, nums2, 0, n - 1, l // 2)
            print(mid_val_1, mid_val_2)
            return (mid_val_1 + mid_val_2) / 2

    def kthSmallest(self, nums1, start1, end1, nums2, start2, end2, k):
        # print(nums1[start1: end1+1], nums2[start2:end2+1], k)
        m = end1 - start1 + 1
        n = end2 - start2 + 1
        l = m + n

        if l < k:
            return 0

        if m == 0:
            return nums2[start2 + k - 1]
        if n == 0:
            return nums1[start1 + k - 1]

        mid1_idx = start1 + m // 2
        mid2_idx = start2 + n // 2

        mid1_val = nums1[mid1_idx]
        mid2_val = nums2[mid2_idx]

        # when k is bigger than the sum of a and b's median indices
        if l // 2 < k:
            # if a's median is smaller than b's, a's first half doesn't include k
            if mid1_val < mid2_val:
                return self.kthSmallest(nums1, mid1_idx + 1, end1, nums2, start2, end2, k - (m // 2 + 1))
            else:
                return self.kthSmallest(nums1, start1, end1, nums2, mid2_idx + 1, end2, k - (n // 2 + 1))
        else:
            if mid1_val < mid2_val:
                return self.kthSmallest(nums1, start1, end1, nums2, start2, mid2_idx - 1, k)
            else:
                return self.kthSmallest(nums1, start1, mid1_idx - 1, nums2, start2, end2, k)


print(Solution().findMedianSortedArrays(
    nums1=[1,2], nums2=[3]))
