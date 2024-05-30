'''
455 - Assign Cookies
Link - https://leetcode.com/problems/assign-cookies/
Tags: ["Greedy", "Sort", "Array", "Two Pointers", "Binary Search"]
Description:
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.
Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.
'''
from typing import List


class Solution:
    '''
    Greedy Algorithm
    - Sort the children's greed factor and cookie sizes
    If the smallest cookie can satisfy the smallest child, then assign the cookie to the child
    - Increment the child index
    - If the child index is equal to the number of children, then break
    - Return the number of contented children
    '''

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0

        for c in s:
            if g[i] <= c:
                i += 1
            if i == len(g):
                break
        return i

    # def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # g = sorted(g)[::-1]
        # s = sorted(s)[::-1]
        # contented = 0
        # j = 0
        # total_children = len(g)

        # def binary_search(target, array, left, right):
        #     # print(array[left: right + 1], target)
        #     res = -1
        #     while left <= right:
        #         mid = left + (right - left) // 2
        #         # print(mid)
        #         if array[mid] <= target:
        #             res = mid
        #             right = mid - 1
        #         else:
        #             left = mid + 1
        #     # print(res)
        #     return res

        # for cookie_size in s:
        #     # Using binary search
        #     while j <= total_children - 1:
        #         x = binary_search(cookie_size, g, j, len(g) - 1)
        #         # print(x)
        #         if x == -1:
        #             return contented
        #         else:
        #             contented += 1
        #             j = x + 1
        #             break

        # return contented


print(Solution().findContentChildren([2, 3, 4], [2, 3]))
