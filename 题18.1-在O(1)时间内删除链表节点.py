"""
题18.1-在 O(1) 时间内删除链表节点
给定单向链表的头指针和一个节点指针，定义一个函数在 O(1) 时间内删除该节点。
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __del__(self):
        self.val = None
        self.next = None


class Solution:
    def DeleteNode(self, pListHead, pToBeDeleted):
        if not pListHead or not pToBeDeleted:
            return None

        # 要删除的节点不是尾节点时
        if pToBeDeleted.next != None:
            pNext = pToBeDeleted.next
            pToBeDeleted.val = pNext.val
            pToBeDeleted.next = pNext.next
            pNext.__del__()


        # 链表只有一个节点时，只能删除头节点
        elif pListHead == pToBeDeleted:
            pToBeDeleted.__del__()
            pListHead.__del__()

        # 要删除的节点是尾节点
        else:
            pNode = pListHead
            while pNode.next != pToBeDeleted:
                pNode = pNode.next
            pNode.next = None
            pToBeDeleted.__del__()


node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node4 = ListNode(15)
node1.next = node2
node2.next = node3
node3.next = node4

S = Solution()
# 删除头节点
S.DeleteNode(node1, node1)
for node in [node1,node2,node3,node4]:
    print(node.val)

# 删除尾节点
S.DeleteNode(node1, node4)
for node in [node1,node2,node3,node4]:
    print(node.val)

S.DeleteNode(node1, node1)
for node in [node1,node2,node3,node4]:
    print(node.val)

# 删除仅剩的头节点
S.DeleteNode(node1, node1)
for node in [node1,node2,node3,node4]:
    print(node.val)
