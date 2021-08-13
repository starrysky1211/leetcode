'''
Author: Zander
Description: Edit Here
Date: 2021-08-12 10:25:35
LastEditors: Zander
LastEditTime: 2021-08-12 10:50:31
FilePath: /python/205.同构字符串.py
'''
#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m = {}
        for i in range(len(s)):
            key = s[i]
            value = t[i]
            keys = m.keys()
            values = m.values()
            if key in keys:
                # 已记录
                if m[key] != value:
                    return False
            else:
                # 未记录
                if value in values:
                    return False
                m[key] = value
        return True
# @lc code=end

