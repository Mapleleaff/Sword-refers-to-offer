"""
题33-二叉搜索树的后序遍历序列
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出 True，否则返回 False。假设输入的数组的任意两个数字都互不相同。
"""

class Solution:
    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return False

        index, length = 0, len(sequence)
        root = sequence[-1]

        for i in range(length-1):
            index = i
            if sequence[i] > root:
                break

        for j in range(index+1, length-1):
            if sequence[j] < root:
                return False

        left, right = True, True
        if index > 0:
            left = self.VerifySquenceOfBST(sequence[:index])

        if index < length-1:
            right = self.VerifySquenceOfBST(sequence[index:length-1])

        return left and right


array = [5, 7, 6, 9, 11, 10, 8]
array2 = [4, 6, 7, 5]
array3 = [1, 2, 3, 4, 5]
S = Solution()
print(S.VerifySquenceOfBST(array))
print(S.VerifySquenceOfBST(array2))
print(S.VerifySquenceOfBST(array3))
