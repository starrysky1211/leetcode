'''
Author: Zander
Description: Edit Here
Date: 2021-08-11 10:00:12
LastEditors: Zander
LastEditTime: 2021-08-11 10:24:51
FilePath: /python/169.多数元素.py
'''
#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 摩尔投票法
        count = 0
        candidate = None
        for i in nums:
            if count == 0:
                candidate = i
                count += 1
            else:
                if candidate != i:
                    count -= 1
                else:
                    count += 1
        return candidate
# @lc code=end

