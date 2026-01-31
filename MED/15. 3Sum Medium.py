from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        idxs = []

        for i, n in enumerate(nums):
            if i > 0 and nums[i-1] == n:
                continue

            j = i+1
            k = len(nums)-1

            while j < k:
                three_sum = n + nums[j] + nums[k]
                if three_sum > 0:
                    k -= 1
                elif three_sum < 0:
                    j += 1
                else:
                    idxs.append([n, nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1

        return idxs


i = Solution()
call = i.threeSum([-1, 0, 1, 2, -1, -4])
print("::", call)
