'''
Author: Zander
Description: Edit Here
Date: 2021-08-20 11:54:48
LastEditors: Zander
LastEditTime: 2021-08-20 12:00:04
FilePath: /python/485.最大连续-1-的个数.py
'''
#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续 1 的个数
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max1, cur1 = 0, 0
        for n in nums:
            if n:
                cur1 += 1
            else:
                max1 = max(max1, cur1)
                cur1 = 0
        return max(max1, cur1)
# @lc code=end

