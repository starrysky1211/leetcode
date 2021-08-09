'''
Author: Zander
Description: Edit Here
Date: 2021-08-09 11:27:46
LastEditors: Zander
LastEditTime: 2021-08-09 11:43:58
FilePath: /python/112.路径总和.py
'''
#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root: return False
        if not root.left and not root.right and root.val != targetSum: return False
        if not root.left and not root.right and root.val == targetSum: return True
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
# @lc code=end

