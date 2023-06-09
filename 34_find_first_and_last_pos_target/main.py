from typing import List
import bisect
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        idx = self.lowerBound(nums, target)
        if idx == len(nums) or nums[idx] != target:
            return [-1, -1]
        
        idx2 = self.upperBound(nums, target)
        return [idx, idx2 - 1]
    
    
    def lowerBound(self, nums, target):
        left = 0
        right = len(nums) - 1
        ans = len(nums)
        
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
    
    def upperBound(self, nums, target):
        left = 0
        right = len(nums) - 1
        ans = len(nums)
        
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans