"""
题32.2-分行从上到下打印二叉树
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，
每一层打印到一行
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        if root==None:
            return root

        result=[]
        queue = [root]
        while len(queue):
            levelnode = []
            curlevel, count = len(queue), 0
            while count < curlevel:
                count += 1
                tree = queue.pop(0)
                levelnode.append(tree.val)
                if tree.left:
                    queue.append(tree.left)
                if tree.right:
                    queue.append(tree.right)
            result += [levelnode]
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
result = S.levelOrder(pNode1)
print(result)
