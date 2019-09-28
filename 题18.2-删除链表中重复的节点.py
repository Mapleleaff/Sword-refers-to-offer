"""
题18.2-删除链表中重复的结点
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表 1->2->3->3->4->4->5 处理后为 1->2->5
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplication(self, pHead):
        if pHead == None:
            return pHead
        preNode, curNode = None, pHead
        nextNode = curNode.next

        while nextNode != None:
            while nextNode.val != curNode.val:
                preNode = curNode
                curNode = nextNode
                nextNode = nextNode.next

            while nextNode.val == curNode.val:
                nextNode = nextNode.next

            if preNode == None:
                pHead = nextNode
                curNode = nextNode
                continue

            else:
                preNode.next = nextNode
                curNode = nextNode
                nextNode = curNode.next

        return pHead


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
print(s.deleteDuplication(node1).next.val)


