from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h = {}
        l = len(nums)/2
        for i in nums:
            h[i] = h[i]+1 if h.get(i) else 1
            if  h[i]>=l:
                return i
        return 0




i = Solution()
call = i.majorityElement([2,2,1,1,1,2,2])
print(":: ", call)