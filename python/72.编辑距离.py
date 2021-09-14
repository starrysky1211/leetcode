'''
Author: Zander
Description: Edit Here
Date: 2021-09-13 10:16:49
LastEditors: Zander
LastEditTime: 2021-09-13 10:35:45
FilePath: /python/72.编辑距离.py
'''
#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 首先决定状态转移空间，我认为是一个m+1 * n+1的矩阵dp，其中dp[i][j]表示word1[:i]到word2[:j]的变换次数
        # 边界条件1：dp[0][0]表示空字符串之间的变换，因此为零
        # 边界条件2：dp[0][j]表示空字符串变成word2[:j]，因此=j
        # 边界条件3：dp[i][0]表示word1[:i]变成空字符串，因此=i
        m, n = len(word1), len(word2)
        dp = [[0]*(n+1) for i in range(m+1)]
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        # 状态转移方程1：dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]+1, dp[i-1][j-1]+1) if word1[i-1] == word2[j-1]
        # 状态转移方程2：dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1 if word1[i] != word2[j]
        ## 这表示可以通过一步操作达成——增加(dp[i][j-1])、删除(dp[i-1][j])、替换(dp[i-1][j-1])
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]+1, dp[i][j-1]+1)
                else:
                    dp[i][j] = min(dp[i-1][j-1]+1, dp[i-1][j]+1, dp[i][j-1]+1)
        return dp[-1][-1]
                    
# @lc code=end

