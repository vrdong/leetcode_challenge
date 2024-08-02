class Solution:
    def minimumDeletions(self, s: str) -> int:
        # Solution 1: Three Pass Through
        return self.threePassThrough(s)

    def threePassThrough(self, s: str) -> int:
        '''
        Solution 1:
        Three pass through the string s
        Choose i as the index to split the string into two parts: s[0:i] and s[i:n]
        Calculate number of 'b' before i and number of 'a' after i
        The minimum number of deletions needed to make the string balanced is the minimum of the sum of number of 'b' before i and number of 'a' after i
        
        1. First pass through the string from left to right, count the number of 'b' before the current index
        2. Second pass through the string from right to left, count the number of 'a' after the current index
        3. Third pass through the string, calculate the minimum number of deletions needed to make the string balanced
        
        Time complexity: O(n)
        Space complexity: O(n)
        '''
        n = len(s)
        num_b_before = [0] * n
        num_a_after = [0] * n

        for i in range(1, n):
            num_b_before[i] = num_b_before[i-1]
            if s[i - 1] == 'b':
                num_b_before[i] += 1

        for i in range(n-2, -1, -1):
            num_a_after[i] = num_a_after[i + 1]
            if s[i + 1] == 'a':
                num_a_after[i] += 1
            
        min_del = n    
        for i in range(n):
            min_del = min(min_del, num_a_after[i] + num_b_before[i])
        return min_del
    
    def DPOptimized(self, s: str) -> int:
        min_del = 0
        b_count = 0
        
        for ch in (s):
            if ch == 'b':
                b_count += 1
            else:
                min_del = min(min_del + 1, b_count)
                b_count += 1
        return min_del
                
     

a = Solution().minimumDeletions(s='a')
print(a)
