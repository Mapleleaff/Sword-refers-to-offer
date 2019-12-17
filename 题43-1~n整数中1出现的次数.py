"""
题43-1~n整数中1出现的次数
输入一个整数 n，求 1~n 这 n 个整数的十进制表示中 1 出现的次数。
例如，输入 12，1~12这些整数中包含 1 的数字有 1、10、11 和 12，
1 一共出现了 5 次。
"""

class Solution:
    def Numberof1Between1AndN(self, n):
        ones, m = 0, 1
        while m <= n:
            ones += (n//m + 8)//10 * m + (n//m % 10==1) * (n % m + 1)
            m *= 10
        return ones


    def Numberof1Between1AndN_v2(self, n):
        ones, m = 0, 1
        while m <= n:
            if ((n//m) % 10) != 0 and ((n//m) % 10) != 1:
                ones += (n//10//m + 1) * m
            elif ((n//m) % 10) == 1:
                ones += (n//m//10) * m + n % m + 1
            m *= 10
        return ones


array = 537
S = Solution()
print(S.Numberof1Between1AndN(array))
print(S.Numberof1Between1AndN_v2(array))
