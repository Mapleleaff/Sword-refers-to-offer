"""
题35-复杂链表的复制
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的 head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
"""

class RandomListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None

class Solution:
    def Clone(self, pHead):
        if pHead == None:
            return None

        self.CloneNodes(pHead)
        self.ConnectRandomNodes(pHead)
        return self.ReconnectNodes(pHead)

    # 复制每个结点, 如原来是 A->B->C 变成 A->A'->B->B'->C->C'
    def CloneNodes(self, pHead):
        pNode = pHead
        while pNode:
            pCloned = RandomListNode(0)
            pCloned.val = pNode.val
            pCloned.next = pNode.next
            pNode.next = pCloned
            pNode = pCloned.next

    # 遍历链表，使 A'->random = A->random->next
    def ConnectRandomNodes(self, pHead):
        pNode = pHead
        while pNode:
            pCloned = pNode.next
            if pNode.random != None:
                pCloned.random = pNode.random.next
            pNode = pCloned.next

    # 拆分链表, 将原始链表的结点组成新的链表, 复制结点组成复制后的链表
    def ReconnectNodes(self, pHead):
        pNode = pHead
        pClonedHead = pClonedNode = pNode.next
        pNode.next = pClonedHead.next
        pNode = pNode.next

        while pNode:
            pClonedNode.next = pNode.next
            pClonedNode = pClonedNode.next
            pNode.next = pClonedNode.next
            pNode = pNode.next

        return pClonedHead


node1 = RandomListNode(1)
node2 = RandomListNode(3)
node3 = RandomListNode(5)
node1.next = node2
node2.next = node3
node1.random = node3
S = Solution()
clonedNode = S.Clone(node1)
print(clonedNode.random.val)

