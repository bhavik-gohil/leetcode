from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums_len = len(nums)
        i =  nums_len - 1
        k = 0
        while i >= 0:
            if nums[i] == val:
                nums.pop(i)
                nums.append("_")
                k = k + 1
            i = i - 1
        return nums_len - k


ins = Solution()
call = ins.removeElement([0,1,2,2,3,0,4,2], 2)
print("call: ", call)
