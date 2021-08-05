'''
Author: Zander
Description: Edit Here
Date: 2021-08-05 11:33:24
LastEditors: Zander
LastEditTime: 2021-08-05 11:37:46
FilePath: /python/58.最后一个单词的长度.py
'''
#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        counter = 0
        flag = False
        for i in s:
            if i == ' ':
                flag = True
            elif flag and i != ' ':
                flag = False
                counter = 1
            else:
                counter += 1
        return counter
# @lc code=end

