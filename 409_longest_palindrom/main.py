from collections import defaultdict


class Solution:
    def longestPalindrome(self, s: str) -> int:
        '''
        find the longest palindrome in string not build the longest palindrome
        '''
        n = len(s)
        check = [[False for _ in range(n)] for _ in range(n)]
        longest = 0
        for k in range(n):
            for i in range(n-k):
                j = i + k
                if s[i] == s[j]:
                    if k < 3:
                        check[i][j] = True
                        longest = k + 1
                    else:
                        if check[i+1][j-1]:
                            check[i][j] = True
                            longest = k + 1

        print(longest)
        return longest


class Solution2:
    def longestPalindromeForBuild(self, s: str) -> int:
        dd = defaultdict(int)
        for c in s:
            dd[c] += 1

        can_build = 0
        have_odd = False
        for value in dd.values():
            if value % 2 == 0:
                can_build += value
            else:
                have_odd = True
                can_build += value - 1
        if have_odd:
            can_build += 1
        return can_build


print(Solution2().longestPalindromeForBuild('civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth'))


Solution().longestPalindrome('abccccdd')
