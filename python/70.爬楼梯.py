'''
Author: Zander
Description: Edit Here
Date: 2021-08-06 10:53:20
LastEditors: Zander
LastEditTime: 2021-08-06 11:02:49
FilePath: /python/70.爬楼梯.py
'''
#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        last = 1
        curr = 2
        step = 2
        while step < n:
            last, curr = curr, last + curr
            step += 1
        return curr
# @lc code=end