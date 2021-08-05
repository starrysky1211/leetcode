'''
Author: Zander
Description: Edit Here
Date: 2021-05-06 11:56:51
LastEditors: Zander
LastEditTime: 2021-08-05 12:01:55
FilePath: /python/try.py
'''
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        taker = 0
        taker, end =divmod(digits[-1] + 1 , 10)
        digits[-1] = end
        length = len(digits)
        if length > 1:
            for i in range(length-2, -1, -1):
                taker, end =divmod(digits[i] + taker , 10)
                digits[i] = end
        if taker:
            digits = [1] + digits
        return digits


s = Solution()
r = s.plusOne([9,9])
print(r)