'''
Author: Zander
Description: Edit Here
Date: 2021-08-20 12:12:11
LastEditors: Zander
LastEditTime: 2021-08-20 12:18:47
FilePath: /python/495.提莫攻击.py
'''
#
# @lc app=leetcode.cn id=495 lang=python3
#
# [495] 提莫攻击
#

# @lc code=start
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not len(timeSeries):
            return 0
        clear = res = 0
        for t in timeSeries:
            if t < clear:
                res += t+duration-clear
            else:
                res += duration
            clear = t + duration
        return res 
# @lc code=end

