'''
Author: Zander
Description: Edit Here
Date: 2021-08-13 11:35:00
LastEditors: Zander
LastEditTime: 2021-08-13 11:38:19
FilePath: /python/258.各位相加.py
'''
#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return num
        return num%9 if num % 9 != 0 else 9
# @lc code=end

