'''
Author: Zander
Description: Edit Here
Date: 2021-08-19 11:12:15
LastEditors: Zander
LastEditTime: 2021-08-19 11:24:36
FilePath: /python/455.分发饼干.py
'''
#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        head = 0
        count = 0
        length = len(g)
        for i in s:
            if head == length:
                break
            if g[head] <= i:
                head += 1
                count += 1
        return count
# @lc code=end

