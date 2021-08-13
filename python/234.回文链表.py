'''
Author: Zander
Description: Edit Here
Date: 2021-08-12 11:56:31
LastEditors: Zander
LastEditTime: 2021-08-12 12:10:32
FilePath: /python/234.回文链表.py
'''
#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        tmp, fast, slow = [head] * 3
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        # 此时slow就是中点，反转slow后面的链表
        rev = self.reverseList(slow.next)
        # 比较前后链表是否相同
        while head and rev:
            if head.val != rev.val:
                return False
            head, rev = head.next, rev.next
        return True
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

