from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        ln = len(s)
        i = ln
        while i > 0:
            s.insert(i, (s[0]))
            del s[0]
            i -= 1
        return s


i = Solution()
call = i.reverseString(["h", "e", "l", "l", "o"])
print("::", call)
