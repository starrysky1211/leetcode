'''
Author: Zander
Description: Edit Here
Date: 2021-08-04 14:03:05
LastEditors: Zander
LastEditTime: 2021-08-05 11:26:56
FilePath: /python/35.搜索插入位置.py
'''
#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while l<=r:
            head = (l+r)//2
            if(nums[head] == target):
                return head
            elif(nums[head]<target):
                l = head+1
            else:
                r = head-1
        return l
                
# @lc code=end

