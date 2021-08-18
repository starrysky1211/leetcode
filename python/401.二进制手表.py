'''
Author: Zander
Description: Edit Here
Date: 2021-08-18 12:21:30
LastEditors: Zander
LastEditTime: 2021-08-18 14:57:41
FilePath: /python/401.二进制手表.py
'''
#
# @lc app=leetcode.cn id=401 lang=python3
#
# [401] 二进制手表
#

# @lc code=start
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        # 时间的可能性更少，所以遍历时间
        res = []
        for h in range(12):
            for m in range(60):
                if self.time2binary(h, m) == turnedOn:
                    res.append(self.time2string(h, m))
        return res
    def time2binary(self, h: int, m: int) -> int:
        # 根据时间返回开灯个数
        hs = "{0:b}".format(h)
        ms = "{0:b}".format(m)
        res = 0
        return (hs+ms).count("1")

    def time2string(self, h:int, m: int) -> str:
        hs = str(h)
        ms = str(m) if m>=10 else "0"+str(m)
        return hs+":"+ms
# @lc code=end

