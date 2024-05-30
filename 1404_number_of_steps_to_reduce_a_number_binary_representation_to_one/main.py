'''
Ref: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/description/?envType=daily-question&envId=2024-05-29
1404. Number of Steps to Reduce a Number in Binary Representation to One
Tags: ["Bit Manipulation", "String", "Math"]
Given the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:
If the current number is even, you have to divide it by 2.
If the current number is odd, you have to add 1 to it.
It is guaranteed that you can always reach one for all test cases.

 
Example 1:
Input: s = "1101"
Output: 6
Explanation: "1101" corressponds to number 13 in their decimal representation.
Step 1) 13 is odd, add 1 and obtain 14. 
Step 2) 14 is even, divide by 2 and obtain 7.
Step 3) 7 is odd, add 1 and obtain 8.
Step 4) 8 is even, divide by 2 and obtain 4.  
Step 5) 4 is even, divide by 2 and obtain 2. 
Step 6) 2 is even, divide by 2 and obtain 1.  

Example 2:
Input: s = "10"
Output: 1
Explanation: "10" corressponds to number 2 in their decimal representation.
Step 1) 2 is even, divide by 2 and obtain 1.  

Example 3:
Input: s = "1"
Output: 0
 

Constraints:
1 <= s.length <= 500
s consists of characters '0' or '1'
s[0] == '1'
'''

class Solution:
    '''
    Solution:
    - Start from the last digit of the binary number and move towards the first digit.
    - If the digit is 0, increment the step count by 1.
    - If the digit is 1, increment the step count by 2 and set the carry_over to 1.
    - At the end, if there is a carry_over, increment the step count by 1.
    - Return the step count.
    
    Time complexity: O(n)
    Space complexity: O(1)
    '''
    def numSteps(self, s: str) -> int:  
        n = len(s)
        step_count = 0
        carry_over = 0

        for i in range(n - 1, 0, -1):
            num = int((int(s[i]) + carry_over) % 2)
            bring = int((int(s[i]) + carry_over) / 2)
            if num == 0:
                step_count += 1
            else:
                step_count += 2
                carry_over = 1
        step_count += carry_over

        return step_count


Solution().numSteps('1101')
