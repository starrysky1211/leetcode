class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # we need to remember the index where we begin a new count of profit(which means (index-1)'s profit is negative)
        profit = 0
        for i in range(1, len(prices)):
            dif = prices[i] - prices[i - 1]
            if dif > 0:
                profit += dif
        return profit
