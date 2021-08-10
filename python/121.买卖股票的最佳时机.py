'''
Author: Zander
Description: Edit Here
Date: 2021-08-09 12:18:23
LastEditors: Zander
LastEditTime: 2021-08-10 10:17:32
FilePath: /python/121.买卖股票的最佳时机.py
'''
#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        # 普通解法
        maxProfit = 0
        minPrice = float('inf')
        for i in prices:
            minPrice = min(i, minPrice)
            maxProfit = max(maxProfit, i-minPrice)
        return maxProfit
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0: return 0
        dp = [0] * n
        minPrice = prices[0]
        for i in range(1, n):
            minPrice = min(prices[i], minPrice)
            dp[i] = max(dp[i-1], prices[i]-minPrice)
        return dp[-1]
# @lc code=end

