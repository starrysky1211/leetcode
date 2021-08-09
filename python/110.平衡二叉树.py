'''
Author: Zander
Description: Edit Here
Date: 2021-08-09 10:32:14
LastEditors: Zander
LastEditTime: 2021-08-09 10:57:05
FilePath: /python/110.平衡二叉树.py
'''
#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # 基本思路就是左右子树均为平衡二叉树且高度差不超过1
        def check(root: TreeNode) -> int:
            """
            return -1 说明不是平衡二叉树
            return n>=0 表示是深度为n的平衡二叉树
            """
            if not root: return 0
            left, right = check(root.left), check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1
        return check(root) != -1
# @lc code=end

