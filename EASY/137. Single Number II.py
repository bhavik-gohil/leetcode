from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # h = {}
        # for i in nums:
        #     if not h.get(i):
        #         h[i] = 0
        #     h[i] += 1
        # for i, j in h.items():
        #     if j != 3:
        #         return i
        # return 0
        i, j = 0, 0
        for num in nums:
            i = i ^ num & ~j
            j = j ^ num & ~i
        return i



i = Solution()
call = i.singleNumber([0, 1, 0, 1, 0, 1, 99])
print(":: ", call)
