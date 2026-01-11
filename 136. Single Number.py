from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        tmp = 0
        for i in nums:
            tmp ^= i
        return tmp


i = Solution()
call = i.singleNumber([2, 2, 1])
print(":: ", call)
