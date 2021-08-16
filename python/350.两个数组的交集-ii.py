'''
Author: Zander
Description: Edit Here
Date: 2021-08-16 11:46:37
LastEditors: Zander
LastEditTime: 2021-08-16 11:53:49
FilePath: /python/350.两个数组的交集-ii.py
'''
#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash1, hash2 = {}, {}
        for num1 in nums1:
            hash1[num1] = hash1.get(num1, 0) + 1
        for num2 in nums2:
            hash2[num2] = hash2.get(num2, 0) + 1
        res = []
        for k,v in hash1.items():
            if k in hash2:
                for i in range(min(v, hash2[k])):
                    res.append(k)
        return res
# @lc code=end

