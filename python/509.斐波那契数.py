'''
Author: Zander
Description: Edit Here
Date: 2021-08-31 11:49:09
LastEditors: Zander
LastEditTime: 2021-08-31 11:51:55
FilePath: /python/509.斐波那契数.py
'''
#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        res = [0 ,1]
        head = 1
        while head < n:
            res.append(res[-2] + res[-1])
            head += 1
        return res[-1]
# @lc code=end

