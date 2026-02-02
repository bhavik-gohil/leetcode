from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        most_water = 0

        ln = len(height)
        i = 0
        j = ln - 1

        while i < j:
            length = j-i
            min_height = min(height[i], height[j])
            most_water = max(length * min_height, most_water)

            if height[j] > height[i]:
                i += 1
            else:
                j -= 1

        return most_water


i = Solution()
call = i.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
# call = i.maxArea([1, 1])
# call = i.maxArea([4, 3, 2, 1, 4])
# call = i.maxArea([1, 2, 1])
print("::", call)

# prev
# prefix_sum

# 1. iterate over arr from idx 1
# 2. check if x n_idx - n_idx-1 is > 0
#     n_idx-2 > n_idx-1

# find i and i nth elements such that it's min(i, i_nth)*min(i, i_nth) is greater than any other pair
