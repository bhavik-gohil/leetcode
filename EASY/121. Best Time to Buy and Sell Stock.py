from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = 0
        # l = len(prices)
        # i = 1
        # price = prices[0]
        # while i < l:
        #     if price > prices[i]:
        #         price = prices[i]
        #     tmp = prices[i]-price
        #     profit = tmp if tmp > profit else profit
        #     i = i + 1
        profit = 0
        price = prices[0]
        for p in prices:
            if price > p:
                price = p
            tmp = p-price
            profit = tmp if tmp > profit else profit
        return profit


i = Solution()
call = i.maxProfit([7,1,5,3,6,4])
# call = i.maxProfit([7,6,4,3,1])
# call = i.maxProfit([1, 2])
print(":: ", call)
