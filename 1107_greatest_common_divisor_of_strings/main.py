'''
1071. Greatest Common Divisor of Strings
https://leetcode.com/problems/greatest-common-divisor-of-strings/

For two strings s and t, we say "t divides s" if and only if s = t + ... + t 
(i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""

Constraints:
1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.

'''


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # print(str1, str2)
        if len(str1) == 0 or len(str2) == 0:
            return ""
        
        if str1 == str2:
            return str1
        
        return self.gcdOfStrings(str2, self.modString(str1, str2))
        
    def modString(self, str1: str, str2: str) -> str:
        # print(str1, str2)
        if len(str2) > len(str1):
            return str1
        
        if str1.find(str2) == 0:
            return str1.removeprefix(str2)
        else:
            return ""
        
    
print(Solution().gcdOfStrings('ABCABC', 'ABC'))