'''
Author: Zander
Description: Edit Here
Date: 2021-09-13 09:47:22
LastEditors: Zander
LastEditTime: 2021-09-13 10:06:58
FilePath: /python/63.不同路径-ii.py
'''
#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        # 边界条件1：第一行(列)遇到障碍之前都是1，遇到障碍之后都是0
        # 边界条件2：每一个有障碍的地方都是0
        taker = 1
        for i in range(m):
            # 第一列
            if obstacleGrid[i][0]:
                taker = 0
            dp[i][0] = taker
        taker = 1
        for i in range(n):
            # 第一行
            if obstacleGrid[0][i]:
                taker = 0
            dp[0][i] = taker
        # 状态转移方程1：若是障碍，dp[i][j] = 0
        # 状态转移方程2：若不是障碍，dp[i][j] = dp[i-1][j] + dp[i][j-1]
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
# @lc code=end

