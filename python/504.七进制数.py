'''
Author: Zander
Description: Edit Here
Date: 2021-08-31 11:11:39
LastEditors: Zander
LastEditTime: 2021-08-31 11:17:41
FilePath: /python/504.七进制数.py
'''
#
# @lc app=leetcode.cn id=504 lang=python3
#
# [504] 七进制数
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        res = ''
        taker = '' if num > 0 else '-'
        num = abs(num)
        while num:
            num, lef = divmod(num, 7)
            res += str(lef)
        return taker + res[::-1]
# @lc code=end

