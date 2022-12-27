from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maximum_idx = 0;
        last_idx = len(nums) - 1
        
        # Conern case 1 element
        if len(nums) == 1:
            return True
            
        for i in range(len(nums) - 1):
            # Case can't jump to next idx
            if i > maximum_idx:
                return False
                
            if maximum_idx < i + nums[i]:
                maximum_idx = i + nums[i]
                if maximum_idx >= last_idx:
                    return True  
        return False
    
print(Solution().canJump(nums = [3,2,1,0,4]))