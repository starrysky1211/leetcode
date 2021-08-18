'''
Author: Zander
Description: Edit Here
Date: 2021-08-17 10:59:21
LastEditors: Zander
LastEditTime: 2021-08-17 11:23:38
FilePath: /python/367.有效的完全平方数.py
'''
#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 0: return False
        x, i = 0, 1
        while x < num:
            x += i
            i += 2
        return x == num
# @lc code=end

