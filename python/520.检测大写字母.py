'''
Author: Zander
Description: Edit Here
Date: 2021-08-31 11:52:17
LastEditors: Zander
LastEditTime: 2021-09-01 09:17:41
FilePath: /python/520.检测大写字母.py
'''
#
# @lc app=leetcode.cn id=520 lang=python3
#
# [520] 检测大写字母
#

# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word in [word.upper(), word.lower(), word.title()]
# @lc code=end

