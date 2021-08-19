'''
Author: Zander
Description: Edit Here
Date: 2021-08-19 09:44:24
LastEditors: Zander
LastEditTime: 2021-08-19 10:18:55
FilePath: /python/414.第三大的数.py
'''
#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#

# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = float('-inf')
        second = float('-inf')
        third = float('-inf')
        for i in nums:
            if i == first or i == second:
                continue
            if i > first:
                third, second, first = second, first, i
            elif i > second:
                third, second = second, i
            elif i > third:
                third = i
        if third != float('-inf'):
            return third
        return first
# @lc code=end

