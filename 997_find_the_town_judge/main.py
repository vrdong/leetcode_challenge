from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        can_not_be = {}
        trust_nums = [0] * (n + 1)

        for idx in range(len(trust)):
            can_not_be[trust[idx][0]] = True
            trust_nums[trust[idx][1]] += 1

        for i in range(1, n + 1):
            if trust_nums[i] == n - 1:
                if not can_not_be.get(i, False):
                    return i

        return -1


print(Solution().findJudge(n=3, trust=[[1, 3], [2, 3], [3, 1]]))
