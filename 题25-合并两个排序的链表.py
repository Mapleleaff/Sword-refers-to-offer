"""
题25-合并两个排序的链表
输入两个单调递增的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
"""

class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # 循环解法
    def Merge(self, p1, p2):
        if not p1:
            return p2
        if not p2:
            return p1

        pMerge = ListNode(-1)
        cur = pMerge
        while p1 != None and p2 != None:
            if p1.val <= p2.val:
                cur.next = p1
                p1 = p1.next
            else:
                cur.next = p2
                p2 = p2.next
            cur = cur.next

        if p1 != None:
            cur.next = p1
        if p2 != None:
            cur.next = p2
        return pMerge.next

    # 递归解法
    def MergeRec(self, pHead1, pHead2):
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1

        if pHead1.val < pHead2.val:
            pMergedHead = pHead1
            pMergedHead.next = self.MergeRec(pHead1.next, pHead2)
        else:
            pMergedHead = pHead2
            pMergedHead.next = self.MergeRec(pHead1, pHead2.next)
        return pMergedHead


node1 = ListNode(1)
node2 = ListNode(3)
node3 = ListNode(5)
node1.next = node2
node2.next = node3

node4 = ListNode(2)
node5 = ListNode(4)
node6 = ListNode(6)
node4.next = node5
node5.next = node6

S = Solution()
S.Merge(node4,node1)
print(node1.next.val)
