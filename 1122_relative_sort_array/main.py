'''
1122 Relative Sort Array
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. 
Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.
'''
from typing import List
from collections import defaultdict
from functools import cmp_to_key

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        '''
        Solution: 
        1. Create a dictionary with elements of arr2 as key and their index as value.
        2. Create a compare function that will compare the elements of arr1 based on the dictionary created in step 1.
        3. Sort the arr1 based on the compare function.
        4. Return the sorted array.

        Time complexity: O(nlogn)
        Space complexity: O(n)
        '''
        dd = defaultdict(int)
        for i in range(len(arr2)):
            dd[arr2[i]] = i + 1
            
        # Modified compare function
        def compare(item1, item2):
            if dd[item1] != 0 and dd[item2] != 0:
                if dd[item1] < dd[item2]:
                    return -1
                elif dd[item1] > dd[item2]:
                    return 1
                else:
                    return 0
            
            if dd[item1] == 0 and dd[item2] == 0:
                if item1 < item2:
                    return -1
                elif item1 > item2:
                    return 1
                else:
                    return 0
            
            if dd[item1] == 0:
                return 1
            else:
                return -1

        key_function = cmp_to_key(compare)
        sorted_array = sorted(arr1, key=key_function)
        return sorted_array

a = Solution().relativeSortArray(arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6])
print(a)