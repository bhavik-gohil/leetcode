from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hs = {}
        for i in range(0, len(nums)):
            if hs.get(nums[i]):
                hs[nums[i]].append(i)
                for x in range(1, len(hs[nums[i]])):
                    if abs(hs[nums[i]][x] - hs[nums[i]][x-1])<=k:
                        return True
            else:
                hs[nums[i]] = [i]
        return False


i = Solution()
call = i.containsNearbyDuplicate([1, 2, 3, 1], 3)
print(":: ", call)
