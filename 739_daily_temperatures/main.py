'''
739 Daily Temperatures
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature.
Tags: Stack
https://leetcode.com/problems/daily-temperatures/

Example:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Solution:
1. Create a list to store the result.
2. Create a stack to store the index of the temperatures.
3. For each temperature, check if the stack is not empty and the current temperature is greater than the temperature at the top of the stack.
4. If the current temperature is greater than the temperature at the top of the stack, calculate the difference between the current index and the index at the top of the stack.
5. Update the result with the difference.
6. Pop the index from the stack.

Time complexity: O(n)
Space complexity: O(n)
'''
from collections import defaultdict, deque
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = deque()

        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return res
 
s = Solution()
print(s.dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73]))