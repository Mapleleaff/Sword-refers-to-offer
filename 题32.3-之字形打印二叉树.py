"""
题32.3-之字形打印二叉树
请实现一个函数按照之字形打印二叉树，
即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，
第三行按照从左到右的顺序打印，其他行以此类推。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # 类似题27，题32.1，题32.2方法
    def ZhiPrint(self, root):
        if root==None:
            return root
            
        result, queue = [], [root]
        level = 0
        while queue:
            level += 1
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
            if level & 1:
                result += [levelnode]
            else:
                result += [levelnode[::-1]]
        return result


    # 引入两个栈
    def Print(self, pRoot):
        if not pRoot:
            return []

        result, nodes = [], [pRoot]
        right = True
        while nodes:
            nextStack, curStack = [], []
            if right:
                for node in nodes:
                    curStack.append(node.val)
                    if node.left:
                        nextStack.append(node.left)
                    if node.right:
                        nextStack.append(node.right)
            else:
                for node in nodes:
                    curStack.append(node.val)
                    if node.right:
                        nextStack.append(node.right)
                    if node.left:
                        nextStack.append(node.left)
            nextStack.reverse()
            right = not right
            result.append(curStack)
            nodes = nextStack
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
result1 = S.ZhiPrint(pNode1)
result2 = S.Print(pNode1)
print(result1)
print(result2)
