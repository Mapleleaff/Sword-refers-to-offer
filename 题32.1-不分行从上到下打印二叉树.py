"""
题32.1-不分行从上到下打印二叉树
从上到下打印出二叉树的每个节点，同一层节点按照从左到右的顺序打印
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def PrintFromTopToBottom(self, root):
        if root==None:
            return root

        result=[]
        queue = [root]
        while len(queue):
            tree = queue.pop(0)
            result.append(tree.val)
            if tree.left:
                queue.append(tree.left)
            if tree.right:
                queue.append(tree.right)
        return result


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
result = S.PrintFromTopToBottom(pNode1)
print(result)
