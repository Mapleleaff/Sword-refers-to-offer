"""
题15-二进制中1的个数
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示
"""

class Solution(object):
    # num右移解法
    def Solution_v1(self,num):
        count = 0
        flag = 1
        if num < 0:
            num = num & 0xffffffff
        while num:
            if num & flag:
                count += 1
            num = num>>1
        return count

    # 1左移解法,循环次数为整数二进制的位数=32
    def Solution_v2(self,num):
        count = 0
        flag = 1
        iter = 32
        for i in range(iter):
            if num & flag:
                count += 1
            flag = flag<< 1
        return count

    # 整数减去1在和原整数做与，会把该整数最右边的1变成0
    def Solution_v3(self,num):
        count = 0
        if num < 0:
            num = num & 0xffffffff
        while num:
            num = (num-1) & num
            count += 1
        return count


S = Solution()
for i in [2,64,63,10,-1]:
    print(S.Solution_v2(i))
    print(S.Solution_v3(i))
    print(S.Solution_v1(i))

