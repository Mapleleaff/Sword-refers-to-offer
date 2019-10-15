"""
题34-二叉树中和为某一值的路径
输入一棵二叉树的根节点和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。
路径定义为从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def FindPath(self, root, sum):
        if root == None:
            return []

        result, ans = [], []
        result = self.PathSum(root, sum, result, ans)
        return result

    def PathSum(self, root, target, result, ans):
        ans += [root.val]
        target = target - root.val

        # 不可以直接 ans.pop(), 否则会导致 result 也改变
        if target == 0 and root.left == None and root.right == None:
            result.append(ans.copy())

        if root.left:
            self.PathSum(root.left, target, result, ans)
            ans.pop()

        if root.right:
            self.PathSum(root.right, target, result, ans)
            ans.pop()

        return result


pNode1 = TreeNode(10)
pNode2 = TreeNode(5)
pNode3 = TreeNode(12)
pNode4 = TreeNode(4)
pNode5 = TreeNode(7)
pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5

S = Solution()
print(S.FindPath(pNode1, 22))
