
from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        total_jump = 1
        i = 0
        
        while i < n:
            if i + nums[i] >= n - 1:
                return total_jump
            temp_max = 0
            temp_index = i
            for j in range (i + 1, i + nums[i] + 1):
                weigh = j + nums[j] if nums[j] > 0 else 0
                if weigh > temp_max:
                    temp_max = weigh
                    temp_index = j
            i = temp_index
            total_jump += 1
        return total_jump
    
print(Solution().jump([2,0,0,0,0]))