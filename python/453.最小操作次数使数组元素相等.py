'''
Author: Zander
Description: Edit Here
Date: 2021-08-19 11:00:05
LastEditors: Zander
LastEditTime: 2021-08-19 11:12:02
FilePath: /python/453.最小操作次数使数组元素相等.py
'''
#
# @lc app=leetcode.cn id=453 lang=python3
#
# [453] 最小操作次数使数组元素相等
#

# @lc code=start
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        base = min(nums)
        res = 0
        for i in nums:
            res += i-base
        return res
# @lc code=end

