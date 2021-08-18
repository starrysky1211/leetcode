'''
Author: Zander
Description: Edit Here
Date: 2021-08-17 12:29:32
LastEditors: Zander
LastEditTime: 2021-08-17 12:34:26
FilePath: /python/387.字符串中的第一个唯一字符.py
'''
#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashtable = {}
        for i, c in enumerate(s):
            hashtable[c] = hashtable.get(c, []) + [i]
        for i, c in enumerate(hashtable):
            if len(hashtable[c]) == 1:
                return hashtable[c][0]
        return -1
# @lc code=end

