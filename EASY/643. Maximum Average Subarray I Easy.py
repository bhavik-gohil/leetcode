from typing import List


# class Solution:
#     def findMaxAverage(self, nums: List[int], k: int) -> float:
#         ln = len(nums)
#         i = 0
#         mx_avg = 0
#         while i <= ln-k:
#             avg_sm = 0
#             j = i
#             while j < i+k:
#                 avg_sm += nums[j]
#                 j += 1
#             mx_avg = max(mx_avg, avg_sm /
#                          k) if avg_sm >= 0 else min(mx_avg, avg_sm/k)
#             i += 1
#         return mx_avg


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ln = len(nums)

        prefix_sum = 0
        i = 0
        while i < k:
            prefix_sum += nums[i]
            i += 1

        max_sum = prefix_sum
        i = k
        while i < ln:
            prefix_sum = prefix_sum - nums[i-k] + nums[i]
            max_sum = max(max_sum, prefix_sum)
            i += 1

        return max_sum/k


i = Solution()
# call = i.findMaxAverage([1, 12, -5, -6, 50, 3], 4)
# call = i.findMaxAverage([5], 1)
# call = i.findMaxAverage([-1], 1)
# call = i.findMaxAverage([0, 4, 0, 3, 2], 1)
# call = i.findMaxAverage([493, 593, 1446, -6013, 2163, 8450, 3008, -1328, 6195, 4102, -6242, -9971, -8327, 4480, -4972, -8305, -1644, 2320, 331, 2465, 2955, -8386, -7580, 1759, -9576, -8088, -9446, -2916, -3600, 923, 1412, -5390, 4492, 9458, -9336, -4754, -3455, 9597, -
#                          324, -5628, 4242, 4076, 8159, -2423, -3449, 6744, 9029, -9231, 2283, 6118, -200, 3610, -7566, -6976, 2519, 9532, 2221, -5167, -2370, 1861, -1558, -9815, -1186, 2021, 7050, -4504, 4926, 8362, 7805, -8274, -351, 5826, 7623, -5520, -2395, -8466, -8461, 3261, -3197], 7)
call = i.findMaxAverage([-6662, 5432, -8558, -8935, 8731, -3083, 4115, 9931, -4006, -3284, -3024, 1714, -2825, -2374, -2750, -959, 6516, 9356, 8040, -2169, -9490, -3068, 6299, 7823, -9767, 5751, -7897, 6680, -1293, -3486, -6785, 6337, -9158, -4183, 6240, -2846, -2588, -5458, -9576, -1501, -908, -5477, 7596, -8863, -
                        4088, 7922, 8231, -4928, 7636, -3994, -243, -1327, 8425, -3468, -4218, -364, 4257, 5690, 1035, 6217, 8880, 4127, -6299, -1831, 2854, -4498, -6983, -677, 2216, -1938, 3348, 4099, 3591, 9076, 942, 4571, -4200, 7271, -6920, -1886, 662, 7844, 3658, -6562, -2106, -296, -3280, 8909, -8352, -9413, 3513, 1352, -8825], 90)

print("::", call)
