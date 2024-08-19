from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
                print(water)
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]
                print(water)
        
        # print(water)
        return water
        


Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])
# Solution().trap([4,2,0,3,2,5])