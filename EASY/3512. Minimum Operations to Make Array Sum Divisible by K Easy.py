from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        sm = 0
        for n in nums:
            sm += n
        cnt = 0
        for n in nums:
            i = 0
            while sm % k != 0:
                n -= 1
                sm -= 1
                cnt += 1
                i += 1
            else:
                return cnt

        return cnt


i = Solution()
# call = i.minOperations([3, 9, 7], 5)
# call = i.minOperations([3, 2], 6)
# call = i.minOperations([8], 3)
call = i.minOperations([9, 18], 20)
print(":: ", call)
