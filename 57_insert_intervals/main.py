from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        START, END = 0, 1
        left = 0
        right = len(intervals) - 1
        start_interval, end_interval = newInterval[START], newInterval[END]
        
        # tim vi tri lon nhat co end < start_interval
        left_ins = len(intervals)
        while left <= right:
            mid = left + (right - left) // 2
            if intervals[mid][END] >= start_interval:
                left_ins = mid
                right = mid - 1
            else:
                left = mid + 1
                
        left_ins -= 1
        
        left = 0
        right = len(intervals) - 1
        right_ins = len(intervals)

        #  Tim vi tri nho nhat co start > end_interval
        while left <= right:
            mid = left + (right - left) // 2
            if intervals[mid][START] > end_interval:
                right_ins = mid
                right = mid - 1
            else:
                left = mid + 1
                
        ans = []
        ans += intervals[0:left_ins + 1]

        if intervals[left_ins + 1][START] < start_interval:
            newInterval[START] = intervals[left_ins + 1][START]
        

        if intervals[right_ins - 1][END] > end_interval:
            newInterval[END] = intervals[right_ins- 1][END]

        ans.append(newInterval)

        ans += intervals[right_ins:]
        return ans

print(Solution().insert(intervals = [[1,3],[6,9]], newInterval = [2,5]))