'''
Author: Zander
Description: Edit Here
Date: 2021-08-16 10:57:36
LastEditors: Zander
LastEditTime: 2021-08-16 11:05:58
FilePath: /python/303.区域和检索-数组不可变.py
'''
#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        self.s = [0]
        for n in nums:
            self.s.append(self.s[-1]+n)

    def sumRange(self, left: int, right: int) -> int:
        return self.s[right+1] - self.s[left]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

