class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        i = 0
        j = 0
        cur = ""
        prev = 0
        while j < l:
            if s[j] in cur:
                length = len(cur)
                if length > prev:
                    prev = length
                cur = ""
                i = i + 1
                j = i
            else:
                cur = cur + s[j]
                j = j + 1
        length = len(cur)
        return prev if prev > length else length

i = Solution()
# call = i.lengthOfLongestSubstring(
#     "fujvlcixlcmjaqqpujyzdowlqzghjfkpbtmoyuljwzszskoounnzbmmtltdv")
call = i.lengthOfLongestSubstring(
    "aab")
print(":: ", call)
