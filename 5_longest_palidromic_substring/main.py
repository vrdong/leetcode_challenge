class Solution:
    def getPalindrome(self, s, l, r):
        '''
        expand left, right to get longest palindrome from a center
        s: string
        l: left_idx
        r: right_idx
        '''
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

    def longestPalindrome(self, s: str) -> str:
        '''
        Time complexity O(n^2)
        Space complexity 
        '''
        res = ""

        for i in range(len(s)):
            odd = self.getPalindrome(s, i, i)
            if len(odd) > len(res):
                res = odd

            even = self.getPalindrome(s, i, i+1)
            if len(even) > len(res):
                res = even
                
        return res


print(Solution().longestPalindrome("babad"))
