'''
Author: Zander
Description: Edit Here
Date: 2021-08-16 11:36:23
LastEditors: Zander
LastEditTime: 2021-08-16 11:43:36
FilePath: /python/345.反转字符串中的元音字母.py
'''
#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        bag = {'a', 'e', 'i', 'o', 'u', 'A', "E", "I", "O", "U"}
        l, r = 0, len(s)-1
        s = list(s)
        while l < r:
            if not s[l] in bag:
                l += 1
                continue
            if not s[r] in bag:
                r -= 1
                continue
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return "".join(s)
# @lc code=end

