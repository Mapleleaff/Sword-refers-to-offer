"""
题8-二叉树的下一个结点
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next  = None


def getNode(pNode):
    if not pNode:
        return None

    if pNode.right != None:
        pNode = pNode.right
        while pNode.left:
            pNode = pNode.left
        return pNode

    elif pNode.next != None and pNode == pNode.next.left:
        return pNode.next

    elif pNode.next != None and pNode == pNode.next.right:
        pNode = pNode.next
        while pNode.next != None and pNode != pNode.next.left:
            pNode = pNode.next
        return pNode.next

    else:
        return None
