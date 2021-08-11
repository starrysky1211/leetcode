'''
Author: Zander
Description: Edit Here
Date: 2021-08-11 09:24:23
LastEditors: Zander
LastEditTime: 2021-08-11 09:35:20
FilePath: /python/167.两数之和-ii-输入有序数组.py
'''
#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target: return [l+1, r+1]
            elif s < target: l += 1
            else: r -= 1
        
# @lc code=end

