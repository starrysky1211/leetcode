'''
Author: Zander
Description: Edit Here
Date: 2021-08-16 09:28:24
LastEditors: Zander
LastEditTime: 2021-08-16 10:47:26
FilePath: /python/290.单词规律.py
'''
#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sl = s.split()
        if len(pattern)!=len(sl): return False
        h = list(zip(pattern, sl))
        hashtable = {}
        for item in h:
            if item[0] in hashtable:
                if item[1] != hashtable[item[0]]: return False
            else:
                if item[1] in hashtable.values():
                    return False
                hashtable[item[0]] = item[1]
        return True
# @lc code=end

