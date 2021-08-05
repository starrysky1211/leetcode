'''
Author: Zander
Description: Edit Here
Date: 2021-08-05 12:02:42
LastEditors: Zander
LastEditTime: 2021-08-05 14:25:15
FilePath: /python/67.二进制求和.py
'''
#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        taker = 0
        res = ""
        while len(a)*len(b) != 0:
            ha = int(a[-1])
            hb = int(b[-1])
            a, b = a[:-1], b[:-1]
            taker, end = divmod(ha+hb+taker, 2)
            res = str(end) + res
        while len(a) != 0:
            ha = int(a[-1])
            a = a[:-1]
            taker, end = divmod(ha + taker, 2)
            res = str(end) + res
        while len(b) != 0:
            hb = int(b[-1])
            b = b[:-1]
            taker, end = divmod(hb + taker, 2)
            res = str(end) + res
        if taker:
            res = "1" + res
        return res
            
# @lc code=end

