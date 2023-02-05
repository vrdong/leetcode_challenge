'''
567. Permutation in String
https://leetcode.com/problems/permutation-in-string/

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
'''
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = Counter(s1)
        s2_count = Counter(s2[:len(s1)])

        if s1_count == s2_count:
            return True

        for idx in range(len(s1), len(s2)):
            s2_count[s2[idx]] += 1
            s2_count[s2[idx - len(s1)]] -= 1
            # Must del. If not => wrong answer
            if s2_count[s2[idx - len(s1)]] == 0:
                del s2_count[s2[idx - len(s1)]]
            if s1_count == s2_count:
                return True

        return False


print(Solution().checkInclusion(s1="ab", s2="eidboaoo"))
