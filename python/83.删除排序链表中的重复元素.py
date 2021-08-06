'''
Author: Zander
Description: Edit Here
Date: 2021-08-06 11:02:52
LastEditors: Zander
LastEditTime: 2021-08-06 11:12:15
FilePath: /python/83.删除排序链表中的重复元素.py
'''
#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        origin = head
        while head and head.next:
            next = head.next
            if head.val == next.val:
                if next.next:
                    head.next = next.next
                else:
                    head.next = None
                    return origin
            else:
                head = head.next
        return origin
# @lc code=end

