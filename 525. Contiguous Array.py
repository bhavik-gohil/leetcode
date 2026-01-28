from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ones = 0
        zeros = 0
        ln = 0
        hs = {}
        for i in range(len(nums)):
            if nums[i] == 1:
                ones += 1
            else:
                zeros += 1

            diff = zeros-ones
            if diff == 0:
                ln = ln if ln > i+1 else i+1
            else:
                if hs.get(diff) is not None:
                    tmp = i - hs.get(diff)
                    ln = ln if ln > tmp else tmp
                else:
                    hs[diff] = i
        return ln


i = Solution()
# call = i.findMaxLength([0, 1, 1, 1, 1, 1, 0, 0, 0])
# call = i.findMaxLength([0, 1])
# call = i.findMaxLength([0, 1, 1])
# call = i.findMaxLength([0, 1, 0, 1])
call = i.findMaxLength([0, 0, 1])
print("::", call)
