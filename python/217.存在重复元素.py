'''
Author: Zander
Description: Edit Here
Date: 2021-08-12 11:01:38
LastEditors: Zander
LastEditTime: 2021-08-12 11:02:14
FilePath: /python/217.存在重复元素.py
'''
#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
# @lc code=end

