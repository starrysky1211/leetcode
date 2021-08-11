'''
Author: Zander
Description: Edit Here
Date: 2021-08-11 12:02:54
LastEditors: Zander
LastEditTime: 2021-08-11 17:27:16
FilePath: /python/203.移除链表元素.py
'''
#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        tmp = ListNode(val = 0, next=head)
        last = tmp
        while last.next:
            if head.val == val:
                last.next = head.next
                head = head.next
            else:
                last = head
                head = head.next
        return tmp.next
# @lc code=end

