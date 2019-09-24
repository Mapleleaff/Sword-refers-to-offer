"""
题9-用两个栈实现队列
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型
"""

class Solution(object):
    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def push(self, x):
        self.stack1.append(x)

    def pop(self):
        if self.stack2 != []:
            return self.stack2.pop()

        while self.stack1 != []:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


P = Solution()
P.push(10)
P.push(11)
P.push(12)
print(P.pop())
P.push(13)
print(P.pop())
print(P.pop())
print(P.pop())
