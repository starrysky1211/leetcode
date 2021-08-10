'''
Author: Zander
Description: Edit Here
Date: 2021-08-10 11:09:13
LastEditors: Zander
LastEditTime: 2021-08-10 11:21:59
FilePath: /python/141.环形链表.py
'''
#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = head
        low = head
        while fast and low:
            # 快慢指针一旦为空就意味这已经走到了尽头
            if not fast.next or not fast.next.next: return False 
            fast = fast.next.next
            low = low.next
            if fast is low:
                return True
# @lc code=end

