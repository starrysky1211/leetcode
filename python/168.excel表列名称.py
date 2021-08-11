'''
Author: Zander
Description: Edit Here
Date: 2021-08-11 09:38:21
LastEditors: Zander
LastEditTime: 2021-08-11 09:58:51
FilePath: /python/168.excel表列名称.py
'''
#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # 相当于26进制换算
        # 创建对应关系
        rela = {}
        for i in range(26):
            rela[i] = chr(ord('A')+i)
        rest = columnNumber
        res = ""
        while rest:
            rest, head = divmod(rest-1, 26)
            res = rela[head] + res
        return res
# @lc code=end

