from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        tmp = 0
        i = 0
        l = len(nums)
        while i < l:
            print("-", i, i+1, tmp)
            tmp = nums[i] ^ (nums[i+1] if i+1 < l else tmp)
            i += 2
        return tmp


i = Solution()
call = i.singleNumber([4,1,2,1,2])
print(":: ", call)
