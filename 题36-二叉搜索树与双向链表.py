"""
题36-二叉搜索树与双向链表
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Convert(self, pRootOfTree):
        if pRootOfTree == None:
            return None

        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree

        self.Convert(pRootOfTree.left)
        left = pRootOfTree.left

        # 连接根与左子树最大节点
        if left:
            while left.right:
                left = left.right
            left.right, pRootOfTree.left = pRootOfTree, left

        self.Convert(pRootOfTree.right)
        right = pRootOfTree.right

        # 连接根与右子树最小节点
        if right:
            while right.left:
                right = right.left
            right.left, pRootOfTree.right = pRootOfTree, right

        while pRootOfTree.left:
            pRootOfTree = pRootOfTree.left
        return pRootOfTree


pNode1 = TreeNode(8)
pNode2 = TreeNode(6)
pNode3 = TreeNode(10)
pNode4 = TreeNode(5)
pNode5 = TreeNode(7)
pNode6 = TreeNode(9)
pNode7 = TreeNode(11)
pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7

S = Solution()
newList = S.Convert(pNode1)
print(newList.val)
