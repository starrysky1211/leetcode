'''
Author: Zander
Description: Edit Here
Date: 2021-09-08 10:30:25
LastEditors: Zander
LastEditTime: 2021-09-09 11:24:50
FilePath: /python/44.通配符匹配.py
'''
#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        # 创建一个存储动态计算结果的二维数组
        dp = [[False]*(n+1) for _ in range(m+1)]
        # 边界条件1-空字符串互相匹配
        dp[0][0] = True
        # 边界条件2-*匹配任意字符串
        for j in range(n):
            if p[j] == '*':
                dp[0][j+1] = True
            else:
                break
        # 开始状态转移
        for i in range(m):
            for j in range(n):
                if p[j] != '*':
                    dp[i+1][j+1] = dp[i][j] and (p[j] == '?' or s[i] == p[j])
                else:
                    dp[i+1][j+1] = dp[i][j+1] or dp[i+1][j]
        return dp[m][n]
# @lc code=end

