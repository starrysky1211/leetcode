'''
Author: Zander
Description: Edit Here
Date: 2021-08-18 09:22:24
LastEditors: Zander
LastEditTime: 2021-08-18 12:15:19
FilePath: /python/392.判断子序列.py
'''
#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution: 
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        pointer, head = 0, 0
        while pointer < m and head < n:
            if t[head] == s[pointer]:
                pointer += 1
            head += 1
        return pointer == m
                
# @lc code=end

