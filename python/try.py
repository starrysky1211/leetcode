'''
Author: Zander
Description: Edit Here
Date: 2021-05-06 11:56:51
LastEditors: Zander
LastEditTime: 2021-08-10 10:58:28
FilePath: /python/try.py
'''
# -*- coding:utf-8 -*-
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        taker = 0
        taker, end =divmod(digits[-1] + 1 , 10)
        digits[-1] = end
        length = len(digits)
        if length > 1:
            for i in range(length-2, -1, -1):
                taker, end =divmod(digits[i] + taker , 10)
                digits[i] = end
        if taker:
            digits = [1] + digits
        return digits
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        head = 0
        for i in range(n):
            num2 = nums2[i]
            for j in range(head, m+n):
                num1 = nums1[j]
                if num2 <= num1:
                    nums1[j:] = [num2] + nums1[j:-1]
                    head = j
                    break
                if j == m + i:
                    nums1[j:] = nums2[i:]
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if root is None:
            return res
        stack = [root]
        while len(stack):
            head = stack.pop()
            if(head.left):
                stack.append(head)
                stack.append(head.left)
                head.left = None
            else:
                res.append(head.val)
                if head.right:
                    stack.append(head.right)
        return res
    def isPalindrome(self, s: str) -> bool:
        # 预处理，变成无空格和标点的小写字符串
        ls = ""
        for c in s:
            if str.isalnum(c):
                ls += c.lower()
        # 判断回文
        mid, tag = divmod(len(ls), 2)
        if tag:
            # 奇数，中间值index是mid为对称轴
            for i in range(mid):
                if ls[i] != ls[-i-1]:
                    return False
        else:
            # 偶数，中间值index是mid-1和mid必须相等
            for i in range(mid):
                if ls[i] != ls[-i-1]:
                    return False
        return True


s = Solution()
data = "A man, a plan, a canal: Panama"
res = s.isPalindrome(data)
print(res)