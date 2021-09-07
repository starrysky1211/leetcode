'''
Author: Zander
Description: Edit Here
Date: 2021-09-07 09:25:00
LastEditors: Zander
LastEditTime: 2021-09-07 10:43:27
FilePath: /python/32.最长有效括号.py
'''
#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        # 使用一个长度为n的数组dp[i]表示以s[i]字符结尾的最长有效括号长度
        dp = [0]*n
        # 那么很明显，所有以'('结尾的长度一定是0，以')'结尾的字符串才有希望>0
        # 而且s.length<2时有效长度一定是0
        # 因此，我们可以取出最近的两个字符进行考虑
        # 状态转移方程1：
        ## if s[i-1]=='(' and s[i] == ')', 那么dp[i] = dp[i-2]+2
        ## if s[i-1]==')' and s[i] == ')', 那么就要考虑dp[i-1]的有效长度前的那个字符c = s[i-dp[i-1]-1]
        ### if c == ')' 那么dp[i]就为0，else c == '(' 那么dp[i] = dp[i-1]+2+dp[i-dp[i-1]-2]，此时注意index不能<0
        if n < 2:
            return 0
        for i in range(1,n):
            if s[i-1] == '(' and s[i] == ')':
                dp[i] = dp[i-2] + 2 if i>=2 else 2
            elif s[i-1] == ')' and s[i] == ')' and i-dp[i-1]>0 and s[i-dp[i-1]-1] == '(':
                dp[i] = dp[i-1] + 2 + (dp[i-dp[i-1]-2] if i-dp[i-1]>=2  else 0)
        return max(dp) 
# @lc code=end

