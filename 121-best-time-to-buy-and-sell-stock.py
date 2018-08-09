class Solution1(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # no need to get which day to buy and sell, just need the money, we can use the DP solution and it's O(n)
        if len(prices) <= 1:
            return 0
        dif = [prices[i+1] - prices[i] for i in range(len(prices)-1)]
        # now we change it to maxSubArray problem
        for i in range(1, len(dif)):
            if dif[i-1] > 0:
                dif[i] += dif[i-1]
        return max(max(dif), 0)
# beats 7.64% mainly beacuse I have traversal the list twice, there is a way that only do traversal once


class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # max() is very slow and we can use less compare operation. 
        # just remember the max profit with recording cheapest day is OK. no need to traversal twice
        re = 0
        low = float('inf')
        for i in prices:
            dif = i-low
            if dif < 0:
                low = i
            elif dif > re:
                re = dif
        return re
