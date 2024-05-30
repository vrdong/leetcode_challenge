""" 
Desceiption: Find the longest substring of s that can be changed to t with at most maxCost cost
Ref: https://leetcode.com/problems/get-equal-substrings-within-budget/discuss/392918/JavaC%2B%2BPython-Sliding-Window
Tags: ["Sliding Window", "String", "Two Pointers", "Array"]
"""
class Solution:
    '''
    Solution:
    Sliding window
    Get max substring length with cost <= maxCost
    Calculate max_len for each end index
    
    Complexity:
    Time complexity: O(n)
    Space complexity: O(n)
    '''
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        cost = [0] * n
        for i in range(n):
            cost[i] = abs(ord(s[i]) - ord(t[i]))
        
        start = 0
        current_cost = 0
        max_len = 0
        for end in range(n):
            current_cost += cost[end]
            while current_cost > maxCost:
                current_cost -= cost[start]
                start += 1
            max_len = max(max_len, end - start + 1)
        return max_len

print(Solution().equalSubstring('pxezla', 'loewbi', 25))