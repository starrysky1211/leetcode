'''
Author: Zander
Description: Edit Here
Date: 2021-08-12 11:38:03
LastEditors: Zander
LastEditTime: 2021-08-12 11:47:35
FilePath: /python/228.汇总区间.py
'''
#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # 若当前数与上一数的差>1，则新开一个区间
        # 若当前数与上一数的差<=1，则延展当前区间
        last = float('-inf')
        res = []
        for num in nums:
            if num - last > 1:
                res.append(str(num))
            else:
                res[-1] = res[-1].split("->")[0] + "->" + str(num)
            last = num
        return res
# @lc code=end

