'''
Author: Zander
Description: Edit Here
Date: 2021-08-11 11:42:08
LastEditors: Zander
LastEditTime: 2021-08-11 11:46:26
FilePath: /python/191.位-1-的个数.py
'''
#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            count += n&1
            n >>= 1
        return count
# @lc code=end

