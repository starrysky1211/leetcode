'''
Author: Zander
Description: Edit Here
Date: 2021-08-13 11:02:51
LastEditors: Zander
LastEditTime: 2021-08-13 11:11:44
FilePath: /python/242.有效的字母异位词.py
'''
#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram1(self, s: str, t: str) -> bool:
        hashtable = {}
        for c in s:
            hashtable[c] = hashtable[c] + 1 if c in hashtable else 1
        for c in t:
            if not c in hashtable: return False
            hashtable[c] -= 1
            if hashtable[c] < 0: return False
        return sum(hashtable.values()) == 0
    def isAnagram(self, s: str, t: str) -> bool:
        hashtable = {}
        for c in s:
            hashtable[c] = hashtable.get(c, 0) + 1
        for c in t:
            hashtable[c] = hashtable.get(c, 0) - 1
            if hashtable[c] < 0: return False
        return sum(hashtable.values()) == 0
# @lc code=end

