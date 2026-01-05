from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)
        middle = 0
        while start < end:
            middle = int((start+end)/2)
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                end = middle
            elif nums[middle] < target:
                start = middle + 1
        return middle + 1 if start != middle else middle


ins = Solution()
call = ins.searchInsert([1, 3, 5, 6], 4)
print("call: ", call)
