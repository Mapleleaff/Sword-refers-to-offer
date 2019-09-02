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
