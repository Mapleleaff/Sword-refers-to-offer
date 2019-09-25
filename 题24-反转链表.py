"""
题24-反转链表
输入一个链表的头节点，反转该链表，并输出新链表的头节点。
"""

class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # 循环解法
    def ReverseList(self, pHead):
        if pHead == None:
            return None
        pre = None
        cur = pHead
        last = cur.next

        # 断开当前节点与下一个节点的链接
        cur.next = None
        while last != None:
            pre = cur
            cur = last
            last = last.next
            cur.next = pre
        return cur

    # 递归实现
    def ReverseListRec(self, pHead):
        if pHead == None:
            return None

        # 只有一个节点时或者到达尾节点
        if pHead.next == None:
            return pHead

        cur = pHead
        last = cur.next
        cur.next = None
        newhead = self.ReverseListRec(last)
        last.next = cur
        return newhead


node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node1.next = node2
node2.next = node3
S = Solution()
p = S.ReverseList(node1)
print(p.val)

node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node1.next = node2
node2.next = node3
S = Solution()
p = S.ReverseListRec(node1)
print(p.next.val)
