'''
Author: Zander
Description: Edit Here
Date: 2021-08-18 15:23:50
LastEditors: Zander
LastEditTime: 2021-08-18 15:28:39
FilePath: /python/409.最长回文串.py
'''
#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashtable = {}
        for c in s:
            hashtable[c] = hashtable.get(c, 0) + 1
        res = 0
        taker = 0
        for v in hashtable.values():
            cur = v//2 * 2
            taker += v - cur
            res += cur
        return res + 1 if taker > 0 else res
# @lc code=end

