'''
Author: Zander
Description: Edit Here
Date: 2021-08-19 12:00:44
LastEditors: Zander
LastEditTime: 2021-08-19 12:23:34
FilePath: /python/461.汉明距离.py
'''
#
# @lc app=leetcode.cn id=461 lang=python3
#
# [461] 汉明距离
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = x^y
        return "{0:b}".format(res).count('1')
# @lc code=end

