'''
Author: Zander
Description: Edit Here
Date: 2021-08-12 11:03:05
LastEditors: Zander
LastEditTime: 2021-08-12 11:16:47
FilePath: /python/219.存在重复元素-ii.py
'''
#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for i, num in enumerate(nums):
            record = hashmap.get(num)
            if not record is None and i - record <= k:
                    return True
            hashmap[num] = i
        return False
# @lc code=end

