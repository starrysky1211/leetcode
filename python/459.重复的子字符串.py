'''
Author: Zander
Description: Edit Here
Date: 2021-08-19 11:30:14
LastEditors: Zander
LastEditTime: 2021-08-19 11:49:47
FilePath: /python/459.重复的子字符串.py
'''
#
# @lc app=leetcode.cn id=459 lang=python3
#
# [459] 重复的子字符串
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern1(self, s: str) -> bool:
        # 首先是个和数，因为如果是质数那就没可能有周期性
        length = len(s)
        # 其次寻找因数，越大越好，因为如果以小的因数为周期，那么必定以这个小因数与其他因数的倍数为周期
        for i in range(1, length//2+1):
            if length%i != 0:
                continue # 不是因数
            # 开始判断
            k = 1
            origin = s[:i]
            flag = True
            while (k+1)*i <= length:
                if origin != s[k*i:(k+1)*i]:
                    flag = False
                    break
                k += 1
            if flag:
                return True
        return False
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s).find(s, 1) != len(s)
# @lc code=end

