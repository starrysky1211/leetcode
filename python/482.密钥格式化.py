'''
Author: Zander
Description: Edit Here
Date: 2021-08-20 11:48:53
LastEditors: Zander
LastEditTime: 2021-08-20 11:54:38
FilePath: /python/482.密钥格式化.py
'''
#
# @lc app=leetcode.cn id=482 lang=python3
#
# [482] 密钥格式化
#

# @lc code=start
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s0 = "".join(s.split("-"))
        n, m = divmod(len(s0), k)
        res = [s0[:m]] if m else []
        left = [s0[i*k+m:(i+1)*k+m] for i in range(n)]
        return "-".join(res + left).upper()
        
# @lc code=end

