class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            bit = n % 2
            count += bit
            n = n >> 1
        return count


i = Solution()
call = i.hammingWeight(2147483645)
print(":: ", call)
