'''
Author: Zander
Description: Edit Here
Date: 2021-08-19 10:57:15
LastEditors: Zander
LastEditTime: 2021-08-19 10:59:45
FilePath: /python/448.找到所有数组中消失的数字.py
'''
#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(range(1, len(nums)+1)) - set(nums))
# @lc code=end

