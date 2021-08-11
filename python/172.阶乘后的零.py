'''
Author: Zander
Description: Edit Here
Date: 2021-08-11 10:33:31
LastEditors: Zander
LastEditTime: 2021-08-11 10:43:46
FilePath: /python/172.阶乘后的零.py
'''
#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#

# @lc code=start
class Solution:
    def trailingZeroes1(self, n: int) -> int:
        # 遍历每个数，每个数的因数中有几个5，最后结果就有几个0
        def div5(num: int) -> int:
            res, head= 0, 0
            while head == 0:
                num, head = divmod(num, 5)
                if head == 0:
                    res += 1
            return res
        res = 0
        for i in range(1, n+1):
            res += div5(i)
        return res
    def trailingZeroes(self, n:int) -> int:
        # 进一步优化，可以直接跳过大部分数字，计算以5为间隔的个数，然后25，125 ...
        r = 0
        while n > 0:
            n //= 5
            r += n
        return r
# @lc code=end

