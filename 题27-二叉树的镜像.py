"""
题27-二叉树的镜像
操作给定的二叉树，将其变换为源二叉树的镜像
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinaryTreeNode:
    # 递归实现
    def BinaryTree(self, root):
        if root == None:
            return

        root.left, root.right = root.right, root.left
        if root.left:
            self.BinaryTree(root.left)
        if root.right:
            self.BinaryTree(root.right)

    # 队列实现，按层遍历
    def MirrorQueue(self, root):
        if root == None:
            return

        queue = [root]
        while len(queue) > 0:
            curlevel, count = len(queue), 0
            while count < curlevel:
                count += 1
                pRoot = queue.pop(0)
                pRoot.left, pRoot.right = pRoot.right, pRoot.left

                if pRoot.left:
                    queue.append(pRoot.left)
                if pRoot.right:
                    queue.append(pRoot.right)

    # 栈实现
    def MirrorStack(self, root):
        if root == None:
            return

        stack = [root]
        while len(stack):
            lastnum = len(stack) -1
            tree = stack.pop()
            lastnum -= 1
            tree.left, tree.right = tree.right, tree.left

            if tree.left:
                stack.append(tree.left)
                lastnum += 1
            if tree.right:
                stack.append(tree.right)
                lastnum += 1


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

S = BinaryTreeNode()
S.BinaryTree(pNode1)
print(pNode1.right.left.val)
