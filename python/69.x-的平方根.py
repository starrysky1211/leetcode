'''
Author: Zander
Description: Edit Here
Date: 2021-08-06 10:08:24
LastEditors: Zander
LastEditTime: 2021-08-06 10:42:42
FilePath: /python/69.x-的平方根.py
'''
#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        if x == 1:
            return 1
        while l < r-1:
            mid = (l + r) // 2
            sq = mid * mid
            if sq == x:
                return mid
            if sq < x:
                l = mid
            if sq > x:
                r = mid
        return l
# @lc code=end

