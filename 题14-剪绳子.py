"""
题14-剪绳子
把一根长度为 n 的绳子剪成 m 段，并且使得每段的长度的乘积最大（n, m 均为整数）
"""

class Solution(object):
    # 动态规划
    def Maxproduct(self,num):

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
    def maxproduct(self,num):
        
        # 因为至少剪一次
        if num < 2:
            return 0
        if num == 2:
            return 1
        if num == 3:
            return 2

        n3 = num // 3
        if num % 3 == 1:
            n3 -=1
        n2 = (num - 3*n3)//2

        return pow(3,n3)*pow(2,n2)

S = Solution()
for i in range(4, 20):
    print(S.Maxproduct(num = i))
    print(S.maxproduct(num = i))
