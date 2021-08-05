'''
Author: Zander
Description: Edit Here
Date: 2021-08-05 11:38:06
LastEditors: Zander
LastEditTime: 2021-08-05 12:02:03
FilePath: /python/66.加一.py
'''
#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        taker = 0
        taker, end =divmod(digits[-1] + 1 , 10)
        digits[-1] = end
        length = len(digits)
        if length > 1:
            for i in range(length-2, -1, -1):
                taker, end =divmod(digits[i] + taker , 10)
                digits[i] = end
        if taker:
            digits = [1] + digits
        return digits
            
# @lc code=end

