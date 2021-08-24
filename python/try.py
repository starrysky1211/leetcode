'''
Author: Zander
Description: Edit Here
Date: 2021-05-06 11:56:51
LastEditors: Zander
LastEditTime: 2021-08-20 15:41:12
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
    def isHappy(self, n: int) -> bool:
        # 探寻规律：4会回到4，2会回到4，3会回到4，5会回到4，6会回到4，7会回到1，8会回到4，9会回到4
        def getSum(num):
            res = 0
            while num > 0:
                num, head = divmod(num, 10)
                res += head**2
            return res
        while n >= 10:
            n = getSum(n)
        if n in [1, 7]:
            return True
        return False
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        # 遍历所有的排列组合
        origin = [0]*(10-turnedOn) + [1]*turnedOn
        poss = self.iterator(origin)
        res = []
        for i in poss:
            h = poss[:4]
            if self.list2binary(h) <= 12:
                res.append(self.binary260(self.list2binary(poss)))
        return res 
    def iterator(self, nums:List[int]):
        def backtrack(first = 0):
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first+1)
                nums[first], nums[i] = nums[i], nums[first]
        n = len(nums)
        res = []
        backtrack()
        return res   
    def binary260(self, num: int) -> str:
        # 二进制换算60进制
        h, t = divmod(num, 60)
        ts = str(t) if t>=10 else "0"+str(t)
        return str(h) + ":" + ts
    def list2binary(self, bl: List[int]) -> int:
        # binary to 10进制整数
        res = 0
        for i in range(len(bl)):
            if bl[-1-i]:
                res += 2**i
        return res
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited_land = []
        # 搜索到第一块陆地
        row, col = len(grid), len(grid[0])
        rs, cs = -1, -1
        for i in range(row):
            flag = 0
            for j in range(col):
                if grid[i][j]:
                    rs, cs = i, j
                    flag = 1
                    break
            if flag:
                break
        # 没有搜索到，直接返回0
        if rs == -1 and cs == -1:
            return 0
        stack =[[rs, cs]]
        visited_land.append([rs, cs])
        res = 0
        while len(stack) != 0:
            point = stack.pop()
            x, y = point
            if x == 0 or grid[x-1][y] == 0:
                # 上方为空，周长加一
                res += 1
            elif grid[x-1][y] == 1:
                # 上方为陆地，压入栈
                if [x-1, y] not in visited_land:
                    stack.append([x-1, y])
                    visited_land.append([x-1, y])
            if y == 0 or grid[x][y-1] == 0:
                # 左侧为空，周长加一
                res += 1
            elif grid[x][y-1] == 1:
                # 左侧为陆地，压入栈
                if [x, y-1] not in visited_land:
                    stack.append([x, y-1])
                    visited_land.append([x, y-1])
            if x == row - 1 or grid[x+1][y] == 0:
                # 下方为空，周长加一
                res += 1
            elif grid[x+1][y] == 1:
                # 下方为陆地，压入栈
                if [x+1, y] not in visited_land:
                    stack.append([x+1, y])
                    visited_land.append([x+1, y])
            if y == col - 1 or grid[x][y+1] == 0:
                # 右侧为空，周长加一
                res += 1
            elif grid[x][y+1] == 1:
                # 右侧为陆地，压入栈
                if [x, y+1] not in visited_land:
                    stack.append([x, y+1])
                    visited_land.append([x, y+1])
        return res
s = Solution()
data = [[1,1],[1,1]]
# res = s.islandPerimeter(data)
# print(res)
import numpy as np
A = np.array([[1, 0, 0, 0],[2, 0, 1, 0], [1, 0, 0, 1], [1, 0, 1, 0]])
A2 = np.linalg.matrix_power(A, 2)
A3 = np.linalg.matrix_power(A, 3)
A4 = np.linalg.matrix_power(A, 4)
print(1, A, A.sum(), np.diagonal(A).sum())
print(2, A2, A2.sum(), np.diagonal(A2).sum())
print(3, A3, A3.sum(), np.diagonal(A3).sum())
print(4, A4, A4.sum(), np.diagonal(A4).sum())
