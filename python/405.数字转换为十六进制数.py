'''
Author: Zander
Description: Edit Here
Date: 2021-08-18 15:12:55
LastEditors: Zander
LastEditTime: 2021-08-18 15:23:15
FilePath: /python/405.数字转换为十六进制数.py
'''
#
# @lc app=leetcode.cn id=405 lang=python3
#
# [405] 数字转换为十六进制数
#

# @lc code=start
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0: return "0"
        s = '0123456789abcdef'
        res = []
        num = num & 0xffffffff
        while num > 0:
            res.append(s[num & 0xf])
            num >>= 4
        return "".join(res[::-1])
# @lc code=end

