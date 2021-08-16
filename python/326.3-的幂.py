'''
Author: Zander
Description: Edit Here
Date: 2021-08-16 11:06:18
LastEditors: Zander
LastEditTime: 2021-08-16 11:11:42
FilePath: /python/326.3-的幂.py
'''
#
# @lc app=leetcode.cn id=326 lang=python3
#
# [326] 3的幂
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467%n == 0 
# @lc code=end

