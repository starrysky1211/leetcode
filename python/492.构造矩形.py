'''
Author: Zander
Description: Edit Here
Date: 2021-08-20 12:00:15
LastEditors: Zander
LastEditTime: 2021-08-20 12:12:01
FilePath: /python/492.构造矩形.py
'''
#
# @lc app=leetcode.cn id=492 lang=python3
#
# [492] 构造矩形
#

# @lc code=start
import math
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        mid = math.sqrt(area)
        w = int(mid // 1)
        while area % w != 0:
            w -= 1
        return [area//w, w]
# @lc code=end

