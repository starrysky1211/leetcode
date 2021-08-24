'''
Author: Zander
Description: Edit Here
Date: 2021-08-20 11:32:44
LastEditors: Zander
LastEditTime: 2021-08-20 11:48:43
FilePath: /python/476.数字的补数.py
'''
#
# @lc app=leetcode.cn id=476 lang=python3
#
# [476] 数字的补数
#

# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        return num ^ 2**num.bit_length()-1
# @lc code=end

