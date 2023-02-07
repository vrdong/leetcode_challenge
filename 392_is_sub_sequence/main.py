
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        if m > n:
            return False
        
        check = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if s[i] == t[j]:
                    if i == 0 or j == 0:
                        check[i][j] = 1
                    else:
                        check[i][j] = check[i-1][j-1] + 1
                else:
                    up = check[i-1][j] if i > 0 else 0
                    front = check[i][j-1] if j > 0 else 0
                    check[i][j] = max(up, front)   
                         
        if check[m - 1][n - 1] == m:
            return True
        return False
Solution().isSubsequence(s = "abc", t = "ahbgdc")