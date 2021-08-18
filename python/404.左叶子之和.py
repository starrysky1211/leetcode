'''
Author: Zander
Description: Edit Here
Date: 2021-08-18 14:58:13
LastEditors: Zander
LastEditTime: 2021-08-18 15:12:40
FilePath: /python/404.左叶子之和.py
'''
#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        stack = [[root, 0]]
        res = 0
        while len(stack)!=0:
            node, t = stack.pop() # 0 表示根节点，1表示右支，-1表示左支
            if not node.left and not node.right and t == -1:
                # 左叶子
                res += node.val
            if node.left:
                stack.append([node.left, -1])
            if node.right:
                stack.append([node.right,1])
        return res
# @lc code=end

