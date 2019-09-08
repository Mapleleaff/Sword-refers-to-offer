# 动态规划
def Maxproduct(num):

    # 因为至少剪一次
    if num < 2:
        return 0
    if num == 2:
        return 1
    if num == 3:
        return 2
    product = [0,1,2,3]
    for i in range(4, num+1):
        max_dot = 0
        for j in range(1,i//2+1):
            pro = product[j] * product[i-j]
            if max_dot < pro:
                max_dot = pro
        product.append(max_dot)

    max_dot = product[-1]
    return max_dot


# 贪心法算法
def maxproduct(num):
    # 因为至少剪一次
    if num < 2:
        return 0
    if num == 2:
        return 1
    if num == 3:
        return 2

    n3 = i//3
    if i%3 == 1:
        n3 -=1
    n2 = (num - 3*n3)//2

    return pow(3,n3)*pow(2,n2)


for i in range(4, 20):
    print(Maxproduct(num = i))
    print(maxproduct(num = i))
