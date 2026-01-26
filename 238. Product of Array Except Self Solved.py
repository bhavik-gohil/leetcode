from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ln = len(nums)
        products = [1]+nums
        for i in range(1, ln+1):
            products[i] = products[i-1]*products[i]
        del products[0]

        product = 1
        i = ln-1
        while i > 0:
            products[i] = products[i-1]*product
            product *= nums[i]
            i -= 1
        products[0] = product
        return products


i = Solution()
# call = i.productExceptSelf([-1, 1, 0, -3, 3])
call = i.productExceptSelf([4,3,2,1,2])
print("::", call)

# 1, 2, 3, 4
# 24 12 8  6

# 24/1=24
# 24/2=12
# 24/3=8
# 24/4=6


# 1, 2, 3, 4
# l 1, 2,

# 1,   2,  3,  4,  5      =n
# 1,   2,  6,  24, 120    =p

# 120, 60, 40, 30, 24

# product = 1
# i=len-1

# p[i+1] = p[i]*product = 24*1 = 24


# i=len

# i=4
# product=1
# p[i] = p[i-1]*product = 24*1 = 24
# product=num[i]*product=5*1=5

# i=3
# product=5
# p[i] = p[i-1]*product = 6*5 = 30
# product=num[i]*product=4*5=20

# i=2
# product=20
# p[i] = p[i-1]*product = 2*20 = 40

# i=1
# product=20
# p[i] = p[i-1]*product = 2*20 = 40
