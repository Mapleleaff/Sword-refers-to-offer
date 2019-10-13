"""
题30-包含 min 函数的栈
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的 min 函数
在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)
"""

class Solution:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, node):
        self.stack.append(node)
        if self.minStack == [] or node < self.min():
            self.minStack.append(node)
        else:
            self.minStack.append(self.min())

    def pop(self):
        if self.stack == [] or self.minStack == []:
            return None
        self.minStack.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.minStack[-1]


S = Solution()
S.push(3)
S.push(4)
S.push(2)
S.push(1)
print(S.min())
S.pop()
print(S.min())
S.pop()
print(S.min())
