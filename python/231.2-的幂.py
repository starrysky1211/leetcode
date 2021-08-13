'''
Author: Zander
Description: Edit Here
Date: 2021-08-12 11:47:50
LastEditors: Zander
LastEditTime: 2021-08-12 11:50:57
FilePath: /python/231.2-的幂.py
'''
#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2 的幂
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        taker = 0
        while taker == 0 and n > 1:
            n, taker = divmod(n, 2)
        return taker == 0
# @lc code=end

