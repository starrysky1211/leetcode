'''
Author: Zander
Description: Edit Here
Date: 2021-08-24 11:06:01
LastEditors: Zander
LastEditTime: 2021-08-31 11:10:58
FilePath: /python/501.二叉搜索树中的众数.py
'''
#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def findMode(self, root: TreeNode) -> List[int]:
        self.current, self.mode, self.currentCount, self.maxCount= float('-inf'),[float('-inf')],0,0
        self.dfs(root)
        if self.maxCount < self.currentCount:
                self.mode, self.maxCount = [self.current], self.currentCount
        elif self.maxCount == self.currentCount:
            self.mode.append(self.current)
        return self.mode
    def dfs(self, root):
        if not root: return
        self.dfs(root.left)
        if self.current == root.val:
            self.currentCount += 1
        else:
            if self.maxCount < self.currentCount:
                self.mode, self.maxCount = [self.current], self.currentCount
            elif self.maxCount == self.currentCount:
                self.mode.append(self.current)
            self.current = root.val
            self.currentCount = 1
        self.dfs(root.right)
    
# @lc code=end

