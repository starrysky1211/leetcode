'''
Author: Zander
Description: Edit Here
Date: 2021-09-13 09:35:54
LastEditors: Zander
LastEditTime: 2021-09-13 09:46:12
FilePath: /python/62.不同路径.py
'''
#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        # 边界条件 第一行和第一列都是只有一条路径
        # 状态转移方程：dp[i][j] = dp[i-1][j] + dp[i][j-1]
        for i in range(m):
            for j in range(n):
                if i*j == 0:
                    # 满足边界条件
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
# @lc code=end

