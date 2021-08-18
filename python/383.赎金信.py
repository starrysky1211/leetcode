'''
Author: Zander
Description: Edit Here
Date: 2021-08-17 11:30:48
LastEditors: Zander
LastEditTime: 2021-08-17 12:27:18
FilePath: /python/383.赎金信.py
'''
#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashtable = {}
        for c in magazine:
            hashtable[c] = hashtable.get(c, 0) + 1
        for r in ransomNote:
            if r in hashtable:
                hashtable[r] -= 1
                if hashtable[r] < 0:
                    return False
            else:
                return False
        return True
# @lc code=end

