'''
Author: Zander
Description: Edit Here
Date: 2021-08-10 11:01:20
LastEditors: Zander
LastEditTime: 2021-08-10 11:08:35
FilePath: /python/136.只出现一次的数字.py
'''
#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        taker = nums[0]
        for num in nums[1:]:
            taker ^= num
        return taker
# @lc code=end

