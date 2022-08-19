'''
6. Zigzag Conversion
https://leetcode.com/problems/zigzag-conversion/

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);
 

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"
 

Constraints:
1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
'''


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        '''
        Time complexity O(N)
        Space compexity O(N)
        Traver throught the string s and store c for each line
        if line_idx = 0, we need to move down
        If line_idx = nuwRows, we need to move up
        If numRows = 1, we dont need to move
        '''
        res = ""
        lines = ["" for _ in range(numRows)]
        direction = 1
        line_idx = 0
        if numRows == 1:
            return s

        for c in s:
            if line_idx == 0:
                direction = 1
            elif line_idx == numRows - 1:
                direction = -1

            lines[line_idx] += c
            line_idx += direction

        res = ''.join(x for x in lines)
        return res


Solution().convert("A", 1)
