"""
题31-栈的压入、弹出序列
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
假设压入栈的所有数字均不相等。例如序列 1,2,3,4,5 是某栈的压入顺序，
序列 4,5,3,2,1 是该压栈序列对应的一个弹出序列，但 4,3,5,1,2 就不可能是该压栈序列的弹出序列。
（注意：这两个序列的长度是相等的）
"""

class Solution:
    def IsPopOrder(self, pushV, popV):
        if pushV == [] or popV == []:
            return False
        stack = []
        for i in pushV:
            stack.append(i)
            while stack and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)

        if stack:
            return False

        return True


pushV = [1, 2, 3, 4, 5]
popV = [4, 5, 3, 2, 1]
popVF = [4, 5, 2, 1, 3]
S = Solution()
print(S.IsPopOrder(pushV, popV))
print(S.IsPopOrder(pushV, popVF))
