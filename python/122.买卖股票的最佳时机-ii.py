'''
Author: Zander
Description: Edit Here
Date: 2021-08-10 10:18:06
LastEditors: Zander
LastEditTime: 2021-08-10 10:42:03
FilePath: /python/122.买卖股票的最佳时机-ii.py
'''
#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        # 贪心, 只要上涨都要买
        profit = 0
        head = prices[0]
        for price in prices[1:]:
            profit = profit + price-head if price - head > 0 else profit
            head = price
        return profit
    def maxProfit(self, prices: List[int]) -> int:
        # 动态规划
        """
        这道题的动态规划思路和上道题不一样的地方在于操作的次数增加了：
            上道题只需要比较上一步操作的最佳值和本次操作的结果值作为本步操作的最佳值
            这道题出现了之前操作已经结束并且开始第二次操作的可能，因此最佳状态有两种：
                一种是本步不持有可达成的最佳状态，有两种达成方式：
                    上一步就没有持有，这一步继续不持有
                    上一步持有，这一步卖出
                一种是本步持有可达成的最佳状态，有两种达成方式：
                    上一步持有，这一步继续持有
                    上一步不持有，这一步增持
        """
        dp = [0, -1*prices[0]] # 第一个元素表示不持有的状态，第二个元素表示持有的状态
        for price in prices[1:]:
            dp = [
                max(dp[0], dp[1] + price),
                max(dp[1], dp[0] - price)
            ]
        return dp[0]
# @lc code=end

