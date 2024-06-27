'''
1482. Minimum Number of Days to Make m Bouquets
Medium
Tags: Binary Search
https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
'''
from typing import List
from collections import Counter
class Solution:
    '''
    Solution:
    1. We need to find the minimum number of days to make m bouquets.
    2. We can use binary search to find the minimum number of days.
    3. We can start with minDay = 1 and maxDay = 1000000000.
    4. For each midDay, we will check if it is possible to make m bouquets.
    5. If it is possible, we will update the result and set maxDay = midDay - 1.
    6. If it is not possible, we will set minDay = midDay + 1.
    7. We will return the result.
    
    Time complexity: O(nlogm)
    n = len(bloomDay)
    m = max(bloomDay)
    Space complexity: O(1)
    '''
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        minDay = min(bloomDay)
        maxDay = max(bloomDay)
        res = 1000000000
        
        while minDay <= maxDay:
            midDay = minDay + (maxDay - minDay) // 2
            if self.isPosibleToMakeBoutique(bloomDay, m, k, midDay):
                res = midDay
                maxDay = midDay - 1
            else:
                minDay = midDay + 1
        return res      
    
    def isPosibleToMakeBoutique(self, bloomDay, m, k, days):
        count = 0 
        consecutive = 0
        
        for i in range(len(bloomDay)):
            if bloomDay[i] <= days:
                consecutive += 1
            else:
                count += consecutive // k
                consecutive = 0
        
        count += consecutive // k
        
        if count >= m:
            return True
        return False 

print(Solution().minDays(bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3))