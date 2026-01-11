import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # i = 0
        # j = len(s)-1
        # while i <= j:
        #     if not s[i].isalnum():
        #         i = i + 1
        #         continue
        #     if not s[j].isalnum():
        #         j = j - 1
        #         continue
        #     if s[i].lower() != s[j].lower():
        #         return False
        #     i = i + 1
        #     j = j - 1
        # return True
        str1 = "".join([i for i in s if i.isalnum()]).lower()
        return str1 == str1[::-1]


i = Solution()
call = i.isPalindrome("0P")
print(":: ", call)
