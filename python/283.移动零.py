'''
Author: Zander
Description: Edit Here
Date: 2021-08-13 12:05:13
LastEditors: Zander
LastEditTime: 2021-08-13 12:12:38
FilePath: /python/283.移动零.py
'''
#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero], nums[i] = nums[i], nums[zero]
                zero += 1
        
# @lc code=end

