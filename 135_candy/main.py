from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        lower_left = [0] * n
        lower_right = [0] * n

        for i in range(1, n):
            if ratings[i] < ratings[i - 1]:
                lower_left[i] = lower_left[i - 1] + 1
        
        for i in range(n-2, -1, -1):
            if ratings[i] < ratings[i + 1]:
                lower_right[i] = lower_right[i + 1] + 1
        
        is_bottom = []        
        
        
        for i in range(1, n - 1):
            if ratings[i] <= ratings[i + 1] and ratings[i] >= ratings[i-1]:
                is_bottom.append(i)
                
        sorted(enumerate())
        
        
        
        print(lower_left, lower_right)
        
        return 0
    


Solution().candy([1,2,2])