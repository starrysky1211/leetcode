'''
Author: Zander
Description: Edit Here
Date: 2021-08-10 10:42:31
LastEditors: Zander
LastEditTime: 2021-08-10 11:00:12
FilePath: /python/125.验证回文串.py
'''
#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 预处理，变成无空格和标点的小写字符串
        ls = ""
        for c in s:
            if str.isalnum(c):
                ls += c.lower()
        # 判断回文
        # 奇数，中间值index是mid为对称轴
        # 偶数，中间值index是mid-1和mid必须相等
        for i in range(len(ls)//2):
            if ls[i] != ls[-i-1]:
                return False
        return True
# @lc code=end

