from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        i = l-1
        while i > 0:
            if nums[i] == nums[i-1]:
                nums.pop(i)
                l = l - 1
            i = i - 1
        return l


ins = Solution()
call = ins.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
print("call", call)
