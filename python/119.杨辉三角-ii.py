'''
Author: Zander
Description: Edit Here
Date: 2021-08-09 11:56:48
LastEditors: Zander
LastEditTime: 2021-08-09 12:17:30
FilePath: /python/119.杨辉三角-ii.py
'''
#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for k in range(rowIndex):
            k = k + 1
            row.append(row[-1]*(rowIndex-k+1)//k)
        return row
# @lc code=end

