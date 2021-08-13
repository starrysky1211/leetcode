'''
Author: Zander
Description: Edit Here
Date: 2021-08-12 10:52:58
LastEditors: Zander
LastEditTime: 2021-08-12 11:01:19
FilePath: /python/206.反转链表.py
'''
#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        last, head, privous = None, head, head.next
        while head.next:
            head.next = last
            last, head, privous = head, privous, privous.next
        head.next = last
        return head
# @lc code=end

