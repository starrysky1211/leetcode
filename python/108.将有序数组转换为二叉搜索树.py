'''
Author: Zander
Description: Edit Here
Date: 2021-08-09 10:08:32
LastEditors: Zander
LastEditTime: 2021-08-09 10:28:06
FilePath: /python/108.将有序数组转换为二叉搜索树.py
'''
#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0: return
        if len(nums) == 1: return TreeNode(val=nums[0])
        if len(nums) == 2: return TreeNode(val=nums[1], left=TreeNode(val=nums[0]))
        mid = len(nums) // 2
        root = TreeNode(val=nums[mid])
        root.left = self.sortedArrayToBST(nums[0:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
# @lc code=end

