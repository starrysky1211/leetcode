# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        pre = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            pre, pre.next, slow = slow, pre, slow.next
        if fast:
            slow = slow.next
        while pre:
            if pre.val != slow.val:
                return False
            pre, slow = pre.next, slow.next
        return True
