'''
Author: Zander
Description: Edit Here
Date: 2021-08-09 11:44:37
LastEditors: Zander
LastEditTime: 2021-08-09 11:54:32
FilePath: /python/118.杨辉三角.py
'''
#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1],[1,1]]
        if numRows == 1: return res[:1]
        if numRows == 2: return res
        while numRows > 2:
            numRows -=1
            newRow = [1] + [res[-1][i] + res[-1][i+1] for i in range(len(res[-1])-1)] + [1]
            res.append(newRow)
        return res
# @lc code=end

