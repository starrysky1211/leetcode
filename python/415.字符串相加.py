'''
Author: Zander
Description: Edit Here
Date: 2021-08-19 10:19:21
LastEditors: Zander
LastEditTime: 2021-08-19 10:44:04
FilePath: /python/415.字符串相加.py
'''
#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        taker = 0
        res = []
        if len(num2) > len(num1):
            num1, num2 = num2, num1
        while len(num1)!=0 and len(num2)!=0:
            taker, head = divmod(int(num1[-1]) + int(num2[-1]) + taker, 10)
            res.append(str(head))
            num1, num2 = num1[:-1], num2[:-1]
        while len(num1)!=0:
            taker, head = divmod(int(num1[-1]) + taker, 10)
            res.append(str(head))
            num1 = num1[:-1]
        if taker:
            res.append(str(taker))
        return "".join(res[::-1])
# @lc code=end

