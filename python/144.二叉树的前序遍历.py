'''
Author: Zander
Description: Edit Here
Date: 2021-08-10 11:24:14
LastEditors: Zander
LastEditTime: 2021-08-10 11:43:42
FilePath: /python/144.二叉树的前序遍历.py
'''
#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def traversal(root: TreeNode):
            if not root:
                return
            res.append(root.val)
            traversal(root.left)
            traversal(root.right)
        traversal(root)
        return res
# @lc code=end

