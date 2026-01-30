class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        lenS = len(s)
        lenT = len(t)
        i = 0
        j = 0
        while i < lenT and j < lenS:
            if s[j] == t[i]:
                j += 1
            i += 1
        return j == lenS


i = Solution()
call = i.isSubsequence("axc", "ahbgdc")
print("::", call)
