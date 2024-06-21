'''
1052. Grumpy Bookstore Owner
Medium
There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter the store. 
You are given an integer array customers of length n where customers[i] is the number of the customer that enters the store at the start of the ith minute and all those customers leave after the end of that minute.
On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.
When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.
The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.
Return the maximum number of customers that can be satisfied throughout the day.

Example 1:
Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes.
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.

Example 2:
Input: customers = [1], grumpy = [0], X = 1
Output: 1

Constraints:
n == customers.length == grumpy.length
1 <= n <= 2 * 10^4
0 <= customers[i] <= 1000
grumpy[i] is either 0 or 1.
'''

from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        '''
        Explanation: 
        1. Calculate the current_satisfy by adding the customers who are satisfied.
        2. Calculate the max_inc_satisfy by adding the customers who are not satisfied in the first X minutes.
        3. Calculate the inc_satisfy by adding the customers who are not satisfied in the first X minutes and subtracting the customers who are not satisfied in the previous X minutes.
        4. Update the max_inc_satisfy if inc_satisfy is greater than max_inc_satisfy.
        5. Return the sum of current_satisfy and max_inc_satisfy.
        
        Time complexity: O(n)
        Space complexity: O(1)
        '''
        base_satisfaction = 0
        n = len(customers)
        for i in range(n):
            if grumpy[i] == 0:
                base_satisfaction += customers[i]

        max_additional_satisfaction = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                max_additional_satisfaction += customers[i]

        additional_satisfaction = max_additional_satisfaction
        for i in range(1, n - minutes + 1):
            if grumpy[i-1] == 1:
                additional_satisfaction -= customers[i - 1]
            if grumpy[i + minutes - 1] == 1:
                additional_satisfaction += customers[i + minutes - 1]
            if additional_satisfaction > max_additional_satisfaction:
                max_additional_satisfaction = additional_satisfaction

        return base_satisfaction + max_additional_satisfaction

print(Solution().maxSatisfied(customers=[1, 0, 1, 2, 1, 1, 7, 5], grumpy=[
      0, 1, 0, 1, 0, 1, 0, 1], minutes=3))  # 16
print(Solution().maxSatisfied(customers=[1], grumpy=[0], minutes=1))  # 1
