

from typing import List
import random


class Sorting:
    def bubble_sort(self, nums: List[int]) -> List[int]:
        '''
        Bubble Sort
        TIME COMPLEXITY: O(N^2)
        SPACE COMPLEXITY: O(1)
        '''
        n = len(nums)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    tmp = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = tmp
        return nums

    def merge_sort(self, nums: List[int]) -> List[int]:
        '''
        Merge Sort
        TIME COMPLEXITY: O(NlogN)
        SPACE COMPLEXITY: O(N)
        '''
        def merge(arr1: List[int], arr2: List[int]) -> List[int]:
            res = []
            i, j = 0, 0
            while i < len(arr1) and j < len(arr2):
                if arr1[i] < arr2[j]:
                    res.append(arr1[i])
                    i += 1
                else:
                    res.append(arr2[j])
                    j += 1
            if i < len(arr1):
                res += arr1[i:len(arr1)]
            else:
                res += arr2[j:len(arr2)]
            return res

        if len(nums) == 1:
            return nums

        mid = (len(nums) - 1) // 2
        arr1 = self.merge_sort(nums[:mid + 1])
        arr2 = self.merge_sort(nums[mid+1:])
        return merge(arr1, arr2)

    def quick_sort(self, nums: List[int]) -> List[int]:
        def random_pivot(arr: List[int], low: int, high: int):
            pivot = random.randrange(low, high)
            arr[pivot], arr[low] = arr[low], arr[pivot]

        def partition(arr: List[int], low: int, high: int):
            random_pivot(arr, low, high)
            pivot = arr[low]
            i = low + 1
            for j in range(i + 1, high + 1):
                if arr[j] < pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
            arr[i-1], arr[low] = arr[low], arr[i - 1]
            return i - 1

        def quick_sort(arr: List[int], low: int, high: int):
            # print(arr[low:high + 1])
            if low < high:
                pivot = partition(arr, low, high)
                quick_sort(arr, low, pivot - 1)
                quick_sort(arr, pivot + 1, high)
            return arr
        return quick_sort(nums, 0, len(nums) - 1)

    def process(self, input_nums: List[List[int]]):
        bubble_sort_result = []
        merge_sort_result = []
        quick_sort_result = []
        for nums in input_nums:
            print(nums)
            bubble_sort_result.append(self.bubble_sort(nums))
            print(nums)
            merge_sort_result.append(self.merge_sort(nums[:]))
            quick_sort_result.append(self.quick_sort(nums[:]))
        
        
        print(input_nums)

        # print(bubble_sort_result)
        # print(merge_sort_result)
        # print(quick_sort_result)
        # print(input_nums)


input_nums = [
    [3, 2, 5, 1, 7, 6, 8],
    [9, 8, 7, 6, 5, 4, 3, 2, 1],
    [2, 3, 3, 4, 5, 7, 8, 9],
    [2, 2, 2, 2, 2, 2, 2, 2]
]

Sorting().process(input_nums)
