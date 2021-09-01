'''
Author: Zander
Description: Edit Here
Date: 2021-08-31 11:31:04
LastEditors: Zander
LastEditTime: 2021-08-31 11:48:09
FilePath: /python/507.完美数.py
'''
#
# @lc app=leetcode.cn id=507 lang=python3
#
# [507] 完美数
#

# @lc code=start
class Solution:
    def checkPerfectNumber1(self, num: int) -> bool:
        primes = [2, 3, 5, 7, 13, 17, 19, 31]
        res = [2**(i-1)*(2**i-1) for i in primes]
        return num in res
    def checkPerfectNumber(self, num: int) -> bool:
        res = [6,28,496,8128,33550336,8589869056,137438691328,2305843008139952128]
        return num in res
# @lc code=end

