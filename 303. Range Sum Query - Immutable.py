from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        nums.insert(0, 0)
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right+1] - self.nums[left] 


i = NumArray([-2, 0, 3, -5, 2, -1])
call = i.sumRange(0,2)
print("::", call)