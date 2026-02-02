from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        trapped_water = 0

        ln = len(height)
        i = 0
        j = ln-1

        left_max = 0
        left_maxes = []

        right_max = 0
        right_maxes = []

        while i < ln:
            left_maxes.append(left_max)
            left_max = max(left_max, height[i])

            right_maxes.insert(0, right_max)
            right_max = max(right_max, height[j])

            i += 1
            j -= 1

        i = 0
        while i < ln:
            water = min(left_maxes[i], right_maxes[i]) - height[i]
            trapped_water += water if water > 0 else 0
            i += 1

        return trapped_water


i = Solution()
# call = i.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
call = i.trap([4, 2, 0, 3, 2, 5])
print("::", call)
