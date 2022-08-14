'''
Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Description
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.


'''



from collections import defaultdict
class Solution:
    '''
    Ideas:
    Duyệt qua rồi dùng hash map để đếm sô phàn tử 
    Nếu có 1 phần từ này trước đó tức hash map có
    => remove phần từ đầu tiền 
    '''
    
    # My solution
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Time complexity
        '''
        result = 0
        dd = defaultdict(bool)
        start = 0
        
        for index in range(len(s)):
            while dd[s[index]]:
                dd[s[start]] = False
                start += 1
            
            dd[s[index]] = True
            cur_range = index - start + 1
            if result < cur_range:
                result = cur_range
        return result
    
    # Almost same as optimal solution
    # Can using set instead of default dict
    
print(Solution().lengthOfLongestSubstring("123123"))
                

            
                
        