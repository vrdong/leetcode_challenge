'''
1442. Count Triplets That Can Form Two Arrays of Equal XOR
Link : https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/
Description:
Given an array of integers arr.
We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).
Let's define a and b as follows:
a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
Note that ^ denotes the bitwise-xor operation.
Return the number of triplets (i, j and k) Where a == b.

Example 1:
Input: arr = [2,3,1,6,7]
Output: 4
Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)

Example 2:
Input: arr = [1,1,1,1,1]
Output: 10
'''

from typing import List
class Solution:
    '''
    Solution:
    if arra[i] ^ arra[i+1] ^ ... ^ arra[j-1] == arra[j] ^ arra[j+1] ^ ... ^ arra[k]
    then arra[i] ^ arra[i+1] ^ ... ^ arra[j-1] ^ arra[j] ^ arra[j+1] ^ ... ^ arra[k] == 0
    so we can get the result by counting the number of j-i that make the xor value equal to 0

    Complexity:
    Time: O(n^2)
    Space: O(1)
    '''
    def countTriplets(self, arr: List[int]) -> int:
        count = 0
        for i in range(len(arr)):
            val = arr[i]

            for j in range(i + 1, len(arr)):
                val ^= arr[j]

                if val == 0:
                    count += j-i

        return count