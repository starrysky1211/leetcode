'''
Author: Zander
Description: Edit Here
Date: 2021-09-13 10:07:44
LastEditors: Zander
LastEditTime: 2021-09-13 10:16:25
FilePath: /python/64.最小路径和.py
'''
#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0]*n for _ in range(m)]
        # 边界条件：dp[0][0] = grid[0][0]
        # 状态转移方程1：若i=0，dp[i][j] = dp[i][j-1] + grid[i][j]
        # 状态转移方程2：若j=0，dp[i][j] = dp[i-1][j] + grid[i][j]
        # 状态转移方程3：dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
        return dp[-1][-1]
# @lc code=end

