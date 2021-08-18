'''
Author: Zander
Description: Edit Here
Date: 2021-08-18 09:19:03
LastEditors: Zander
LastEditTime: 2021-08-18 09:22:10
FilePath: /python/389.找不同.py
'''
#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashtable = {}
        for c in t:
            hashtable[c] = hashtable.get(c, 0) + 1
        for c in s:
            hashtable[c] -= 1
        for k in hashtable:
            if hashtable[k] == 1:
                return k
        
# @lc code=end

