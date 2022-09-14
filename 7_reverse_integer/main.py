'''
7. Reverse Integer
https://leetcode.com/problems/reverse-integer/

Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

'''

import math
import time

#  NOT DONE YET
class Solution:
    def reverse(self, x: int) -> int:
        max_int = int(pow(2, 31) - 1)
        min_int = int(-pow(2, 31))
        max_int_digits = []
        min_int_digits = []

        sign = [-1, 1][x > 0]

        while max_int != 0:
            max_int_digits.append(max_int % 10)
            max_int = max_int // 10
        max_int_digits.reverse()

        min_int_digits = max_int_digits[:]
        min_int_digits[9] = 8

        digits = []
        if sign == -1:
            if x == min_int:
                digits = min_int_digits
            else: 
                x = x * -1
                  
        while x > 0:
            digits.append(x % 10)
            x = x // 10
        
        print(max_int_digits)
        print(min_int_digits)
        print(digits)
            
        # print(min_int_digits)
        # if len(digits) == 10:
        #     if digits[0] > 2:
        #         return 0

        # cur_ans = digits[0] * pow(10, len(digits) - 1)

        # for i in range(1, len(digits)):
        #     next_plus = digits[i] * pow(10, len(digits) - i)
        #     if max_int - next_plus < cur_ans:
        #         return 0
        #     else:
        #         cur_ans += next_plus

        # print(cur_ans)
        # return cur_ans


Solution().reverse(-2147483648)
