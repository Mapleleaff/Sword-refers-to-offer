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
