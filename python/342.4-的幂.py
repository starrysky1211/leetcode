'''
Author: Zander
Description: Edit Here
Date: 2021-08-16 11:19:59
LastEditors: Zander
LastEditTime: 2021-08-16 11:24:21
FilePath: /python/342.4-的幂.py
'''
#
# @lc app=leetcode.cn id=342 lang=python3
#
# [342] 4的幂
#

# @lc code=start
import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and math.log10(n)/math.log10(4) % 1 < 2* 0.0001
# @lc code=end

