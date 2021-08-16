'''
Author: Zander
Description: Edit Here
Date: 2021-08-16 10:48:11
LastEditors: Zander
LastEditTime: 2021-08-16 10:57:29
FilePath: /python/292.nim-游戏.py
'''
#
# @lc app=leetcode.cn id=292 lang=python3
#
# [292] Nim 游戏
#

# @lc code=start
class Solution:
    def canWinNim(self, n: int) -> bool:
        return n%4 != 0
    def canWinNim2(self, n: int) -> bool:
        return n&3 != 0
# @lc code=end

