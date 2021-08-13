'''
Author: Zander
Description: Edit Here
Date: 2021-08-13 11:45:57
LastEditors: Zander
LastEditTime: 2021-08-13 12:00:48
FilePath: /python/278.第一个错误的版本.py
'''
#
# @lc app=leetcode.cn id=278 lang=python3
#
# [278] 第一个错误的版本
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l <= r:
            mid = (l + r) // 2
            bad = isBadVersion(mid)
            if bad:
                r = mid - 1
            else:
                l = mid + 1
        return l
# @lc code=end

