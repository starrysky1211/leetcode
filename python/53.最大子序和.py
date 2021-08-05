'''
Author: Zander
Description: Edit Here
Date: 2021-08-05 11:27:56
LastEditors: Zander
LastEditTime: 2021-08-05 11:32:58
FilePath: /python/53.最大子序和.py
'''
#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        remain = nums[0]
        _max = remain
        for i in nums[1:]:
            remain = i + remain if remain > 0 else i
            _max = max(remain, _max)
        return _max
            
# @lc code=end

