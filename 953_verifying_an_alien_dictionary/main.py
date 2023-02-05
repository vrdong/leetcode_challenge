'''
953. Verifying an Alien Dictionary
https://leetcode.com/problems/verifying-an-alien-dictionary/

In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. 
The order of the alphabet is some permutation of lowercase letters.
Given a sequence of words written in the alien language, and the order of the alphabet, 
return true if and only if the given words are sorted lexicographically in this alien language.

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) 
According to lexicographical rules "apple" > "app", because 'l' > '∅', 
where '∅' is defined as the blank character which is less than any other character (More info).
'''

from typing import List
from collections import defaultdict


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        '''
        '''
        dictionary = defaultdict(int)
        for idx in range(len(order)):
            dictionary[order[idx]] = idx + 1

        def compareStr(str1, str2) -> bool:
            idx = 0
            while idx < len(str1) and idx < len(str2):
                if dictionary[str1[idx]] == dictionary[str2[idx]]:
                    idx += 1
                    continue
                if dictionary[str1[idx]] < dictionary[str2[idx]]:
                    return True
                else:
                    return False
                
            if len(str1) <= len(str2):
                return True
            else:
                return False

        for idx in range(len(words) - 1):
            if compareStr(words[idx], words[idx + 1]) is False:
                return False

        return True


print(Solution().isAlienSorted(
    words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"))
