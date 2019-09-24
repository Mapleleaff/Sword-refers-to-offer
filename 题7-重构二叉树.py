"""
题7-重构二叉树
输入某二叉树的前序遍历和中序遍历的结果，重建该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildtree(pre, tin):
    if pre == []:
        return None
    root = TreeNode(pre[0])
    print(root.val)
    j = tin.index(pre[0])
    root.left = buildtree(pre[1:j+1], tin[:j])
    root.right = buildtree(pre[j+1:], tin[j+1:])

    return root


pre = [1, 2, 4, 7, 3, 5, 6, 8]
tin = [4, 7, 2, 1, 5, 3, 8, 6]
buildtree(pre,tin)
