'''
Author: Zander
Description: Edit Here
Date: 2021-08-11 10:44:06
LastEditors: Zander
LastEditTime: 2021-08-11 11:41:52
FilePath: /python/190.颠倒二进制位.py
'''
#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        binary = '{0:032b}'.format(n)
        return int(binary[::-1], 2)
# @lc code=end

