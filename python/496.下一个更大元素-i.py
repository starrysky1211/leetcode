'''
Author: Zander
Description: Edit Here
Date: 2021-08-20 12:21:11
LastEditors: Zander
LastEditTime: 2021-08-24 10:44:20
FilePath: /python/496.下一个更大元素-i.py
'''
#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        stack = []
        hashtable = {}
        for n in nums2:
            while len(stack) != 0 and stack[-1] < n:
                hashtable[stack.pop()] = n
            stack.append(n)
        
        for n in nums1:
            res.append(hashtable.get(n, -1))
        return res
# @lc code=end

