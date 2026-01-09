class Solution:
    def isHappy(self, n: int) -> bool:
        h = {}
        num_hash = {}
        while n != 1:
            ar = list(str(n))
            tmp = 0
            for i in ar:
                tmp += pow(int(i), 2)
            if h.get(tmp):
                return False
            n = tmp
            h[n] = 1
        return True


i = Solution()
call = i.isHappy(8)
print(":: ", call)

