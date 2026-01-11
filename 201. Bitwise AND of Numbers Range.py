class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:

        shift = 0
        while left < right:
            left = left >> 1
            right = right >> 1
            shift += 1
        return left << shift


i = Solution()
call = i.rangeBitwiseAnd(2, 6)
# call = i.rangeBitwiseAnd(5, 7)
print(":: ", call)


101
111
