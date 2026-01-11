import math
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = [[1]]
        i = 1

        while i <= rowIndex:
            t = [1]
            prev_array = triangle[i-1]
            j = 1
            while j < len(prev_array):
                t.append(prev_array[j-1]+prev_array[j])
                j = j + 1
            t.append(1)
            triangle.append(t)
            i = i + 1

        return triangle[rowIndex]


i = Solution()
call = i.getRow(3)
print(" :: ", call)
