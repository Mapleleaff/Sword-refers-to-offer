"""
题23-链表中环的入口节点
如果一个链表中包含环，如何找出环的入口节点
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def findEntry(self, pHead):
        if pHead == None:
            return None

        fast = pHead.next.next
        slow = pHead.next
        while fast != slow:
            fast = fast.next.next
            slow = slow.next

        fast = pHead
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node3

s = Solution()
print(s.findEntry(node1).val)
