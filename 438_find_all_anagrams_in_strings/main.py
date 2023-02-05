'''
438. Find All Anagrams in a String
https://leetcode.com/problems/find-all-anagrams-in-a-string/

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "a

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.

'''

from typing import List
from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''
        Tags: ['Slice Window', 'Hash Map']
        Using slice window + hashmap
        '''
        
        # If p can not be an anagram of s if len(p) > len(s)
        if len(s) < len(p):
            return []
        
        # Init hash map for p. + 1 for every character
        result = []
        dd = defaultdict(int)
        for c in p:
            dd[c] += 1
        
        # Init first set from s. - 1 for every character
        for idx in range(len(p)):
            dd[s[idx]] -= 1
        
        # Move the window
        for idx in range(len(p) - 1, len(s)):
            # If hash map contain all zero value character => current window string is an anagrams
            if self.isAnagram(dd):
                result.append(idx + 1 - len(p))
            
            # Move window forward 1 character
            if idx < len(s) - 1:
                dd[s[idx+1]] -= 1
                dd[s[idx+1 - len(p)]] += 1
    
        return result

        
    def isAnagram(self, dd) -> bool:
        for remain in dd.values():
            if remain != 0:
                return False
        return True
print(Solution().findAnagrams('abab', 'ab'))


# Another solution by Chat GPT using Counter instead of default_dict
from collections import Counter

def findAnagrams(s, p):
    result = []
    p_count = Counter(p)
    s_count = Counter(s[:len(p)])
    if p_count == s_count:
        result.append(0)
    for i in range(len(p), len(s)):
        s_count[s[i]] += 1
        s_count[s[i - len(p)]] -= 1
        if s_count[s[i - len(p)]] == 0:
            del s_count[s[i - len(p)]]
        if p_count == s_count:
            result.append(i - len(p) + 1)
    return result