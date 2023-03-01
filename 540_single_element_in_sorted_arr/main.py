from typing import List
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        def getNonDuplicate(left, right) -> int:
            print(left, right,nums[left:right+1])
            if left == right:
                return nums[left]

            half = (right - left + 1) // 2
            if half % 2 == 0:
                print(half)
                if nums[left + half - 1] == nums[left + half - 2]:
                    return getNonDuplicate(left + half, right)
                else:
                    return getNonDuplicate(left, left + half - 2)
            else:
                if nums[left + half] == nums[left + half + 1]:
                    return getNonDuplicate(left, left + half - 1)
                else:
                    return getNonDuplicate(left + half + 1, right)

        return getNonDuplicate(0, len(nums) - 1)
    
print(Solution().singleNonDuplicate([1,1,2,3,3]))