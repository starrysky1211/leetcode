'''
Author: Zander
Description: Edit Here
Date: 2021-08-13 11:12:10
LastEditors: Zander
LastEditTime: 2021-08-13 11:34:41
FilePath: /python/257.二叉树的所有路径.py
'''
#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        def dfs(root: TreeNode, path_list: List[str], ls: str):
            if not root.left and not root.right:
                res.append(ls + str(root.val))
            if root.left:
                dfs(root.left, path_list, ls+str(root.val)+"->")
            if root.right:
                dfs(root.right, path_list, ls+str(root.val)+"->")
        dfs(root, res, "")
        return res

# @lc code=end

