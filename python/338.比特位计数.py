'''
Author: Zander
Description: Edit Here
Date: 2021-08-16 11:13:10
LastEditors: Zander
LastEditTime: 2021-08-16 11:19:42
FilePath: /python/338.比特位计数.py
'''
#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        # 使用官方最低设置位思路解题
        bits = [0]
        for i in range(1, n+1):
            bits.append(bits[i&(i-1)]+1)
        return bits
# @lc code=end

