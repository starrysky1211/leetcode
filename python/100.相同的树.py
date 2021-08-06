'''
Author: Zander
Description: Edit Here
Date: 2021-08-06 12:14:10
LastEditors: Zander
LastEditTime: 2021-08-06 12:21:42
FilePath: /python/100.相同的树.py
'''
#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q
            
# @lc code=end

