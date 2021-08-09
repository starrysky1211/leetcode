'''
Author: Zander
Description: Edit Here
Date: 2021-08-09 10:05:59
LastEditors: Zander
LastEditTime: 2021-08-09 10:08:07
FilePath: /python/104.二叉树的最大深度.py
'''
#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        if not root.right and not root.left : return 1
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
# @lc code=end

