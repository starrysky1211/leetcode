'''
Author: Zander
Description: Edit Here
Date: 2021-08-16 11:43:54
LastEditors: Zander
LastEditTime: 2021-08-16 11:46:00
FilePath: /python/349.两个数组的交集.py
'''
#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
# @lc code=end

