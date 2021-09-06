'''
Author: Zander
Description: Edit Here
Date: 2021-09-01 11:19:48
LastEditors: Zander
LastEditTime: 2021-09-01 17:17:16
FilePath: /python/521.最长特殊序列-ⅰ.py
'''
#
# @lc app=leetcode.cn id=521 lang=python3
#
# [521] 最长特殊序列 Ⅰ
#

# @lc code=start
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a != b:
            return max(len(a), len(b))
        return -1
# @lc code=end

