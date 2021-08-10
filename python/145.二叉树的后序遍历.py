'''
Author: Zander
Description: Edit Here
Date: 2021-08-10 11:43:55
LastEditors: Zander
LastEditTime: 2021-08-10 11:46:02
FilePath: /python/145.二叉树的后序遍历.py
'''
#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def traversal(root: TreeNode):
            if not root: return
            traversal(root.left)
            traversal(root.right)
            res.append(root.val)
        traversal(root)
        return res
# @lc code=end

