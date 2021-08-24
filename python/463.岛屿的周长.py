'''
Author: Zander
Description: Edit Here
Date: 2021-08-20 09:43:05
LastEditors: Zander
LastEditTime: 2021-08-20 11:27:08
FilePath: /python/463.岛屿的周长.py
'''
#
# @lc app=leetcode.cn id=463 lang=python3
#
# [463] 岛屿的周长
#

# @lc code=start
class Solution:
    def islandPerimeter1(self, grid: List[List[int]]) -> int:
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
    def islandPerimeter(self, grid: List[List[int]]) -> int:
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
        grid[rs][cs] = 2
        res = 0
        while len(stack) != 0:
            point = stack.pop()
            x, y = point
            if x == 0 or grid[x-1][y] == 0:
                # 上方为空，周长加一
                res += 1
            elif grid[x-1][y] == 1:
                # 上方为陆地，压入栈
                stack.append([x-1, y])
                grid[x-1][y] = 2
            if y == 0 or grid[x][y-1] == 0:
                # 左侧为空，周长加一
                res += 1
            elif grid[x][y-1] == 1:
                # 左侧为陆地，压入栈
                stack.append([x, y-1])
                grid[x][y-1] = 2
            if x == row - 1 or grid[x+1][y] == 0:
                # 下方为空，周长加一
                res += 1
            elif grid[x+1][y] == 1:
                # 下方为陆地，压入栈
                stack.append([x+1, y])
                grid[x+1][y] = 2
            if y == col - 1 or grid[x][y+1] == 0:
                # 右侧为空，周长加一
                res += 1
            elif grid[x][y+1] == 1:
                # 右侧为陆地，压入栈
                stack.append([x, y+1])
                grid[x][y+1] = 2
        return res
# @lc code=end

