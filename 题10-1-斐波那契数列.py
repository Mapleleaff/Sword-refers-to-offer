"""
题10-1-斐波那契数列
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）
"""

# 循环解法
def Fibonacci(n):
    N0 = 0
    N1 = 1
    
    if n<=1:
        return n
    
    while n>1:
        N1 = N0 + N1
        N0 = N1 - N0
        n -= 1
    return N1


# 递归解法
def Fibonaccii(n):
    if n<=1:
        return n
    return Fibonaccii(n-1) + Fibonaccii(n-2)


for n in range(10):
    result = Fibonacci(n)
    print(result)
    result = Fibonaccii(n)
    print(result)
