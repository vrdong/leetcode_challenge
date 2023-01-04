'''
1962. Remove Stones to Minimize the Total
Example 1:
Input: piles = [5,4,9], k = 2
Output: 12
Explanation: Steps of a possible scenario are:
- Apply the operation on pile 2. The resulting piles are [5,4,5].
- Apply the operation on pile 0. The resulting piles are [3,4,5].
The total number of stones in [3,4,5] is 12.

Example 2:
Input: piles = [4,3,6,7], k = 3
Output: 12
Explanation: Steps of a possible scenario are:
- Apply the operation on pile 2. The resulting piles are [4,3,3,7].
- Apply the operation on pile 3. The resulting piles are [4,3,3,4].
- Apply the operation on pile 0. The resulting piles are [2,3,3,4].
The total number of stones in [2,3,3,4] is 12.
'''


from typing import List
import heapq
import math


class Solution:
    def minStoneSum_2(self, piles: List[int], k: int) -> int:
        '''
        Space O(max_high)
        Time O(NlogN) sort
        
        '''
        sorted_piles = sorted(piles)
        max_high = sorted_piles[len(piles) - 1]
        piles_high = [0] * (max_high + 1)

        for high in sorted_piles:
            piles_high[high] += 1

        cur_max_high = max_high
        for _ in range(k):
            while cur_max_high > 0 and piles_high[cur_max_high] == 0:
                cur_max_high -= 1
            if piles_high[cur_max_high] > 0:
                piles_high[cur_max_high] -= 1
                piles_high[math.ceil(cur_max_high/2)] += 1

        sum_total = 0
        for i in range(cur_max_high + 1):
            if piles_high[i] > 0:
                sum_total += piles_high[i] * i

        return sum_total
    
    '''
    Using greedy to remove maximum number height.
    Using heap k times to get the smallest
    '''
    
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-num for num in piles]
        heapq.heapify(heap)
        print(heap)
        for _ in range(k):
            curr = -heapq.heappop(heap)
            remove = curr // 2
            heapq.heappush(heap, -(curr - remove))
            print(heap)
        
        return -sum(heap)        



print(Solution().minStoneSum([4, 3, 6, 7], k=3))
