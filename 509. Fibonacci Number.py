class Solution:
    def fib(self, n: int) -> int:
        hs = {}
        def f(x):
            if x < 2:
                return x
            if hs.get(x):
                return hs[x]
            z = f(x-1) + f(x-2)
            hs[x]=z
            return z
        return f(n)


i = Solution()
call = i.fib(6)
print(":: ", call)

# 0, 1, 1, 2, 3, 5, 8, 13

# 2=1
