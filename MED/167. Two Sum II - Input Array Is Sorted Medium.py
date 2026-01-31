from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            if numbers[i] + numbers[j] > target:
                j-=1
            else:
                i+=1
        return


i = Solution()
call = i.twoSum([2, 7, 11, 15], 9)
# call = i.twoSum([-1,0], -1)
# call = i.twoSum([5, 25, 75], 100)
print("::", call)
