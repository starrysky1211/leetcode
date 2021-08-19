'''
Author: Zander
Description: Edit Here
Date: 2021-08-19 10:46:07
LastEditors: Zander
LastEditTime: 2021-08-19 10:46:49
FilePath: /python/434.字符串中的单词数.py
'''
#
# @lc app=leetcode.cn id=434 lang=python3
#
# [434] 字符串中的单词数
#

# @lc code=start
class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())
# @lc code=end

