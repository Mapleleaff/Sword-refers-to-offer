"""
题6-从尾到头打印链表
输入链表的头节点，从尾到头反过来打印出每点的值。
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 使用栈
def Solution(ListNode):
    array = []
    while ListNode != None:
        array.append(ListNode.val)
        ListNode = ListNode.next
    return [ array.pop() for _ in range(len(array))]


# 使用递归
def solu(ListNode):
    if ListNode != None:
        if ListNode.next != None:
            solu(ListNode.next)
        print(ListNode.val)
    return


# 创建链表用来测试
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4

print(Solution(node1))
print(solu(node1))
