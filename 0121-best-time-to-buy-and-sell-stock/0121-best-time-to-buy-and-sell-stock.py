class Solution(object):
    def maxProfit(self, prices):
       n=len(prices)
       min_price=float("inf")
       profit=0
       for i in range(0,n):

        min_price=min(min_price,prices[i])
        profit=max(profit,prices[i]-min_price)
       return profit
       