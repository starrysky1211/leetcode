'''
Author: Zander
Description: Edit Here
Date: 2021-08-06 14:15:46
LastEditors: Zander
LastEditTime: 2021-08-06 15:34:57
FilePath: /python/101.对称二叉树.py
'''
#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isSym(l: TreeNode, r: TreeNode) -> bool:
            if not l and not r:
                return True
            if l and r and l.val == r.val:
                return isSym(l.left, r.right) and isSym(l.right, r.left)
            return False
        return isSym(root, root)
# @lc code=end

