"""
题37-序列化二叉树
请实现两个函数，分别用来序列化和反序列化二叉树
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Serialize(self, root):
        if root == None:
            return '#'
        return str(root.val) + ',' + self.Serialize(root.left) + ',' + self.Serialize(root.right)

    def Deserialize(self, s):
        L = s.split(',')
        tree = self.deserialize(L)
        return tree

    def deserialize(self, L):
        if len(L) <= 0:
            return None

        val = L.pop(0)
        node = None
        if val != '#':
            node = TreeNode(int(val))
            node.left = self.deserialize(L)
            node.right = self.deserialize(L)
        return node


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
newList = S.Serialize(pNode1)
print(newList)
tree = S.Deserialize(newList)
print(tree)
