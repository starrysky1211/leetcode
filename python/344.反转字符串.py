'''
Author: Zander
Description: Edit Here
Date: 2021-08-16 11:24:45
LastEditors: Zander
LastEditTime: 2021-08-16 11:32:32
FilePath: /python/344.反转字符串.py
'''
#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        mid = l//2 - 1
        while mid >= 0:
            s[mid], s[l-1-mid] = s[l-1-mid], s[mid]
            mid -= 1
        
# @lc code=end

