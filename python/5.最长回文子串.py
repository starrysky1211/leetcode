'''
Author: Zander
Description: Edit Here
Date: 2021-09-01 17:18:12
LastEditors: Zander
LastEditTime: 2021-09-03 11:39:50
FilePath: /python/5.最长回文子串.py
'''
#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        begin, maxlength = 0,0
        # 边界条件1，长度为1的天然回文，因此对角线为1
        # 边界条件2，所以需要在边界条件中添加dp[i][i+1] = s[i]==s[i+1]
        dp = [[0]*l for _ in range(l)]
        # 转移方程 dp[i][j] = dp[i+1][j-1] && s[i] == s[j] 需要注意(0,2->1,1)√ (0,1->1,0)x，所以需要在边界条件中添加dp[i][i+1] = s[i]==s[i+1]
        for L in range(1, l+1):
            # L 表示字符串长度
            for i in range(l):
                # j - i + 1 = L
                j = L + i - 1
                if j >= l:
                    break
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        # 触发边界条件
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                # 更新最长纪录
                if dp[i][j] and j-i+1 > maxlength:
                    begin, maxlength = i, j-i+1
        
        return s[begin:begin+maxlength]
# @lc code=end

