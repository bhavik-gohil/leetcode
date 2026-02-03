from typing import List


# class Solution:
#     def minimumOperations(self, nums: List[int]) -> int:
#         cnt=0
#         for n in nums:
#             mod=n%3
#             print(n, mod)
#             if mod!=0:
#                 i=1
#                 while n%3!=0:
#                     n = n-1 if mod==2 else n+1
#                     if n%3:
#                         cnt+=1
#                     i+=1
#         return cnt
    
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt=0
        for n in nums:
            mod=n%3
            if mod!=0:
                cnt+=1
        return cnt
    
i = Solution()
call = i.minimumOperations([1,2,3,4])
print(":: ", call)