'''
1002. Find Common Characters
Tags: ["Array", "Hash Table", "String", "Counting"]
Given an array A of strings made only from lowercase letters, 
return a list of all characters that show up in all strings within the list (including duplicates).
For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.
You may return the answer in any order.

Example 1:
Input: ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: ["cool","lock","cook"]
Output: ["c","o"]

Constraints:
1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter
'''

from collections import defaultdict as dd
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        '''
        Solution:
        1. Create a defaultdict to store the count of characters in the first word.
        2. For each word from the second word onwards, create a defaultdict to store the count of characters.
        3. For each character in the first word, update the count to the minimum of the current count and the count in the current word.
        4. Return the characters in the first word based on the count.
        
        Complexity:
        Let n be the number of words and m be the maximum length of the words.
        Time: O(n * m)
        Space: O(m)
        '''
        char_count = dd(int)
        for char in words[0]:
            char_count[char] += 1

        for word in words[1:]:
            current_char_count = dd(int)
            for char in word:
                current_char_count[char] += 1
            for k in char_count.keys():
                char_count[k] = min(char_count[k], current_char_count[k])

        return [key for key, value in char_count.items() for _ in range(value)]

print(Solution().commonChars(["bella", "label", "roller"]))
