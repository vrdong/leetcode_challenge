'''
1232. Check If It Is a Straight Line
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point.
Check if these points make a straight line in the XY plane.

Example 1:
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true


Example 2:
Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false

Constraints:
2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.
'''

from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        line_vector_x, line_vector_y =  coordinates[1][0] - coordinates[0][0], coordinates[1][1] - coordinates[0][1]
        perpendicular_vector_x, perpendicular_vector_y = -line_vector_y, line_vector_x
        
        def is_perpendicular(vector_x, vector_y):
            if vector_x * perpendicular_vector_x + vector_y * perpendicular_vector_y == 0:
                return True
            return False
        
        
        for i in range(2,len(coordinates)):
            if not is_perpendicular(coordinates[i][0] - coordinates[0][0], coordinates[i][1] - coordinates[0][1]):
                return False
            
        return True
            
print(Solution().checkStraightLine(coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))      