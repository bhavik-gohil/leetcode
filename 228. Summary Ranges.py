from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l = len(nums)
        i = 0
        result = []

        mem = nums[0]
        i = 1
        while i < l-1:
            cur = nums[i]
            prev = nums[i-1]
            next = nums[i+1]

            if cur == next-1:
                

        return result


i = Solution()
call = i.summaryRanges([0, 2, 3, 4, 6, 8, 9])
print(":: ", call)
