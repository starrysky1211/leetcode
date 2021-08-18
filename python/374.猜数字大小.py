'''
Author: Zander
Description: Edit Here
Date: 2021-08-17 11:26:13
LastEditors: Zander
LastEditTime: 2021-08-17 11:30:05
FilePath: /python/374.猜数字大小.py
'''
#
# @lc app=leetcode.cn id=374 lang=python3
#
# [374] 猜数字大小
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l < r:
            mid = (l + r) // 2
            res = guess(mid)
            if res == 0:
                return mid
            elif res == -1:
                r = mid -1
            else:
                l = mid + 1
        return l
# @lc code=end

