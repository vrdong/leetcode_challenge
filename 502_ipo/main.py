from typing import List
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        profits = [-x for x in profits]
        
        capital, profits = zip(*sorted(zip(capital, profits)))
        
        cur_cap = w
        cur_work = 0        
        heap = []
        heapq.heapify(heap)
        capital_idx = 0

        while cur_work < k:
            while capital_idx < len(capital) and cur_cap >= capital[capital_idx]:
                heapq.heappush(heap, profits[capital_idx])
                capital_idx += 1
            
            if len(heap) == 0:
                return cur_cap
            
            profit = -heapq.heappop(heap)
            cur_cap += profit
            cur_work += 1

        return cur_cap
            
            
        
        
print(Solution().findMaximizedCapital(k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]))
