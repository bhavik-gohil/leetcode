from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hs = {}
        ln = len(numbers)
        i = 0
        while i < ln:
            if hs.get(target-numbers[i]) is not None:
                return [hs.get(target-numbers[i]), i]
            hs[numbers[i]] = i
            i += 1
        return


i = Solution()
# call = i.twoSum([3, 2, 4], 6)
call = i.twoSum([2, 7, 11, 15], 9)
print("::", call)
