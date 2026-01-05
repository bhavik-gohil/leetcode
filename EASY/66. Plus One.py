from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits)
        i = 0
        s = ""
        while i < l:
            s = s + str(digits[i])
            i = i + 1
        return [int(i) for i in str(int(s)+1)]


ins = Solution()
call = ins.plusOne([9,9])
print("call: ", call)
