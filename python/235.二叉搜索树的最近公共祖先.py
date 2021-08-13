'''
Author: Zander
Description: Edit Here
Date: 2021-08-13 10:24:10
LastEditors: Zander
LastEditTime: 2021-08-13 10:51:23
FilePath: /python/235.二叉搜索树的最近公共祖先.py
'''
#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 确保p，q的顺序
        if q.val < p.val: p, q = q, p
        if root.val < p.val:
            # p, q均在右侧
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
# @lc code=end

