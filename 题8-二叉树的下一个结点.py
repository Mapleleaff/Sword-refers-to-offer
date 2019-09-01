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
