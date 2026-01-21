from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # ln = len(nums)+1
        # for i in range(0, ln):
        #     if i not in nums:
        #         return i
        # return
        ln = len(nums)-1
        i = 0
        x 
        while i < ln:
            if nums[i] < nums[i+1]:
                nums[i] = nums[i]+nums[i+1]
                nums[i+1] = nums[i+1]-nums[i]
            i += 1

        return nums


i = Solution()
call = i.missingNumber([9,6,4,2,3,5,7,0,1])
print(":: ", call)
