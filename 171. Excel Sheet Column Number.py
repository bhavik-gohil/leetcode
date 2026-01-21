class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        cnt = 0
        for i in range(0, len(columnTitle)-1):
            cnt += (ord(columnTitle[i])-64)*26/(cnt%26)
            print(cnt, (ord(columnTitle[i])-64)*26,
                  ord(columnTitle[i])-64, ord(columnTitle[i]))

        cnt += (ord(columnTitle[-1])-64)
        return cnt


i = Solution()
call = i.titleToNumber("FXSHRXW")
print(":: ", call)
