'''
Author: Zander
Description: Edit Here
Date: 2021-08-13 11:41:56
LastEditors: Zander
LastEditTime: 2021-08-13 11:44:34
FilePath: /python/268.丢失的数字.py
'''
#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 丢失的数字
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return (n+1)*n//2 - sum(nums)
# @lc code=end

