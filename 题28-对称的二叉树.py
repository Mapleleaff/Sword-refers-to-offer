"""
题28-对称的二叉树
请实现一个函数，用来判断一棵二叉树是不是对称的
注意，如果一棵二叉树和它的镜像一样，那么它是对称的
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetrical(self, root):
         return self.selfIsSymmetrical(root, root)

    def selfIsSymmetrical(self, root1, root2):
        if root1 == None and root2 == None:
            return True

        if root1 == None or root2 == None:
            return False

        if root1.val != root2.val:
            return False

        result1 = self.selfIsSymmetrical(root1.left, root2.right)
        result2 = self.selfIsSymmetrical(root1.right, root2.left)
        return result1 and result2


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
result = S.isSymmetrical(pNode1)
print(result)
