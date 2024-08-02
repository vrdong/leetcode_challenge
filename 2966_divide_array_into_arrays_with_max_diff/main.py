from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        ans = []
        sorted_arr = sorted(nums)
        n = len(nums)

        for i in range(n//3):
            if sorted_arr[i*3 + 2] - sorted_arr[i*3] > k:
                return []
            else:
                ans.append(sorted_arr[i*3: i*3 + 3])
        return ans

s = Solution()
s.divideArray(nums = [4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11], k = 14)