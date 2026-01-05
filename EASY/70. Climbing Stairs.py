class Solution:
    def __init__(self):
        self.n_stairs_map = {}

    def get_n_stairs(self, n):
        if n < 3:
            return n
        else:
            if self.n_stairs_map.get(n):
                return self.n_stairs_map.get(n)
            sum = self.get_n_stairs(n - 1) + self.get_n_stairs(n - 2)
            self.n_stairs_map[n] = sum
            return sum

    def climbStairs(self, n: int) -> int:
        return self.get_n_stairs(n)


ins = Solution()
call = ins.climbStairs(44)
print("call: ", call)


# getN(n)
#    if n < 4
#      return n
#     else
#      x = n - 1
#       y = n - 2
#        sum = getN(x) + getN(y)
#         return sum

# getN(1)

# 1 = 1
# 2 = 1+1, 2
# 3 = 1+1+1, 1 = 2, 2+1,
# 4 = 1 1 1 1, 1 1 2, 1 2 1, 2 1 1, 2 2


# 1
# 1+1
# 1+1+1
# 1+1+1+1
# 1+1+1+1+1
# 1+1+1+1+1+1


# 2
# 2+2
# 2+2+2


# 1+2
# 2+1

# 1+1+2
# 1+2+1
# 2+1+1

# 1+1+1+2
# 1+1+2+1
# 1+2+1+1
# 2+1+1+1

# 1+1+2+2
# 1+2+1+2
# 2+1+1+2
