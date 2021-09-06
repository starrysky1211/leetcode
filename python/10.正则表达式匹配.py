'''
Author: Zander
Description: Edit Here
Date: 2021-09-03 11:39:55
LastEditors: Zander
LastEditTime: 2021-09-06 16:40:42
FilePath: /python/10.正则表达式匹配.py
'''
#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 初始化动态规划数组，dp[i][j]表示s[:i]与p[:j]的匹配关系，dp[0][0]表示两个空字符串的匹配，因此注意长度都要+1
        dp = [[False]*(len(p)+1) for _ in range(len(s)+1)]
        # 对于非'*'字符匹配的处理：都是一对一的，因此统一写一个函数来简化
        def match(i:int, j:int) -> bool:
            if i == 0:
                # 空字符，不可能匹配成功
                return False
            if p[j-1] == '.':
                # 匹配任意字符
                return True
            return s[i-1] == p[j-1]
        # 初始边界条件，两个空字符串一定相匹配
        dp[0][0] = True
        # 状态转移方程：
        ## 如果p[j]!="*"，显然直接比较即可 dp[i][j] = dp[i-1][j-1] and match(i,j)
        ## 如果p[j]=="*"，情况稍微复杂一些，首先需要比较的是s[i]和p[j-1]
        ### 如果 match(i, j-1)，那么有两种情况都可以导致dp[i][j]为真，
        #### 如果dp[i][j-2]即星号pattern出现之前可以匹配，那么当前星号表达式匹配字符出现次数为0，因此可以匹配
        #### 如果dp[i-1][j]即星号pattern上一次匹配成功，那么当前字符再次成功匹配
        ### 因此dp[i][j] = dp[i][j-2] or dp[i-1][j] if match[i, j-1] else dp[i][j-2]
        for i in range(len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] == '*':
                    dp[i][j] |= dp[i][j-2]
                    if match(i, j-1):
                        dp[i][j] |= dp[i-1][j]
                else:
                    if match(i, j):
                        dp[i][j] |= dp[i-1][j-1]
        return dp[len(s)][len(p)]
        
# @lc code=end

