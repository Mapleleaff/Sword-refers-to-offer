"""
题22-链表中倒数第K个节点
输入一个链表，输出该链表中倒数第k个结点
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def findKthNode(self, head, k):
        if head == None or k <= 0:
            return None
            
        p1,p2 = head, head
        for i in range(k):
            p1 = p1.next
            if p1 == None:
                return None

        while p1.next != None:
            p1 = p1.next
            p2 = p2.next

        return p2


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(3)
node5 = ListNode(4)
node6 = ListNode(4)
node7 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

s = Solution()
print(s.findKthNode(node1, 4).val)
