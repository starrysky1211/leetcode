class node(object):
    def __init__(self, val):
        self.next = None
        self.val = val

class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return None
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        self.size += 1
        new = node(val)
        new.next = self.head
        self.head = new

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        size = self.size
        self.size += 1
        cur = self.head
        if not cur:
            self.head = node(val)
        else:
            while cur.next:
                cur = cur.next
            cur.next = node(val)

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        print self.size, index, val
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
        else:
            new = node(val)
            cur = self.head
            for i in range(1,index):
                cur = cur.next
            new.next = cur.next
            cur.next = new
            self.size += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index < 0 or index >= self.size:
            return
        self.size -= 1
        if index == 0:
            self.head = self.head.next
        else:
            cur = self.head
            for i in range(1, index):
                cur = cur.next
            cur.next = cur.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
