class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l, r = 0, 1

        maxProfit = 0

        while l < r and r < len(prices):
            profit = prices[r] - prices[l]

            if profit >= 0:
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1
        return maxProfit
            


        #attempt 1
        #O(n^2)
        # maxProfit = 0
        # for i in range(len(prices) - 1):
        #     for j in range(i + 1, len(prices)):
        #         profit = prices[j] - prices[i]
        #         if profit >= 0:
        #             maxProfit = max(maxProfit, profit)
                
        # return maxProfit

