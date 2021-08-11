'''
Author: Zander
Description: Edit Here
Date: 2021-08-11 10:30:11
LastEditors: Zander
LastEditTime: 2021-08-11 10:33:13
FilePath: /python/171.excel-表列序号.py
'''
#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel 表列序号
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        rela = {}
        for i in range(26):
            rela[chr(ord('A')+i)] = i+1
        res = 0
        for j in range(len(columnTitle)):
            c = columnTitle[-j-1]
            res += rela[c]*26**j
        return res
# @lc code=end

