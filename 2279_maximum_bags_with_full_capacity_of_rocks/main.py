
from typing import List


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        rock_to_full = []
        for i in range(len(capacity)):
            rock_to_full.append(capacity[i]-rocks[i])
        rock_to_full = sorted(rock_to_full)
        maximum_bags = 0
        remain_rocks = additionalRocks
        for i in range(len(rock_to_full)):
            if rock_to_full[i] == 0:
                maximum_bags += 1
            else:
                if remain_rocks >= rock_to_full[i]:
                    maximum_bags += 1
                    remain_rocks -= rock_to_full[i]
                else:
                    break
        return maximum_bags
        
print(Solution().maximumBags(capacity = [10,2,2], rocks = [2,2,0], additionalRocks = 100))