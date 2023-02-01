from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:

        n = len(s)
        map_palindrom = [[0] * n] * n
        result = []

        def is_palindrom(left, right):
            if left >= right:
                return True
            if map_palindrom[left][right] == 0:
                if s[left] != s[right]:
                    map_palindrom[left][right] == -1
                    return False
                else:
                    return is_palindrom(left + 1, right - 1)
            else:
                return map_palindrom[left][right]

        def backtrack(left, right, current):
            # print(s[left:right], left, right, current)
            if left == right:
                result.append(current[:])
                return result

            for i in range(left, right):
                if is_palindrom(left, i):
                    current.append(s[left:i + 1])
                    # print(current)
                    backtrack(i + 1, right, current)
                    current.pop()
        backtrack(0, n, [])

        return result


print(Solution().partition("a"))
