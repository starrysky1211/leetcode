'''
Author: Zander
Description: Edit Here
Date: 2021-08-19 10:47:17
LastEditors: Zander
LastEditTime: 2021-08-19 10:57:07
FilePath: /python/441.排列硬币.py
'''
#
# @lc app=leetcode.cn id=441 lang=python3
#
# [441] 排列硬币
#

# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((-1 + (1 + 8*n)**0.5)//2)
# @lc code=end

