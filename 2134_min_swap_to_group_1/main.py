from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        return self.suffix_sum(nums)
        

    def suffix_sum(self, nums: List[int]) -> int:
        op1 = self.min_swap_helper(nums, 0)
        op2 = self.min_swap_helper(nums, 1)

        return min(op1, op2)

    def min_swap_helper(self, data: List[int], val: int) -> int:
        n = len(data)
        total_val_count = 0

        for i in range(n-1, -1, -1):
            if data[i] == val:
                total_val_count += 1
                
        if total_val_count == 0 or total_val_count == n:
            return 0
        
        # print(total_val_count)
        start = 0
        end = 0
        max_val_in_window = 0
        current_val_in_window = 0
        
        while end < total_val_count:
            if data[end] == val:
                current_val_in_window += 1
            end += 1
        max_val_in_window = max(current_val_in_window, max_val_in_window)
        
        while end < n:
            if data[start] == val:
                current_val_in_window -= 1
            start += 1
            if data[end] == val:
                current_val_in_window += 1
            end += 1
            max_val_in_window = max(current_val_in_window, max_val_in_window)
            
        return total_val_count - max_val_in_window


print(Solution().minSwaps([0,1,0,1,1,0,0]))
