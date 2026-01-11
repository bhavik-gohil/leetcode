class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l1 = len(haystack)
        l2 = len(needle)
        i = 0
        while i < l1:
            if(haystack[i:i+l2]) == needle:
                return i
            i = i + 1
        return -1


ins = Solution()
call = ins.strStr("leetcode", "sad")
print("call: ", call)
